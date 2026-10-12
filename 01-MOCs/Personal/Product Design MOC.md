---
created: 2026-10-12
tags: [moc]
aliases: [Product Design, UI-UX, UX Design, Design Taste, Design Critique]
---

A roadmap for judging and directing product design: how people perceive and think, how interfaces are built from that, and how to tell good design from generic AI output.

AI now generates screens in seconds. The scarce skill is knowing which of ten generated screens is right, and saying why in words.

Parts 1 to 4 build the foundations, part 5 builds the process, and parts 6 and 7 train the eye on top.

---

## Part 1: The field

- [ ] UX is the whole experience of using a product, UI is the surface you touch
- [ ] UX vs usability: usability is one measurable slice of UX
- [ ] UX vs product design vs interaction design: scope of each role
- [ ] Don Norman coined "user experience" at Apple in 1993
- [ ] You are not the user: the designer's own preference is not evidence
- [ ] Human-centred design starts from the person, not the technology
- [ ] Bad UX has a business cost: support load, churn, lost conversion

---

## Part 2: How humans perceive

### Visual perception
- [ ] Foveal vs peripheral vision: only a thumbnail-sized area is sharp
- [ ] Pre-attentive processing: colour, size and motion register before thought
- [ ] Visual hierarchy: what the eye lands on first, second, third
- [ ] Selective attention: users see only what they are looking for

### Gestalt grouping
- [ ] Proximity: nearby things read as related
- [ ] Similarity: alike things read as a group
- [ ] Prägnanz: the brain picks the simplest interpretation
- [ ] Common region: a shared container creates a group
- [ ] Uniform connectedness: connected elements feel related
- [ ] Closure: the brain completes incomplete shapes
- [ ] Figure-ground: separating foreground from background

### Colour as signal
- [ ] Hue, saturation and value: the three dimensions of colour
- [ ] Contrast and WCAG ratios: AA 4.5:1, AAA 7:1
- [ ] Colour carries cultural and semantic meaning
- [ ] Aesthetic-usability effect: beautiful things feel easier to use

---

## Part 3: How humans think and decide

### Memory
- [ ] Working memory holds only a few chunks at once
- [ ] Chunking groups information to beat memory limits
- [ ] Recognition beats recall: menus beat blank fields

### Mental models
- [ ] Knowledge in the head vs knowledge in the world
- [ ] Mental model vs conceptual model: what users believe vs what the design communicates
- [ ] A mental-model mismatch is the root of user confusion
- [ ] Jakob's law: users expect your product to work like the ones they know

### Attention and effort
- [ ] Cognitive load: intrinsic vs extraneous
- [ ] Users scan, not read: F-pattern and Z-pattern
- [ ] Satisficing: users pick good enough, not the best
- [ ] Paradox of the active user: people explore instead of reading docs

### Psychology laws applied to UI
- [ ] Fitts's law: bigger, closer targets are faster to hit
- [ ] Hick's law: more choices mean slower decisions
- [ ] Postel's law: accept messy input, produce precise output
- [ ] Peak-end rule: experiences are judged by the peak and the ending
- [ ] Von Restorff effect: the distinct item is remembered
- [ ] Tesler's law: irreducible complexity must be absorbed by someone
- [ ] Doherty threshold: responses under 400 ms feel instant
- [ ] Goal-gradient and Zeigarnik: progress and unfinished tasks pull users forward
- [ ] Serial position effect: first and last items are remembered best
- [ ] Choice overload: too many options cause paralysis
- [ ] Pareto principle: most usage comes from few features

---

## Part 4: Norman's design vocabulary

- [ ] Affordance: what an object allows you to do
- [ ] Signifier: the cue that shows how to use it
- [ ] Feedback: the system confirms an action was received
- [ ] Mapping: how a control relates to its effect
- [ ] Constraints: physical, semantic, cultural and logical limits that guide action
- [ ] Forcing functions: interlocks, lock-ins and lock-outs prevent errors
- [ ] System image: what the design communicates about itself
- [ ] Discoverability and understandability: can users find it, can they interpret it
- [ ] Gulf of execution vs gulf of evaluation
- [ ] Seven stages of action: goal, plan, specify, perform, perceive, interpret, compare

---

## Part 5: Building the interface

### Visual craft
- [ ] One dominant element per screen, everything else steps down
- [ ] Spacing scale and the 8-point grid: consistent gaps read as intentional
- [ ] Alignment and grids: every edge lines up with something
- [ ] White space is a design tool, not empty space
- [ ] Typography does most of UI: scale, weight, measure 45 to 75 characters, leading
- [ ] Typeface vs font, legibility vs readability, font pairing
- [ ] Limited colour: a neutral ramp plus one accent, colour carrying meaning
- [ ] Colour-blind-safe palettes
- [ ] Depth and shadow: one light source, elevation over borders
- [ ] Touch targets at least 44 pt or 48 dp

### Information architecture
- [ ] IA vs navigation: structure vs the way through it
- [ ] Card sorting discovers how users group content
- [ ] Tree testing validates a navigation structure
- [ ] Navigation patterns: global, local, contextual, breadcrumbs
- [ ] Search vs browse: when users reach for each
- [ ] Labels users recognise, findability vs discoverability
- [ ] Faceted navigation filters large content sets

### Interaction design
- [ ] Input types: click, tap, swipe, hover, keyboard, voice
- [ ] Microinteractions: trigger, rules, feedback, loops
- [ ] Motion with purpose: easing and duration explain change
- [ ] UI states: default, hover, active, disabled, loading, error, empty
- [ ] Error design: slips vs mistakes, prevention, recovery, good messages
- [ ] Feedback design: progress, loading, confirmation
- [ ] Microcopy is interface: vague labels are a design bug

