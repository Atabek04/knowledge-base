---
created: 2026-10-12
tags: [moc]
aliases: [Education Research Methods, EdTech Research Methods]
---

The methods needed to evaluate a learning platform with real pupils and defend the result in a master's thesis: ethics, design science, causal inference, power, multilevel models and measurement.
General research craft (argument, writing, defence) stays in the Research Craft MOC; this map covers only what is specific to evaluating educational interventions.

Parent: none. Read in order; each section assumes the ones above. Teaching progress: not started.

---

## 1. Research ethics with minors (Core)

- [ ] The Belmont principles (respect for persons, beneficence, justice) underpin ethics review of research with children (Belmont Report 1979)
- [ ] Research with children needs guardian consent plus the child's own assent in age-appropriate language (APA Ethics Code 2017)
- [ ] Participation must be separable from schooling and grades, so a non-participating pupil loses nothing (BERA 2018) (unverified)
- [ ] Kazakhstan Order 529 requires informed consent, safety, dignity and data consent, but its text does not mention minors (MSHE 2024)
- [ ] Order 529 demands a bioethics opinion only for biomedical research; an education study needs a commission only if the university says so (MSHE 2024)
- [ ] Kazakhstan Law 94-V lets a legal representative consent to personal data use and honours withdrawal within 15 working days (Law 94-V art 8)
- [ ] Telemetry with timestamps can identify a child in a small class, so pseudonymise and minimise (data-protection practice)
- [ ] A founder evaluating his own product has a conflict of interest to declare, for example by using independent outcome assessment (COPE) (unverified)

## 2. Design Science Research methodology (Core)

