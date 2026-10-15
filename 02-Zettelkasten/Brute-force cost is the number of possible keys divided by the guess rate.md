---
created: 2026-10-09
tags: [cryptography/core]
aliases: [Brute force cost, Keyspace, Security strength, Bits of security]
---

A brute-force attack tries every possible secret until one works.
Whether that is a real threat or a joke comes down to one division: how many secrets exist, over how fast the attacker can test them.

---

### The keyspace formula

#### Counting the possibilities

<mark style="background: #FFF3A3A6;">The keyspace is the number of distinct secrets an attacker would have to try: the number of choices per position raised to the number of positions.</mark>

$$N = A^{L}$$

$A$ is how many values each position can take, and $L$ is how many positions there are.

| Secret | $A$ | $L$ | $N$ |
|---|---|---|---|
| 4-digit PIN | 10 | 4 | $10^4$ |
| AES-128 key | 2 | 128 | $2^{128} \approx 3.4 \times 10^{38}$ |
| AES-256 key | 2 | 256 | $2^{256} \approx 1.2 \times 10^{77}$ |

#### Why the average search covers half the keyspace

The attacker walks the list of all $N$ keys in some order, and the real key is equally likely to sit at any position in that list.

Take a 4-digit PIN, so $N = 10\,000$ and the attacker tries `0000`, `0001`, `0002` and so on:

- Luckiest case: the PIN is `0000`, found on guess 1.
- Unluckiest case: the PIN is `9999`, found on guess 10 000.
- Every position in between is equally likely, so the average lands in the middle, around guess 5 000.

<mark style="background: #ABF7F7A6;">Because the key is equally likely to be anywhere in the list, the expected number of guesses is half the keyspace, N divided by 2.</mark>

#### Turning guesses into seconds

$R$ is the guess rate: how many keys the attacker's hardware can test per second.
Time is work divided by speed, the same as distance divided by speed.

$$t = \frac{\text{guesses needed}}{\text{guesses per second}} = \frac{N/2}{R} = \frac{N}{2R}$$

For the PIN, at $R = 100$ guesses per second:

$$t = \frac{10\,000}{2 \times 100} = 50 \text{ s on average, and } \frac{10\,000}{100} = 100 \text{ s at worst}$$

#### Odds of success when the attacker stops early

The time formula answers "how long until I find it?".
A real attacker asks the opposite question: "I can afford this many guesses, so what are my odds?"

$k$ is that budget: the number of guesses the attacker actually makes before giving up, set by their time and hardware as $k = R \times t$.
Each guess eliminates one of the $N$ equally likely keys, so:

$$P(\text{found}) = \frac{k}{N} = \frac{R \times t}{N}$$

$N/2$ and $N$ are not separate rules, just two particular values of $k$:

| Guesses made, $k$ | PIN odds, $\dfrac{k}{10\,000}$ | Meaning |
|---|---|---|
| $100$ | $1\%$ | a short attempt |
| $N/2 = 5\,000$ | $50\%$ | the average case above |
| $N = 10\,000$ | $100\%$ | the worst case above, success guaranteed |

<mark style="background: #ABF7F7A6;">The success probability of a brute force is the fraction of the keyspace the attacker can afford to search, k divided by N.</mark>

That fraction is what makes a long key safe: a full year at $R = 10^{12}$ is $k \approx 3.2 \times 10^{19}$ guesses, and against AES-256 that gives $\dfrac{3.2 \times 10^{19}}{1.2 \times 10^{77}} \approx 2.7 \times 10^{-58}$.

Every extra bit of key doubles the keyspace, so the attacker's cost grows exponentially with key length while the defender's grows only linearly.

---

### AES-256 against a generous attacker

Give the attacker $R = 10^{12}$ guesses per second, far beyond any real cluster.

$$t = \frac{2^{256}}{2 \times 10^{12}} \approx 5.8 \times 10^{64} \text{ s} \approx 1.8 \times 10^{57} \text{ years}$$

The universe is about $1.4 \times 10^{10}$ years old.
AES-128 at the same rate still takes about $5.4 \times 10^{18}$ years.

#### Why the attacker targets the key, not the plaintext

To brute-force the plaintext, an attacker needs a way to check a guess.
For a ciphertext, the only check is "encrypt my guess and compare", and that needs the key.

<mark style="background: #ABF7F7A6;">Without the key, a ciphertext gives the attacker no way to test a guessed plaintext, so the only brute force left is over the keyspace itself.</mark>

<mark style="background: #FF5582A6;">With a full-length random key, nobody brute-forces encryption; real attacks steal the key from wherever it is stored or loaded.</mark>
That is why [[Encryption transforms data using key to ensure confidentiality#Key Security|key secrecy]] is the whole game.

---

### Security strength versus key length

The formula assumes the best attack is trying every key.
For some algorithms a shortcut exists, and then key length overstates the real cost.

<mark style="background: #FFF3A3A6;">Security strength, in bits, is the base-2 logarithm of the work the best known attack needs, regardless of how long the key is.</mark>

[[RSA uses modular exponentiation with large primes for encryption|RSA]] is the classic case: its private key is recovered by factoring the modulus, which is far cheaper than guessing.
NIST SP 800-57 Part 1 equates the following:

| Security strength | Symmetric | RSA modulus |
|---|---|---|
| 112 bits | 3TDEA | 2048 bits |
| 128 bits | AES-128 | 3072 bits |
| 256 bits | AES-256 | 15360 bits |

<mark style="background: #FF5582A6;">A 2048-bit RSA key gives about 112 bits of security, not 2048, so key lengths are comparable only across algorithms that share the same best attack.</mark>

Sources: [NIST SP 800-57 Part 1 Rev 5](https://doi.org/10.6028/NIST.SP.800-57pt1r5), [Security level (Wikipedia)](https://en.wikipedia.org/wiki/Security_level), [Crypto++ wiki: Security Level](https://cryptopp.com/wiki/Security_Level).

---

### Read more

- [[Encryption transforms data using key to ensure confidentiality]]
- [[Symmetric cryptography uses single key for encryption and decryption]]
- [[AES is most widely used symmetric encryption algorithm]]
- [[RSA uses modular exponentiation with large primes for encryption]]
- [[Preimage attack reverses hash to recover input and is prevented by salting and slow KDFs]]
- [[1. Cryptography MOC]]
