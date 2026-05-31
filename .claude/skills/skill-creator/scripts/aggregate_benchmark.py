#!/usr/bin/env python3
"""
Aggregate individual benchmark run results into summary statistics.

Usage:
    python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
"""

import argparse
import json
import math
import sys
from datetime import datetime
from pathlib import Path


def calculate_stats(values: list[float]) -> dict:
    """Calculate mean, std, min, max for a list of values."""
    if not values:
        return {"mean": 0, "std": 0, "min": 0, "max": 0}

    n = len(values)
    mean = sum(values) / n

    if n > 1:
        variance = sum((x - mean) ** 2 for x in values) / (n - 1)
        std = math.sqrt(variance)
    else:
        std = 0

    return {
        "mean": round(mean, 3),
        "std": round(std, 3),
        "min": round(min(values), 3),
        "max": round(max(values), 3),
    }


def load_run_results(benchmark_dir: Path) -> list[dict]:
    """Load grading.json files from benchmark directories."""
    runs = []

    # Try workspace layout (eval directories directly under benchmark_dir)
    eval_dirs = [d for d in benchmark_dir.iterdir() if d.is_dir() and d.name.startswith("eval")]

    # If no eval dirs found, try legacy layout (under runs/)
    if not eval_dirs:
        runs_dir = benchmark_dir / "runs"
        if runs_dir.exists():
            eval_dirs = [d for d in runs_dir.iterdir() if d.is_dir()]

    for eval_dir in sorted(eval_dirs):
        # Look for config subdirectories (with_skill, without_skill, old_skill)
        for config_dir in eval_dir.iterdir():
            if not config_dir.is_dir():
                continue

            grading_path = config_dir / "grading.json"
            timing_path = config_dir.parent / "timing.json"
            metadata_path = eval_dir / "eval_metadata.json"

            if not grading_path.exists():
                continue

            try:
                grading = json.loads(grading_path.read_text())
            except (json.JSONDecodeError, IOError):
                continue

            # Load timing if available
            timing = {}
            if timing_path.exists():
                try:
                    timing = json.loads(timing_path.read_text())
                except (json.JSONDecodeError, IOError):
                    pass

            # Load metadata if available
            metadata = {}
            if metadata_path.exists():
                try:
                    metadata = json.loads(metadata_path.read_text())
                except (json.JSONDecodeError, IOError):
                    pass

            run = {
                "eval_id": metadata.get("eval_name", eval_dir.name),
                "config": config_dir.name,
                "pass_rate": grading.get("summary", {}).get("pass_rate", 0),
                "time_seconds": timing.get("total_duration_seconds", 0),
                "tokens": timing.get("total_tokens", 0),
                "expectations": grading.get("expectations", []),
            }
            runs.append(run)

    return runs


def aggregate_results(runs: list[dict]) -> dict:
    """Aggregate runs into summary statistics per configuration."""
    configs = {}

    for run in runs:
        config = run["config"]
        if config not in configs:
            configs[config] = {
                "pass_rates": [],
                "times": [],
                "tokens": [],
            }
        configs[config]["pass_rates"].append(run["pass_rate"])
        if run["time_seconds"]:
            configs[config]["times"].append(run["time_seconds"])
        if run["tokens"]:
            configs[config]["tokens"].append(run["tokens"])

    summary = {}
    for config, data in configs.items():
        summary[config] = {
            "pass_rate": calculate_stats(data["pass_rates"]),
            "time_seconds": calculate_stats(data["times"]),
            "tokens": calculate_stats(data["tokens"]),
        }

    # Calculate delta between first two configs (typically with_skill vs without_skill)
    config_names = list(configs.keys())
    if len(config_names) >= 2:
        c1, c2 = config_names[0], config_names[1]
        delta = {
            "pass_rate": f"{summary[c1]['pass_rate']['mean'] - summary[c2]['pass_rate']['mean']:+.3f}",
            "time_seconds": f"{summary[c1]['time_seconds']['mean'] - summary[c2]['time_seconds']['mean']:+.1f}",
            "tokens": f"{int(summary[c1]['tokens']['mean'] - summary[c2]['tokens']['mean']):+d}",
        }
        summary["delta"] = delta

    return summary


def generate_benchmark(benchmark_dir: Path, skill_name: str) -> dict:
    """Generate comprehensive benchmark.json."""
    runs = load_run_results(benchmark_dir)
    summary = aggregate_results(runs)

    # Sort runs so with_skill comes before its baseline
    def sort_key(run):
        config_order = {"with_skill": 0, "without_skill": 1, "old_skill": 1}
        return (run["eval_id"], config_order.get(run["config"], 2))

    runs.sort(key=sort_key)

    return {
        "metadata": {
            "skill_name": skill_name,
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "iteration": int(benchmark_dir.name.split("-")[-1]) if "-" in benchmark_dir.name else 1,
        },
        "runs": runs,
        "summary": summary,
        "analyzer_notes": [],
    }


def generate_markdown(benchmark: dict) -> str:
    """Generate human-readable markdown report."""
    lines = [
        f"# Benchmark Results: {benchmark['metadata']['skill_name']}",
        f"",
        f"Generated: {benchmark['metadata']['generated_at']}",
        f"Iteration: {benchmark['metadata']['iteration']}",
        f"",
        "## Summary",
        "",
    ]

    summary = benchmark["summary"]
    for config, stats in summary.items():
        if config == "delta":
            continue
        lines.append(f"### {config}")
        lines.append(f"- Pass rate: {stats['pass_rate']['mean']:.2f} ± {stats['pass_rate']['std']:.2f}")
        lines.append(f"- Time: {stats['time_seconds']['mean']:.1f}s ± {stats['time_seconds']['std']:.1f}s")
        lines.append(f"- Tokens: {int(stats['tokens']['mean'])} ± {int(stats['tokens']['std'])}")
        lines.append("")

    if "delta" in summary:
        lines.append("### Delta")
        delta = summary["delta"]
        lines.append(f"- Pass rate: {delta['pass_rate']}")
        lines.append(f"- Time: {delta['time_seconds']}s")
        lines.append(f"- Tokens: {delta['tokens']}")
        lines.append("")

    lines.append("## Individual Runs")
    lines.append("")
    lines.append("| Eval | Config | Pass Rate | Time (s) | Tokens |")
    lines.append("|------|--------|-----------|----------|--------|")

    for run in benchmark["runs"]:
        lines.append(
            f"| {run['eval_id']} | {run['config']} | {run['pass_rate']:.2f} | "
            f"{run['time_seconds']:.1f} | {run['tokens']} |"
        )

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Aggregate benchmark results")
    parser.add_argument("benchmark_dir", help="Path to benchmark directory")
    parser.add_argument("--skill-name", required=True, help="Name of the skill")
    parser.add_argument("--output", help="Output directory (defaults to benchmark_dir)")

    args = parser.parse_args()

    benchmark_dir = Path(args.benchmark_dir)
    if not benchmark_dir.exists():
        print(f"Error: Directory not found: {benchmark_dir}")
        sys.exit(1)

    output_dir = Path(args.output) if args.output else benchmark_dir

    # Generate benchmark
    benchmark = generate_benchmark(benchmark_dir, args.skill_name)

    # Write JSON
    json_path = output_dir / "benchmark.json"
    json_path.write_text(json.dumps(benchmark, indent=2))
    print(f"Created: {json_path}")

    # Write markdown
    md_path = output_dir / "benchmark.md"
    md_path.write_text(generate_markdown(benchmark))
    print(f"Created: {md_path}")


if __name__ == "__main__":
    main()
