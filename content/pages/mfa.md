Title: MFA at the ASF
license: https://www.apache.org/licenses/LICENSE-2.0

**Draft policy** Infra will update this page with further details, replacing the _TBD_ notes, as they become available, and will make an announcement when the policy comes into force.

## MFA
Multi-factor authentication (MFA; also referred to as two-factor authentication, or 2FA) lets a user gain access to a website or application by presenting two or more pieces (or factors) of evidence of their identity which a mechanism can successfully authenticate. As well as protecting general access to the site or application, MFA protects users' and others' personally identifiable information, or PII, better than systems that only require presentation of a user name and password.

## MFA at the ASF
Currently, ASF project committers mainly encounter MFA when they set their accounts to work with GitHub repositories. This is GitHub's 2FA verification system, not the Foundation's; however, as we extend MFA to cover ASF apps and processes, the method for setting up MFA will be similar to the current GitHub experience.

  - The committer should use an existing feature at <a href="https://id.apache.org/" target="_blank">id.apache.org</a> to upload their GPG public key.
  - This GPG key can be used by Infra to validate an account if MFA tokens are lost.
  - The committer should link their ASF and GitHub accounts via <a href="https://gitbox.apache.org/boxer/" target="_blank">Boxer</a>. This establishes a verifiable relationship between the ASF account and the GitHub account which Infra can use to validate an account if MFA tokens are lost.
  - The committer should visit (URL TBD) to establish their Keycloak MFA tokens.
      - Be sure to save the provided recovery keys!
      - You can add multiple tokens, including standard TOTP (Authy, Google Authenticator, etc.) or WebAuthN tokens (Apple Magic Keyboard, YubiKey, etc.)
   - If a committer attempts to access an ASF (not GitHub) feature or service protected by MFA prior to establishing their MFA factors, Keycloak walks the committer through the process of setting up those factors.

See also the draft <a href="https://infra.apache.org/mfa-reset.html">MFA reset policy</a>.
