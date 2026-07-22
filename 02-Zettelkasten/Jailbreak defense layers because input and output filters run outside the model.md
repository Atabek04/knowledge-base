---
aliases: [jailbreak defense, jailbreak prevention, LLM defense in depth]
---

If [[Jailbreaking crafts prompts that bypass an LLM's safety guardrails|a jailbreak bypasses the model's guardrails]], how do you stop it? The trap is thinking the model's own refusal is the wall. It isn't — jailbreaks defeat that wall by design. The answer is <mark style="background: #FFF3A3A6; font-weight: bold;">defense in depth</mark>: stack independent layers so beating one does not mean a full break.

### The key insight

A jailbreak bends the *model's behavior* — it talks the model out of refusing. It cannot bend a <mark style="background: #81C7D4A6; font-weight: bold;">separate classifier running outside the model</mark>. So the strongest defenses sit *around* the model, not inside it: a jailbroken model still hands its input and output to filters it has no control over.

Split the layers by where they live:

- <mark style="background: #FF9D9DA6;">**In-model (beatable)**</mark> — training-time alignment and the system prompt. Both live inside the conversation the attacker is manipulating, so a clever enough prompt can override them.
- <mark style="background: #ABF7F7A6;">**Out-of-model (survives the bypass)**</mark> — input and output filters are separate models or rules. The attacker cannot talk to them, so they keep firing even when the main model is fully fooled.

---

### The layers

1. **Training-time alignment** — RLHF and safety tuning bake refusal into the weights. Raises the bar; beatable alone.
2. **System prompt** — strong fixed instructions. Weakest layer — later user text can override it, so never the sole defense.
3. **Input filter** — a separate classifier scans the prompt *before* the main model sees it, catching known patterns ("ignore previous", DAN, smuggled role-play).
4. **Output filter** — a content-moderation pass scans the *response*. Even if the model is fooled into generating banned text, it never reaches the user.
5. **Least privilege** — structurally cap the blast radius so a jailbroken model can't do harm: no raw tool access, [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access|scoped permissions]], human approval on sensitive actions, no secrets in context.
6. **Red-team evals** — adversarial testing finds holes before attackers do, then you patch and re-test. Continuous, not one-time.

---

### No defense is total

<mark style="background: #FF9D9DA6;">There is no 100% jailbreak-proof system</mark> — it remains an open problem. The realistic goal is not perfection but to **raise the attacker's cost**, **shrink the blast radius**, and **layer defenses so no single bypass breaks everything**. Least privilege matters most here: it assumes the model *will* eventually be jailbroken and limits what that buys the attacker.

### Read more

- [[Jailbreaking crafts prompts that bypass an LLM's safety guardrails]]
- [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access]]
- [[AI Engineering MOC]]
