---
created: 2026-10-07
aliases: [Manim, Manim Community, ManimCE, ManimGL]
tags: [ai-video, code-to-video, python, math]
---

Manim is the Python animation engine Grant Sanderson wrote for the 3Blue1Brown channel: the morphing equations, sliding vectors and transforming graphs of those videos are Manim scenes. Its name is short for *Mathematical Animation*.

<mark style="background: #FFF3A3A6;">Manim renders a video from a Python class whose construct method creates mathematical objects and plays animations on them in order.</mark>

---

### Two editions

**Manim Community (ManimCE)** is the community-maintained fork, started in 2020, with stable documentation and releases. **ManimGL** is Grant Sanderson's own version, which changes with his videos.

<mark style="background: #ADCCFFA6;">Start with Manim Community, because its documentation and examples match its code, while ManimGL tracks one creator's needs.</mark>

---

### A scene is a class

```python
from manim import *

class Pythagoras(Scene):
    def construct(self):
        eq = MathTex(r"a^2 + b^2 = c^2")
        square = Square(side_length=2).next_to(eq, DOWN)
        self.play(Write(eq))
        self.play(Create(square))
        self.play(Transform(square, Circle().move_to(square)))
        self.wait(1)
```

```bash
manim -pql scene.py Pythagoras      # p: preview when done, ql: low quality for fast drafts
```

Each `self.play()` call runs one animation and advances the timeline by its run time; `self.wait()` holds the frame.

#### Mobjects

Everything on screen is a **mobject** (mathematical object): `Square`, `Axes`, `NumberPlane`, `MathTex`. `Transform` morphs one mobject's points into another's, which produces Manim's signature smooth shape changes.

---

### Placement is by coordinates

<mark style="background: #ABF7F7A6;">Every mobject has an exact position in scene units, set with move_to, next_to and shift, so a label sits precisely where the code puts it on every render.</mark>

The default frame is 8 units tall with the origin at the centre, and `UP`, `DOWN`, `LEFT`, `RIGHT` are unit vectors.

#### LaTeX dependency

<mark style="background: #FF5582A6;">MathTex and Tex compile their strings with a local LaTeX installation, so formulas fail to render on a machine without one even when the rest of the scene works.</mark>

---

### Read more
- [[Choose Manim for math, Remotion for text and data, Motion Canvas for explainers and three.js for 3D video]]
- [[Code-rendered video has an AI write a program that draws every frame instead of generating pixels]]
- [[AI Video Production MOC]]
- [[Math for ML MOC]]

### External Resources
- [Manim Community documentation](https://docs.manim.community/en/stable/)
- [ManimGL: Grant Sanderson's original repository](https://github.com/3b1b/manim)
- [3Blue1Brown: linear algebra series (videos made with Manim)](https://www.3blue1brown.com/topics/linear-algebra)
