---
aliases: [LLM dependency model, uncoupled coupled dependent, cognitive virus model]
---

Solé, Levin, Krakauer, de Domenico and colleagues model the spread of large language model use through a population the way epidemiologists model a virus: people sit in a few states and move between them at fixed rates.

Source: Solé et al. (2026), *Large-Language Models as a Cognitive Virus*, arXiv preprint, [arXiv:2609.03344](https://arxiv.org/abs/2609.03344).

---

### The three population states

Every person is in exactly one state, and the three shares add up to 1.

- <b>Uncoupled (U)</b>: does not use LLMs, or uses them only weakly.
- <b>Coupled (C)</b>: uses LLMs regularly but can still do the cognitive work alone.
- <b>Dependent (D)</b>: the LLM has replaced the person's own reasoning, and the coupling persists.

<mark style="background: #FFF3A3A6;">Dependency is defined by persistence and substitution, not by how often someone uses the tool.</mark>

A programmer who asks a model ten times a day but can still debug without it is coupled, not dependent.

---

### The transition rates

$$\frac{dU}{dt} = -\lambda UC + \rho C + \kappa U^2 C$$
$$\frac{dC}{dt} = \lambda UC - (\mu+\rho)C + \sigma D - \kappa U^2 C$$
$$\frac{dD}{dt} = \mu C - \sigma D$$

Each Greek letter is one arrow between states:

| Symbol | Arrow | Meaning |
|---|---|---|
| $\lambda$ | U to C | transmission: social, institutional and platform pressure to adopt |
| $\rho$ | C to U | return: coupled users drop back to non-use |
| $\mu$ | C to D | dependency: regular use hardens into substitution |
| $\sigma$ | D to C | recovery: dependent users regain autonomous use |
| $\kappa$ | C to U | reinforcement: autonomous practice spreads when autonomous people are common |

#### Why the model counts as nonlinear

The terms $\lambda UC$ and $\kappa U^2 C$ multiply states together. <mark style="background: #ABF7F7A6;">Adoption spreads through contact between users and non-users, so its speed depends on how many of each already exist.</mark>

That product is what lets the system jump suddenly instead of drifting smoothly, which the [[A social reinforcement term makes LLM dependency easier to prevent than to reverse|tipping-point note]] works out.

---

### What the model does not claim

<mark style="background: #FF5582A6;">The model is a theoretical preprint: its rates and competence values are illustrative, not measured from any population.</mark>

It shows what shape the dynamics could take if the assumptions hold. Whether real people behave this way is the job of empirical studies such as the correlational work on [[Heavy AI use correlates with weaker critical thinking but the causal arrow may run both ways|AI use and critical thinking]].

---

### Read more

- [[A social reinforcement term makes LLM dependency easier to prevent than to reverse]]
- [[Lowering the dependency rate raises competence without moving the LLM tipping point]]
- [[Heavy AI use correlates with weaker critical thinking but the causal arrow may run both ways]]
- [[Using AI to bypass work causes skill atrophy while using it for inquiry builds skill]]
- [[AI in Education MOC]]
