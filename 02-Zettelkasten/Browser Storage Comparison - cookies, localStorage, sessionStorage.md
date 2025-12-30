**Browser Storage Comparison:**

|Storage|Where Sent|Lifetime|Access|Best For|
|---|---|---|---|---|
|**Cookies**|Auto in every request|Can persist (expires date)|JS + Server|Session auth, tracking|
|**localStorage**|Must manually send (headers)|Persists until deleted|JS only|Long-term client data|
|**sessionStorage**|Must manually send (headers)|Clears when tab closes|JS only|Temporary session data|

---

**Sending Across Multiple Requests - Pros/Cons:**

**Cookies (automatic):**

- ✅ No manual work, just set once
- ✅ HttpOnly flag blocks XSS attacks
- ❌ Vulnerable to CSRF
- ❌ Sent with every request (slightly more bandwidth)

**JWT in localStorage (manual):**

- ✅ Only sent when you want it
- ✅ Better for cross-origin (CORS)
- ❌ Vulnerable to XSS (JavaScript can steal it)
- ❌ Must write custom logic to send it

**JWT in sessionStorage (manual):**

- ✅ Cleared on tab close (safer than localStorage)
- ✅ Vulnerable to XSS (but shorter window)
- ❌ Lost if user refreshes or closes tab

---

**Best Practice:** For web apps with **server-side rendering**, use **secure cookies with HttpOnly flag**. For **SPAs or mobile**, use **JWT in localStorage with strong XSS defenses**.

---

Now we can actually talk about CSRF—which is the specific vulnerability that affects cookies. Shall we move to understanding what CSRF is?
