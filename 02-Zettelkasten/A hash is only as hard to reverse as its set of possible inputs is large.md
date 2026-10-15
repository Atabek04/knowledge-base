---
created: 2026-10-09
tags: [cryptography/hash, security/attacks]
aliases: [Guess-forward attack, Small input space, Hash guessing attack]
---

A cryptographic hash cannot be run backwards, and that is often read as "a hashed value is safe".
It is not, because an attacker never needs to run it backwards: running it forwards on every candidate input works just as well when the candidates are few.

---

### Reversing a hash by guessing forward

#### Anyone can test a guess

[[Hashing produces fixed-length fingerprint that cannot be reversed|Hashing]] has no key, so the attacker can compute the exact same function the defender used.
That gives them a perfect test for any guess:

1. Pick a candidate input.
2. Hash it.
3. Compare with the stolen digest. A match means the input is found.

<mark style="background: #ABF7F7A6;">Because a hash needs no key, every guess can be checked offline against a stolen digest, so the attacker searches the inputs instead of reversing the function.</mark>

This is exactly what encryption denies the attacker: a ciphertext gives [[Brute-force cost is the number of possible keys divided by the guess rate#Why the attacker targets the key, not the plaintext|no way to test a guessed plaintext]] without the key.

#### The cost counts inputs, not output bits

The [[Brute-force cost is the number of possible keys divided by the guess rate|brute-force formula]] still applies, $t = \dfrac{N}{2R}$.
What changes is what $N$ counts.

<mark style="background: #FF5582A6;">The 2 to the n preimage cost of an n-bit hash holds only when the input is itself random; when the inputs are guessable, the real cost is the number of possible inputs.</mark>

$$N = \min\left(2^{n},\ \text{number of possible inputs}\right)$$

A 256-bit digest of a 4-digit PIN protects exactly as well as a list of $10\,000$ entries.

---

### How fast a small input space falls

$R$ is high for a fast hash: a single RTX 4090 computes about $2.2 \times 10^{10}$ SHA-256 hashes per second in hashcat (mode 1400, [hashcat forum benchmark](https://hashcat.net/forum/post-63595.html)).

| Input | $N$ | Average time at $R = 2.2 \times 10^{10}$ |
|---|---|---|
| 4-digit PIN | $10^{4}$ | well under a millisecond |
| 8 lowercase letters | $26^{8} \approx 2.1 \times 10^{11}$ | about 5 s |
| random 256-bit value | $2^{256} \approx 1.2 \times 10^{77}$ | about $8 \times 10^{58}$ years |

#### A national ID number: Kazakhstan's IIN

An IIN looks like a 12-digit secret, which suggests $10^{12}$ possibilities.
Its structure says otherwise ([LookupTax IIN guide](https://lookuptax.com/docs/tax-identification-number/kazakhstan-tax-id-guide), [OECD: Kazakhstan TIN](https://oecd.org/tax/automatic-exchange/crs-implementation-and-assistance/tax-identification-numbers/Kazakhstan-TIN.pdf)):

| Digits | Meaning | Choices |
|---|---|---|
| 1 to 6 | birth date, YYMMDD | only real calendar dates |
| 7 | century and gender | 2 per date (male or female) |
| 8 to 11 | serial number | $10^{4}$ |
| 12 | check digit | 1, computed from the first 11 |

Counting everyone born from 1900-01-01 to 2026-10-09, which is $46\,302$ days:

$$N = 46\,302 \times 2 \times 10^{4} \times 1 \approx 9.3 \times 10^{8}$$

$$t = \frac{9.3 \times 10^{8}}{2 \times 2.2 \times 10^{10}} \approx 0.02 \text{ s on average, about } 0.04 \text{ s at worst}$$

Even allowing all three century codes in the standard (1800s to 2000s), $N \approx 2.2 \times 10^{9}$ and the worst case is about 0.1 s.

<mark style="background: #FF5582A6;">Structure shrinks an ID number's input space far below its digit count: a 12-digit IIN has under a billion valid values, so its SHA-256 falls in a fraction of a second.</mark>

An unsalted hash makes it worse: one pass over all $9.3 \times 10^{8}$ IINs builds a lookup table that reverses <i>every</i> row of a leaked table at once, not just one.

<mark style="background: #ADCCFFA6;">Never treat a fast hash of a low-entropy value, such as a PIN, phone number or ID number, as protecting that value.</mark>

#### The two levers a defender has

The formula has only two places to push:

- **Make each guess slower** (shrink $R$): a deliberately slow function such as bcrypt or Argon2.
- **Make each guess useless elsewhere**: a per-row salt forces the attacker to redo the search for every row, as the [[Preimage attack reverses hash to recover input and is prevented by salting and slow KDFs#Prevention|preimage note]] shows.

Neither one enlarges $N$ itself; only a secret ingredient the attacker lacks, a key, puts the guess test out of reach.

---

### Read more

- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Brute-force cost is the number of possible keys divided by the guess rate]]
- [[Preimage attack reverses hash to recover input and is prevented by salting and slow KDFs]]
- [[HMAC creates fingerprint using hash function and secret key]]
- [[1. Cryptography MOC]]
