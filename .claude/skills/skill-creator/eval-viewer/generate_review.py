#!/usr/bin/env python3
"""
Generate and serve an interactive web-based review interface for evaluation results.

Usage:
    python generate_review.py <workspace> --skill-name <name> [--benchmark <path>] [--static <output>]
"""

import argparse
import base64
import http.server
import json
import mimetypes
import os
import socketserver
import sys
import threading
import webbrowser
from pathlib import Path
from urllib.parse import parse_qs, urlparse


def find_runs(workspace: Path) -> list[dict]:
    """Find all evaluation runs in the workspace."""
    runs = []

    for path in workspace.rglob("outputs"):
        if not path.is_dir():
            continue

        run_dir = path.parent
        run_id = f"{run_dir.parent.name}-{run_dir.name}"

        # Load metadata
        metadata_path = run_dir.parent / "eval_metadata.json"
        metadata = {}
        if metadata_path.exists():
            try:
                metadata = json.loads(metadata_path.read_text())
            except (json.JSONDecodeError, IOError):
                pass

        # Load grading
        grading_path = run_dir / "grading.json"
        grading = None
        if grading_path.exists():
            try:
                grading = json.loads(grading_path.read_text())
            except (json.JSONDecodeError, IOError):
                pass

        # Extract prompt from metadata or transcript
        prompt = metadata.get("prompt", "")
        if not prompt:
            transcript_path = run_dir / "transcript.md"
            if transcript_path.exists():
                content = transcript_path.read_text()
                # Try to extract prompt from transcript
                if "## Prompt" in content:
                    start = content.find("## Prompt") + len("## Prompt")
                    end = content.find("##", start)
                    prompt = content[start:end].strip() if end > start else content[start:start+500].strip()

        runs.append({
            "run_id": run_id,
            "outputs_dir": str(path),
            "prompt": prompt,
            "grading": grading,
            "metadata": metadata,
        })

    return sorted(runs, key=lambda r: r["run_id"])


def embed_file(file_path: Path) -> dict:
    """Embed a file's content for the viewer."""
    mime_type, _ = mimetypes.guess_type(str(file_path))
    mime_type = mime_type or "application/octet-stream"

    # Text files - embed directly
    text_types = [
        "text/", "application/json", "application/xml",
        "application/javascript", "application/x-python",
    ]
    if any(mime_type.startswith(t) or t in mime_type for t in text_types):
        try:
            content = file_path.read_text()
            return {
                "name": file_path.name,
                "type": "text",
                "mime": mime_type,
                "content": content,
            }
        except UnicodeDecodeError:
            pass

    # Images - base64 encode
    if mime_type.startswith("image/"):
        content = base64.b64encode(file_path.read_bytes()).decode()
        return {
            "name": file_path.name,
            "type": "image",
            "mime": mime_type,
            "content": f"data:{mime_type};base64,{content}",
        }

    # Binary files - base64 for download
    content = base64.b64encode(file_path.read_bytes()).decode()
    return {
        "name": file_path.name,
        "type": "binary",
        "mime": mime_type,
        "content": content,
    }


def build_run_data(runs: list[dict], previous_workspace: Path | None = None) -> list[dict]:
    """Build complete run data with embedded files."""
    result = []

    for run in runs:
        outputs_dir = Path(run["outputs_dir"])
        files = []

        for f in sorted(outputs_dir.iterdir()):
            if f.is_file():
                files.append(embed_file(f))

        run_data = {
            **run,
            "files": files,
        }

        # Load previous output if available
        if previous_workspace:
            prev_outputs = previous_workspace / outputs_dir.relative_to(outputs_dir.parents[2])
            if prev_outputs.exists():
                prev_files = []
                for f in sorted(prev_outputs.iterdir()):
                    if f.is_file():
                        prev_files.append(embed_file(f))
                run_data["previous_files"] = prev_files

        result.append(run_data)

    return result


