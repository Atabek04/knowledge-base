---
created: 2026-10-12
tags: [moc]
aliases: [Gamification MOC, Learning Analytics MOC]
---

Gamification, game-based learning, learning analytics and experimentation: the evidence on what game mechanics do to motivation and learning, and how a platform measures and tests its own effect.
The thesis rests on this subject, because every claim about engagement must be separated from a claim about learning.

Parent: none. Read in order; each section assumes the ones above. Teaching progress: not started.

---

## 1. Gamification defined (Core)

- [ ] Gamification means using game design elements in a non-game context, unlike serious games or playful design (Deterding 2011)
- [ ] Game elements form a hierarchy from interface patterns through mechanics to principles and models (Deterding 2011)
- [ ] Points, badges and leaderboards are only the surface layer of gamification and the weakest evidence (Sailer 2017)
- [ ] Gamification adds elements to a task while game-based learning makes the game itself the task (Landers 2014)
- [ ] Gamification research is mostly short, small and weakly controlled, so stated effects need a skeptical reading (Dichev 2017, Hamari 2014)
- [ ] Self-determination theory is the standard lens: elements work through autonomy, competence and relatedness (Sailer 2017, Huang 2024)

## 2. Gamification meta-analyses (Core)

- [ ] Gamification has a small to medium positive effect on cognitive, motivational and behavioral outcomes (Sailer 2020)
- [ ] Effect sizes shrink under rigorous designs, so pooled quasi-experimental estimates overstate the truth (Sailer 2020, Huang 2020)
- [ ] Gamification raises intrinsic motivation, autonomy and relatedness but barely moves competence (Huang and Hew 2024)
- [ ] In K-12 the motivation effect exists but varies strongly by element, duration and subject (Kurnaz 2025)
- [ ] Academic performance gains depend on moderators such as duration, age and discipline (Zeng 2024)
- [ ] Gamification works better combined with narrative, collaboration or competence feedback than with points alone (Sailer 2020)
- [ ] Heterogeneity is huge, so the right question is which element, for whom, for how long (Dichev 2017)
- [ ] Language-learning gamification reviews show engagement gains with thin learning evidence (Zhang 2023, Shen 2024, Shortt 2023)

## 3. Where gamification backfires (Core)

- [ ] Extrinsic rewards undermine intrinsic motivation when expected, tangible and contingent on completion (Deci 1999)
- [ ] A gamified course lowered intrinsic motivation, satisfaction and exam scores versus a non-gamified one (Hanus and Fox 2015)
- [ ] Leaderboards demotivate low-ranked students more than they help top-ranked ones (Hanus and Fox 2015, Mekler 2017)
- [ ] Points, badges and leaderboards raised task performance without raising intrinsic motivation (Mekler 2017)
- [ ] The novelty effect inflates early results that fade over weeks, while familiarization can recover them (Rodrigues 2022)
- [ ] Game elements can reduce learning by consuming working memory and shifting attention from content to points (Landers 2014)
- [ ] Students can game the system by optimizing points instead of understanding (Dichev 2017)
- [ ] Claiming a gamification effect needs at minimum a longitudinal evaluation over a full term (Rodrigues 2022, Hanus and Fox 2015)

## 4. Serious games and game-based learning (Working)

- [ ] Digital games improve learning modestly compared to non-game instruction (Clark 2016, Wouters 2013)
- [ ] Games work better with feedback, scaffolding and debriefing than as unguided play (Wouters 2013, Mayer 2019)
- [ ] Games that integrate content into core mechanics beat games that bolt on quizzes (Habgood and Ainsworth 2011)
- [ ] Games were not found more motivating than conventional instruction, so motivation claims need care (Wouters 2013)
- [ ] Duolingo is the largest gamified platform, yet its efficacy evidence is company-linked and small (Vesselinov 2012, Loewen 2019)

## 5. Adaptive and personalized gamification (Working)

- [ ] The Hexad model types users as philanthropist, socializer, free spirit, achiever, player and disruptor (Tondello 2016)
- [ ] Matching elements to user type helps engagement in some studies but learning evidence is thin (Rodrigues 2022)
- [ ] Bartle player types came from MUD players and are untestable, so avoid them as a design basis (Yee, Bartle 1996)
- [ ] Choosing game elements per learner is an adaptation problem, treatable as a contextual bandit
- [ ] Behavior-based adaptation beats self-reported player types because questionnaires have modest reliability

