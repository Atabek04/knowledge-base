---
created: 2026-05-31
tags: [moc]
---

Understanding how people think, perceive, and behave — then designing around that.

UI/UX is not about making things look good. It is about removing friction between human intention and system response.

---

## Chapter 1 — The Field and the Mindset

What UI/UX is, who does it, and the philosophy that makes it work.

- What is User Experience (UX)
- What is User Interface (UI)
- UX vs UI — the distinction and the overlap
- The origin of "UX" — Don Norman at Apple (1993)
- UX vs Usability — not the same thing
- Who is a UX Designer — roles and responsibilities
- UX vs Product Design vs Interaction Design
- The core principle: You ≠ User
- Human-centered design — designing for the human, not the technology
- The cost of bad UX — why it matters for business

---

## Chapter 2 — How Humans Perceive

Vision and perception are the entry point to every interface. Design that ignores this fights human biology.

### Visual Perception
- How the human eye works — foveal vs peripheral vision
- Pre-attentive processing — what the brain sees before thinking
- Visual hierarchy — why some elements register before others
- Selective attention — users only see what they are looking for

### Gestalt Laws (Visual Grouping)
- Law of Proximity — nearby things appear related
- Law of Similarity — similar things appear grouped
- Law of Prägnanz — the brain simplifies complex images
- Law of Common Region — shared borders create groups
- Law of Uniform Connectedness — connected elements feel related
- Law of Closure — the brain completes incomplete shapes
- Figure-ground relationship — separating foreground from background

### Color & Visual Signal
- Color perception basics — hue, saturation, value
- Color contrast and accessibility (WCAG)
- Color as meaning — cultural and semantic implications
- The Aesthetic-Usability Effect — beautiful things feel easier to use

---

## Chapter 3 — How Humans Think and Remember

Interfaces that fit how memory works require less effort and fewer errors.

### Memory Systems
- Working memory (short-term) — capacity and limits
- Miller's Law — 7 ± 2 items in working memory
- Chunking — grouping information to overcome memory limits
- Long-term memory — how knowledge gets stored and retrieved
- Recognition vs recall — why menus beat blank fields

### Knowledge and Mental Models
- Knowledge in the head vs knowledge in the world
- Mental models — what users believe about how a system works
- Conceptual models — what the designer communicates
- When mental models mismatch — the root of user confusion
- Jakob's Law — users expect new systems to work like systems they already know

### Attention and Cognition
- Cognitive load — the mental cost of using an interface
- Intrinsic vs extraneous cognitive load
- How users scan, not read — F-pattern and Z-pattern
- Satisficing — users pick "good enough," not the best option
- The Paradox of the Active User — users explore instead of reading docs

---

## Chapter 4 — Psychology Laws in UX

Applied behavioral science — each law maps directly to a design decision.

- **Fitts's Law** — larger, closer targets are acquired faster (button sizing, thumb zones)
- **Hick's Law** — more choices = longer decision time (menus, onboarding)
- **Miller's Law** — 7 ± 2 chunks in working memory (navigation, forms)
- **Postel's Law** — accept varied input, produce precise output (form tolerance)
- **Peak-End Rule** — users judge experiences by peak moment and ending
- **Aesthetic-Usability Effect** — beautiful interfaces are perceived as more usable
- **Von Restorff Effect** — distinctive items are remembered (CTAs, highlights)
- **Tesler's Law** — every system has irreducible complexity; someone must absorb it
- **Doherty Threshold** — interactions under 400ms feel instantaneous
- **Goal-Gradient Effect** — motivation increases as users near completion
- **Zeigarnik Effect** — unfinished tasks stay in memory (progress bars, streaks)
- **Serial Position Effect** — first and last items in a list are most remembered
- **Choice Overload** — too many options cause paralysis (The Jam Study)
- **Pareto Principle (80/20)** — 80% of usage comes from 20% of features
- **Parkinson's Law** — tasks expand to fill available time (deadlines, timers)

---

## Chapter 5 — Core Design Vocabulary

The conceptual building blocks Don Norman established. Every other concept traces back here.

- **Affordances** — what an object allows you to do (real vs perceived)
- **Signifiers** — cues that communicate how to use something
- **Feedback** — system response that confirms action was received
- **Mapping** — relationship between control and its effect
- **Constraints** — limitations that guide toward correct action
  - Physical constraints
  - Semantic constraints
  - Cultural constraints
  - Logical constraints
