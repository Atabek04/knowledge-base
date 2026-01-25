---
created: 2026-01-23
tags: [survey, customer-discovery, google-forms, interview-guide]
---
# Survey & Interview Framework — Index & Implementation Guide

Complete customer discovery framework for screening interview candidates and validating product assumptions through Google Forms.

---

## Quick Navigation

### Core Documents

1. **[[Survey-Rules]]** — Foundational principles for effective survey & interview question design
   - When to use multiple choice vs checkboxes vs linear scales
   - Common pitfalls to avoid
   - Question quality checklist

2. **[[General-Questions]]** — Pre-branching screening questions (all respondents)
   - Demographics & learning status
   - Motivation & commitment discovery
   - **Critical:** Segment identification via branching question
   - Time estimate: 5-7 minutes for all respondents

### Segment-Specific Files (Choose One Path)

3. **[[Segment-Telegram-Live-Classes]]** — For active Telegram/WhatsApp live class students
   - Segment 1: Current users of live classes ($25-40/month)
   - 7 conditional question sets (Q10-Q16)
   - Interview script with follow-up priorities

4. **[[Segment-Arabicle-Users]]** — For active Arabicle.ru platform users
   - Segment 2: Current or active users ($48.97 one-time)
   - 7 conditional question sets (Q10-Q16)
   - Competitive analysis insights

5. **[[Segment-Self-Taught]]** — For active free resource learners
   - Segment 3: YouTube, ChatGPT, textbooks (entirely free)
   - 8 conditional question sets (Q10-Q17)
   - Pricing discovery and willingness-to-pay exploration

6. **[[Segment-Inactive-Wanting-Restart]]** — For inactive learners wanting to restart
   - Special segment: Previously used any method, stopped, wants to restart
   - Questions asked in **past tense** with churn analysis focus
   - 13 conditional question sets (Q10-Q22)
   - Reactivation triggers and product-market fit insights

### All-Respondent Closing

7. **[[Interview-Consent-Section]]** — Interview screening & contact collection (all segments)
   - Interview opportunity gating (Yes/No/Maybe)
   - Contact information (Telegram/Email)
   - Scheduling preferences
   - Data quality validation
   - Outreach workflow

---

## Survey Flow Architecture

```
START: Google Forms Survey
│
├─> General-Questions (Q1-Q9)
│   ├─> Q4: Are you currently learning?
│   │
│   ├─ YES (actively learning)
│   │  └─> Q5: What are you using RIGHT NOW?
│   │      ├─ Telegram → Segment-Telegram-Live-Classes (Q10-Q16)
│   │      ├─ Arabicle.ru → Segment-Arabicle-Users (Q10-Q16)
│   │      └─ Self-taught → Segment-Self-Taught (Q10-Q17)
│   │
│   ├─ "I STOPPED BUT WANT TO RESTART"
│   │  └─> Q4b: What WERE you using?
│   │      ├─ Telegram → Segment-Inactive-Wanting-Restart (Q10-Q22, past tense)
│   │      ├─ Arabicle.ru → Segment-Inactive-Wanting-Restart (Q10-Q22, past tense)
│   │      ├─ Self-taught → Segment-Inactive-Wanting-Restart (Q10-Q22, past tense)
│   │      └─ Other → Segment-Inactive-Wanting-Restart (Q10-Q22, generic path)
│   │
│   └─ NOT LEARNING / EXPLORING
│      └─> Skip Q5, Continue to Q6-Q9
│          └─> "Not Learning" path (secondary analysis)
│
├─ ALL PATHS CONVERGE
│  └─> Interview-Consent-Section (Q17/18/19-Q21)
│      ├─> Contact & Scheduling
│      └─> SURVEY COMPLETE
```

**Survey Completion Times by Path:**
- Active learners: 15-22 minutes
- Inactive wanting to restart: 18-25 minutes (deeper churn analysis)
- Not learning/exploring: 10-15 minutes

---

## Implementation Checklist

### Phase 1: Setup (Before Publishing)

