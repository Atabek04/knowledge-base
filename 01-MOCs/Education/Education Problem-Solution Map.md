---
created: 2026-10-12
tags: [moc, product]
aliases: [Problem-Solution Map, EdTech Problem Map]
draft: true
---

Each section names one problem in education, the evidence that it is real, and how an AI learning platform could solve it better, cheaper, and for more learners, Muslim learners first. The atomic notes stay general; this map is where research turns into product decisions.

Every entry has the same seven fields. A lever with no evidence is a hypothesis to test in a pilot, never a feature to promise.

---

## 1. Learners forget most of what they study

- **Evidence:** retrieval practice beats rereading (g = 0.50, Rowland 2014); spaced beats massed retrieval (g = 0.74, Latimier 2021).
- **Root cause:** schools teach once and test once; nothing schedules review.
- **Platform lever:** every lesson ends in retrieval questions, rescheduled by a spacing algorithm per learner.
- **AI's role:** generate varied retrieval items from the lesson, so review is not the same card repeated.
- **Risk:** expanding intervals add nothing over even ones (g = 0.03); do not sell a complex scheduler as the benefit.
- **Access and cost:** works offline on a cheap phone; no teacher time needed.
- **Status:** evidence strong; build first.

## 2. One-to-one tutoring works but only the rich can afford it

- **Evidence:** human tutoring 0.29 SD across 89 RCTs (Nickow 2023); Bloom's 2 sigma shrinks in modern evidence.
- **Root cause:** a tutor's hour is expensive, and rural Kazakhstan has few tutors.
- **Platform lever:** an AI tutor that gives step-level hints, never final answers.
- **AI's role:** Socratic dialogue, error diagnosis, explanation in the learner's language.
- **Risk:** plain chatbots raise practice scores and lower exam scores (Bastani 2025); intelligent tutors show near-zero effect in K-12 maths (Steenbergen-Hu and Cooper).
- **Access and cost:** marginal cost per learner is model inference, falling yearly.
- **Status:** promising, contested; the thesis pilot tests it.

## 3. AI makes cheating easy and erodes skill

- **Evidence:** AI help without guardrails lowers unassisted performance (Bastani 2025); heavy use correlates with weaker critical thinking (Gerlich 2025, correlational).
- **Root cause:** homework can no longer prove a skill.
- **Platform lever:** hint-only tutor, write-before-AI flow, oral or live follow-up checks.
- **AI's role:** generate follow-up questions that a copied answer cannot survive.
- **Risk:** surveillance-style proctoring harms trust; avoid it.
- **Access and cost:** cheaper than human oral exams at scale.
- **Status:** design principle for every feature.

## 4. Learners quit before they finish

- **Evidence:** average MOOC completion 6.5% (Jordan 2014).
- **Root cause:** no teacher, no peers, no visible progress.
- **Platform lever:** short sessions, visible mastery, teacher in the loop, peer accountability.
- **AI's role:** detect disengagement early and alert the teacher, not just the learner.
- **Risk:** streaks and rewards can turn into dark patterns.
- **Access and cost:** retention is what makes a low price sustainable.
- **Status:** needs a pilot metric that is learning, not time on app.

## 5. Gamification motivates in the short term but can backfire

- **Evidence:** learning g = 0.49, motivation 0.36, behaviour 0.25, and only the learning effect survives rigorous studies (Sailer and Homner 2020); tangible rewards cut free-choice interest by d = -0.28 to -0.40 (Deci, Koestner and Ryan 1999).
- **Root cause:** points reward the behaviour, not the understanding.
- **Platform lever:** game elements that serve competence and autonomy (mastery maps, choice), not leaderboards.
- **AI's role:** adapt challenge to the learner so success stays reachable (Hexad-type personalisation).
- **Risk:** leaderboards and social comparison; novelty fades within weeks.
- **Access and cost:** no extra cost.
- **Status:** the thesis's central question.

## 6. Teachers have no time and do not adopt tools

- **Evidence:** most EdTech averages an effect of 0.16 and falls in large studies (Cheung and Slavin 2013); adoption depends on teacher fit (Scherer 2019).
- **Root cause:** tools add work instead of removing it.
- **Platform lever:** the teacher designs the path and acts on a dashboard; the AI tutors and grades routine work.
- **AI's role:** draft items, mark practice, summarise who is stuck.
- **Risk:** a dashboard nobody opens.
- **Access and cost:** saves teacher hours, which is the selling point to schools.
- **Status:** co-design with pilot teachers.

## 7. Feedback is slow, generic, or harmful

- **Evidence:** feedback d = 0.48 (Wisniewski 2020), but over a third of feedback interventions lower performance (Kluger and DeNisi 1996).
- **Root cause:** feedback about the person, or too late to act on.
- **Platform lever:** immediate, task-level feedback on each step.
- **AI's role:** explain the specific error, not "wrong, try again".
- **Risk:** feedback that gives the answer replaces the thinking.
- **Access and cost:** instant feedback costs almost nothing per learner.
- **Status:** evidence strong.

## 8. Arabic learners stall between script, grammar and real use

- **Evidence:** explicit instruction beats implicit in second language learning (Norris and Ortega 2000); incidental vocabulary gains are small, 9 to 18% of words (Webb 2023).
- **Root cause:** diglossia, and courses that teach grammar without meaningful input.
- **Platform lever:** explicit grammar plus graded reading, spaced vocabulary, Quranic and classical goals as a track.
- **AI's role:** generate graded texts and converse at the learner's level.
- **Risk:** LLM quality in Arabic is uneven; verify generated text.
- **Access and cost:** a qualified Arabic teacher is scarce outside cities.
- **Status:** second product.

## 9. Children's data is at risk

- **Evidence:** Kazakhstan requires local storage (Law 94-V art. 12) and consent for automated decisions affecting rights (art. 19-1).
- **Root cause:** EdTech business models built on data.
- **Platform lever:** data minimisation, local hosting, explainable adaptivity.
- **AI's role:** run personalisation without sending identifiable data abroad.
- **Risk:** inBloom closed over privacy fears despite $100M.
- **Access and cost:** compliance is cheaper designed in than retrofitted.
- **Status:** precondition for the pilot.

## 10. Learners with special needs are left out

- **Evidence:** phonics is the only confirmed reading approach for dyslexia (g = 0.32, Galuschka 2014); WCAG 2.2 is the current standard.
- **Root cause:** one pace, one format.
- **Platform lever:** accessible by default, adjustable pace, text-to-speech, dyslexia-friendly reading mode.
- **AI's role:** adapt text difficulty and modality per learner.
- **Risk:** UDL has weak evidence; do not cite it as proof.
- **Access and cost:** the same build serves everyone.
- **Status:** build in from the start.

---

## Related MOCs

- [[Learning Science MOC]]
- [[Learner Development & Motivation MOC]]
- [[AI in Education MOC]]
- [[Gamification & Learning Analytics MOC]]
- [[EdTech Product & Policy MOC]]
- [[Second Language Acquisition MOC]]
- [[Islamic Educational Thought MOC]]
