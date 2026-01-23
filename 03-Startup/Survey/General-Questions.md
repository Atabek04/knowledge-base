---
created: 2026-01-23
tags: [survey, customer-discovery, screening, demographics, arabic-learning]
---

# General Screening Questions — All Respondents

Pre-branching questions for Google Forms survey. All respondents answer these questions before routing to segment-specific sections.

**Survey Goal:** Screen potential interview candidates from Telegram group, identify current learning method, understand motivation, collect baseline metrics.

---

## Section 1: Demographics & Learning Status

### Q1: How old are you?
**Type:** Short answer (numeric)

**Purpose:** Demographic screening, understand maturity and time availability

---

### Q2: Where are you located?
**Type:** Dropdown (single select)

**Options:**
- Russia
- Kazakhstan
- Uzbekistan
- Kyrgyzstan
- Other CIS country
- Other (please specify)

**Purpose:** Geographic filtering, understand time zone for interviews, market validation

---

### Q3: What do you do for work/study?
**Type:** Short answer (text)

**Purpose:** Understand time availability and budget context; identify if they're students (different willingness to pay)

---

### Q4: Are you currently learning Arabic?
**Type:** Multiple choice (single select) — *CRITICAL SCREENING*

**Options:**
- Yes, actively learning now → GO TO Q5
- I stopped but want to restart → GO TO Q4b
- Not learning and not planning to → SKIP TO Q6
- Not sure / just exploring → SKIP TO Q6

**Purpose:** Filter for active vs churned vs cold-prospect learners; affects interview priority

---

### Q4b: What were you using before you stopped? *(Conditional on "I stopped but want to restart")*
**Type:** Multiple choice (single select) — *SEGMENT IDENTIFICATION FOR INACTIVE*

**Options:**
- Live classes via Telegram or WhatsApp → **ROUTE TO: [[Segment-Inactive-Wanting-Restart]] (with Segment 1 context)**
- Arabicle.ru platform → **ROUTE TO: [[Segment-Inactive-Wanting-Restart]] (with Segment 2 context)**
- Self-taught (YouTube, textbooks, ChatGPT, etc.) → **ROUTE TO: [[Segment-Inactive-Wanting-Restart]] (with Segment 3 context)**
- Something else / I don't remember → **ROUTE TO: [[Segment-Inactive-Wanting-Restart]] (generic path)**

**Purpose:** Understand what method they previously used; enables past-tense questioning with segment context

---

### Q5: What are you using RIGHT NOW to learn Arabic? *(Conditional on Q4="Yes, actively learning")*
**Type:** Multiple choice (single select) — *BRANCHING LOGIC FOR ACTIVE LEARNERS*

**Options:**
- Live classes via Telegram or WhatsApp → **ROUTE TO: [[Segment-Telegram-Live-Classes]]**
- Arabicle.ru platform → **ROUTE TO: [[Segment-Arabicle-Users]]**
- Self-taught (YouTube, textbooks, ChatGPT, etc.) → **ROUTE TO: [[Segment-Self-Taught]]**
- I'm not currently learning (but thought I was) → **ROUTE TO: [[General-Questions#Section 5 (Not Learning)]]**

**Purpose:** Primary segmentation for active learners; determines all downstream questions and interview targeting

---

## Section 2: Motivation & Commitment

### Q6: Why is learning Arabic important to you?
**Type:** Checkboxes (multiple select)

**Options:**
- Read Quran in original language
- Read classical Islamic texts (hadith, fiqh, etc.)
- Understand Arabic grammar deeply
- Cultural/heritage connection
- Career/professional reasons
- Personal intellectual challenge
- Other (please specify)

**Purpose:** Understand motivation depth and how much "pull" the learner has (internal motivation = higher retention)

---

### Q7: What's your ultimate goal with Arabic?
**Type:** Paragraph (open-ended)

**Purpose:** Jobs-to-be-Done discovery; reveals desired outcome and helps identify unmet needs

**Example answer we're looking for:** "I want to understand the Quran without always needing translation. It's about connection to my faith and understanding the language as it was originally written."

---

### Q8: How much time do you study per week?
**Type:** Multiple choice (single select)

**Options:**
- Less than 1 hour
- 1-3 hours
- 3-5 hours
- 5-10 hours
- More than 10 hours

**Purpose:** Commitment level indicator; shows which learners are serious vs casual; affects segment analysis

---

## Section 3: Behavioral Anchor

### Q9: How long have you been learning Arabic?
**Type:** Multiple choice (single select)

**Options:**
- Less than 3 months
- 3-6 months
- 6-12 months
- 1-2 years
- 2+ years

**Purpose:** Timeline for understanding persistence, how many methods they've tried, expected churn signals

---

## Section 4: Skip Logic Reference

**Routing depends on Q4 and conditional questions:**

**If Q4 = "Yes, actively learning" (via Q5):**
- **Telegram Live Classes → See [[Segment-Telegram-Live-Classes]] Q10-Q16**
- **Arabicle.ru → See [[Segment-Arabicle-Users]] Q10-Q16**
- **Self-Taught → See [[Segment-Self-Taught]] Q10-Q17**

**If Q4 = "I stopped but want to restart" (via Q4b):**
- **Any previous method → See [[Segment-Inactive-Wanting-Restart]] Q10-Q22**
  - Questions asked in past tense with segment context
  - Focuses on churn reasons and reactivation triggers
  - Validates willingness to restart

**If Q4 = "Not learning/Exploring" (skip Q5, Q6-Q9, then):**
- **Not Currently Learning → See Section 5 (Not Learning Path)**

**All segments then proceed to → Section 6: [[Interview-Consent-Section|Interview Consent & Contact]]**

---

## Notes for Survey Administrator

- **Keep this section under 5 minutes** — General questions should not feel like an interview
- **Make only the branching questions required** — Optional fields increase completion rate
- **Test on mobile** — Most respondents will use phones in Telegram
- **Order matters** — Demographics first (easy), branching question in middle, commitment questions last
- **Don't reveal segments** — Don't say "This survey is about finding customers for our platform"

---

## Common Response Patterns

| Pattern | Interpretation | Interview Priority |
|---------|----------------|-------------------|
| Active learning + 5+ hours/week + strong JTBD | Highly engaged, serious learner | **HIGH** |
| Active learning + 1-3 hours/week + vague goal | Casual learner, lower commitment | MEDIUM |
| Stopped + wants to restart + clear churn reason | Pre-qualified buyer; reactivation gold mine | **PRIORITY** |
| Stopped < 3 months ago + specific trigger | Hot churn; insights are fresh and vivid | **PRIORITY** |
| Stopped but 6+ month engagement + satisfied | Life churn, not product churn; likely reactivatable | **HIGH** |
| "Just exploring" + low time commitment | Low intent; may not complete interview | LOW |
| Active + frustrated motivation + 3+ hours/week | At-risk learner; may churn soon | **HIGH** |

