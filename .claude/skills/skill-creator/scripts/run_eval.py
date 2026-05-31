#!/usr/bin/env python3
"""
Evaluate whether a skill's description causes Claude to trigger for test queries.

Usage:
    python -m scripts.run_eval --eval-set <path> --skill-path <path> [options]
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from .utils import parse_skill_md


def find_project_root() -> Path | None:
    """Find project root by searching for .claude/ directory."""
    current = Path.cwd()
    while current != current.parent:
        if (current / ".claude").exists():
            return current
        current = current.parent
    return None


def run_single_query(
    query: str,
    skill_path: str,
    model: str,
    timeout: int,
) -> dict:
    """
    Run a single query and detect if the skill triggers.

    Returns dict with 'triggered' (bool) and 'error' (str or None).
    """
    project_root = find_project_root()
    if not project_root:
        return {"triggered": False, "error": "Could not find project root"}

    # Create temporary command file to inject the skill
    commands_dir = project_root / ".claude" / "commands"
    commands_dir.mkdir(parents=True, exist_ok=True)

    cmd_file = commands_dir / f"_eval_temp_{os.getpid()}.md"

    try:
        # Write skill reference to command file
        cmd_file.write_text(f"Use skill at: {skill_path}")

        # Build claude command
        cmd = [
            "claude",
            "-p", query,
            "--model", model,
            "--output-format", "stream-json",
        ]

        # Remove CLAUDECODE env var to allow nested invocation
        env = os.environ.copy()
        env.pop("CLAUDECODE", None)

        # Run and stream output
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
            text=True,
        )

        triggered = False
        try:
            for line in process.stdout:
                line = line.strip()
                if not line:
                    continue
                try:
                    event = json.loads(line)
                    # Check for skill triggering in stream events
                    if event.get("type") == "content_block_start":
                        content = event.get("content_block", {})
                        if "skill" in str(content).lower():
                            triggered = True
                            break
                    # Also check tool use for skill invocation
                    if event.get("type") == "tool_use":
                        if "skill" in event.get("name", "").lower():
                            triggered = True
                            break
                except json.JSONDecodeError:
                    continue

            process.terminate()
            process.wait(timeout=5)

        except subprocess.TimeoutExpired:
            process.kill()
            return {"triggered": False, "error": "Timeout"}

        return {"triggered": triggered, "error": None}

    finally:
        # Cleanup
        if cmd_file.exists():
            cmd_file.unlink()


def run_eval(
    eval_set: list[dict],
    skill_path: str,
    model: str = "claude-sonnet-4-20250514",
    timeout: int = 60,
    threshold: float = 0.5,
    runs_per_query: int = 3,
    max_workers: int = 10,
) -> dict:
    """
    Run evaluation across all queries.

    Args:
        eval_set: List of {"query": str, "should_trigger": bool}
        skill_path: Path to skill directory
        model: Model ID to use
        timeout: Timeout per query in seconds
        threshold: Trigger rate threshold for pass/fail
        runs_per_query: Number of times to run each query
        max_workers: Max parallel workers

    Returns:
        Dict with results, trigger rates, and pass/fail status
    """
    results = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {}

        for item in eval_set:
            for run_idx in range(runs_per_query):
                future = executor.submit(
                    run_single_query,
                    item["query"],
                    skill_path,
                    model,
                    timeout,
                )
                futures[future] = {
                    "query": item["query"],
                    "should_trigger": item["should_trigger"],
                    "run_idx": run_idx,
                }

        for future in as_completed(futures):
            meta = futures[future]
            result = future.result()
            results.append({
                **meta,
                "triggered": result["triggered"],
                "error": result["error"],
            })

    # Aggregate by query
    query_results = {}
    for r in results:
        q = r["query"]
        if q not in query_results:
            query_results[q] = {
                "should_trigger": r["should_trigger"],
                "triggers": [],
                "errors": [],
            }
        query_results[q]["triggers"].append(r["triggered"])
        if r["error"]:
            query_results[q]["errors"].append(r["error"])

    # Calculate metrics
    output = []
    for query, data in query_results.items():
        trigger_rate = sum(data["triggers"]) / len(data["triggers"])
        should = data["should_trigger"]

        if should:
            passed = trigger_rate >= threshold
        else:
            passed = trigger_rate < threshold

        output.append({
            "query": query,
            "should_trigger": should,
            "trigger_rate": round(trigger_rate, 3),
            "passed": passed,
            "errors": data["errors"],
        })

    # Calculate overall metrics
    total = len(output)
    passed = sum(1 for o in output if o["passed"])
    positive = [o for o in output if o["should_trigger"]]
    negative = [o for o in output if not o["should_trigger"]]

    true_positives = sum(1 for o in positive if o["trigger_rate"] >= threshold)
    false_negatives = sum(1 for o in positive if o["trigger_rate"] < threshold)
    true_negatives = sum(1 for o in negative if o["trigger_rate"] < threshold)
    false_positives = sum(1 for o in negative if o["trigger_rate"] >= threshold)

    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    accuracy = passed / total if total > 0 else 0

    return {
        "results": output,
        "metrics": {
            "total": total,
            "passed": passed,
            "accuracy": round(accuracy, 3),
            "precision": round(precision, 3),
            "recall": round(recall, 3),
            "true_positives": true_positives,
            "false_positives": false_positives,
            "true_negatives": true_negatives,
            "false_negatives": false_negatives,
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Evaluate skill triggering")
    parser.add_argument("--eval-set", required=True, help="Path to eval set JSON")
    parser.add_argument("--skill-path", required=True, help="Path to skill directory")
    parser.add_argument("--model", default="claude-sonnet-4-20250514", help="Model ID")
    parser.add_argument("--timeout", type=int, default=60, help="Timeout per query")
    parser.add_argument("--threshold", type=float, default=0.5, help="Trigger threshold")
    parser.add_argument("--runs", type=int, default=3, help="Runs per query")
    parser.add_argument("--workers", type=int, default=10, help="Max parallel workers")
    parser.add_argument("--output", help="Output file path")

    args = parser.parse_args()

    # Load eval set
    eval_set = json.loads(Path(args.eval_set).read_text())

    # Run evaluation
    results = run_eval(
        eval_set=eval_set,
        skill_path=args.skill_path,
        model=args.model,
        timeout=args.timeout,
        threshold=args.threshold,
        runs_per_query=args.runs,
        max_workers=args.workers,
    )

    # Output
    output = json.dumps(results, indent=2)
    if args.output:
        Path(args.output).write_text(output)
        print(f"Results written to: {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
