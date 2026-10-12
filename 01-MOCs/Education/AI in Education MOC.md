---
created: 2026-10-03
tags: [moc]
aliases: [AI in Education]
---

What AI does to learning and teaching: when it tutors, when it becomes a crutch, and what is left for the human teacher and the school. Doubles as the roadmap for the thesis on AI-powered personalized learning, from tutoring-system architecture and learner models to the trials that test large language model tutors.

Parent: none. Read in order; each section assumes the ones above. Teaching progress: discussion series, topic 5 (why attend university) next.

---

## 1. Discussion Series: Education in the Age of AI (Core)

- [[Students rate a polished lecture higher yet learn more from active learning|1. Lecture: a fluent explanation feels like learning but isn't]]
- [[In AI-supported learning the teacher designs the path and acts on data while the AI tutors|2. Teacher as orchestrator: designs the path, AI tutors]]
- [[An oral exam with live follow-up questions proves a skill that AI-written homework can no longer prove|3. Assessment: live follow-ups prove what homework can't]]
	- [[Curve grading ranks students against each other while criterion grading measures them against a fixed standard|Curve grading ranks; criterion grading measures]]
- [[One-to-one tutoring beats classroom teaching but Bloom's two sigma gain shrinks to under one sigma in later evidence|4. Mentorship: tutoring wins, but 2 sigma is really under 1]]
- [ ] 5. Why attend university when knowledge is free

## 2. Intelligent tutoring system anatomy and evidence (Core)

- [ ] An intelligent tutoring system has four parts: domain model, learner model, tutoring model, and interface (Woolf 2009)
- [ ] Step-based tutors give feedback on each solution step, unlike answer-based tutors that only grade the final answer (VanLehn 2011)
- [ ] Human tutoring and step-based tutoring reach about the same effect, while answer-based tutoring reaches less (VanLehn 2011)
- [ ] Intelligent tutoring systems beat conventional instruction with a clearly positive median effect (Kulik and Fletcher 2016)
- [ ] Tutoring-system effects on K-12 maths are near zero to small on standardized tests but moderate in college (Steenbergen-Hu and Cooper 2013)
- [ ] Meta-analytic effects shrink when the comparison group is stronger and the test is standardized rather than developer-made (Ma et al. 2014)
- [ ] Cognitive Tutor Algebra I showed a small first-cohort effect and a larger second-cohort effect, so implementation maturity matters (Pane et al. 2014)
- [ ] ASSISTments homework feedback produced a small but replicated gain in a large randomized trial of seventh grade maths (Roschelle et al. 2016)
- [ ] A tutor works by an outer loop that picks the next task and an inner loop that gives feedback within a task (VanLehn 2006)
- [ ] Model tracing follows each student step against an expert rule model, while constraint-based tutoring only checks that no rule is violated (Anderson 1995)
- [ ] Example-tracing tutors let non-programmers author tutors by demonstrating correct and incorrect solution paths (Aleven et al. 2016)

## 3. Tutoring dose and why Bloom's effect shrinks (Core)

- [ ] Bloom's two sigma claim came from small mastery-learning dissertations, not from a large trial (Bloom 1984)
- [ ] High-dosage school tutoring in modern randomized trials averages about 0.29 SD across 89 trials (Nickow, Oreopoulos and Quan 2023)
- [ ] Tutoring effects are larger for teacher or paraprofessional tutors than for volunteer or parent tutors (Nickow et al. 2020)
- [ ] Only some tutor-tutee events cause learning, which makes whole-session comparisons misleading (Chi et al. 2001)
- [ ] Human tutors do not tutor as ideally as theory says, yet reach large effects through scaffolding and error feedback (Chi et al. 2001)

## 4. Learner modeling and knowledge tracing (Core)

- [ ] A learner model estimates hidden knowledge from observed answers, which is why every adaptive system needs one (Pelanek 2017)
- [ ] Bayesian knowledge tracing models each skill as a hidden binary state with four parameters: prior, learn, slip, guess (Corbett and Anderson 1994)
- [ ] Slip and guess make a correct answer weaker evidence of mastery than naive percent correct suggests (Corbett and Anderson 1994)
- [ ] Performance factors analysis predicts the next answer from counts of past successes and failures on each skill (Pavlik, Cen and Koedinger 2009)
- [ ] Item response theory estimates learner ability and item difficulty on one scale, which supports calibrated item banks (Embretson and Reise 2000)
- [ ] The Elo rating system adapted for learning updates ability and difficulty after every answer and runs cheaply at scale (Pelanek 2016)
- [ ] Deep knowledge tracing predicts answers with a recurrent network but raised questions about interpretability and real gains (Piech et al. 2015)
- [ ] Extended Bayesian models matched deep knowledge tracing, and logistic regression won on moderate data (Khajah et al. 2016; Gervet et al. 2020)
- [ ] Mastery criteria such as a streak of correct answers perform close to full knowledge tracing in practice (Kelly et al. 2015)
- [ ] Prediction accuracy of a model is not learning benefit: test whether students actually learn more (Pelanek 2017)
- [ ] Cold start means a new learner has no history, so the first questions must carry the most information (Pelanek 2017)

## 5. Knowledge spaces, skill graphs and curriculum ontologies (Working)

- [[Concept prerequisite mapping sequences instruction along the dependency graph|Prerequisite mapping: sequence instruction along the dependency graph]]
- [ ] A knowledge space lists the feasible sets of mastered items, so one answer rules in or out many others (Doignon and Falmagne 1985)
- [ ] ALEKS uses a knowledge space to find the outer fringe, the topics a learner is ready to learn next (Falmagne et al. 2013)
- [ ] The Q-matrix maps each item to the skills it needs, and a wrong Q-matrix quietly corrupts every estimate (Tatsuoka 1983)
- [ ] A skill taxonomy needs a stable identifier scheme, or progress data cannot be compared across courses (Koedinger, Corbett and Perfetti 2012)
- [ ] Language models can draft prerequisite relations between concepts, but a subject expert must audit the graph (Aytekin and Saygin 2024)
- [ ] Mapping national curriculum standards to a skill graph is the technical heart of a Kazakhstan K-12 pilot (product inference, unverified)

## 6. Adaptive learning and educational recommenders (Working)

- [ ] AI-enabled adaptive learning systems show a moderate positive effect on outcomes with large variation by design (Wang et al. 2024)
- [ ] Adaptive sequencing should pick the item with the highest expected learning gain, not the one the learner will most likely get right (Pelanek 2017)
- [ ] Spacing and mastery thresholds can be combined so review items return before forgetting (Settles and Meeder 2016)
- [ ] Recommenders that maximize engagement can reduce learning, so the objective must be learning gain (Pelanek 2017)
- [ ] Matching instruction to learning styles has no support, while matching to prior knowledge does (Pashler et al. 2008)

## 7. Large language model tutors: what the trials show (Core)

- [[An AI tutor that gives hints instead of answers avoids the learning loss a plain chatbot causes|Hint-only AI tutors avoid the crutch effect]]
- [[Using AI to bypass work causes skill atrophy while using it for inquiry builds skill|Inquiry builds skill, bypassing the work atrophies it]]
- [[Writing unaided before turning to AI preserves the recall that starting with AI loses|Think first, then AI: order protects recall]]
- [[Effective AI learning removes friction from busywork and adds friction to thinking|Remove friction from busywork, keep it on thinking]]
- [[Treating AI as a collaborator rather than an assistant separates top learners|Treat AI as a collaborator, not an assistant]]
- [[Rich personal context is the main differentiator between elite and average AI users|Rich personal context separates elite AI users]]
- [[Doing reps with AI builds intuition for its real limits and capabilities|Reps with AI build intuition for its limits]]
- [ ] A scaffolded AI tutor beat in-class active learning in Harvard physics, with an effect of about 0.63 SD (Kestin et al. 2025)
- [ ] The Kestin tutor worked because its prompt forced step-by-step guidance built on instructor-written solutions (Kestin et al. 2025)
- [ ] A plain GPT-4 interface raised practice scores 48 percent but lowered later unassisted exam scores by 17 percent (Bastani et al. 2025)
- [ ] The hint-based tutor prompt avoided the exam drop but showed no exam gain over control either (Bastani et al. 2025)
- [ ] Students with an AI assistant reported learning more than they did, so self-report is an unreliable outcome (Bastani et al. 2025)
- [ ] A teacher-guided ChatGPT tutoring programme in Nigeria showed large six-week gains, but it is a working paper (De Simone et al. 2025, unverified)
- [ ] Tutor CoPilot coaches human tutors in real time and raises mastery most for the weakest tutors (Wang et al. 2024)
- [ ] Rori, a WhatsApp maths tutor in Ghana, shows a low-bandwidth AI tutor can work at scale (Henkel et al. 2024)
- [ ] Khanmigo has no peer-reviewed randomized trial yet, so its claims are product claims (vendor publications)
- [ ] Media comparisons of ChatGPT against no ChatGPT are confounded, and positive effects rarely isolate the cause (Lawson et al. 2026)
- [ ] Meta-analyses of ChatGPT in education report large positive effects, but most trials are short and weakly controlled (Deng et al. 2025)

## 8. Large language model failure modes in tutoring (Core)

- [[Desirable difficulties make learning harder in ways that improve long-term retention over short-term fluency|Desirable difficulties: answer-giving removes the retrieval that builds memory]]
- [[AI-assisted learners score about two letter grades lower with debugging the most degraded skill|AI-assisted learners score two grades lower: debugging hit worst]]
- [[Ten minutes of AI help makes people give up sooner on problems they then face alone|Ten minutes of AI help makes people quit sooner alone]]
- [[Routine AI assistance erodes an expert's existing skill, not only a learner's skill formation|Deskilling: routine AI erodes experts' existing skill too]]
- [[Heavy AI use correlates with weaker critical thinking but the causal arrow may run both ways|Heavy AI use tracks weaker thinking, causation unclear]]
- [[Trusting AI more predicts less critical thinking while trusting yourself predicts more|Trust in AI cuts checking; self-confidence raises it]]
- [[Over-relying on AI coding tools without reading output erodes genuine programming confidence|Vibe-coding without reading output erodes confidence]]
- [ ] Hallucination means a model produces fluent false content, and a tutor stating a false step teaches the error (Ji et al. 2023)
- [ ] Sycophancy means a model shifts its answer to please the user, so a tutor may confirm a wrong belief (Sharma et al. 2023)
- [ ] Metacognitive laziness means learners hand planning and monitoring to the AI, so the product improves while the skill stays flat (Fan et al. 2025)
- [ ] Cognitive offloading relieves working memory in the moment but weakens later memory of what was offloaded (Risko and Gilbert 2016)
- [ ] Accumulated cognitive debt appeared in AI-assisted essay writing, but the study is a 54-person preprint (Kosmyna et al. 2025)
- [ ] About a third of raw ChatGPT hints failed quality checks, and self-consistency cut that sharply, so generated help needs verification (Pardos and Bhandari 2024)
- [ ] Students asking the tutor for the answer is a jailbreak risk that a system prompt alone does not close (Bastani et al. 2025)

## 9. Pedagogical prompting, retrieval and guardrails (Core)

- [ ] A tutor prompt encodes pedagogy: ask before telling, give one hint at a time, never reveal the final answer (Kestin et al. 2025)
- [ ] Retrieval-augmented generation grounds tutor answers in the course material and cuts hallucination about local content (Lewis et al. 2020)
- [ ] Retrieval that pulls the wrong passage produces confident wrong answers, so retrieval quality is evaluated separately (Lewis et al. 2020)
- [ ] Combining a knowledge-tracing learner model with retrieval lets a language model target the learner's weak skills (Li et al. 2025)
- [ ] Multi-agent tutors separate planner, tutor and checker roles to keep goals and pedagogy consistent (Wang et al. 2025)
- [ ] Teacher-visible logs and dashboards let a human catch tutor failures and equalize feedback across students (Knoop-van Campen et al. 2023)
- [ ] Help-seeking must itself be taught, since students either abuse hints or avoid them (Aleven et al. 2003)

## 10. Evaluating AI tutors (Core)

- [ ] A fair tutor trial compares against a matched alternative with the same time on task, not against nothing (Kestin et al. 2025)
- [ ] Learning is measured by a delayed unassisted test, because performance with the tutor present misleads (Soderstrom and Bjork 2015)
- [ ] Developer-made tests inflate effects compared with standardized tests (Kulik and Fletcher 2016)
- [ ] Micro-randomized trials randomize tutor features per interaction, which suits fast iteration in small school pilots (Klasnja et al. 2015)
- [ ] Practice-time confounds appear when the AI group simply studies longer (Fischer et al. 2025)
- [ ] Offline benchmarks of tutor dialogue quality do not replace learning outcomes with real students (Burns 2026)

## 11. Chatbot and conversational agent meta-analyses (Working)

- [ ] Educational chatbots show a moderate positive effect that depends on duration, subject and pedagogical design (Alemdag 2023)
- [ ] Language-learning chatbots improve speaking and willingness to communicate, with short-term studies dominating (Lyu et al. 2024)
- [ ] Chatbots with structured pedagogy outperform open conversation (Zhang et al. 2026)

## 12. AI for item and content generation (Working)

- [ ] Language models write many practice items quickly, but each needs validation of key, distractors and difficulty (Kasneci et al. 2023)
- [ ] Generated items are calibrated by piloting them with learners and fitting item response theory parameters (Embretson and Reise 2000)
- [ ] Automatic question generation should be checked for answerability and alignment with the learning objective (Kurdi et al. 2020)
- [ ] Personalized textbook content generated by AI is promising but only vendor-evaluated (Google Research 2025)

## 13. Automated essay scoring and feedback (Working)

- [[LLM essay scoring matches examiners on average but varies by over a band on any single essay|LLM essay scoring: right on average, a band off on one essay]]
- [[Ask an LLM what rule a sentence breaks rather than what band the essay is|Ask the LLM which rule is broken, not which band]]
- [ ] Scoring models can be fooled by length and surface features, so they need adversarial checks (Perelman 2014)
- [ ] Fairness audits compare score error across subgroups, because average accuracy hides bias (Bridgeman et al. 2012)

## 14. The Future of Schooling (Aware)

- [[Education 2030 makes technology invisible while personalizing learning at scale|Education 2030: invisible tech, personalized at scale]]
- [[AI agent building is the foundational career skill of the next thirty years|Agent building: the foundational skill for 30 years]]

---

## Resources

### Books
- Woolf (2009, 1st ed.). *Building Intelligent Interactive Tutors*. Morgan Kaufmann/Elsevier. Clearest ITS architecture text. Start here.
- Nkambou, Bourdeau and Mizoguchi (eds., 2010). *Advances in Intelligent Tutoring Systems*. Springer. 24 chapters on domain, tutor and student modeling. Advanced.
- Falmagne and Doignon (2011). *Learning Spaces*. Springer. Graduate maths; basis of ALEKS. Advanced.
- Embretson and Reise (2000, 1st ed.). *Item Response Theory for Psychologists*. Lawrence Erlbaum. Standard applied IRT text.
- Baker (8th ed. open textbook). *Big Data and Education*. University of Pennsylvania, CC BY 4.0. Free educational data mining text with video lectures. Start here.
- Liu et al. (2021, revised 2024). *A Survey of Knowledge Tracing: Models, Variants, and Applications*. arXiv 2105.15106. Free survey with open-source code.

### Courses and lectures
- CMU LearnLab certificate courses (learnlab.org/certificate/courses): Introduction to Learning Engineering, then Adaptive Learning and Intelligent Tutoring Systems, ending in a capstone that redesigns a cognitive tutor.
- Ryan Baker, *Big Data and Education* video lectures (learninganalytics.upenn.edu/MOOT/bigdataeducation.html). The earlier Coursera version is unverified.
- Baker's EDM core-methods course schedules (learninganalytics.upenn.edu/ryanbaker/EDM2024/): tutorial-style path.

### Websites and blogs
- educationaldatamining.org: the EDM conference and the Journal of Educational Data Mining.
- Education Next (2023), "Two-Sigma Tutoring: Separating Science Fiction from Science Fact": readable critique of Bloom.
- Stanford SCALE repository (scale.stanford.edu): curated AI-in-education study abstracts.
- CMU DataShop (pslcdatashop.web.cmu.edu): open tutor interaction datasets (unverified).
- ASSISTments research pages (assistments.org) (unverified).

### YouTube
- None confirmed: no official channel for IEDMS, SoLAR, AIED Society or LearnLab was found.

### Podcasts
- Ed-Technical (Libby Hills and Owen Henkel), season 2 episode 6 with Ryan Baker: educational data mining and algorithmic bias.
- SoLAR Spotlight, episode 20, "Learning Analytics & AI: Opportunities & Challenges".
- Tec Sounds, episode 22 with George Siemens on learning analytics and AI.

### Key papers
- Nickow, Oreopoulos and Quan (2023). The Promise of Tutoring for PreK-12 Learning. AERJ. Pooled 0.288 SD over 89 RCTs. Replaces the two sigma expectation.
- Chi et al. (2001). Learning from human tutoring. Cognitive Science. What tutors actually do (unverified).
- Pane, Griffin, McCaffrey and Karam (2014). Effectiveness of Cognitive Tutor Algebra I at scale. EEPA 36(2). Cohort effects about 0.07 and 0.22 SD.
- Roschelle et al. (2016). Online mathematics homework increases student achievement. AERA Open. g 0.18, grade 7.
- Steenbergen-Hu and Cooper (2013, 2014). K-12 maths g 0.01 to 0.09; college g 0.32 to 0.37.
- Khajah, Lindsey and Mozer (2016). How deep is knowledge tracing? EDM. Extended BKT matches DKT.
- Gervet, Koedinger, Schneider and Mitchell (2020). When is deep learning the best approach to knowledge tracing? JEDM 12(3). Best model depends on data.
- Pavlik, Cen and Koedinger (2009). Performance factors analysis. AIED 2009.
- Sharma et al. (2023). Towards understanding sycophancy in language models. arXiv 2310.13548.
- Kosmyna et al. (2025). Your brain on ChatGPT. arXiv 2506.08872. Preprint, treat as hypothesis.
- Pardos and Bhandari (2024). ChatGPT-generated help produces learning gains equivalent to human tutor-authored help. PLOS ONE. About a third of raw hints failed quality checks.
- Pashler, McDaniel, Rohrer and Bjork (2008). Learning styles: concepts and evidence. Psychological Science in the Public Interest 9(3).

## Thesis papers to know
- Bloom (1984). The 2 sigma problem. Origin of the tutoring benchmark, now heavily discounted. `bloom1984sigma`
- Kulik and Fletcher (2016). Effectiveness of intelligent tutoring systems: a meta-analytic review. Standardized-test caveat. `kulik2016its`
- Ma, Adesope, Nesbit and Liu (2014). Intelligent tutoring systems and learning outcomes: a meta-analysis. Moderate effect, near parity with human tutors. `ma2014its`
- VanLehn (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. Interaction granularity thesis. `vanlehn2011tutoring`
- Wang et al. (2024). Efficacy of AI-enabled adaptive learning systems 2010 to 2022. Recent adaptive-learning effect size. `wang2024ai`
- Kestin et al. (2025). AI tutoring outperforms in-class active learning. Strongest LLM tutor RCT, single course. `kestin2025aitutor`
- Fischer, Rau and Rilke (2025). AI tutoring enhances student learning without crowding out reading effort. Tests substitution of effort. `fischer2025aitutoring`
- Fazlollahi et al. (2022). AI tutoring vs expert instruction for surgical skills. RCT in a skills domain. `fazlollahi2022aitutoring`
- Galindo-Dominguez et al. (2025). AI to promote adolescents' learning motivation. Self-determination angle. `galindo2025using`
- Futterer et al. (2026). Enhancing school students' self-regulated learning through generative AI support. School RCT. `futterer2026srl`
- Wang et al. (2025). LLM-powered multi-agent framework for goal-oriented learning in ITS (GenMentor). Multi-agent tutor architecture. `wang2025genmentor`
- Li et al. (2025). TutorLLM: knowledge tracing plus retrieval-augmented generation. Closest design to the thesis platform. `li2025tutorllm`
- Alemdag (2023). The effect of chatbots on learning: a meta-analysis. Chatbot baseline effect. `alemdag2023chatbot`
- Zhang, Zhang and Lu (2026). How do pedagogical approaches affect chatbot impact? Pedagogy as moderator. `zhang2026pedagogical`
- Nemeth et al. (2025). Retrieval-augmented generation in higher education tutoring: a pilot. `nemeth2025rag`
- Lyu, Lai and Guo (2024). Chatbots in language learning: meta-analysis. Relevant to the Arabic platform. `lyu2024chatbot`
- Wiboolyasarin et al. (2025). AI chatbots in second language education: systematic review. `wiboolyasarin2025chatbot`
- Wang et al. (2024). Conversational generative AI chatbots and EFL learners. Language anxiety outcomes. `wang2024chatbot`
- Pan et al. (2025). AI chatbots as reading companions. SDT lens (author list truncated, bib entry needs checking). `pan2025chatbot`
- Bastani et al. (2025). Generative AI without guardrails can harm learning. Key crutch-effect RCT; key year is 2024, published PNAS 2025. `bastani2024harm`
- Fan et al. (2025). Beware of metacognitive laziness. Defines the term empirically. `fan2025metacognitive`
- Lawson et al. (2026). Color me confounded. Critique of ChatGPT media comparisons (bib entry needs checking). `lawson2026confounded`
- Weidlich et al. (2025). ChatGPT in education: an effect in search of a cause. Same critique. `weidlich2025effectcause`
- Risko and Gilbert (2016). Cognitive offloading. Foundational theory. `risko2016offloading`
- Gerlich (2025). AI tools in society: cognitive offloading and critical thinking. Correlational, correction issued. `gerlich2025aitools`
- Jose et al. (2025). The cognitive paradox of AI in education. Review of enhancement vs erosion. `jose2025cognitiveparadox`
- Burns (2026). What the research shows about generative AI in tutoring (Brookings). Policy-level synthesis. `burns2026brookings`
- Google Research (2025). Learn Your Way. Vendor evaluation of generated personalized content. `google2025learnyourway`
- Kasneci et al. (2023). ChatGPT for good? Opportunities and challenges of LLMs for education. Standard overview. `kasneci2023chatgpt`
- Kohnke, Moorhouse and Zou (2023). ChatGPT for language teaching and learning. `kohnke2023chatgpt`
- Aleven et al. (2016). Example-tracing tutors. Cheap tutor authoring. `aleven2016exampletracing`
- De Simone et al. (2025). From chalkboards to chatbots, Nigeria. Large effect, working paper (bib entry needs checking). `desimone2025nigeria`
- Wang et al. (2024). Tutor CoPilot. Human-AI tutoring at scale. `wang2024tutorcopilot`
- Henkel et al. (2024). Rori AI tutor, Ghana. Low-resource deployment. `henkel2024rori`
- Harrison et al. (2026). Micro-randomised trials of AI tutoring in GCSE science. Preprint (bib entry needs checking). `harrison2026mrt`
- Klasnja et al. (2015). Microrandomized trials. Design basis. `klasnja2015mrt`
- Deng et al. (2025). Does ChatGPT enhance student learning? Meta-analysis. `deng2025chatgpt`
- Knoop-van Campen, Wise and Molenaar (2023). Equalizing effect of teacher dashboards. Teacher-in-the-loop evidence. `knoopvancampen2023dashboards`
- Corbett and Anderson (1994). Knowledge tracing. Origin of BKT. `corbett1994bkt`
- Piech et al. (2015). Deep knowledge tracing. Origin of DKT. `piech2015dkt`
- Pelanek (2017). BKT, logistic models and beyond. Best single overview of learner models. `pelanek2017overview`
- Doignon and Falmagne (1985). Spaces for the assessment of knowledge. Knowledge space theory root. `doignon1985spaces`
- Fang et al. (2019). Meta-analysis of ALEKS. Effect of a knowledge-space system. `fang2019aleks`
- Gagne (1968). Learning hierarchies. Prerequisite theory. `gagne1968hierarchies`
- Kelly et al. (2015). Defining mastery: knowledge tracing vs n consecutive correct. Simple rule vs model (bib entry needs checking, page range). `kelly2015mastery`
- Pelanek and Rihak (2017). Experimental analysis of mastery learning criteria. Mastery threshold choice. `pelanek2017mastery`
- Aytekin and Saygin (2024). ACE: AI-assisted construction of knowledge graphs with prerequisites. LLM-built skill graphs. `aytekin2024ace`
- Aleven et al. (2003). Help seeking and help design. Hint design theory. `aleven2003helpseeking`
- Roll et al. (2011). Improving help-seeking skills with metacognitive feedback. `roll2011helptutor`
- Klock et al. (2023). Adaptive gamification and motivation over time. Adaptive personalization (bib entry needs checking). `klock2023adaptive_gamification`
- Also in the bibliography: Kulik 1979 PSI meta-analysis `kulik1979psimeta`, Kulik 1990 mastery meta-analysis `kulik1990masterymeta`, Bloom 1968 mastery learning `bloom1968masterylearning`.

## Contested claims to avoid
- Bloom's two sigma as a current expectation: the original came from small mastery-learning studies; modern tutoring meta-analyses sit near 0.3 to 0.4 SD (Nickow et al. 2023; VanLehn 2011).
- "AI tutors double learning": the Kestin result is one course, one design, short horizon, and Bastani shows the opposite without guardrails.
- Deep knowledge tracing as clearly superior: extended BKT matched it and logistic regression won on moderate datasets (Khajah et al. 2016; Gervet et al. 2020).
- Learning styles personalization: no supporting evidence (Pashler et al. 2008).
- "Your brain on ChatGPT" brain-damage headlines: 54 participants, 18 in the final session, EEG, preprint (Kosmyna et al. 2025).
- Gerlich 2025 as proof that AI harms thinking: correlational, self-report, correction issued.
- Vendor claims (Khanmigo, Learn Your Way, the Nigeria working paper): no independent peer-reviewed trial confirmed.
- Self-reported learning with chatbots: students overestimate (Bastani et al. 2025).

## Related MOCs

- [[EdTech Product & Policy MOC]]: the AI law and child-safety rules an AI tutor must meet
- [[Gamification & Learning Analytics MOC]]: motivation design and the data side of adaptive systems
- [[Learning Science MOC]]: how memory and understanding work, the base both learning and teaching rest on
- [[Self-Study MOC]]: the learner's side, methods you apply to yourself
- [[Teaching & Instructional Design MOC]]: the teacher's side, designing lessons for others
- [[Agentic Engineering MOC]]: AI's effect on a developer's skill
- [[Research Craft - MOC]]: the thesis methodology