### Platforms
- [ ] Mobile-first vs desktop-first
- [ ] Responsive vs adaptive design and breakpoints
- [ ] Thumb zones and touch vs mouse
- [ ] Progressive disclosure: show more as the user needs it
- [ ] Apple HIG and Material as baselines broken only on purpose
- [ ] Design systems: tokens and components, and why one-offs rot

---

## Part 6: Research, process and evaluation

### User research
- [ ] Generative vs evaluative research
- [ ] What users say vs what they do: attitudinal vs behavioural
- [ ] Interviews without leading questions
- [ ] Contextual inquiry, diary studies, surveys
- [ ] Analytics, A/B tests, heatmaps and session recordings
- [ ] Synthesis: affinity maps, personas, jobs to be done, journey maps

### Design process
- [ ] Double Diamond: discover, define, develop, deliver
- [ ] Problem framing and "How might we"
- [ ] Ideation: quantity first, Crazy Eights
- [ ] Fidelity spectrum: sketch, wireframe, mockup, prototype
- [ ] Prototype the riskiest assumption first
- [ ] Design sprints: five days from problem to tested prototype

### Usability evaluation
- [ ] Nielsen's ten heuristics
- [ ] Heuristic evaluation and cognitive walkthrough
- [ ] Usability testing: think-aloud, moderated vs unmoderated
- [ ] Five users find most usability problems in one round

### Accessibility
- [ ] POUR: perceivable, operable, understandable, robust
- [ ] Screen readers, keyboard navigation and focus states
- [ ] Inclusive design: designing for the edges helps everyone

### Ethics
- [ ] The Hook model and variable rewards
- [ ] Dark patterns: hidden costs, roach motels, confirmshaming
- [ ] Defaults are design decisions
- [ ] Designing for wellbeing over attention

---

## Part 7: Taste and critique

### How taste is trained
- [ ] Taste is trained judgment: volume of looking plus naming why
- [ ] Generation vs judgment: AI delegates polish, the human keeps the decision
- [ ] The taste gap: your eye outgrows your hands first
- [ ] A swipe file of annotated real screens
- [ ] Copywork: rebuilding a great screen reveals invisible decisions

### Recognising AI slop
- [ ] The AI tells: purple gradients, gradient text, glassmorphism, glowing dark mode
- [ ] Identical card grids and the hero-metric layout
- [ ] Default fonts everywhere and emoji as icons
- [ ] Everything in a card, everything rounded the same
- [ ] Decoration without a point of view
- [ ] The gut-check: if told AI made it, would you believe it instantly
- [ ] Specific vs generic: good design belongs to one product and one user

### How to critique
- [ ] Critique against the goal, not personal preference
- [ ] Critique order: goal, hierarchy, flow, content, visual details
- [ ] Squint and blur tests: hierarchy survives when detail disappears
- [ ] Five-second test: what a stranger remembers
- [ ] Feedback as observation, impact, question
- [ ] Comparing options: pick one and argue it in two sentences
- [ ] Simplicity is removal: often the best decision is deleting

### Practice loop
- [ ] Daily: write a critique of one real screen
- [ ] Weekly: generate a screen with AI, fix it, list every change
- [ ] Redesign teardown: critique first, then redesign
- [ ] Post work in a community and compare their critique with yours

---

## Resources

Ranked by how often design communities and roundups recommend them, weighted toward this MOC's goal of judgment over tools.

### YouTube
1. Nielsen Norman Group: short research-backed UX explainers, the most trusted source
2. Kole Jain: fixes real bad UI on screen, closest to taste training
3. Mizko: UI craft and Figma, the most recommended in roundups
4. DesignCourse (Gary Simon): UI critiques, layout, colour and fonts
5. Flux Academy (Ran Segall): web design and taste for visual work
6. AJ&Smart: design sprints and workshops (Part 6)
7. The Futur: design thinking and the business of design
8. Femke.design: product design career and process

### Books
1. Refactoring UI (Wathan, Schoger): visual craft, the best fit for Part 5 and 7
2. The Design of Everyday Things (Norman): the vocabulary of Part 4
3. Don't Make Me Think (Krug): usability at a glance
4. Laws of UX (Yablonski): the psychology laws of Part 3
5. Designing with the Mind in Mind (Johnson): cognitive science behind UI rules
6. 100 Things Every Designer Needs to Know About People (Weinschenk)
7. Designing Interfaces (Tidwell): pattern library
8. Hooked (Eyal): habit design, read with the ethics section
9. The Elements of Typographic Style (Bringhurst): typography depth, optional

### Galleries for the eye
1. mobbin.com: real shipped app screens
2. godly.website, land-book.com, siteinspire.com: curated web
3. Products to study closely: Linear, Stripe, Vercel, Apple, Things 3

### Writers and sites
1. nngroup.com/articles, starting with the UX basics study guide
2. lawsofux.com: every law with a visual
3. Rauno Freiberg (rauno.me): interaction craft
4. Emil Kowalski (emilkowal.ski): motion and polish
5. Erik Kennedy, Learn UI Design blog: practical visual rules
6. Julie Zhuo's essays: design judgment and product thinking

### Newsletters and podcasts
1. UX Collective: weekly, critical thinking about design
2. Dense Discovery: broad visual sensibility
3. Typewolf: typography taste
4. Design Matters (Debbie Millman): long-form designer interviews

### Courses
1. NN/g UX certification: most credible, paid
2. Interaction Design Foundation: theory-first, cheap subscription
3. Google UX Design Certificate: full process, free to audit
4. Georgia Tech Intro to UX on Coursera: short, concept-only

### Communities
1. r/UXDesign: career and process discussion
2. r/UI_Design: post screens for critique
3. Dribbble and Layers: visual inspiration, read with the AI-slop list in mind