def generate_html(
    runs: list[dict],
    skill_name: str,
    benchmark: dict | None = None,
    previous_feedback: dict | None = None,
) -> str:
    """Generate the complete HTML viewer."""
    # This is a simplified version - the full viewer.html template would be much larger
    runs_json = json.dumps(runs)
    benchmark_json = json.dumps(benchmark) if benchmark else "null"
    feedback_json = json.dumps(previous_feedback) if previous_feedback else "{}"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eval Review - {skill_name}</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Lora:wght@400;500&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Poppins', sans-serif;
            background: #faf9f5;
            color: #1a1a1a;
            line-height: 1.6;
        }}
        .header {{
            background: white;
            padding: 1rem 2rem;
            border-bottom: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
        }}
        .title {{
            font-family: 'Lora', serif;
            font-size: 1.5rem;
        }}
        .nav {{
            display: flex;
            gap: 1rem;
            align-items: center;
        }}
        .tabs {{
            display: flex;
            gap: 0.5rem;
        }}
        .tab {{
            padding: 0.5rem 1rem;
            border: none;
            background: #f0f0f0;
            border-radius: 6px;
            cursor: pointer;
            font-family: inherit;
        }}
        .tab.active {{
            background: #2d2d2d;
            color: white;
        }}
        .counter {{
            font-size: 0.875rem;
            color: #666;
        }}
        .nav-buttons {{
            display: flex;
            gap: 0.5rem;
        }}
        .nav-btn {{
            padding: 0.5rem 1rem;
            border: 1px solid #ddd;
            background: white;
            border-radius: 6px;
            cursor: pointer;
            font-family: inherit;
        }}
        .nav-btn:hover {{ background: #f5f5f5; }}
        .nav-btn:disabled {{ opacity: 0.5; cursor: not-allowed; }}
        .content {{
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .panel {{
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .panel-title {{
            font-size: 1rem;
            font-weight: 500;
            margin-bottom: 1rem;
            color: #444;
        }}
        .prompt {{
            background: #f5f5f5;
            padding: 1rem;
            border-radius: 6px;
            font-family: monospace;
            font-size: 0.875rem;
            white-space: pre-wrap;
        }}
        .file {{
            border: 1px solid #eee;
            border-radius: 6px;
            margin-bottom: 1rem;
            overflow: hidden;
        }}
        .file-header {{
            background: #f5f5f5;
            padding: 0.5rem 1rem;
            font-size: 0.875rem;
            font-weight: 500;
            border-bottom: 1px solid #eee;
        }}
        .file-content {{
            padding: 1rem;
            max-height: 400px;
            overflow: auto;
        }}
        .file-content pre {{
            font-family: monospace;
            font-size: 0.813rem;
            white-space: pre-wrap;
            word-break: break-word;
        }}
        .file-content img {{
            max-width: 100%;
            height: auto;
        }}
        .feedback-area {{
            width: 100%;
            min-height: 100px;
            padding: 1rem;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-family: inherit;
            font-size: 0.875rem;
            resize: vertical;
        }}
        .feedback-status {{
            font-size: 0.75rem;
            color: #666;
            margin-top: 0.5rem;
        }}
        .grading {{
            margin-top: 1rem;
        }}
        .expectation {{
            display: flex;
            gap: 0.5rem;
            padding: 0.5rem;
            border-radius: 4px;
            margin-bottom: 0.5rem;
        }}
        .expectation.pass {{ background: #e8f5e9; }}
        .expectation.fail {{ background: #ffebee; }}
        .expectation-icon {{ font-weight: bold; }}
        .expectation.pass .expectation-icon {{ color: #2e7d32; }}
        .expectation.fail .expectation-icon {{ color: #c62828; }}
        .submit-btn {{
            padding: 0.75rem 1.5rem;
            background: #2e7d32;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-family: inherit;
            font-weight: 500;
        }}
        .submit-btn:hover {{ background: #1b5e20; }}
        .submit-btn:disabled {{ background: #ccc; cursor: not-allowed; }}
        .benchmark-tab {{ display: none; }}
        .benchmark-tab.active {{ display: block; }}
        .outputs-tab {{ display: block; }}
        .outputs-tab.hidden {{ display: none; }}
        .collapsible {{
            cursor: pointer;
            user-select: none;
        }}
        .collapsible::before {{
            content: '▶ ';
            font-size: 0.75rem;
        }}
        .collapsible.open::before {{
            content: '▼ ';
        }}
        .collapsible-content {{
            display: none;
            margin-top: 0.5rem;
        }}
        .collapsible-content.open {{
            display: block;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1 class="title">Eval Review: {skill_name}</h1>
        <div class="nav">
            <div class="tabs">
                <button class="tab active" onclick="showTab('outputs')">Outputs</button>
                <button class="tab" onclick="showTab('benchmark')">Benchmark</button>
            </div>
            <span class="counter"><span id="current">1</span> / <span id="total">0</span></span>
            <div class="nav-buttons">
                <button class="nav-btn" id="prev-btn" onclick="navigate(-1)">← Prev</button>
                <button class="nav-btn" id="next-btn" onclick="navigate(1)">Next →</button>
            </div>
            <button class="submit-btn" id="submit-btn" onclick="submitReviews()" disabled>Submit All Reviews</button>
        </div>
    </div>

    <div class="content">
        <div class="outputs-tab" id="outputs-tab"></div>
        <div class="benchmark-tab" id="benchmark-tab"></div>
    </div>

    <script>
        const runs = {runs_json};
        const benchmark = {benchmark_json};
        const previousFeedback = {feedback_json};

        let currentIndex = 0;
        let visited = new Set();
        let feedback = {{}};

        // Initialize feedback from previous
        if (previousFeedback.reviews) {{
            previousFeedback.reviews.forEach(r => {{
                feedback[r.run_id] = r.feedback;
            }});
        }}

        function showTab(tab) {{
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelector(`.tab:nth-child(${{tab === 'outputs' ? 1 : 2}})`).classList.add('active');

            document.getElementById('outputs-tab').classList.toggle('hidden', tab !== 'outputs');
            document.getElementById('benchmark-tab').classList.toggle('active', tab === 'benchmark');

            if (tab === 'benchmark') {{
                renderBenchmark();
            }}
        }}

        function navigate(delta) {{
            currentIndex = Math.max(0, Math.min(runs.length - 1, currentIndex + delta));
            renderCurrent();
        }}

        function renderCurrent() {{
            if (runs.length === 0) return;

            visited.add(currentIndex);
            const run = runs[currentIndex];

            document.getElementById('current').textContent = currentIndex + 1;
            document.getElementById('total').textContent = runs.length;

            document.getElementById('prev-btn').disabled = currentIndex === 0;
            document.getElementById('next-btn').disabled = currentIndex === runs.length - 1;

            // Enable submit when all visited
            document.getElementById('submit-btn').disabled = visited.size < runs.length;

            let html = `
                <div class="panel">
                    <div class="panel-title">Prompt</div>
                    <div class="prompt">${{escapeHtml(run.prompt || 'No prompt available')}}</div>
                </div>

                <div class="panel">
                    <div class="panel-title">Outputs</div>
                    ${{run.files.map(f => renderFile(f)).join('')}}
                </div>
            `;

            // Previous output (if available)
            if (run.previous_files && run.previous_files.length > 0) {{
                html += `
                    <div class="panel">
                        <div class="panel-title collapsible" onclick="toggleCollapsible(this)">Previous Output</div>
                        <div class="collapsible-content">
                            ${{run.previous_files.map(f => renderFile(f)).join('')}}
                        </div>
                    </div>
                `;
            }}

            // Grading (if available)
            if (run.grading && run.grading.expectations) {{
                html += `
                    <div class="panel">
                        <div class="panel-title collapsible" onclick="toggleCollapsible(this)">
                            Formal Grades (${{run.grading.summary?.passed || 0}}/${{run.grading.summary?.total || 0}} passed)
                        </div>
                        <div class="collapsible-content grading">
                            ${{run.grading.expectations.map(e => `
                                <div class="expectation ${{e.passed ? 'pass' : 'fail'}}">
                                    <span class="expectation-icon">${{e.passed ? '✓' : '✗'}}</span>
                                    <span>${{escapeHtml(e.text)}}</span>
                                </div>
                            `).join('')}}
                        </div>
                    </div>
                `;
            }}

            // Feedback
            const savedFeedback = feedback[run.run_id] || '';
            html += `
                <div class="panel">
                    <div class="panel-title">Feedback</div>
                    <textarea class="feedback-area" id="feedback-input"
                        placeholder="Enter your feedback for this output..."
                        onchange="saveFeedback()"
                        onkeyup="saveFeedback()">${{escapeHtml(savedFeedback)}}</textarea>
                    <div class="feedback-status" id="feedback-status">Auto-saves as you type</div>
                </div>
            `;

            document.getElementById('outputs-tab').innerHTML = html;
        }}

        function renderFile(file) {{
            let content = '';
            if (file.type === 'text') {{
                content = `<pre>${{escapeHtml(file.content)}}</pre>`;
            }} else if (file.type === 'image') {{
                content = `<img src="${{file.content}}" alt="${{file.name}}">`;
            }} else {{
                content = `<a href="data:${{file.mime}};base64,${{file.content}}" download="${{file.name}}">Download ${{file.name}}</a>`;
            }}

            return `
                <div class="file">
                    <div class="file-header">${{escapeHtml(file.name)}}</div>
                    <div class="file-content">${{content}}</div>
                </div>
            `;
        }}

        function renderBenchmark() {{
            if (!benchmark) {{
                document.getElementById('benchmark-tab').innerHTML = '<div class="panel"><p>No benchmark data available.</p></div>';
                return;
            }}

            let html = `
                <div class="panel">
                    <div class="panel-title">Summary</div>
                    <table style="width: 100%; border-collapse: collapse;">
                        <tr style="border-bottom: 1px solid #eee;">
                            <th style="text-align: left; padding: 0.5rem;">Config</th>
                            <th style="text-align: left; padding: 0.5rem;">Pass Rate</th>
                            <th style="text-align: left; padding: 0.5rem;">Time</th>
                            <th style="text-align: left; padding: 0.5rem;">Tokens</th>
                        </tr>
            `;

            for (const [config, stats] of Object.entries(benchmark.summary || {{}})) {{
                if (config === 'delta') continue;
                html += `
                    <tr style="border-bottom: 1px solid #eee;">
                        <td style="padding: 0.5rem;">${{config}}</td>
                        <td style="padding: 0.5rem;">${{(stats.pass_rate?.mean * 100).toFixed(1)}}% ± ${{(stats.pass_rate?.std * 100).toFixed(1)}}%</td>
                        <td style="padding: 0.5rem;">${{stats.time_seconds?.mean?.toFixed(1)}}s</td>
                        <td style="padding: 0.5rem;">${{Math.round(stats.tokens?.mean || 0)}}</td>
                    </tr>
                `;
            }}

            html += '</table></div>';

            // Individual runs
            html += '<div class="panel"><div class="panel-title">Individual Runs</div><table style="width: 100%; border-collapse: collapse;">';
            html += '<tr style="border-bottom: 1px solid #eee;"><th style="text-align: left; padding: 0.5rem;">Eval</th><th style="text-align: left; padding: 0.5rem;">Config</th><th style="text-align: left; padding: 0.5rem;">Pass Rate</th></tr>';

            for (const run of benchmark.runs || []) {{
                html += `<tr style="border-bottom: 1px solid #eee;"><td style="padding: 0.5rem;">${{run.eval_id}}</td><td style="padding: 0.5rem;">${{run.config}}</td><td style="padding: 0.5rem;">${{(run.pass_rate * 100).toFixed(0)}}%</td></tr>`;
            }}

            html += '</table></div>';

            document.getElementById('benchmark-tab').innerHTML = html;
        }}

        function toggleCollapsible(element) {{
            element.classList.toggle('open');
            element.nextElementSibling.classList.toggle('open');
        }}

        function saveFeedback() {{
            const run = runs[currentIndex];
            const input = document.getElementById('feedback-input');
            feedback[run.run_id] = input.value;
            document.getElementById('feedback-status').textContent = 'Saved';
            setTimeout(() => {{
                document.getElementById('feedback-status').textContent = 'Auto-saves as you type';
            }}, 1000);
        }}

        function submitReviews() {{
            const data = {{
                reviews: Object.entries(feedback).map(([run_id, fb]) => ({{
                    run_id,
                    feedback: fb,
                    timestamp: new Date().toISOString()
                }})),
                status: 'complete'
            }};

            // Try to POST to server first
            fetch('/feedback', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify(data)
            }}).then(response => {{
                if (response.ok) {{
                    alert('Feedback submitted successfully!');
                }} else {{
                    throw new Error('Server error');
                }}
            }}).catch(() => {{
                // Fallback: download as file
                const blob = new Blob([JSON.stringify(data, null, 2)], {{ type: 'application/json' }});
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'feedback.json';
                a.click();
                alert('Feedback downloaded as feedback.json. Copy it to the workspace directory.');
            }});
        }}

        function escapeHtml(text) {{
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }}

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {{
            if (e.target.tagName === 'TEXTAREA') return;
            if (e.key === 'ArrowLeft') navigate(-1);
            if (e.key === 'ArrowRight') navigate(1);
        }});

        // Initialize
        renderCurrent();
    </script>
</body>
</html>
"""


class ReviewHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler for the review server."""

    def __init__(self, *args, html_content=None, workspace=None, **kwargs):
        self.html_content = html_content
        self.workspace = workspace
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(self.html_content.encode())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/feedback":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)

            feedback_path = self.workspace / "feedback.json"
            feedback_path.write_bytes(data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "ok"}')
        else:
            self.send_error(404)

    def log_message(self, format, *args):
        pass  # Suppress logging


def serve(html: str, workspace: Path, port: int = 8765):
    """Start the review server."""
    handler_class = lambda *args, **kwargs: ReviewHandler(
        *args, html_content=html, workspace=workspace, **kwargs
    )

    for p in range(port, port + 10):
        try:
            with socketserver.TCPServer(("", p), handler_class) as httpd:
                url = f"http://localhost:{p}"
                print(f"Serving at {url}")
                webbrowser.open(url)
                httpd.serve_forever()
        except OSError:
            continue


def main():
    parser = argparse.ArgumentParser(description="Generate evaluation review interface")
    parser.add_argument("workspace", help="Path to workspace directory")
    parser.add_argument("--skill-name", required=True, help="Name of the skill")
    parser.add_argument("--benchmark", help="Path to benchmark.json")
    parser.add_argument("--previous-workspace", help="Path to previous iteration workspace")
    parser.add_argument("--static", help="Write static HTML to file instead of serving")
    parser.add_argument("--port", type=int, default=8765, help="Server port")

    args = parser.parse_args()

    workspace = Path(args.workspace)
    if not workspace.exists():
        print(f"Error: Workspace not found: {workspace}")
        sys.exit(1)

    # Find runs
    runs = find_runs(workspace)
    if not runs:
        print("No evaluation runs found in workspace")
        sys.exit(1)

    # Load previous workspace if specified
    previous = Path(args.previous_workspace) if args.previous_workspace else None

    # Build run data
    run_data = build_run_data(runs, previous)

    # Load benchmark if specified
    benchmark = None
    if args.benchmark:
        try:
            benchmark = json.loads(Path(args.benchmark).read_text())
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load benchmark: {e}")

    # Load previous feedback
    prev_feedback = None
    feedback_path = workspace / "feedback.json"
    if feedback_path.exists():
        try:
            prev_feedback = json.loads(feedback_path.read_text())
        except (json.JSONDecodeError, IOError):
            pass

    # Generate HTML
    html = generate_html(run_data, args.skill_name, benchmark, prev_feedback)

    if args.static:
        Path(args.static).write_text(html)
        print(f"Static HTML written to: {args.static}")
    else:
        serve(html, workspace, args.port)


if __name__ == "__main__":
    main()
