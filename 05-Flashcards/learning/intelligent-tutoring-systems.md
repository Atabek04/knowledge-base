TARGET DECK: Tech-KB::Learning::Intelligent Tutoring Systems
Tags: learning its
**Chapter:** Intelligent tutoring system anatomy and evidence
**Related:** [[AI in Education MOC]]

---

START
Coding Questions
What are the four parts of an intelligent tutoring system, and what question does each answer?
Back:
- **Domain model**: what is correct in the subject?
- **Learner model**: what does this student know?
- **Tutoring model**: what should happen next?
- **Interface**: how does the student see and touch it?
Source: Woolf (2009)
Tags: learning its
<!--ID: 1791913206490-->
END

START
Coding Questions
What is a **learner model** in an intelligent tutoring system?
Back: The system's current estimate of what this particular student knows.
Tags: learning its
<!--ID: 1791913206520-->
END

START
Coding Questions
A tutor has a domain model and an interface but no learner model. What can it do, and what can't it do?
Back:
- **Can**: mark an answer right or wrong now (the domain model knows the rule)
- **Can't**: remember the weakness tomorrow, so it cannot choose practice for that gap
Tags: learning its
<!--ID: 1791913206542-->
END

START
Coding Questions
Why can't a plain chatbot tutor report what a student has mastered?
Back: It is mostly an **interface** over a language model with no explicit **learner model**. Chat history stands in for one only until the context is cleared.
Tags: learning its
<!--ID: 1791913206564-->
END

START
Coding Questions
What is the **tutoring model** in an intelligent tutoring system?
Back: The part that decides the next teaching move: which task, which hint, when to move on.
Tags: learning its
<!--ID: 1791913206590-->
END

START
Coding Questions
What is tutoring **granularity** (VanLehn 2011)?
Back: The size of the unit of student work a tutor responds to: the whole **answer**, each **step**, or parts of a step (**substep**).
Tags: learning its
<!--ID: 1792329293730-->
END

START
Coding Questions
Two students give the same wrong case ending for different reasons. Why can't an answer-based tutor tell them apart?
Back: A final answer is the output of every step at once: it shows **that** some step failed, not **which** one. A step-based tutor asks for each step (which word is the preposition? which case?) and so locates the error.
Tags: learning its
<!--ID: 1792329293734-->
END

START
Coding Questions
What must the interface do for a tutor to be step-based?
Back: Make the student **enter the steps**. A box that receives only the final answer stays answer-based, however smart the model behind it.
Tags: learning its
<!--ID: 1792329293736-->
END
