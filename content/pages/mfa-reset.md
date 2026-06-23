Title: MFA Reset Policy
license: https://www.apache.org/licenses/LICENSE-2.0

A committer may need to reset their ASF multi-factor authentication (MFA) if they lose access to their MFA devices or believe their MFA has been compromised.

There are two paths to recovery if you have lost your MFA token(s):

  1. **Self-service with a recovery code** established during initial MFA setup.
    - Visit https://mfa.apache.org and use a recovery token by clicking "Select another authentication method." 

  2. **Identity validation by Infra.** 
    - Have someone from your PMC or Department open an Infra Jira ticket, or email security@infra.apache.org. Infra will validate identity against factors that you previously registered with the ASF.

To keep this process low-friction, we strongly encourage committers to register multiple factors in advance:

  - *Save the recovery codes provided during MFA setup.*
  - Upload a valid GPG public key to <a href="https://id.apache.org/" target="_blank">id.apache.org</a>.
  - Link their ASF and GitHub accounts via <a href="https://gitbox.apache.org/boxer/" target="_blank">Boxer</a>.

If a committer cannot establish their identity through any of their registered factors or through any other Infra-estabilished process, the affected account will be **disabled**, and the committer will need to work with their project to be onboarded again through the new-committer process.

More Committer-specific details related to the reset procedure are maintained on the <a href="https://cwiki.apache.org/confluence/display/INFRA/MFA+Reset+Policy">ASF Infra Cwiki</a>. (Committer authentication required.)
