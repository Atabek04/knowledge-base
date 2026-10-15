TARGET DECK: Tech-KB::Security::Cryptography
Tags: security cryptography
**Related:** [[1. Cryptography MOC]]

START
Coding Questions
How do you count the **keyspace** N of a secret with L positions and A choices per position?
Back: <div>\( N = A^{L} \)</div>
- the **keyspace** is every distinct secret an attacker would have to try
- e.g. AES-256: A = 2 (a bit), L = 256, so N = 2<sup>256</sup> ≈ 1.2 × 10<sup>77</sup>
Tags: security cryptography brute-force
<!--ID: 1791528949632-->
END

START
Coding Questions
Why does an average brute-force search need only half the keyspace?
Back: The real key is **equally likely at any position** in the list of N keys.
- luckiest: found on guess 1; unluckiest: guess N
- so the average lands in the middle: **N / 2** guesses
Tags: security cryptography brute-force
<!--ID: 1791528949637-->
END

START
Coding Questions
What is the expected brute-force time t, and what does R stand for?
Back: <div>\( t = \dfrac{N}{2R} \)</div>
- **R** = the guess rate, keys the attacker's hardware tests **per second**
- time = guesses needed (N/2) ÷ guesses per second
Tags: security cryptography brute-force
<!--ID: 1791528949640-->
END

START
Coding Questions
In brute force, what is k, and what is the attacker's chance of success after it?
Back: **k** = the guesses the attacker can afford before giving up, k = R × t
<div>\( P(\text{found}) = \dfrac{k}{N} = \dfrac{R \times t}{N} \)</div>
- k = N/2 is the average case (50%), k = N the worst case (100%)
Tags: security cryptography brute-force
<!--ID: 1791528949643-->
END

START
Coding Questions
Why can't an attacker brute-force the plaintext behind a ciphertext without the key?
Back: They have **no way to test a guess**: checking "does my guess encrypt to this?" needs the key.
- so the only brute force left is over the keyspace, which is hopeless for a full-length key
- real attacks therefore **steal the key** instead
Tags: security cryptography brute-force
<!--ID: 1791528949646-->
END

START
Coding Questions
What does **security strength** in bits measure?
Back: The base-2 logarithm of the work the **best known attack** needs, regardless of key length.
- equals key length only when the best attack is trying every key
Tags: security cryptography brute-force
<!--ID: 1791528949650-->
END

START
Coding Questions
Why does a 2048-bit RSA key give only about 112 bits of security strength?
Back: Its private key is recovered by **factoring the modulus**, a shortcut far cheaper than guessing 2<sup>2048</sup> keys.
- NIST SP 800-57 rates RSA-2048 ≈ 112 bits, RSA-3072 ≈ AES-128
Tags: security cryptography brute-force
<!--ID: 1791528949654-->
END

START
Coding Questions
What key does a hash function like SHA-256 use, and what follows from that?
Back: **None**: a hash is a public recipe.
- anyone hashing the same input gets the same digest, including the attacker
- unlike encryption, there is no key that could reverse it
Tags: security cryptography hash
<!--ID: 1791528949657-->
END

START
Coding Questions
Using the toy hash "add up the digits", why can no hash be reversed?
Back: Hashing **throws information away**: 16, 25 and 1111111 all give 7.
- given only 7, the original input cannot be determined
- SHA-256 squeezes any input into 32 bytes the same way, so no inverse function exists
Tags: security cryptography hash
<!--ID: 1791528949659-->
END

START
Coding Questions
How does an attacker recover the input of a stolen hash without reversing the function?
Back: **Guess forward**: hash each candidate input and compare with the stolen digest.
- possible because a hash has **no key**, so every guess can be checked offline
Tags: security cryptography hash
<!--ID: 1791528949662-->
END

START
Coding Questions
What really sets the cost of recovering a hashed value: the digest length or something else?
Back: The **number of possible inputs**, whenever that is smaller than 2<sup>n</sup>.
<div>\( N = \min\left(2^{n},\ \text{number of possible inputs}\right) \)</div>
- a SHA-256 of a 4-digit PIN falls in 10 000 guesses
Tags: security cryptography hash
<!--ID: 1791528949666-->
END

START
Coding Questions
About how long does one RTX 4090 need, on average, to recover an 8-lowercase-letter input from its SHA-256?
Back: About **5 seconds**.
- N = 26<sup>8</sup> ≈ 2.1 × 10<sup>11</sup>, R ≈ 2.2 × 10<sup>10</sup> SHA-256/s (hashcat)
- fast hash + small input space = no protection
Tags: security cryptography hash
<!--ID: 1791528949669-->
END

START
Coding Questions
Which two levers does a defender have against guess-forward attacks on hashes?
Back:
- **Slow each guess** (shrink R): bcrypt, Argon2
- **Salt per row**: the search must be redone for every row
Neither shrinks the input space; only a **secret key** removes the attacker's ability to test guesses.
Tags: security cryptography hash
<!--ID: 1791528949672-->
END

START
Coding Questions
Why does a 12-digit Kazakh IIN have far fewer than 10<sup>12</sup> possible values?
Back: Its digits are **structured**, not random:
- 6 digits are a real birth date, 1 digit is century + gender (2 per date), the last is a computed check digit
- only the 4 serial digits are free: ≈ 46 302 days × 2 × 10<sup>4</sup> ≈ **9.3 × 10<sup>8</sup>** values
Tags: security cryptography hash
<!--ID: 1791529019704-->
END

START
Coding Questions
How long does one RTX 4090 need to recover an IIN from its unsalted SHA-256, and why is a whole leaked table at risk?
Back: About **0.02 s on average**, 0.04 s at worst (9.3 × 10<sup>8</sup> inputs at 2.2 × 10<sup>10</sup> hashes/s).
- unsalted: one pass over all IINs builds a lookup table that reverses **every row at once**
Tags: security cryptography hash
<!--ID: 1791529019707-->
END
