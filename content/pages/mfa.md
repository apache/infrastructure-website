Title: MFA at the ASF
license: https://www.apache.org/licenses/LICENSE-2.0

## MFA
Multi-factor authentication (MFA; also referred to as two-factor authentication, or 2FA) lets a user gain access to a website or application by presenting two or more pieces (or factors) of evidence of their identity which a mechanism can successfully authenticate. As well as protecting general access to the site or application, MFA protects users' and others' personally identifiable information, or PII, better than systems that only require presentation of a user name and password.

## MFA at the ASF
ASF project committers will encounter MFA when they set up their accounts to work with GitHub repositories. This is GitHub's 2FA verification system, not the Foundation's.

The ASF is expanding the use of MFA to cover its own applications and processes. The method for setting up MFA is similar to the current GitHub experience. To ensure smooth enrollment in The ASF's MFA system, committers can prepare by:

  - Using an existing feature at <a href="https://id.apache.org/" target="_blank">id.apache.org</a> to upload their GPG public key. This gives the committer an additional factor Infra can rely on during account recovery.
  - Linking their ASF and GitHub accounts via <a href="https://gitbox.apache.org/boxer/" target="_blank">Boxer</a>. This establishes a verifiable relationship between the two accounts.

If a committer attempts to access an ASF (not GitHub) feature or service protected by MFA before enrolling, they will be walked through the enrollment process at that time.

See also the <a href="https://infra.apache.org/mfa-reset.html">MFA reset policy</a>.
