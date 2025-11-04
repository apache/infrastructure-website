Title: MFA reset policy
license: https://www.apache.org/licenses/LICENSE-2.0

**_Draft policy_** Infra will update this page with further details, replacing the _TBD_ notes, as they become available, and will make an announcement when the policy comes into force.

## Resetting MFA
Resetting a committer's MFA may be necessary because:

  - The committer has lost access to the MFA devices
  - The committer's MFA has been compromised in some way
  - Other reasons

There will be at least two methods to restore MFA:

  1. The committer uses a recovery key that they had previously established during initial MFA setup.
  
     - Visit (URL TBD) to reset MFA using a recovery key.
<br>
  2. The committer establishes their identity with the ASF via one or more of the following methods:

     - Have the project PMC open an Infra Jira ticket to address the issue
     - Work with the project PMC to validate their identity to the best of the project's ability. 
     - Provide proof of ownership of the ASF linked GitHub account to Infra via a process TBD.
     - Provide proof of ownership of the GPG key associated with the ASF ID via a process TBD.
     - Fill out a form TBD containing the information the committer provided on their original ICLA. Infra will perform address/signature validation

If a committer has lost their ASF MFA, GitHub 2FA, their GPG private key/passphrase, and Infra is unable to perform ICLA validation, the person will need to work with their project to be considered as a new committer, and will need to go through the new committership/new account process. The old account is unrecoverable and will be **disabled**.
