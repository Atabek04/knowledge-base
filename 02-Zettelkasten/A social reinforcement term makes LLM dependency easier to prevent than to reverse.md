---
aliases: [LLM tipping point, cognitive hysteresis, AI dependency lock-in]
---

In the [[Regular LLM use is not dependency until the coupling persists and replaces the user's own thinking|three-state LLM dependency model]] of Solé et al. (2026), one term decides whether society slides into LLM use gradually or flips into it suddenly: $\kappa$, the social reinforcement of autonomous practice.

Source: Solé et al. (2026), *Large-Language Models as a Cognitive Virus*, arXiv preprint, [arXiv:2609.03344](https://arxiv.org/abs/2609.03344).

---

### Two thresholds instead of one

As adoption pressure $\lambda$ rises, two critical values appear:

$$\lambda_{TC} = \rho + \kappa \qquad \lambda_{SN} = 2\sqrt{\kappa\rho}$$

- $\lambda_{TC}$ is the <b>invasion threshold</b>: above it, a population of non-users can no longer stay that way.
- $\lambda_{SN}$ is the <b>recovery threshold</b>: pressure must fall below it before a coupled population returns to non-use.

When $\kappa > \rho$, the recovery threshold sits below the invasion threshold, and between them both outcomes are stable.

#### Hysteresis: the path back is not the path forward

<mark style="background: #FFF3A3A6;">Hysteresis means a system's state depends on its history, so undoing the push that caused a change does not undo the change.</mark>

A thermostat set to heat at 19 °C and stop at 21 °C behaves this way: at 20 °C, whether the heater runs depends on where the room came from.

<mark style="background: #ABF7F7A6;">Social reinforcement keeps non-use stable while non-users are common, so the population resists adoption, then collapses all at once, and the same reinforcement is now missing on the way back.</mark>

The width of the trap is $\lambda_{TC} - \lambda_{SN} = (\sqrt{\kappa} - \sqrt{\rho})^2$.

---

### Competence falls with the flip

The paper weights competence per state (1 for uncoupled, 0.5 for coupled, 0.1 for dependent) and averages it over the population.

With its example rates, average competence drops from 1 to about 0.43 at the tipping point. Reducing pressure back to $\lambda_{SN}$ only restores it to about 0.62.

<mark style="background: #ADCCFFA6;">Act on adoption pressure before the tipping point, because after it a much larger reduction is needed to recover less than was lost.</mark>

<mark style="background: #FF5582A6;">The competence weights are assumptions chosen for illustration, so the exact numbers say nothing about real populations; only the asymmetry is the result.</mark>

---

### Read more

- [[Regular LLM use is not dependency until the coupling persists and replaces the user's own thinking]]
- [[Lowering the dependency rate raises competence without moving the LLM tipping point]]
- [[Routine AI assistance erodes an expert's existing skill, not only a learner's skill formation]]
- [[AI in Education MOC]]
