---
created: 2026-01-23
tags: [survey, segment-1, telegram, live-classes, customer-discovery]
---
# Segment 1: Telegram Live Class Students

Conditional survey questions for respondents using live classes via Telegram groups.

**Segment Goal:** Validate that Segment 1 learners will switch from free/cheap Telegram groups to hybrid model (pre-recorded + live practice) at $20-30/month.

**Interview Goal:** Understand what keeps them in live classes, what frustrates them, when/why they miss classes, what would make them upgrade.

---

## Q10: How much do you pay per month for live classes?
**Type:** Short answer (numeric)

**Purpose:** Current pricing anchor; validates stated $25-40/month; shows willingness to pay

**Example:** 30 (dollars/rubles equivalent)

**Red flag:** "Free" or "0" — means free Telegram group (different segment); reconfirm segment

---

## Q11: How many classes do you attend per week?
**Type:** Multiple choice (single select)

**Options:**
- 1-2 classes
- 3-4 classes
- 5+ classes
- It varies a lot

**Purpose:** Engagement frequency; shows commitment level

**Analysis:** 5+ classes = highly committed; 1-2 = exploring or busy; "varies" = scheduling conflict signal

---

## Q12: What do you LIKE about live classes?
**Type:** Checkboxes (multiple select)

**Options:**
- [ ] Ability to ask questions in real-time
- [ ] Structured curriculum
- [ ] Community/group motivation
- [ ] Teacher feedback and correction
- [ ] Flexible pacing (can pause, repeat)
- [ ] Personal connection to teacher
- [ ] Time accountability (scheduled time forces study)
- [ ] Other (please specify)

**Purpose:** Identify value drivers; what to preserve in new platform

**Interview follow-up:** "You said [community/accountability]. Tell me about that — what does that look like in your classes?"

---

## Q13: What FRUSTRATES you about live classes?
**Type:** Checkboxes (multiple select)

**Options:**
- [ ] Scheduling conflicts (can't attend consistently)
- [ ] Too fast pace (feel behind)
- [ ] Too slow pace (feel bored)
- [ ] Anxiety about speaking/asking questions
- [ ] Expensive
- [ ] No recording/can't review lessons later
- [ ] Technical issues (internet, audio quality)
- [ ] Group feels too large or too small
- [ ] Can't get personalized feedback
- [ ] Only interact during class (no support between sessions)
- [ ] Other (please specify)

**Purpose:** Identify pain points that hybrid model could solve

**Critical pain:** "No recording" + "Can't review" signals strong demand for pre-recorded content

**Interview follow-up:** "You mentioned [frustration]. Tell me about the last time that happened — what did you do?"

---

## Q14: Have you missed classes in the last month?
**Type:** Multiple choice (single select) — *CONDITIONAL BRANCHING*

**Options:**
- [ ] Yes, missed multiple classes → GO TO Q15
- [ ] Yes, missed 1-2 classes → GO TO Q15
- [ ] No, attended all classes → SKIP TO Q16

**Purpose:** Retention/engagement indicator; if missing classes = churn risk

**Red flag:** "Missed multiple" = potential churn; high priority for interview

---

## Q15: Why did you miss classes? *(conditional on Q14)*
**Type:** Checkboxes (multiple select)

**Options:**
- [ ] Work/schedule conflict
- [ ] Forgot/didn't get reminder
- [ ] Felt behind/overwhelmed
- [ ] Technical issues (internet didn't work)
- [ ] Lost motivation
- [ ] Sick or personal emergency
- [ ] Scheduling conflict with other commitment
- [ ] Other (please specify)

**Purpose:** Understand churn drivers

**Insight patterns:**
- "Schedule conflict" → Would pre-recorded help? (can study async)
- "Felt behind" → Need better onboarding or remedial content
- "Lost motivation" → JTBD not being met; interview priority HIGH

**Interview follow-up:** "You mentioned [reason]. Walk me through exactly what happened that day."

---

## Q16: On a scale of 1-5, how satisfied are you with live classes?
**Type:** Linear scale (1-5)

**Scale:**
- 1 = Very unsatisfied
- 2 = Somewhat unsatisfied
- 3 = Neutral
- 4 = Somewhat satisfied
- 5 = Very satisfied

**Purpose:** Baseline satisfaction metric for comparison after trying hybrid model

**Analysis:**
- 5 = Very sticky; would be hard to convert; but valuable for validating "what's working"
- 4 = Some friction; good candidate for hybrid model test
- 1-3 = At-risk churn; high priority for interview to understand if fixable

---

## Routing After Q16

All respondents → **Proceed to Section 6: Interview Consent & Contact**

See: [[General-Questions#Section 6 Interview Consent & Contact]]

---

## Interview Script (After Survey Match)

When interviewing Segment 1 respondents, prioritize these topics:

1. **Community effect** (5-7 min)
   - "Tell me about the group dynamic in your Telegram class. What's the community like?"
   - "Have you connected with other classmates outside of class?"
   - "What would you lose if you switched to something else?"

2. **Switching costs** (3-5 min)
   - "You've been with live classes for [timeline from survey]. What would it take to try something new?"
   - "How much flexibility do you need in your schedule?"

3. **Hybrid model test** (5-10 min)
   - "Imagine you could watch pre-recorded lessons at your own pace, but still had live group practice sessions. What's appealing about that? What concerns you?"
   - "How important is the ability to review lessons vs getting real-time feedback?"

4. **Pricing** (2-3 min)
   - "You mentioned paying $[amount] per month. What would be a fair price for pre-recorded + practice combo?"
   - "At what price would you say 'no, too expensive'?"

---

## Common Segment 1 Patterns

| Survey Response | Interpretation | Interview Value |
|-----------------|----------------|-----------------|
| Likes: community, accountability | Social motivation | Test: would async model kill engagement? |
| Frustrates: schedule conflicts | Inflexibility issue | Solution fit: pre-recorded addresses this |
| Missing classes regularly | Churn risk | **PRIORITY** — understand real blocker |
| Willing to pay $25-40+ | Price acceptance | Can we charge $20-30? |
| 5+ hours/week commitment | Serious learner | Long-term retention potential |

