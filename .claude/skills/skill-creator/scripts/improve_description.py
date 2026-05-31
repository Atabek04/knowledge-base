#!/usr/bin/env python3
"""
Improve a skill description based on evaluation results.

This script is typically called by run_loop.py but can be used standalone.

Usage:
    python -m scripts.improve_description --skill-path <path> --eval-results <path> [options]
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from .utils import parse_skill_md


def improve_description(
    current_description: str,
    eval_results: dict,
    skill_content: str,
    history: list[dict] | None = None,
    model: str = "claude-sonnet-4-20250514",
) -> tuple[str, dict]:
    """
    Generate an improved description using Claude.

    Args:
        current_description: Current skill description
        eval_results: Results from run_eval
        skill_content: Full SKILL.md content
        history: Previous improvement attempts
        model: Model ID to use

    Returns:
        Tuple of (improved_description, transcript_data)
    """
    history = history or []

    # Build analysis of failures
    failed = [r for r in eval_results.get("results", []) if not r.get("passed", True)]
    false_negatives = [r for r in failed if r.get("should_trigger", False)]
    false_positives = [r for r in failed if not r.get("should_trigger", True)]

    metrics = eval_results.get("metrics", {})

    prompt = f"""You are improving a Claude Code skill's description to optimize triggering behavior.

## Current State

**Description** (max 1024 chars):
{current_description}

**Metrics**:
- Accuracy: {metrics.get('accuracy', 'N/A')}
- Precision: {metrics.get('precision', 'N/A')} (of triggered, how many should have?)
- Recall: {metrics.get('recall', 'N/A')} (of should-trigger, how many did?)
- True positives: {metrics.get('true_positives', 0)}
- False positives: {metrics.get('false_positives', 0)}
- True negatives: {metrics.get('true_negatives', 0)}
- False negatives: {metrics.get('false_negatives', 0)}

## Failures to Address

**Should have triggered but didn't** (false negatives - PRIORITY):
{json.dumps([{'query': r['query'][:200], 'trigger_rate': r.get('trigger_rate', 0)} for r in false_negatives], indent=2) if false_negatives else "None - recall is perfect!"}

**Shouldn't have triggered but did** (false positives):
{json.dumps([{'query': r['query'][:200], 'trigger_rate': r.get('trigger_rate', 0)} for r in false_positives], indent=2) if false_positives else "None - precision is perfect!"}

## Previous Attempts
{json.dumps([{
    'description': h.get('description', '')[:100] + '...',
    'accuracy': h.get('accuracy', h.get('test_accuracy', 'N/A'))
} for h in history[-3:]], indent=2) if history else "This is the first improvement attempt."}

## Skill Context
{skill_content[:1500]}
{'...(truncated)' if len(skill_content) > 1500 else ''}

## Your Task

Write an improved description that:

1. **Generalizes** from the failure patterns - don't overfit to specific failing queries
2. **Balances** precision and recall - but when in doubt, prefer triggering (Claude undertriggers)
3. **Uses specific keywords** that appear in should-trigger queries
4. **Excludes keywords** that appear only in shouldn't-trigger queries
5. **Is pushy** - explicitly say "use this skill when..." with multiple phrasings
6. **Stays under 1024 characters** - this is a hard limit

Write ONLY the new description text. No explanation, no markdown formatting, just the description."""

    # Remove CLAUDECODE env var for nested invocation
    env = os.environ.copy()
    env.pop("CLAUDECODE", None)

    transcript = {
        "prompt": prompt,
        "response": None,
        "shortened": False,
        "final_description": None,
    }

    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", model],
            capture_output=True,
            text=True,
            env=env,
            timeout=120,
        )

        new_description = result.stdout.strip()
        transcript["response"] = new_description

        # If too long, ask for shorter version
        if len(new_description) > 1024:
            transcript["shortened"] = True

            shorten_prompt = f"""This description is {len(new_description)} characters but must be under 1024.
Shorten it while keeping the key triggering phrases and specificity:

{new_description}

Write ONLY the shortened description, nothing else."""

            result = subprocess.run(
                ["claude", "-p", shorten_prompt, "--model", model],
                capture_output=True,
                text=True,
                env=env,
                timeout=60,
            )
            new_description = result.stdout.strip()

        # Final truncation if still too long
        new_description = new_description[:1024]
        transcript["final_description"] = new_description

        return new_description, transcript

    except subprocess.TimeoutExpired:
        transcript["error"] = "Timeout"
        return current_description, transcript
    except Exception as e:
        transcript["error"] = str(e)
        return current_description, transcript


def main():
    parser = argparse.ArgumentParser(description="Improve skill description")
    parser.add_argument("--skill-path", required=True, help="Path to skill directory")
    parser.add_argument("--eval-results", required=True, help="Path to eval results JSON")
    parser.add_argument("--history", help="Path to history JSON")
    parser.add_argument("--model", default="claude-sonnet-4-20250514", help="Model ID")
    parser.add_argument("--output", help="Output file for transcript")
    parser.add_argument("--apply", action="store_true", help="Apply to SKILL.md")

    args = parser.parse_args()

    # Load inputs
    name, current_description, skill_content = parse_skill_md(args.skill_path)
    eval_results = json.loads(Path(args.eval_results).read_text())

    history = []
    if args.history:
        history = json.loads(Path(args.history).read_text())

    # Generate improvement
    new_description, transcript = improve_description(
        current_description=current_description,
        eval_results=eval_results,
        skill_content=skill_content,
        history=history,
        model=args.model,
    )

    # Output
    output = {
        "original_description": current_description,
        "new_description": new_description,
        "transcript": transcript,
    }

    if args.output:
        Path(args.output).write_text(json.dumps(output, indent=2))
        print(f"Transcript saved to: {args.output}")
    else:
        print(json.dumps(output, indent=2))

    # Apply if requested
    if args.apply:
        import re

        skill_md_path = Path(args.skill_path) / "SKILL.md"
        old_content = skill_md_path.read_text()

        new_content = re.sub(
            r'(description:\s*)[^\n]+(\n(?:[ \t]+[^\n]+\n)*)?',
            f'\\1{new_description}\n',
            old_content,
            count=1,
        )
        skill_md_path.write_text(new_content)
        print(f"Updated: {skill_md_path}")


if __name__ == "__main__":
    main()
