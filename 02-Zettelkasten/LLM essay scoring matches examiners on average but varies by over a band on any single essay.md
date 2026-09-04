---
aliases: [AI band scoring reliability, ChatGPT IELTS grading]
created: 2026-09-04
tags: [ielts, writing, ai, research]
---

Koraishi (2024) ran 55 officially graded Task 2 scripts through GPT-4 with a fixed examiner prompt and a fresh session per essay. The aggregate agreement is genuinely good: <mark style="background: #ADCCFFA6;">mean 6.027 for both human and model</mark>, intraclass correlation 0.814, weighted kappa 0.811.

The per-essay agreement is not. Bland-Altman limits of agreement are roughly <mark style="background: #FFB8EBA6;">±1.3 bands, with individual outliers of 1.5</mark> — against official Writing inter-rater reliability of 0.92.

Two things follow, and they point in opposite directions from the usual advice.

<mark style="background: #FFF3A3A6;">The popular claim that AI graders inflate by a band is not supported</mark> — this sample shows no mean bias at all. But "no mean bias" hides the shape of the error.

The wider automated-scoring literature identifies that shape as <mark style="background: #FFB8EBA6;">regression toward the mean</mark>: weak scripts are over-scored and strong scripts under-scored. Koraishi's own figures show it — the model's scores stop short of 8.0 where official grades reach it.

<mark style="background: #ADCCFFA6;">So the bias points the wrong way for a candidate near band 8: an LLM will tend to call a 7.5 a 7.</mark> Community reports match, including one candidate who fed it examiner-marked band 9 essays and got 7.5 back.

Two practical corollaries. Re-running the same essay buys little — models are largely self-consistent within a version, though they shift across version updates. And pushing back destroys the reading entirely: LLM judges abandon their verdict under casual disagreement, so "are you sure, I thought that was 7.5" reliably produces a 7.5.

Source: [Koraishi (2024), *Language Teaching Research Quarterly* 43, 22-42](https://files.eric.ed.gov/fulltext/EJ1457168.pdf) · [Regression effect in LLM essay scoring (arXiv 2401.03401)](https://arxiv.org/pdf/2401.03401) · [LLM judges under pushback (arXiv 2509.16533)](https://arxiv.org/abs/2509.16533)

### Read more
- [[Ask an LLM what rule a sentence breaks rather than what band the essay is]]
- [[Study hours convert into band gains worse as the starting band rises]]