- **Conceptual model** — the user's mental picture of how a system works
- **System image** — what the design communicates about itself
- **Discoverability** — can users figure out what to do?
- **Understandability** — can users interpret what happened?
- **Forcing functions** — design that prevents error before it occurs
  - Interlocks
  - Lock-ins
  - Lock-outs
- **The Gulf of Execution** — gap between user intent and available actions
- **The Gulf of Evaluation** — gap between system state and user interpretation
- **The Seven Stages of Action** — form goal → plan → specify → perform → perceive → interpret → compare

---

## Chapter 6 — Visual Design Principles

How to arrange visual elements so the interface communicates clearly without effort.

### Hierarchy and Layout
- Visual hierarchy — directing attention through size, weight, contrast, position
- Grid systems — columns, gutters, alignment
- White space (negative space) — breathing room as a design tool
- Alignment — creating order and reducing noise
- The F-pattern and Z-pattern scan paths

### Typography
- Typeface vs font — the distinction
- Readability vs legibility
- Type hierarchy — heading, body, caption scales
- Line length (measure) — 45–75 characters per line
- Line height (leading) — spacing for readability
- Font pairing principles

### Color
- Color theory basics — complementary, analogous, triadic
- Contrast ratios — WCAG AA (4.5:1) and AAA (7:1)
- Using color to communicate status, hierarchy, action
- Color blindness — accessible color combinations

### Spacing and Scale
- The 8-point grid system
- Consistent spacing scales
- Touch target sizing (minimum 44×44px / 48×48dp)

---

## Chapter 7 — Information Architecture

How to organize, label, and structure content so users can find what they need.

- What is Information Architecture (IA)
- IA vs Navigation — the difference
- Mental models and IA — designing structure users expect
- Card sorting — how to discover user mental models
- Tree testing — validating navigation structure
- Sitemaps — mapping content structure
- Navigation patterns — global, local, contextual, supplemental
- Breadcrumbs — wayfinding within hierarchy
- Search vs browse — when users use each
- Labeling systems — naming things users recognize
- Findability vs discoverability
- Faceted navigation — filtering large content sets

---

## Chapter 8 — Interaction Design

How interfaces behave — the behavior and flow layer on top of visual design.

- What is Interaction Design (IxD)
- Input types — click, tap, swipe, hover, keyboard, voice
- Affordances in interaction — what users try to do
- Microinteractions — small moments that build trust
  - Trigger → rules → feedback → loops + modes
- Animation and motion — purpose, timing, easing
- Transition types — explain spatial relationships
- Error design — preventing, detecting, recovering from errors
  - Slips vs mistakes
  - Capture errors, description errors, mode errors
  - Designing good error messages
- Feedback design — progress indicators, loading states, confirmations
- Responsiveness — the Doherty Threshold in practice
- States of UI components — default, hover, active, disabled, loading, error, empty

---

## Chapter 9 — User Research

How to learn what users actually need, not what we assume.

### Research Fundamentals
- Why research — designers are not users
- Generative vs evaluative research
- Qualitative vs quantitative methods
- Attitudinal vs behavioral research — what users say vs what they do

### Research Methods
- User interviews — how to ask without leading
- Contextual inquiry — observing users in their environment
- Surveys — scale over depth
- Diary studies — longitudinal self-reporting
- A/B testing — controlled experiments
- Analytics — behavioral data from real usage
- Heatmaps and session recordings

### Synthesis
- Affinity diagramming — clustering observations into themes
- Personas — composite user archetypes built from research
- User stories — "As a [user], I want [goal], so that [reason]"
- Jobs-to-be-done (JTBD) — what users are trying to accomplish
- Empathy mapping — what users think, feel, say, do
- User journey mapping — the full experience across touchpoints

---

## Chapter 10 — Design Process

How to go from a problem to a tested solution without building the wrong thing.

### Design Thinking
- The five phases: Empathize → Define → Ideate → Prototype → Test
- Design thinking is iterative, not linear
- Problem framing — solving the right problem, not the obvious one
- "How Might We" (HMW) — reframing problems as opportunities
- The Double Diamond model — discover → define → develop → deliver