## 6. Streaks, habit design and dark patterns (Working)

- [ ] Streaks use loss aversion to sustain daily use, raising retention but risking anxiety and shallow sessions
- [ ] A dark pattern steers users against their own interests, and engagement-maximizing streaks can qualify (Mathur 2019, Gray 2018)
- [ ] Ethical habit design asks whether the habit serves the learner's own goal, using forgiveness mechanics
- [[Track Returns Not Streaks — Resuming Fast Matters More Than Never Breaking|Streaks: resuming fast matters more than never breaking]]
- [ ] Planning prompts and scheduling nudges raise course completion without game mechanics (Yeomans and Reich 2017, Baker 2016)
- [ ] Children's platforms must exclude loot boxes and variable rewards, which also conflict with Islamic limits on gambling-like mechanics

## 7. Learning analytics and educational data mining (Core)

- [ ] Learning analytics is the measurement, collection, analysis and reporting of learner data to optimize learning (Siemens 2012)
- [ ] Educational data mining stresses automated discovery while learning analytics stresses human-in-the-loop decisions (Siemens and Baker 2012)
- [ ] A learning analytics dashboard helps only when teachers can turn it into action (Molenaar 2019, Verbert 2014)
- [ ] Teacher dashboards can equalize feedback across students in K-12 classrooms (Knoop-van Campen 2023)
- [ ] Early warning systems predict dropout, but prediction without effective intervention changes nothing (Arnold and Pistilli 2012)
- [ ] MOOC learners cluster into completing, auditing, disengaging and sampling subpopulations (Kizilcec 2013)
- [ ] Mastery criteria such as consecutive correct answers versus knowledge tracing change the learner experience measurably (Kelly 2015, Pelanek 2017)
- [ ] Predictive models in education carry bias risk, so audit error rates by subgroup (Baker and Hawn 2022)

## 8. Data standards: xAPI and Caliper (Working)

- [ ] xAPI records learning activity as actor, verb, object statements stored in a learning record store (ADL)
- [ ] IMS Caliper Analytics defines a metric-profile event model that competes with xAPI in institutions (1EdTech)
- [ ] An event schema should be designed from the research questions first, then mapped to xAPI or Caliper
- [ ] Learner data for minors needs a data-minimization stance

## 9. Engagement measurement (Working)

- [ ] School engagement has behavioral, emotional and cognitive facets, and logs capture mostly the behavioral one (Fredricks 2004)
- [ ] Self-report instruments such as the Student Engagement Instrument capture what logs cannot see
- [ ] The ICAP framework ranks engagement as passive, active, constructive, interactive in predicted learning order (Chi and Wylie 2014)
- [ ] Clickstream measures like time on task and streak length need validation against learning gains before use as outcomes
- [ ] Engagement is a means, so a platform claiming learning must measure learning directly

## 10. A/B testing and experimentation in education (Core)

- [ ] An A/B test is a randomized experiment inside a live product and gives causal evidence observational analytics cannot (Kohavi 2020)
- [ ] Micro-randomized trials randomize repeated intervention moments within a person, suiting just-in-time support (Klasnja 2015)
- [ ] Practitioner-led micro-randomized trials allow rapid evaluation of AI tutor variants (Harrison 2026)
- [ ] Optimizing engagement in A/B tests can select harmful designs, so the primary metric must be learning (Kohavi 2020)
- [ ] ASSISTments and Carnegie Learning trials show how to run replicable experiments at school scale (Heffernan 2014)
- [ ] A school pilot should randomize at class or school level and pre-register outcomes (Shadish 2002)
- [ ] Underpowered educational A/B tests produce noise, so compute sample size with clustering before launch

---

## Resources

### Books
- Kohavi, Tang, Xu (2020, 1st ed.). *Trustworthy Online Controlled Experiments*. Cambridge University Press. The general A/B reference. Advanced. https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59
- Lang, Siemens, Wise, Gasevic, Merceron (eds.) (2022, 2nd ed.). *Handbook of Learning Analytics*. SoLAR, open access. Standard entry point. Intermediate. https://solaresearch.org/hla-22/
- Plass, Mayer, Homer (eds.) (2020). *Handbook of Game-Based Learning*. MIT Press. Empirical and theory-grounded. Intermediate to advanced.
- Werbach and Hunter (2020, 2nd ed.). *For the Win*. Wharton School Press. Practitioner framework, weak on evidence. Start here for vocabulary (unverified imprint).
- Chou (2015). *Actionable Gamification*. Popular, evidence-light (unverified).
- Mayer (2014). *Computer Games for Learning*. MIT Press (unverified).

