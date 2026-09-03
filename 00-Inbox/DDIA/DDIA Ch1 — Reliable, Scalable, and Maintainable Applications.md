
# Questions

- Meaning of quotes of Alan Kay, about "computing is pop culture"?
- Why data-intensive applications are more concerning and problematic, rather than compute-intensive? why we have data is limiting factor? it's not about buyding memory in server, isn't it? Is it about processing and reading those data when they're TB?

# Recall

## Thinking about Data Systems

- Applications have different requirements, therefore to cover them, a lot of different tools used and stitched together with application code
- you create special-purpose data system from general-purpose components

For our data systems and software systems we want to achieve: 
1. Reliability
2. Scalability
3. Maintanibilty

## Reliability

en: when something reliable or unreliable

in software context it includes:
- performs all functional requirements as expected
- tolerant for faults and user mistakes
- performative under expected load
- system prevents unauthorized access and abuse

> Reliability: continuing to work correctly, even when things go wrong.

The things that can go wrong are called **Faults**
The systems that can anticipate them are called **fault-tolerant** or **resilient**

Expand more about:
- tolerating certain types of faults
- fault vs failure
- to have fault-tolerant system, increase the rate of faults by deliberatly triggering them
	- Netflix's Chaos Monkey
- why to prefer tolerating faults rather than preventing faults?
	- prevention is better than cure, when cure doesn't exist
	  such as security vulnerabilities

### Hardware Faults

Hard disk crash, RAM becomes faulty, power grid blackout 

Fixes:
1. redundancy of hardware components :luc_arrow_big_right: hot-swappable
2. disks: RAID configuration ❓
3. servers: dual power supplies ❓
4. backup power: batteries & diesel generators

❓ Didn't the AWS multi-machine redundancy in page 8. and the paragraph after it
	How can system tolerate machine failure? by having multi-machines?

### Software Error

If hardware faults are random, independent and has weak correlations. 
But in other hand we have systematic errors.

❓why it's harder to anticipate, even if it's correlated across nodes ? (node here meaning server stack?)

Examples:
- **Software bug** when applications start to crash because of the bad input, system expected something different, and you give another thing, that's why it crashes
- Runaway processes that eats up the shared reousrces
	- why it's called the runaway? what does it mean?
- system depdens on service, and he starts to:
	- slow down
	- becomes unresponsive
	- returns corrupted responses

---

from this point I wanna focus only on questions here
 AI agent should read all those chapter and as well GitHub notes, and then create atomic cards from it
 and create flashcards
 in flashcards add my questions as well, that I asked if they're not in your flashcards.

---

Human Errors | p9:
- didn't get the first solution for human error, I got the idea of making good abstraction, API etc. But then why author talking about balance. Why would people work around them? give me examples.
- 