---
created: 2026-01-23
tags: [survey, google-forms, customer-discovery, mom-test, interview-design]
---

# Survey & Interview Question Writing Rules

Principles for creating effective Google Forms surveys and follow-up interviews aligned with The Mom Test framework.

---

## Survey-Specific Rules (Google Forms)

### DO

- **Use multiple choice for branching logic** — Identify segments early (Telegram, Arabicle, Self-taught)
- **Ask about PAST behavior** — "What did you pay last month?" not "Would you pay $20?"
- **Use checkboxes for multiple selections** — Resources used, frustrations, pain points
- **Keep survey under 10 minutes** — 15-20 questions maximum
- **Use linear scales for satisfaction** — 1-5 ratings show baseline metrics
- **Make questions under 20 words** — Clarity improves response quality
- **Test all conditional paths** — Verify every branching route works before publishing

### DON'T

- **Ask hypothetical future questions** — "Would you pay $20?" is guessing, not discovery
- **Use leading questions** — "Don't you think X is bad?" influences answers
- **Make required fields excessive** — Only essentials (segment ID, contact if interested)
- **Use paragraph text for numeric data** — Use short answer for amounts (price, hours)
- **Skip segment identification** — Need branching question early to customize experience
- **Include optional demographic fields** — Collect only what affects segment routing

---

## Interview-Specific Rules (Post-Survey)

### DO

- **Ask "Tell me about..."** — Prompts stories, not yes/no answers
- **Use silence to encourage elaboration** — Let uncomfortable pauses work for you
- **Ask "Why?" repeatedly** — Dig into motivation and constraints
- **Observe what they SHOW you** — Apps, notes, books, progress screenshots
- **Focus 80% listening, 20% asking** — Your job is to understand, not validate

### DON'T

- **Pitch your solution during interview** — You're learning, not selling
- **Accept vague answers** — "It's good/bad" needs concrete examples
- **Skip asking about money spent** — Real currency reveals true value
- **Move on without examples** — Every statement needs evidence
- **Talk about your idea before understanding theirs** — Listen first, pitch never

---

## Question Type Selection Guide

| Goal | Survey Type | Interview Follow-Up |
|------|-------------|-------------------|
| **Identify segment** | Multiple choice | "What are you using right now?" |
| **Measure satisfaction** | Linear scale (1-5) | "Tell me about your experience with X" |
| **Find pain points** | Checkboxes (multi-select) | "What frustrates you about X?" |
| **Validate willingness to pay** | Short answer (numeric) | "What did you pay for your last course?" |
| **Understand motivation** | Paragraph (open-ended) | "Why is learning Arabic important to you?" |
| **Screen for interviews** | Yes/No + contact info | N/A (the survey IS the first filter) |

---

## Google Forms Setup Checklist

- [ ] Segment branching question shows relevant sections only
- [ ] All conditional paths end in "Interview Consent" section
- [ ] Contact fields appear only for "Yes" or "Maybe" responses
- [ ] Linear scales use consistent 1-5 format across all questions
- [ ] Checkbox options include "Other (please specify)" where applicable
- [ ] No required fields except segment ID and contact (if interested)
- [ ] Survey preview tested on mobile device
- [ ] All text is clear and under 20 words per question

---

## Segment Routing Logic

```
Q5: "What are you using RIGHT NOW?"
├─ Telegram/WhatsApp classes → Section 2 (Segment 1)
├─ Arabicle.ru platform → Section 3 (Segment 2)
├─ Self-taught (YouTube, ChatGPT, etc.) → Section 4 (Segment 3)
└─ Not currently learning → Section 5 (Inactive learners)

All paths → Section 6 (Interview Consent & Contact)
```

---

## Red Flags in Survey Responses

Watch for these patterns when reviewing survey data:

- **High satisfaction (5/5) but low engagement** — Possibly satisficing (accepting adequate)
- **Willing to pay more than current spend** — Check if hypothetical (usually unreliable)
- **"Everything frustrates me" in checkboxes** — They may be venting; validate in interview
- **No contact info collected despite "Yes"** — They weren't serious; filter out
- **Time spent studying doesn't match motivation** — Motivation may be aspirational

---

## Interview Screening Criteria

**Priority for interviews (in order):**
1. Active users with specific frustrations (Segment 1 & 2)
2. High-commitment self-taught learners (Segment 3, 5+ hours/week)
3. Recently churned users (Segment 5, wanting to restart)
4. Edge cases with unique pain points

**Skip interviews with:**
- Zero engagement time (claimed to be learning but 0 hours/week)
- No contact info despite "Yes" to interview
- Clearly hypothetical answers ("I would maybe try if...")