### Courses and lectures
- Baker, R. *Big Data and Education*. Open course from Penn and Teachers College covering prediction modeling, validation and knowledge inference. https://learninganalytics.upenn.edu/MOOC/bigdataeducation.html
- CMU LearnLab, *Introduction to Learning Engineering* (Koedinger). https://learnlab.org/introduction-to-learning-engineering/
- CMU LearnLab, *Quantitative and Experimental Methods for Designing and Evaluating Learning*. A/B testing of e-learning designs. https://learnlab.org/quantitative-and-experimental-methods-for-designing-and-evaluating-learning/
- Gasevic and Baker, 2016 learning analytics syllabus. https://learninganalytics.upenn.edu/ryanbaker/LA-PT-2016/LAK-PT-Spr2016-v3.pdf
- Coursera *Gamification* (Werbach, Wharton) (unverified)

### Websites and blogs
- SoLAR: https://www.solaresearch.org/
- SoLAR webinars: https://www.solaresearch.org/?p=7791
- Gamification research blog: https://gamification-research.org/2019/08/does-gamification-of-learning-work/
- HCI Games Group, Hexad scale: https://hcigames.com/the-gamification-user-types-hexad-scale/
- Penn Center for Learning Analytics: https://learninganalytics.upenn.edu/
- International Educational Data Mining Society, ADL xAPI and 1EdTech Caliper documentation (unverified, no URLs checked)

### YouTube
- SoLAR official channel: webinar and LAK recordings (unverified, channel URL and activity not confirmed)

### Podcasts
- SoLAR Spotlight podcast (unverified, current activity not confirmed)
- Humans of Learning Sciences Podcast (UIC): https://lsri.uic.edu/humans-of-learning-sciences-podcast
- Learning Science Weekly Podcast: workplace learning, gamification episode with Karl Kapp. Tangential to K-12.

### Key papers
- Deterding, Dixon, Khaled, Nacke (2011). From game design elements to gamefulness: defining gamification. MindTrek. The standard definition.
- Hamari, Koivisto, Sarsa (2014). Does gamification work? HICSS. Mixed outcomes across empirical studies.
- Bai, Hew, Huang (2020). Does gamification improve student learning outcome? Educational Research Review. g 0.504 over 30 interventions; varied with sample size and duration, not element type.
- Wouters, van Nimwegen, van Oostendorp, van der Spek (2013). Meta-analysis of the cognitive and motivational effects of serious games. J Educ Psychol 105(2). d 0.29 learning, 0.36 retention.
- Clark, Tanner-Smith, Killingsworth (2016). Digital games, design, and learning. Rev Educ Res 86(1). g 0.33 game versus non-game.
- Tondello et al. (2016). The gamification user types Hexad scale. CHI PLAY. Validated alternative to Bartle.
- Mekler, Bruhlmann, Tuch, Opwis (2017). Effects of individual gamification elements on intrinsic motivation and performance. Computers in Human Behavior.
- Siemens and Baker (2012). Learning analytics and educational data mining: towards communication and collaboration. LAK.
- Verbert et al. (2014). Learning dashboards: an overview and future research opportunities. Personal and Ubiquitous Computing.
- Mathur et al. (2019). Dark patterns at scale. CSCW.

