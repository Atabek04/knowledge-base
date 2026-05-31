# JSON Schemas

This document outlines the JSON schemas used throughout the skill-creator system.

---

## evals.json

Located in `evals/evals.json`. Defines evaluation test cases.

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": ["path/to/input/file.txt"],
      "assertions": [
        "Output file contains the processed data",
        "No errors in execution"
      ]
    }
  ]
}
```

**Fields:**
- `skill_name`: Identifier for the skill being tested
- `evals`: Array of test cases
  - `id`: Unique identifier for the eval
  - `prompt`: The task prompt to give Claude
  - `expected_output`: Human-readable description of expected result
  - `files`: Optional array of input file paths
  - `assertions`: Optional array of verifiable expectations

---

## history.json

Tracks version progression during Improve mode.

```json
{
  "started": "2024-01-15T10:30:00Z",
  "skill_name": "example-skill",
  "current_best_version": 3,
  "iterations": [
    {
      "version": 1,
      "parent_version": null,
      "pass_rate": 0.67,
      "grading_results": {...}
    }
  ]
}
```

**Fields:**
- `started`: ISO timestamp of when iteration began
- `skill_name`: Name of the skill being improved
- `current_best_version`: Version number with highest pass rate
- `iterations`: Array of iteration data
  - `version`: Version number
  - `parent_version`: Previous version this was based on
  - `pass_rate`: Overall pass rate for this version
  - `grading_results`: Full grading output

---

## grading.json

Output from the grader agent.

```json
{
  "expectations": [
    {
      "text": "The original expectation text",
      "passed": true,
      "evidence": "Specific quote or description"
    }
  ],
  "summary": {
    "passed": 2,
    "failed": 1,
    "total": 3,
    "pass_rate": 0.67
  },
  "execution_metrics": {
    "tool_calls": {"Read": 5, "Write": 2, "Bash": 8},
    "total_tool_calls": 15,
    "total_steps": 6,
    "errors_encountered": 0,
    "output_chars": 12450,
    "transcript_chars": 3200
  },
  "timing": {
    "executor_duration_seconds": 165.0,
    "grader_duration_seconds": 26.0,
    "total_duration_seconds": 191.0
  },
  "claims": [
    {
      "claim": "Statement being verified",
      "type": "factual",
      "verified": true,
      "evidence": "Supporting evidence"
    }
  ],
  "user_notes_summary": {
    "uncertainties": [],
    "needs_review": [],
    "workarounds": []
  },
  "eval_feedback": {
    "suggestions": [],
    "overall": "Assessment of eval quality"
  }
}
```

**Important:** The `expectations` array must use the fields `text`, `passed`, and `evidence` — the viewer depends on these exact field names.

---

## metrics.json

Executor agent output with execution statistics.

```json
{
  "tool_calls": {
    "Read": 5,
    "Write": 2,
    "Bash": 8
  },
  "total_tool_calls": 15,
  "total_steps": 6,
  "files_created": ["output.txt", "report.md"],
  "errors_encountered": 0,
  "output_chars": 12450,
  "transcript_chars": 3200
}
```

---

## timing.json

Captures wall clock timing data.

```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```

**Important:** Task notifications include `total_tokens` and `duration_ms` — save these immediately as they are not persisted elsewhere.

---

## benchmark.json

Comprehensive benchmark results for the viewer.

```json
{
  "metadata": {
    "skill_name": "example-skill",
    "generated_at": "2024-01-15T10:30:00Z",
    "iteration": 1
  },
  "runs": [
    {
      "eval_id": "descriptive-name",
      "config": "with_skill",
      "pass_rate": 1.0,
      "time_seconds": 45.2,
      "tokens": 12500,
      "expectations": [
        {"text": "...", "passed": true, "evidence": "..."}
      ]
    },
    {
      "eval_id": "descriptive-name",
      "config": "without_skill",
      "pass_rate": 0.67,
      "time_seconds": 62.1,
      "tokens": 18200,
      "expectations": [...]
    }
  ],
  "summary": {
    "with_skill": {
      "pass_rate": {"mean": 0.89, "std": 0.15, "min": 0.67, "max": 1.0},
      "time_seconds": {"mean": 48.3, "std": 12.1},
      "tokens": {"mean": 14200, "std": 3100}
    },
    "without_skill": {
      "pass_rate": {"mean": 0.56, "std": 0.21, "min": 0.33, "max": 0.83},
      "time_seconds": {"mean": 65.7, "std": 18.4},
      "tokens": {"mean": 21000, "std": 5200}
    },
    "delta": {
      "pass_rate": "+0.33",
      "time_seconds": "-17.4",
      "tokens": "-6800"
    }
  },
  "analyzer_notes": [
    "Assertion 'file exists' passes in both configs — consider strengthening"
  ]
}
```

**Fields:**
- `metadata`: Information about the benchmark run
- `runs`: Individual run data, ordered with `with_skill` before its baseline
- `summary`: Statistical aggregates per configuration
- `analyzer_notes`: Observations from the analyzer pass

---

## comparison.json

Output from blind comparator.

```json
{
  "winner": "A",
  "reasoning": "Detailed explanation of why A won",
  "rubric": {
    "content": {
      "correctness": {"A": 5, "B": 3},
      "completeness": {"A": 5, "B": 4},
      "accuracy": {"A": 5, "B": 5}
    },
    "structure": {
      "organization": {"A": 4, "B": 4},
      "formatting": {"A": 5, "B": 5},
      "usability": {"A": 5, "B": 4}
    }
  },
  "overall_scores": {"A": 8.5, "B": 6.8},
  "quality_assessment": {
    "A": {
      "strengths": ["..."],
      "weaknesses": ["..."]
    },
    "B": {
      "strengths": ["..."],
      "weaknesses": ["..."]
    }
  },
  "expectations": [
    {
      "text": "Expectation text",
      "A_passed": true,
      "B_passed": false
    }
  ],
  "expectation_summary": {
    "A_pass_rate": 1.0,
    "B_pass_rate": 0.5
  }
}
```

---

## analysis.json

Post-hoc analyzer output.

```json
{
  "comparison_summary": "Brief description of comparison outcome",
  "winner_analysis": {
    "instruction_score": 8,
    "key_strengths": [
      {
        "category": "Instructions",
        "observation": "Clear step-by-step process",
        "evidence": "Lines 45-60 of SKILL.md"
      }
    ],
    "execution_patterns": ["Used bundled script"]
  },
  "loser_analysis": {
    "instruction_score": 5,
    "key_weaknesses": [
      {
        "category": "Error Handling",
        "observation": "No guidance for failures",
        "evidence": "Transcript line 34"
      }
    ],
    "execution_patterns": ["Reinvented existing utility"]
  },
  "improvement_suggestions": [
    {
      "priority": "high",
      "suggestion": "Add bundled validation script",
      "rationale": "Winner had this, loser didn't",
      "expected_impact": "Would likely flip comparison"
    }
  ]
}
```

---

## eval_metadata.json

Per-eval metadata file in each eval directory.

```json
{
  "eval_id": 0,
  "eval_name": "descriptive-name-here",
  "prompt": "The user's task prompt",
  "assertions": [
    "Output file exists",
    "Contains expected data"
  ]
}
```

---

## feedback.json

User feedback from the review viewer.

```json
{
  "reviews": [
    {
      "run_id": "eval-0-with_skill",
      "feedback": "the chart is missing axis labels",
      "timestamp": "2024-01-15T10:45:00Z"
    },
    {
      "run_id": "eval-1-with_skill",
      "feedback": "",
      "timestamp": "2024-01-15T10:46:00Z"
    }
  ],
  "status": "complete"
}
```

Empty feedback means the user thought it was fine.