### Ideation
- Brainstorming rules — defer judgment, quantity over quality
- Crazy Eights — 8 sketches in 8 minutes
- Competitive analysis — learning from existing solutions
- Design patterns — reusing proven solutions

### Prototyping
- Why prototype before building
- Fidelity spectrum — paper sketch → wireframe → mockup → prototype
- Paper prototyping — fastest way to test a flow
- Wireframes — structure without visual design
- Low-fidelity vs high-fidelity prototypes
- What to prototype — the riskiest assumptions first

### Design Sprints
- The 5-day Google Design Sprint structure
- When to run a sprint
- Sprint artifacts — maps, sketches, storyboards, prototypes, test insights

---

## Chapter 11 — Usability and Heuristics

Frameworks for evaluating design without running full user tests.

### Nielsen's 10 Usability Heuristics
1. Visibility of system status
2. Match between system and the real world
3. User control and freedom (undo/redo)
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, and recover from errors
10. Help and documentation

### Evaluation Methods
- Heuristic evaluation — expert review against heuristics
- Cognitive walkthrough — simulating user's step-by-step thinking
- Usability testing — watching real users attempt real tasks
  - Moderated vs unmoderated
  - In-person vs remote
  - Think-aloud protocol
- Sample size for usability testing — 5 users catch 85% of issues

### Accessibility
- WCAG 2.1 principles — Perceivable, Operable, Understandable, Robust (POUR)
- Screen readers — designing for non-visual navigation
- Keyboard navigation — tabindex, focus states
- Color contrast requirements
- Alt text and semantic HTML
- Inclusive design — designing for the margins improves for everyone

---

## Chapter 12 — Responsive and Multi-Platform Design

One product, many screen sizes and contexts.

- Mobile-first vs desktop-first design
- Responsive vs adaptive design
- Breakpoints — when and how layout shifts
- Touch vs mouse — different interaction models
- Thumb zones — comfortable reach on mobile
- Progressive disclosure — showing more as users need it
- Native app vs web app patterns
- Platform conventions — iOS HIG vs Material Design

---

## Chapter 13 — Ethics and Persuasion

The responsibility that comes with knowing how human psychology works.

- Persuasive design — using psychology to influence behavior
- The Hook Model (Nir Eyal) — trigger, action, variable reward, investment
- Intermittent variable rewards — why they're addictive
- Dark patterns — design that tricks users against their interests
  - Hidden costs, roach motels, misdirection, confirmshaming, trick questions
- Design for attention vs design for wellbeing
- User autonomy — respecting the user's right to choose
- Default settings as a design decision
- When to use and not use engagement techniques
- The designer's ethical responsibility

---

## Resources

### Books (read in this order)

1. **The Design of Everyday Things** — Don Norman → foundational mental models
2. **Don't Make Me Think** — Steve Krug → usability thinking, web context
3. **Laws of UX** — Jon Yablonski → applied psychology laws
4. **Designing with the Mind in Mind** — Jeff Johnson → cognitive science behind UI rules
5. **100 Things Every Designer Needs to Know About People** — Susan Weinschenk → behavioral science reference
6. **Hooked** — Nir Eyal → habit-forming design and ethics
7. **Universal Principles of Design** — William Lidwell → reference encyclopedia
8. **Thinking, Fast and Slow** — Daniel Kahneman → System 1/2 thinking (not UX-specific but foundational)

### Courses

- **Interaction Design Foundation (IxDF)** — ixdf.org — best theory-first platform ($11–16/month)
  - Start: Human-Computer Interaction: Foundations of UX Design
  - Then: Perception and Memory in HCI and UX
  - Then: Gestalt Psychology and Web Design
  - Then: Design Thinking: The Ultimate Guide
- **Google UX Design Certificate** — Coursera — free to audit, covers full process
- **Introduction to User Experience Design** — Georgia Tech on Coursera — pure concepts, 6 hours
- **Nielsen Norman Group UX Basic Training** — live online, most credible certification

### Free References

- **lawsofux.com** — all UX laws with visuals, free
- **nngroup.com/articles** — research-backed articles on every UX topic
- **nngroup.com/articles/ux-basics-study-guide** — curated reading path
- **nngroup.com/articles/ten-usability-heuristics** — the 10 heuristics (bookmark this)
