
## Why we need Dual-Writing for CH

Currently, we have PG for duplicating incoming data
Why CH can't handle that alone?

---

We need to create atomic notes about how CH works, and why it has those problems?
Something related to its Engine types, as well as buffers.

And also learning why it's soo fast.
And in what scenarios CH better than PG.
And when does PG is right call?

we have already created MOC, where we gonna append new atomic notes: [[ClickHouse - MOC]]

---

I heard that you can't really update records in CH, so you just simply add new record, correct?
Then how you get the latest relevant record?
I think it depends on what Engine Type you're using, correct?
Also mention keywords like FINAL, my colleague that, it's bad for performance. In that case what is the best practiced solution for it.

---

If the dual writing is the right call, how to avoid data drift and also losing some data. How to guarantee that writing.
Is this related to topics like Outbox pattern, Debezium and etc.?

---

.bin  -> so CH stored data in binary straight away?

How PG stores data? so it's per column as we get it. But then how? for each table? I remember they have different levels, like pages and etc. with some limits

