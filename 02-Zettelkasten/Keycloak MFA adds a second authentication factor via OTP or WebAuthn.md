---
aliases: [Keycloak MFA, MFA Keycloak, OTP Keycloak]
tags: [keycloak, security, mfa, authentication]
created: 2026-06-23
---

Keycloak MFA adds a second authentication factor on top of the standard username/password step. It plugs into the [[Keycloak Authentication Flows define the ordered steps a user must complete to authenticate|Browser flow]] as an extra authenticator that runs after the user's primary credentials are verified. Two factor types ship out of the box: <mark style="background: #FFF3A3A6;">TOTP (Time-based One-Time Password)</mark> and <mark style="background: #FFF3A3A6;">WebAuthn</mark>.

---

### TOTP — OTP via authenticator app

TOTP is the classic "six-digit code that rotates every 30 seconds" approach. Keycloak supports both <mark style="background: #FFF3A3A6;">TOTP and HOTP</mark> (counter-based) through the standard RFC 6238 / RFC 4226 specs, making it compatible with Google Authenticator, Authy, and any other standards-compliant app.

#### Registration flow

The first time a user hits an OTP-required step they haven't completed before, Keycloak redirects them to a setup screen. It renders a QR code that encodes the TOTP secret. The user scans it with their authenticator app, enters the first code to confirm, and the secret is stored in Keycloak. Subsequent logins just show the OTP input field.

#### Enabling OTP in the Browser flow

To require OTP for all users:

1. Go to **Authentication → Flows → Browser** and create a copy.
2. Inside the `Browser Forms` sub-flow, add **OTP Form** (`auth-otp-form`).
3. Set its requirement to `Required`.
4. Bind the copy as the realm's Browser flow under **Authentication → Bindings**.

---

### WebAuthn — FIDO2 and passkeys

<mark style="background: #FFF3A3A6;">WebAuthn</mark> is the FIDO2 browser API. It covers hardware security keys (YubiKey), device biometrics (Touch ID, Windows Hello), and passkeys. Keycloak ships two WebAuthn authenticators:

- **WebAuthn Authenticator** — acts as a second factor after password, replacing OTP.
- **WebAuthn Passwordless Authenticator** — acts as a *first* factor, replacing the password entirely.

For MFA use, you want the first one. Add `webauthn-authenticator` to the Browser flow's forms sub-flow in the same position where you'd add OTP Form.

#### Why prefer WebAuthn over TOTP

<mark style="background: #FF5582A6;">WebAuthn is the phishing-resistant option — prefer it over TOTP when security is critical.</mark> TOTP codes can be intercepted by a real-time phishing proxy (the attacker relays the code before it expires). WebAuthn binds the credential cryptographically to the origin domain, so a fake site cannot reuse the response — the authenticator refuses to sign a challenge for the wrong origin.

---

### Conditional MFA — require it only for certain users

Requiring MFA for every user is often too disruptive. Keycloak supports conditional execution via a `Conditional` sub-flow inside the Browser Forms.

#### Setup with a role condition

1. In the Browser flow copy, add a `Conditional` sub-flow to the Forms group.
2. Inside it, add **Condition - User Role** and configure it to check for a role such as `mfa-required`.
3. Add **OTP Form** (or WebAuthn Authenticator) as the next step inside the same sub-flow.
4. Set the sub-flow requirement to `Conditional`.

<mark style="background: #BBFABBA6;">Users without the `mfa-required` role skip the sub-flow entirely. Users with that role are prompted for the second factor.</mark> This lets you roll out MFA incrementally — assign the role to admins first, then to broader groups over time.

#### Condition - User Configured

An alternative condition is **Condition - User Configured**: it requires the second factor only if the user has already set up a credential of that type. Useful for self-enrollment flows where MFA is optional but enforced once configured.

---

### Skip vs Force OTP headers

Keycloak's conditional OTP evaluator can inspect request headers to decide whether to skip or force the OTP step — a common pattern for trusted internal networks.

<mark style="background: #FF5582A6;">Force takes precedence over skip.</mark> If a request matches both a force-OTP header and a skip-OTP header, Keycloak enforces the OTP prompt. This is intentional — the security-positive action wins. Getting this backwards leads to misconfigured flows where a trusted-network header can accidentally bypass a forced second factor.

---

### Read more

- [[Keycloak Authentication Flows define the ordered steps a user must complete to authenticate]]