- [ ] Create Google Forms with exact questions from files
- [ ] Set up conditional branching for Q4 (active vs stopped vs not learning)
- [ ] Set up conditional branching for Q4b (what method were you using when you stopped?)
- [ ] Set up conditional branching for Q5 (what are you using NOW for active learners)
- [ ] Create separate answer key for each segment (Sheets integration)
- [ ] Test all 5 paths: Telegram (active) → Arabicle (active) → Self-taught (active) → Inactive-Wanting-Restart → Not Learning
- [ ] Verify contact fields show ONLY on "Yes" or "Maybe" to interview
- [ ] Review on mobile device (most respondents use phones in Telegram)
- [ ] Set up email notifications for new responses
- [ ] Create respondent screening spreadsheet with prioritization columns

### Phase 2: Publishing (Go-Live)

- [ ] Write 2-3 sentence intro post for Telegram group
  - Do NOT say: "We're creating a competitor product"
  - DO say: "We're researching Arabic learning to understand what works and what doesn't"
- [ ] Pin survey link for 24-48 hours
- [ ] Include incentive (optional): "Top 20 respondents invited to 1:1 conversation"
- [ ] Ensure group admin approval before posting
- [ ] Post follow-up reminder at 24 hours ("Last chance to share feedback")

### Phase 3: Response Management

- [ ] **Daily:** Review new responses, tag priority respondents
- [ ] **Every 10 responses:** Update analysis spreadsheet
- [ ] **By Day 3:** Begin contacting Tier 1 priority candidates
- [ ] **By Day 7:** Contact should be extended to Tier 2
- [ ] **By Day 14:** Close survey, begin interview scheduling

### Phase 4: Interview Scheduling

- [ ] Use contact info from Q19-Q20 (Telegram/Email + preferred time)
- [ ] Send outreach message referencing their survey answer (Q21 personalization)
- [ ] Confirm 24 hours before scheduled interview
- [ ] Prepare segment-specific interview script
- [ ] Set up recording (with permission) for note review

---

## Key Decision Points in Survey

### Critical Gate 1: Q4 (Current Learning Status)

| Answer | Routing | Impact |
|--------|---------|--------|
| Yes, actively learning now | → Q5 (What method RIGHT NOW?) | Standard 3-segment path |
| I stopped but want to restart | → Q4b (What method WERE you using?) | Churn analysis + reactivation |
| Not learning / Exploring | → Skip Q5, continue to Q6-Q9 | Secondary analysis segment |

**Purpose:** Separates active learners from churn/inactive, enabling appropriate question framing.

### Critical Gate 1b: Q4b (Previous Method for Inactive) — *Conditional on Q4="Stopped wanting restart"*

| Answer | Routing | Impact |
|--------|---------|--------|
| Telegram/WhatsApp | → Segment-Inactive (Telegram context) | Understand live class churn |
| Arabicle.ru | → Segment-Inactive (Arabicle context) | Validate churn reasons |
| Self-taught | → Segment-Inactive (Self-taught context) | Understand free-learner churn |
| Other / Don't remember | → Segment-Inactive (generic path) | Generic reactivation analysis |

**Purpose:** Maintains segment context while asking past-tense questions.

### Critical Gate 2: Q5 (Current Method for Active Learners) — *Conditional on Q4="Yes, actively learning"*

| Answer | Routing | Impact |
|--------|---------|--------|
| Telegram/WhatsApp | → Segment-Telegram-Live-Classes (Q10-Q16) | High willingness to pay validation |
| Arabicle.ru | → Segment-Arabicle-Users (Q10-Q16) | Competitive analysis & satisfaction |
| Free resources (YouTube, ChatGPT, etc.) | → Segment-Self-Taught (Q10-Q17) | Conversion from free → paid discovery |
| Not currently learning (mistake) | → Reroute or clear up | Data validation |

**Action:** If response is vague ("I use multiple"), ask for PRIMARY method → reselect category.

### Critical Gate 3: Q17 (Interview Consent)

| Answer | Action |
|--------|--------|
| Yes | Collect contact (Q19) + timing (Q20) — HIGH PRIORITY |
| Maybe | Collect contact (Q19) + timing (Q20) — MEDIUM PRIORITY |
| No | Skip to thank you — do NOT contact |

**Fraud Prevention:** If respondent says "Yes" but leaves Q19 empty, mark as "no serious intent" — don't contact.

---

## Response Analysis & Prioritization

### Interview Priority Framework

**TIER 1: HIGHEST PRIORITY** (Interview first)

