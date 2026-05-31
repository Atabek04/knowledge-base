#!/usr/bin/env python3
"""
Generate HTML report from run_loop.py output.

Usage:
    python -m scripts.generate_report <results.json> [--output <file.html>] [--skill-name <name>]
"""

import argparse
import json
import sys
from pathlib import Path


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skill Description Optimization Report - {skill_name}</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Lora:wght@400;500&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Poppins', sans-serif;
            background: #faf9f5;
            color: #1a1a1a;
            line-height: 1.6;
            padding: 2rem;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{
            font-family: 'Lora', serif;
            font-size: 2rem;
            margin-bottom: 1.5rem;
            color: #2d2d2d;
        }}
        h2 {{
            font-size: 1.25rem;
            margin: 1.5rem 0 1rem;
            color: #444;
        }}
        .summary {{
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
        }}
        .stat {{
            text-align: center;
            padding: 1rem;
            background: #f5f5f5;
            border-radius: 6px;
        }}
        .stat-value {{
            font-size: 1.5rem;
            font-weight: 600;
            color: #2d2d2d;
        }}
        .stat-label {{
            font-size: 0.875rem;
            color: #666;
        }}
        .description-box {{
            background: #f0f0f0;
            padding: 1rem;
            border-radius: 6px;
            font-family: monospace;
            font-size: 0.875rem;
            white-space: pre-wrap;
            word-break: break-word;
            margin: 0.5rem 0;
        }}
        .legend {{
            display: flex;
            gap: 1.5rem;
            margin-bottom: 1rem;
            flex-wrap: wrap;
        }}
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.875rem;
        }}
        .legend-color {{
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }}
        .legend-color.positive {{ background: #e8f5e9; border: 2px solid #2e7d32; }}
        .legend-color.negative {{ background: #ffebee; border: 2px solid #c62828; }}
        .legend-color.test {{ background: #e3f2fd; }}
        .legend-color.best {{ background: #c8e6c9; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        th, td {{
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid #eee;
        }}
        th {{
            background: #f5f5f5;
            font-weight: 500;
            font-size: 0.875rem;
        }}
        tr:hover {{ background: #fafafa; }}
        .score-badge {{
            display: inline-block;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 500;
        }}
        .score-good {{ background: #c8e6c9; color: #2e7d32; }}
        .score-ok {{ background: #fff9c4; color: #f57f17; }}
        .score-bad {{ background: #ffcdd2; color: #c62828; }}
        .best-row {{ background: #e8f5e9 !important; }}
        .query-cell {{
            max-width: 400px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }}
        .pass {{ color: #2e7d32; }}
        .fail {{ color: #c62828; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Skill Description Optimization: {skill_name}</h1>

        <div class="summary">
            <h2>Summary</h2>
            <div class="summary-grid">
                <div class="stat">
                    <div class="stat-value">{iterations}</div>
                    <div class="stat-label">Iterations</div>
                </div>
                <div class="stat">
                    <div class="stat-value">{best_score:.1%}</div>
                    <div class="stat-label">Best Test Score</div>
                </div>
                <div class="stat">
                    <div class="stat-value">{train_count}</div>
                    <div class="stat-label">Train Queries</div>
                </div>
                <div class="stat">
                    <div class="stat-value">{test_count}</div>
                    <div class="stat-label">Test Queries</div>
                </div>
            </div>

            <h2>Original Description</h2>
            <div class="description-box">{original_description}</div>

            <h2>Best Description</h2>
            <div class="description-box">{best_description}</div>
        </div>

        <h2>Iteration Results</h2>
        <div class="legend">
            <div class="legend-item">
                <div class="legend-color positive"></div>
                <span>Should trigger</span>
            </div>
            <div class="legend-item">
                <div class="legend-color negative"></div>
                <span>Should NOT trigger</span>
            </div>
            <div class="legend-item">
                <div class="legend-color test"></div>
                <span>Test set query</span>
            </div>
            <div class="legend-item">
                <div class="legend-color best"></div>
                <span>Best iteration</span>
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Iteration</th>
                    <th>Train Accuracy</th>
                    <th>Test Accuracy</th>
                    <th>Description Preview</th>
                </tr>
            </thead>
            <tbody>
                {iteration_rows}
            </tbody>
        </table>

        {query_details}
    </div>
</body>
</html>
"""


def score_badge(score: float) -> str:
    """Generate score badge HTML."""
    if score >= 0.8:
        return f'<span class="score-badge score-good">{score:.1%}</span>'
    elif score >= 0.5:
        return f'<span class="score-badge score-ok">{score:.1%}</span>'
    else:
        return f'<span class="score-badge score-bad">{score:.1%}</span>'


def generate_report(results: dict, skill_name: str | None = None) -> str:
    """Generate HTML report from run_loop results."""
    skill_name = skill_name or results.get("skill_name", "Unknown Skill")

    # Build iteration rows
    best_idx = max(
        range(len(results.get("history", []))),
        key=lambda i: results["history"][i].get("test_accuracy", 0),
        default=0
    )

    iteration_rows = []
    for i, h in enumerate(results.get("history", [])):
        is_best = i == best_idx
        row_class = ' class="best-row"' if is_best else ''
        desc_preview = h.get("description", "")[:80] + "..." if len(h.get("description", "")) > 80 else h.get("description", "")

        iteration_rows.append(f"""
            <tr{row_class}>
                <td>{h.get('iteration', i+1)}{' (best)' if is_best else ''}</td>
                <td>{score_badge(h.get('train_accuracy', 0))}</td>
                <td>{score_badge(h.get('test_accuracy', 0))}</td>
                <td class="query-cell" title="{h.get('description', '')}">{desc_preview}</td>
            </tr>
        """)

    # Build query details section (optional)
    query_details = ""

    return HTML_TEMPLATE.format(
        skill_name=skill_name,
        iterations=len(results.get("history", [])),
        best_score=results.get("best_test_score", 0),
        train_count=len(results.get("train_queries", [])),
        test_count=len(results.get("test_queries", [])),
        original_description=results.get("original_description", "N/A"),
        best_description=results.get("best_description", "N/A"),
        iteration_rows="\n".join(iteration_rows),
        query_details=query_details,
    )


def main():
    parser = argparse.ArgumentParser(description="Generate optimization report")
    parser.add_argument("input", help="Path to results JSON (or - for stdin)")
    parser.add_argument("--output", "-o", help="Output HTML file (default: stdout)")
    parser.add_argument("--skill-name", help="Override skill name in report")

    args = parser.parse_args()

    # Load input
    if args.input == "-":
        results = json.load(sys.stdin)
    else:
        results = json.loads(Path(args.input).read_text())

    # Generate report
    html = generate_report(results, args.skill_name)

    # Output
    if args.output:
        Path(args.output).write_text(html)
        print(f"Report written to: {args.output}")
    else:
        print(html)


if __name__ == "__main__":
    main()
