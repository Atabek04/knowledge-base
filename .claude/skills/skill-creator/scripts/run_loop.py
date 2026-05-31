#!/usr/bin/env python3
"""
Iterative evaluation and improvement loop for skill descriptions.

Usage:
    python -m scripts.run_loop --eval-set <path> --skill-path <path> [options]
"""

import argparse
import json
import os
import random
import subprocess
import sys
import webbrowser
from datetime import datetime
from pathlib import Path

from .run_eval import run_eval
from .utils import parse_skill_md


def split_eval_set(eval_set: list[dict], holdout_fraction: float = 0.4, seed: int = 42) -> tuple[list, list]:
    """
    Split eval set into train and test using stratified sampling.

    Args:
        eval_set: List of {"query": str, "should_trigger": bool}
        holdout_fraction: Fraction for test set
        seed: Random seed for reproducibility

    Returns:
        Tuple of (train_set, test_set)
    """
    random.seed(seed)

    # Stratify by should_trigger
    positive = [e for e in eval_set if e["should_trigger"]]
    negative = [e for e in eval_set if not e["should_trigger"]]

    random.shuffle(positive)
    random.shuffle(negative)

    # Split each stratum
    pos_split = int(len(positive) * (1 - holdout_fraction))
    neg_split = int(len(negative) * (1 - holdout_fraction))

    train = positive[:pos_split] + negative[:neg_split]
    test = positive[pos_split:] + negative[neg_split:]

    random.shuffle(train)
    random.shuffle(test)

    return train, test


def improve_description(
    current_description: str,
    eval_results: dict,
    skill_content: str,
    history: list[dict],
    model: str,
) -> str:
    """
    Call Claude to generate an improved description based on eval failures.

    Args:
        current_description: Current skill description
        eval_results: Results from run_eval
        skill_content: Full SKILL.md content
        history: Previous improvement attempts
        model: Model ID to use

    Returns:
        Improved description string
    """
    # Build prompt
    failed = [r for r in eval_results["results"] if not r["passed"]]
    false_negatives = [r for r in failed if r["should_trigger"]]
    false_positives = [r for r in failed if not r["should_trigger"]]

    prompt = f"""You are improving a Claude Code skill's description to optimize when it triggers.

Current description:
{current_description}

Current metrics:
- Accuracy: {eval_results['metrics']['accuracy']}
- Precision: {eval_results['metrics']['precision']}
- Recall: {eval_results['metrics']['recall']}

Failed to trigger (should have):
{json.dumps([r['query'] for r in false_negatives], indent=2) if false_negatives else "None"}

Incorrectly triggered (shouldn't have):
{json.dumps([r['query'] for r in false_positives], indent=2) if false_positives else "None"}

Previous attempts:
{json.dumps([{'description': h['description'][:100] + '...', 'accuracy': h['accuracy']} for h in history[-3:]], indent=2) if history else "None"}

Full skill content for context:
{skill_content[:2000]}...

Write an improved description that:
1. Generalizes from failures rather than overfitting to specific queries
2. Is clear about what the skill does AND when to use it
3. Uses "pushy" language to encourage triggering (Claude tends to undertrigger)
4. Stays under 1024 characters

Return ONLY the new description, nothing else."""

    # Call claude CLI
    env = os.environ.copy()
    env.pop("CLAUDECODE", None)

    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", model],
            capture_output=True,
            text=True,
            env=env,
            timeout=120,
        )
        new_description = result.stdout.strip()

        # If too long, ask for shorter version
        if len(new_description) > 1024:
            result = subprocess.run(
                ["claude", "-p", f"Shorten this to under 1024 characters while keeping the key points:\n\n{new_description}", "--model", model],
                capture_output=True,
                text=True,
                env=env,
                timeout=60,
            )
            new_description = result.stdout.strip()

        return new_description[:1024]

    except subprocess.TimeoutExpired:
        return current_description
    except Exception as e:
        print(f"Error calling Claude: {e}")
        return current_description