- **Inactive wanting to restart** (Q4b answer) — Pre-qualified buyers with churn insight
  - Especially if churned < 3 months ago (Q12 answer)
  - OR if satisfied (Q22 rating 4-5) but life happened
- Segment 1 or 2 (current/active customers with sunk costs)
- Active learners (Q4 = "actively learning") + 5+ hours/week + "Yes" to interview + complete contact
- Specific pain points or high frustration mentioned

**TIER 2: MEDIUM PRIORITY**

- Inactive wanting to restart with vague churn reason or older churn (6+ months)
- Segment 3 (self-taught) with 5+ hours/week + willing to pay $20+ + "Yes" to interview
- "Maybe" to interview with complete info (any segment)
- Active learners with medium engagement (3-5 hours/week)

**TIER 3: LOWER PRIORITY**

- "Maybe" to interview with incomplete info
- Low engagement (1-3 hours/week)
- Exploratory mindset ("just looking")
- Inactive wanting to restart with low confidence in Q20 (1-2 rating)

**DO NOT CONTACT**

- "No" to interview
- No contact information
- Clearly hypothetical responses ("I would maybe try if...")
- Zero hours/week study time

---

## Quality Metrics: What Good Survey Data Looks Like

### Response Quality Indicators ✓

- Specific numbers in short-answer fields (prices, hours, months)
- Detailed frustrations in open-ended questions (not "it's okay")
- Multiple checkbox selections (not just "other")
- Segment-specific context in answers (mentions specific platform)
- Contact info provided + interview consent given

### Red Flags ⚠️

- All checkboxes selected ("I want everything")
- Generic one-word answers ("good," "bad," "hard")
- Inconsistent data (says 0 hours/week but marked "actively learning")
- No segment specificity (answers apply to everyone)
- Respondent "just exploring" with no actual usage

---

## Interview Follow-Up Templates

### Tier 1 Outreach (Within 24 Hours of Response)

```
Hi [Name]!

Thanks for filling out the survey. You mentioned [reference something from Q12 or Q21], and that really resonated with what we're hearing from others.

We'd love to chat with you briefly about your experience — just 20-30 minutes when you're free.

You mentioned [preferred time from Q20], so we could try [specific time slots].

Does that work?

Looking forward to connecting!
```

### Tier 2 Outreach (Day 3-5)

Similar template but emphasize: "Only reaching out to 15-20 people total based on their responses."

### Interview Prep (24 Hours Before Call)

- Review their survey answers
- Prepare segment-specific script
- Identify 2-3 follow-up questions based on their Q12/Q14 answer
- Test audio/video setup

---

## Related Documentation

- **[[../Interview Scripts by Segment]]** — Detailed interview execution scripts with follow-up questions
- **[[../Interview Red Flags & Validation Checklist]]** — Quality control during interviews
- **[[../Customer Interview Analysis]]** — Analytical framework: why these assumptions matter
- **[[../../CLAUDE.md]]** — Zettelkasten writing style and knowledge management rules

---

## Common Questions

**Q: Can I use this survey outside Telegram groups?**
A: Yes. Modify the platform references (replace "Telegram" with context-appropriate channel) but keep the segment routing logic and branching structure.

**Q: How do I handle "Other (please specify)" responses?**
A: If a respondent selects "Other," review their specified text. If it creates a new segment, note it for Phase 2 (plan future interviews). Don't force them into existing segments.

**Q: What if most respondents refuse to be interviewed?**
A: This is valuable data. It suggests:
- Survey incentive wasn't compelling
- Ask earlier in the survey why they're hesitant to be contacted
- Consider offering $5 gift card for interviews

**Q: Should I offer a prize for completing the survey?**
A: Optional. If resources allow, offering $5-10 gift card for interviews (not surveys) improves contact quality significantly. Most respondents agree to "maybe," but gift card filters for serious candidates.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.1 | 2026-01-23 | Added Segment-Inactive-Wanting-Restart: Q4b conditional routing, past-tense questions, churn analysis focus |
| 1.0 | 2026-01-23 | Initial survey framework: 6 component files, segmented branching, interview consent flow |

---

**Status:** Ready for implementation in Google Forms

**Next Step:** Copy question text from individual segment files into Google Forms, set up conditional branching per routing logic above

**Implementation Priority:** Set up Q4 → Q4b → Q5 conditional logic first (foundational routing)

