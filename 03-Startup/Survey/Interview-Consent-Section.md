---
created: 2026-01-23
tags: [survey, interview-screening, contact-collection, consent]
---

# Section 6: Interview Consent & Contact — All Respondents

Final section shown to all respondents after completing segment-specific questions. Screens for interview candidates and collects contact information.

---

## Q17/18/19: Interview Screening

### Q17: Interview Opportunity *(CRITICAL GATE)*
**Type:** Multiple choice (single select)

**Question:** "We're looking for people to interview for 20-30 minutes to understand Arabic learning better. We'd like to have a conversation with you about your experience. Would you be willing?"

**Options:**
- [ ] Yes, I'm interested in being interviewed → SHOW Q18-Q21
- [ ] Maybe, depends on timing → SHOW Q18-Q21
- [ ] No, thank you → SKIP TO THANK YOU PAGE

**Purpose:** Screen for interview candidates; separate serious vs casual respondents

**Analysis:**
- "Yes" = strong signal; prioritize for contact
- "Maybe" = qualified interest; include in outreach
- "No" = end survey; do not contact

---

## Contact Information Section *(conditional on "Yes" or "Maybe")*

### Q18: What's your name?
**Type:** Short answer (text) — **OPTIONAL**

**Purpose:** Personalization for outreach; makes communication feel less mass-market

**Note:** Optional field; not required to proceed

**Tip:** Many respondents hesitate to give names; don't make required

---

### Q19: How can we reach you?
**Type:** Short answer (text) — **REQUIRED** (if Q17 = Yes/Maybe)

**Instruction:** "Email address or Telegram username"

**Purpose:** Primary contact method for scheduling interviews

**Format acceptance:**
- Email: ayub@example.com
- Telegram: @ayub_username

**Red flag:** If respondent selected "Yes" but leaves this empty, they may not be serious

---

### Q20: What's the best time to reach you?
**Type:** Checkboxes (multiple select)

**Options:**
- [ ] Morning (9am-12pm Moscow time)
- [ ] Afternoon (12pm-5pm Moscow time)
- [ ] Evening (5pm-9pm Moscow time)
- [ ] Weekend
- [ ] Anytime (flexible)

**Purpose:** Scheduling optimization; shows time zone and flexibility

**Analysis:**
- "Anytime" = highly available; good for interviews
- Multiple time windows = flexible
- Single narrow window = scheduling constraint; plan accordingly

---

### Q21: Is there anything else you'd like us to know about your Arabic learning journey?
**Type:** Paragraph (text) — **OPTIONAL**

**Purpose:** Bonus insights; rapport building for interview

**Example valuable responses:**
- "I'm studying because I want to read the Quran with my kids."
- "I'm frustrated because I feel like I'm hitting a wall with progress."
- "I'd love to connect with other learners — feeling isolated right now."

**Interview use:** Reference these comments when calling to build rapport ("You mentioned wanting to connect with other learners — that's something we're thinking about...")

---

## Survey Completion Page

### Thank You Message

Display this message to all survey completers:

> **Thank you for your feedback!**
>
> If you agreed to an interview, we'll reach out within 3-5 business days via [email/Telegram] to schedule a time that works for you.
>
> Your insights help us understand how to better serve Arabic learners. We're grateful for your time.
>
> If you have questions, reply to this survey or reach out to [contact email/Telegram].

---

## Interview Outreach Workflow

### Contact Priority Ranking

**Tier 1: HIGHEST PRIORITY** (Interview first)
- Active learners (Q4 = "Yes, actively learning")
- Segment 1 or 2 (paying customers or ex-customers)
- High engagement (5+ hours/week from General Q8)
- Specific pain points mentioned (Q12 for self-taught, Q13 for Arabicle)
- "Yes" to interview (Q17 = Yes)
- Completed contact info (Q19 provided)

**Tier 2: MEDIUM PRIORITY**
- Active learners with "Maybe" to interview
- Segment 3 (self-taught) with 3+ hours/week commitment
- Willing to pay $20+ per month (Q16)
- "Maybe" to interview with complete contact info

**Tier 3: LOWER PRIORITY** (Interview if time allows)
- Inactive learners wanting to restart (Q4 = "stopped but want to restart")
- "Maybe" to interview with incomplete contact info
- Low engagement levels (1-3 hours/week) but expressed interest

**Do NOT Contact:**
- "No" to interview (Q17 = No)
- No contact information provided (Q19 = empty)
- Clearly hypothetical answers ("just exploring," 0 hours/week study)

---

## Email/Telegram Outreach Template

### For Telegram Users

```
Hi [Name if provided, else "Friend"]!

Thanks again for filling out our Arabic learning survey.

We'd love to chat with you briefly about your experience —
just 20-30 minutes whenever works best for you.

You mentioned [reference something from Q21 or their segment]
and we'd love to hear more about that.

What times work for you next week?
[List their preferred times from Q20]

Looking forward to connecting!
[Your name]
```

### For Email Users

Same message, but send via email.

---

## Data Validation Checklist

Before conducting interviews, validate survey data:

- [ ] Q5 answer (segment) clearly recorded
- [ ] Contact information is valid (email or Telegram handle)
- [ ] Q12 (biggest challenge) or Q14 (paid methods tried) show genuine response, not placeholder
- [ ] Time commitment (hours/week) is realistic (0 hours = not active learner)
- [ ] "Yes" to interview + contact info = ready to call

**Data Quality Issues:**
- Missing segment info → Contact anyway if data otherwise valid
- Invalid contact (fake email) → Mark as "bad data," don't contact
- Clearly joke responses → Skip
- Generic checkbox-only responses (no open-ended insight) → Lower priority

---

## Interview Scheduling Best Practices

1. **Text first, then call** — Telegram message or email asking for availability
2. **Confirm 24 hours before** — Reduce no-shows with reminder
3. **Record permission** — Ask at start of call: "Is it okay if I record this?"
4. **Quiet environment** — Interview should be 1:1, no background noise
5. **Prepare segment context** — Review their survey answers before calling
6. **Reference their answers** — "You mentioned [Q12 answer]. Tell me about that..."

---

## Common Response Patterns to Watch

| Pattern | Signal | Action |
|---------|--------|--------|
| Q17=Yes + Q19=empty | Not serious despite claim | Don't contact |
| Q17=Maybe + Q20=single evening | Interested but constrained | Contact with evening options first |
| Q21 is very detailed | Invested in experience | High-priority interview |
| Q21 is empty despite Q17=Yes | Time-starved or impulsive | May no-show; confirm harder |
| Multiple checkboxes in all questions | Careful respondent | Quality response; interview-ready |
| All single-click minimal answers | Low effort | Quality suspect; lower priority |

---

## Privacy & Data Handling

**Email collection for interviews only:**
- Do not add to marketing list without explicit consent
- Do not share with third parties
- Use for interview scheduling and follow-up only
- Offer option to opt-out from future contacts

**Telegram usernames:**
- Lower privacy concern (public-facing identifier)
- Still request permission before contacting

**Recording interviews:**
- Request explicit permission before recording
- Store recordings securely
- Do not share without consent
- Delete after analysis (typically 6 months)