def run_loop(
    eval_set_path: str,
    skill_path: str,
    model: str = "claude-sonnet-4-20250514",
    max_iterations: int = 5,
    holdout_fraction: float = 0.4,
    verbose: bool = False,
    output_dir: str | None = None,
) -> dict:
    """
    Run the full optimization loop.

    Args:
        eval_set_path: Path to eval set JSON
        skill_path: Path to skill directory
        model: Model ID
        max_iterations: Maximum iterations
        holdout_fraction: Fraction for test set
        verbose: Print detailed progress
        output_dir: Output directory for results

    Returns:
        Dict with best_description, scores, and history
    """
    # Load eval set and skill
    eval_set = json.loads(Path(eval_set_path).read_text())
    name, original_description, skill_content = parse_skill_md(skill_path)

    # Split into train/test
    train_set, test_set = split_eval_set(eval_set, holdout_fraction)

    if verbose:
        print(f"Skill: {name}")
        print(f"Train set: {len(train_set)} queries")
        print(f"Test set: {len(test_set)} queries")
        print()

    # Track iterations
    history = []
    best_description = original_description
    best_test_score = 0

    current_description = original_description

    for iteration in range(max_iterations):
        if verbose:
            print(f"=== Iteration {iteration + 1} ===")

        # Evaluate on train set
        train_results = run_eval(
            eval_set=train_set,
            skill_path=skill_path,
            model=model,
        )

        # Evaluate on test set
        test_results = run_eval(
            eval_set=test_set,
            skill_path=skill_path,
            model=model,
        )

        train_accuracy = train_results["metrics"]["accuracy"]
        test_accuracy = test_results["metrics"]["accuracy"]

        if verbose:
            print(f"Train accuracy: {train_accuracy:.3f}")
            print(f"Test accuracy: {test_accuracy:.3f}")
            print()

        # Record iteration
        history.append({
            "iteration": iteration + 1,
            "description": current_description,
            "train_accuracy": train_accuracy,
            "test_accuracy": test_accuracy,
            "accuracy": test_accuracy,
            "train_results": train_results,
            "test_results": test_results,
        })

        # Track best by test score
        if test_accuracy > best_test_score:
            best_test_score = test_accuracy
            best_description = current_description

        # Check if all passing
        if train_accuracy == 1.0 and test_accuracy == 1.0:
            if verbose:
                print("All queries passing - stopping early")
            break

        # Generate improved description
        if iteration < max_iterations - 1:
            if verbose:
                print("Generating improved description...")

            new_description = improve_description(
                current_description=current_description,
                eval_results=train_results,
                skill_content=skill_content,
                history=history,
                model=model,
            )

            # Update skill file with new description
            skill_md_path = Path(skill_path) / "SKILL.md"
            old_content = skill_md_path.read_text()

            # Replace description in frontmatter
            import re
            new_content = re.sub(
                r'(description:\s*)[^\n]+(\n(?:[ \t]+[^\n]+\n)*)?',
                f'\\1{new_description}\n',
                old_content,
                count=1,
            )
            skill_md_path.write_text(new_content)

            current_description = new_description

            if verbose:
                print(f"New description: {new_description[:100]}...")
                print()

    # Prepare output
    result = {
        "skill_name": name,
        "original_description": original_description,
        "best_description": best_description,
        "best_test_score": best_test_score,
        "iterations": len(history),
        "history": history,
        "train_queries": train_set,
        "test_queries": test_set,
    }

    # Save if output_dir specified
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_path = output_path / f"results_{timestamp}.json"
        json_path.write_text(json.dumps(result, indent=2))

        if verbose:
            print(f"Results saved to: {json_path}")

    return result


def main():
    parser = argparse.ArgumentParser(description="Run skill description optimization loop")
    parser.add_argument("--eval-set", required=True, help="Path to eval set JSON")
    parser.add_argument("--skill-path", required=True, help="Path to skill directory")
    parser.add_argument("--model", default="claude-sonnet-4-20250514", help="Model ID")
    parser.add_argument("--max-iterations", type=int, default=5, help="Max iterations")
    parser.add_argument("--holdout", type=float, default=0.4, help="Test set fraction")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--output", help="Output directory")

    args = parser.parse_args()

    result = run_loop(
        eval_set_path=args.eval_set,
        skill_path=args.skill_path,
        model=args.model,
        max_iterations=args.max_iterations,
        holdout_fraction=args.holdout,
        verbose=args.verbose,
        output_dir=args.output,
    )

    if not args.output:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