## Thesis papers to know
- Sailer and Homner (2020). The gamification of learning: a meta-analysis. Anchor meta-analysis with outcome-wise effect sizes. `sailer2020gamification`
- Huang, Tlili, Chang, Zhang, Nascimbeni, Burgos (2020). Impact of gamification on student learning outcomes: a meta-analysis. Second major pooled estimate; confirm which paper owns the g 0.464 value before citing (bib entry needs checking). `huangr2020gamification`
- Huang and Hew (2024). Gamification enhances intrinsic motivation, autonomy and relatedness, but minimal impact on competency. SDT-based, key for the motivation argument. `huang2024gamification`
- Zeng, Sun, Looi, Fan (2024). Gamification and students' academic performance: meta-analysis 2008 to 2023. Most recent performance meta-analysis. `zeng2024gamification`
- Kurnaz and Koçtürk (2025). Meta-analysis of gamification's impact on student motivation in K-12. Matches the K-12 target. `kurnaz2025gamification`
- Zainuddin, Chu, Shujahat, Perera (2020). Systematic review of gamification empirical evidence. Broad review. `zainuddin2020gamification`
- Hanus and Fox (2015). Assessing the effects of gamification in the classroom. The classic backfire study. `hanus2015gamification`
- Rodrigues et al. (2022). Gamification suffers from the novelty effect but benefits from the familiarization effect. Longitudinal timing evidence. `rodrigues2022novelty`
- Dichev and Dicheva (2017). Gamifying education: what is known, believed and uncertain. Critical review with methodological warnings. `dichev2017gamifying`
- Sailer, Hense, Mayr, Mandl (2017). How gamification motivates. Element-level experiment on need satisfaction. `sailer2017gameelements`
- Unknown authors (2023). How does adaptive gamification impact different types of student motivation over time? Authors and DOI unverified, likely Klock et al. (bib entry needs checking). `klock2023adaptive_gamification`
- Zhang and Hasim (2023). Gamification in EFL/ESL instruction: systematic review. Language-learning relevance. `zhang2023efl_gamification`
- Shen, Lai, Wang (2024). Gamification and motivation in online language learning. `shen2024gamification`
- Shortt et al. (2023). Gamification in mobile-assisted language learning: Duolingo review. `shortt2023duolingoreview`
- Vesselinov and Grego (2012). Duolingo Effectiveness Study: Final Report. Company-commissioned, treat cautiously. `vesselinov2012duolingo`
- Loewen et al. (2019). Mobile-assisted language learning: a Duolingo case study. `loewen2019duolingo`
- Deci, Koestner, Ryan (1999). Meta-analytic review of extrinsic rewards and intrinsic motivation. Foundation of the overjustification argument. `deci1999meta`
- Knoop-van Campen, Wise, Molenaar (2023). Equalizing effect of teacher dashboards. `knoopvancampen2023dashboards`
- Molenaar and Knoop-van Campen (2019). How teachers make dashboard information actionable. `molenaar2019dashboards`
- Kizilcec, Piech, Schneider (2013). Deconstructing disengagement in MOOCs. Learner clusters. `kizilcec2013disengagement`
- Kelly, Wang, Thompson, Heffernan (2015). Defining mastery: knowledge tracing versus n-consecutive correct. `kelly2015mastery`
- Pelanek (2017). Experimental analysis of mastery learning criteria. `pelanek2017mastery`
- Klasnja et al. (2015). Microrandomized trials. `klasnja2015mrt`
- Harrison et al. (2026). Evaluating AI tutoring at the speed of innovation: micro-randomised trials. `harrison2026mrt`
- Yeomans and Reich (2017). Planning prompts increase course completion in MOOCs. `yeomans2017planning`
- Baker et al. (2016). Scheduling nudge MOOC experiment. `baker2016scheduling`
- Patterson (2018). Can behavioral tools improve online student outcomes? `patterson2018behavioral`
- van Klaveren et al. (2017). Adaptive versus static practicing: field experiment. `vanklaveren2017adaptive`
- Fredricks, Blumenfeld, Paris (2004). School engagement. `fredricks2004engagement`
- Chi and Wylie (2014). The ICAP framework: linking cognitive engagement to active learning outcomes. `chi2014icap`
- Shadish, Cook, Campbell (2002). Experimental and quasi-experimental designs. Design backbone for pilots. (no bibtex key in report)

## Contested claims to avoid
- Gamification "increases engagement by X percent": vendor numbers, unreviewed; meta-analyses show small to moderate, heterogeneous effects (Sailer 2020, Dichev 2017).
- Bartle's four player types as a learner design basis: derived from MUD players, no educational validation (Yee).
- Player-type matching as proven personalization: thin evidence.
- Duolingo "34 hours equals a university semester": company-commissioned, small, not independent (Vesselinov 2012).
- Course Signals as a proven retention success: later analyses questioned its causal claims.
- Leaderboards as universal motivators: they help some and demotivate many (Hanus and Fox 2015).
- Pooled gamification effect sizes read as causal: most included studies are quasi-experimental and short (Sailer 2020).

## Related MOCs
- [[Education Research Methods MOC]]: designing and analysing the gamification pilot
- [[Learner Development & Motivation MOC]]: motivation theory behind every gamification claim
- [[AI in Education MOC]]: AI tutoring that these experiments evaluate