- [[Design science builds an artifact to test an idea and the knowledge from evaluating it is the contribution|Design science: artifact is the treatment, evaluation knowledge is the contribution]]
- [[Wieringa's engineering cycle separates validation before transfer from evaluation after it|Engineering cycle: validation is controlled context, evaluation is real use]]
- [ ] Design science research has three cycles: relevance, rigor and an inner design-evaluate loop (Hevner 2007)
- [ ] Hevner's seven guidelines are a reviewer checklist, and weak evaluation is where theses most often fail (Hevner et al. 2004)
- [ ] The Peffers DSRM process has six activities from problem identification to communication and four entry points (Peffers et al. 2007)
- [ ] A contribution is placed on a grid of solution versus problem maturity: invention, improvement, exaptation or routine design (Gregor and Hevner 2013)
- [ ] Routine design applies a known solution to a known problem and is not a research contribution (Gregor and Hevner 2013)
- [ ] A design theory bundles purpose, constructs, principles and testable propositions, so an artifact alone is not a theory (Gregor and Jones 2007)
- [ ] Wieringa's four knowledge-question types decide which empirical design a study needs: descriptive, explanatory, predictive, evaluative (Wieringa 2014)
- [ ] A validation claim holds only under stated context assumptions, so write artifact, requirements and context as a triple (Wieringa 2014)
- [ ] Evaluation methods should match the claim being made, not the convenience of the study (Hevner et al. 2004)

## 3. Design-based research in education (Working)

- [ ] Design-based research iterates a theory-driven intervention in real classrooms to refine both intervention and local theory (Design-Based Research Collective 2003)
- [ ] Design-based research and DSR differ in origin and output: local learning theory versus artifacts and design principles (Barab and Squire 2004)
- [ ] Design-based research is criticised for weak causal warrant and designer bias, so claims must be bounded (Anderson and Shattuck 2012)

## 4. Causal inference basics (Core)

- [ ] A causal effect compares what happened with what would have happened without treatment, never observed for the same student (Holland 1986)
- [ ] Random assignment equalises groups in expectation on everything, including unmeasured traits (Shadish et al. 2002)
- [ ] Selection into treatment is the central classroom threat, because intact classes differ before the intervention (Shadish et al. 2002)
- [ ] A confounder affects both treatment and outcome, and controlling for a collider or mediator can add bias (Pearl 2009; Hernan and Robins 2020)
- [ ] Intention-to-treat analysis keeps students in their assigned group, even if they never used the app (Hernan and Robins 2020)
- [ ] Mediation analysis is weaker than experiments for establishing mechanism (Spencer, Zanna and Fong 2005)
- [ ] A causal diagram drawn before data collection makes assumptions inspectable and decides what to adjust for (Pearl 2009; McElreath 2020)

## 5. Quasi-experimental designs with intact classes (Core)

- [ ] A nonequivalent-groups pretest-posttest design adjusts for, but does not remove, initial class differences (Shadish et al. 2002)
- [ ] Regression to the mean misleads studies that pick low scorers for an intervention (Shadish et al. 2002)
- [ ] Groups that start different may also grow at different rates, which a pretest cannot reveal (Shadish et al. 2002)
- [ ] A switching-replication or stepped-wedge design gives every class the treatment eventually and is the ethically easiest school design (Shadish et al. 2002)
- [ ] A counterbalanced crossover controls student differences but needs an argument about learning carryover (Lazar et al. 2017)
- [ ] Regression discontinuity estimates an effect at an assignment cutoff and is credible when students cannot manipulate their score (Imbens and Lemieux 2008)
- [ ] The What Works Clearinghouse accepts a quasi-experiment only with demonstrated baseline equivalence (WWC Standards Handbook)
- [ ] Difference-in-differences assumes parallel trends before treatment, which can be inspected (Cunningham 2021)

## 6. Effect sizes in education (Core)

- [ ] Cohen's d is a mean difference in standard deviation units, which makes tests on different scales comparable (Cohen 1988)
- [ ] Cohen's 0.2, 0.5 and 0.8 are too large for typical education field effects (Kraft 2020)
- [ ] Kraft's bands for standardized achievement outcomes are under 0.05 small, 0.05 to under 0.20 medium, 0.20 or more large (Kraft 2020)
- [ ] Kraft's bands come from about 750 randomized trials with median near 0.10, and are contested for using published effects (Kraft 2020; Simpson critique)
- [ ] Hattie's 0.40 hinge point is an average over heterogeneous studies, not a principled cutoff (Hattie 2009)
- [ ] Small, short, researcher-made-test studies give larger effects than large, long, standardized ones, so compare like with like (Kraft 2020)
- [ ] Hedges' g corrects small-sample bias in d and is the right choice at classroom sample sizes (Hedges 1981)
- [ ] Report an effect size with its confidence interval; at 25 to 30 students the interval will be wide (Lakens 2022)

## 7. Statistical power and sample-size justification (Core)

- [ ] Power is the probability of detecting an effect of a stated size; with 25 to 30 students only large within-subject effects are detectable (Cohen 1988)
- [ ] A sensitivity analysis states the smallest effect detectable at 80 percent power, the honest framing for a small pilot (Lakens 2022)
- [ ] Planning power from a published effect overestimates it, because publication bias inflates published effects (Lakens 2022)
- [ ] The smallest effect size of interest, set from practical or cost reasoning, is a better power input than a guessed true effect (Lakens 2022)
- [ ] An equivalence test lets you claim "no effect larger than a set bound" where a non-significant result is uninterpretable (Lakens 2017)
- [ ] Power for mixed models depends on both participant and trial counts and is estimated by simulation (Brysbaert and Stevens 2018; Westfall et al. 2014)
- [ ] Interaction effects, such as who benefits from personalisation, need far larger samples than main effects (Brookes et al. 2004)
- [ ] Cluster-randomised studies need many classes rather than many students, because effective sample size tracks the class count (Hedges and Hedberg 2007)

## 8. Multilevel models for nested data (Core)

- [ ] Students in one class resemble each other, so treating them as independent understates standard errors and inflates false positives (Raudenbush and Bryk 2002)
- [ ] The intraclass correlation is the share of outcome variance between classes, and US achievement values near 0.15 to 0.25 exceed the 0.05 to 0.15 folk rule (Hedges and Hedberg 2007) (secondary source only)
- [ ] The design effect, one plus cluster size minus one times the intraclass correlation, shrinks the effective sample size (Kish 1965)
- [ ] A random intercept gives each class its own baseline while estimating one overall treatment effect (Gelman and Hill 2007)
- [ ] Omitting random slopes makes tests anti-conservative (Barr et al. 2013)
- [ ] Repeated measures within a student are nested data and call for a multilevel model, not repeated t-tests (Singer and Willett 2003)
- [ ] Crossed random effects handle students and items together (Baayen, Davidson and Bates 2008)
- [ ] With fewer than about 20 clusters, default multilevel inference is unreliable and needs small-sample corrections (McNeish and Stapleton 2016) (unverified)

## 9. Measurement and validated instruments (Core)

- [ ] Validity is an argument that scores support an interpretation, not a property of a questionnaire (Messick 1995)
- [ ] Cronbach's alpha is a restrictive lower bound, and McDonald's omega is usually the better reliability report (Hayes and Coutts 2020)
- [ ] A translated scale needs forward and back translation, a pilot and its own validity evidence (Beaton et al. 2000)
- [ ] Measurement invariance must hold before comparing groups on a latent scale, such as Kazakh versus Russian-medium classes (Putnick and Bornstein 2016)
- [ ] Choose a motivation scale by construct (interest, need satisfaction or regulation style), not by familiarity (Ryan 1982; Chen et al. 2015) (unverified)
- [ ] Platform telemetry such as streaks and time-on-task is an engagement proxy and must be validated against a test (Baker 2016; Appleton et al. 2006)
- [ ] A learning gain is interpretable only if pretest and posttest are parallel and reliable (Shadish et al. 2002)

## 10. Open science, preregistration, replication (Working)

- [ ] A preregistration fixes hypotheses, outcomes and analysis before data exist, so a confirmatory test cannot be quietly changed (Nosek et al. 2018)
- [ ] Flexible analysis can reach p below 0.05 from noise, which preregistration blocks (Simmons, Nelson and Simonsohn 2011)
- [ ] The Open Science Collaboration replicated 36 percent of significant psychology findings, with effects about half the originals (Open Science Collaboration 2015)
- [ ] Only 0.13 percent of articles in 100 top education journals were replications, and 67 percent of those succeeded (Makel and Plucker 2014)

## 11. Qualitative and mixed methods (Working)

- [ ] Reflexive thematic analysis is researcher interpretation, not a coding procedure checked by inter-rater agreement (Braun and Clarke 2006)
- [ ] Mixed designs are named by order and priority: explanatory sequential means numbers first, then interviews to explain them (Creswell and Plano Clark)
- [ ] Triangulation helps only when each method addresses a different threat (Creswell and Plano Clark)

## 12. Usability evaluation and the SUS (Working)

- [ ] The System Usability Scale has ten items scored 0 to 100 with an average near 68, so a raw score is not a percentage (Brooke 1996; Sauro and Lewis)
- [ ] SUS is read through a curved grade or percentile scale, for example 75 sits near the 73rd percentile (Sauro and Lewis)
- [ ] Five users find most problems in a formative test but cannot estimate a score (Nielsen 2000)

---

## Resources

### Books
- Wieringa (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer. Operational DSR method. Intermediate.
- Shadish, Cook, Campbell (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*. Houghton Mifflin. Validity threats. Advanced reference.
- Murnane, Willett (2011). *Methods Matter: Improving Causal Inference in Educational and Social Science Research*. Oxford UP. Education-specific causal inference, regression discontinuity, cluster randomisation. Start here for designs.
- Reichardt (2019). *Quasi-Experimentation: A Guide to Design and Analysis*. Guilford. Modern successor to Shadish for pretest-posttest and nonequivalent groups. Intermediate.
- Gelman, Hill, Vehtari (2020). *Regression and Other Stories*. Cambridge UP; free PDF on the Aalto site. Easier than the 2007 multilevel text. Start here for regression.
- Gelman, Hill (2007). *Data Analysis Using Regression and Multilevel/Hierarchical Models*. Cambridge UP. Multilevel models and causal inference. Intermediate.
- McElreath (2020, 2nd ed.). *Statistical Rethinking*. CRC Press. Causal diagrams plus multilevel models, Bayesian. Intermediate (edition per search, publisher page not opened).
- Cunningham (2021). *Causal Inference: The Mixtape*; Huntington-Klein, *The Effect*. Quasi-experiment texts. Intermediate.
- Angrist, Pischke (2009). *Mostly Harmless Econometrics*. Princeton. Intermediate.
- Creswell, Plano Clark. *Designing and Conducting Mixed Methods Research*. Sage. Use the latest edition (4th, 2025/26).
- Raudenbush, Bryk (2002). *Hierarchical Linear Models*. Sage. Advanced reference (edition unverified).
- Lazar, Feng, Hochheiser (2017, 2nd ed.). *Research Methods in HCI*. Morgan Kaufmann. In the thesis learning path.

### Courses and lectures
- Lakens, *Improving Your Statistical Inferences*, Coursera, Eindhoven University of Technology. 8 modules, intermediate, audit free (price unverified). Do before mixed-model power work.
- McElreath, *Statistical Rethinking* 2023 lectures, full YouTube playlist, slides and code on GitHub (rmcelreath/stat_rethinking_2023).
- Gregor and Hevner 2013 is assigned in a Lund University DSR syllabus, a useful model reading order.

### Websites and blogs
- Lakens, *The 20% Statistician* blog (URL unverified).
- What Works Clearinghouse (IES) Standards Handbook.
- Education Endowment Foundation evaluation guidance.
- MeasuringU (Sauro): SUS interpretation.
- Center for Open Science / OSF preregistration templates.
- CausalPy "written resources on causal inference" list.

### YouTube
- Richard McElreath: Statistical Rethinking lectures, 25+ hours.
- StatQuest with Josh Starmer: basic statistics and machine learning.
- Quantitude video side (unverified).

### Podcasts
- *Quantitude* (Greg Hancock, Patrick Curran; quantitudepod.org): 150+ episodes.
- *Everything Hertz* (Dan Quintana, James Heathers): 190+ episodes.

### Key papers
- Kraft (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49(4), 241-253. Education-specific effect size bands.
- Peffers, Tuunanen, Rothenberger, Chatterjee (2007). *J. Management Information Systems*, 24(3), 45-77. DSRM process.
- Gregor, Hevner (2013). *MIS Quarterly*, 37(2), 337-355. Positions the contribution.
- Hevner (2007). A three cycle view of design science research. *Scandinavian J. Information Systems*, 19(2) (not re-verified).
- Design-Based Research Collective (2003). *Educational Researcher*, 32(1) (not re-verified).
- Open Science Collaboration (2015). *Science*, 349. 36 percent replicated, effects about half.
- Makel, Plucker (2014). *Educational Researcher*, 43(6). 0.13 percent replications.
- Hedges, Hedberg (2007). *Educational Evaluation and Policy Analysis*, 29(1), 60-87. Intraclass correlations for achievement.
- Simmons, Nelson, Simonsohn (2011). *Psychological Science*, 22(11) (not re-verified).
- Hill, Bloom, Black, Lipsey (2008). *Child Development Perspectives*. Growth benchmarks (not re-verified).

## Thesis papers to know
- Hevner, March, Park, Ram (2004). Design science in information systems research. Names what the thesis is. `hevner2004designscience`
- Wieringa (2014). Design Science Methodology. Treatment, validation, empirical cycle. `wieringa2014designscience`
- Shadish, Cook, Campbell (2002). Quasi-experimental designs. Validity threats. `shadish2002quasi`
- Cohen (1988). Statistical Power Analysis. Source of d and power. `cohen1988power`
- Lakens (2017). Equivalence tests: a practical primer. `lakens2017equivalence`
- Westfall, Kenny, Judd (2014). Power with participants and stimuli as random samples. `westfall2014power`
- Brysbaert, Stevens (2018). Power analysis and effect size in mixed effects models. `brysbaert2018poweranalysis`
- Baayen, Davidson, Bates (2008). Crossed random effects. `baayen2008crossedrandom`
- Brookes et al. (2004). Subgroup analyses and the interaction test. `brookes2004subgroups`
- Spencer, Zanna, Fong (2005). Experiments over mediation analyses. `spencer2005causalchain`
- Braun, Clarke (2006). Using thematic analysis in psychology. `braun2006thematic`
- Creswell, Plano Clark. Mixed methods research. Edition year disputed (bib says 2017, catalogue suggests 2018, 4th edition 2025/26); check the copyright page before citing. `creswell2017mixed` (bib entry needs checking)
- Nielsen (2000). Why you only need to test with 5 users. `nielsen2000users`
- Appleton et al. (2006). Student Engagement Instrument validation. `appleton2006sei`
- MSHE Kazakhstan (2024). Standard rules of scientific ethics, Order 529. `mshe2024scientificethics`
- Liao et al. (2016); Boruvka et al. (2018). Micro-randomized trial sample size and moderation, relevant if prompts are randomised within students. `liao2016mrtsamplesize`, `boruvka2018timevarying`
- Hattie (2009). Visible Learning. Treat the 0.40 hinge point critically. `hattie2009visiblelearning`
- Hyndman and Bisin (2026). Replication of Ariely and Wertenbroch's precommitment study. A worked example of a direct replication. `hyndman2026replication`
- Ryan (1982). Control and information in the intrapersonal sphere. Origin of the Intrinsic Motivation Inventory, the likely pilot instrument. `ryan1982imi`

## Contested claims to avoid
- Hattie's 0.40 as a threshold for "worth doing": an average over heterogeneous studies with varied critiques (Education Week 2018).
- Cohen's 0.2, 0.5, 0.8 as universal: Kraft 2020 gives education bands, themselves criticised for using the distribution of published effects (Simpson).
- A non-significant result at 25 to 30 students means no effect: use an equivalence test or sensitivity analysis.
- SUS as a percentage, or used unchanged with young children (unverified for children).
- The intraclass correlation folk rule of 0.05 to 0.15: contradicted by the Hedges and Hedberg reference values.
- The Open Science Collaboration 36 percent as proof most findings are false: Wilson and Wixted (2023) argue it needs a model to interpret.
- Creswell and Plano Clark edition read as 2017 without checking: catalogues conflict.

## Related MOCs
- [[Gamification & Learning Analytics MOC]]: the intervention the thesis pilot evaluates
- [[EdTech Product & Policy MOC]]: the data law behind consent and storage in the pilot
- [[Research Craft - MOC]]: argument, writing, literature, publishing and defence
