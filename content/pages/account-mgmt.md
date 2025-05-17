Title: ASF account management
license: https://www.apache.org/licenses/LICENSE-2.0

## Your ASF account

Committers to Apache Software Foundation projects and ASF Members have personal accounts to facilitate their work and communications.

### Your Apache email address

Your account includes an Apache email address which is usually `userID@apache.org`. You can link that mailbox to a personal email address so you can receive mail from your Apache address and send mail with your Apache address as the "from" address. See <a href="https://infra.apache.org/committer-email.html">Committer email</a>.

### Managing your account details

Log in to <a href="https://whimsy.apache.org/" target="_blank">Whimsy</a> and, in the _Available to Committers_ section, click `Your personal details`. You can update any information in blue by double-clicking it and making the necessary changes in the form that appears.

### Regaining access to your committer account 

If you forgot your password, try...

  1. to reset it at <a href="https://id.apache.org/reset/enter" target="_blank">id.apache.org/reset/enter</a>. That will email to
your `@apache.org` address (which forwards to your non-apache email account) a short-lived password reset link. The link may be encrypted to <a href="https://people.apache.org/keys/committer/" target="_blank">your PGP key</a>.
  1. decrypting the e-mail - one way to do this is to save the e-mail contents as a text file, e.g. `password.txt`. Open a shell command window, and run the following command:

```
gpg -d password.txt</code>
```

This should decrypt the file and display the output in the window.

  3. If you have lost access to your registered email address, file an additional ICLA with Secretary. Follow the directions for <a href="https://www.apache.org/licenses/#submitting" target="_blank">submitting an ICLA</a>. Include your current Apache ID and mention in your cover email that you are requesting a change to your email address.

  4. If that didn't work, email `root@`. In your email, mention the following information:
 
  - Your username.
  - The fact that you have tried a self-service password reset, and why it didn't work. (Was the mail received? Did you decrypt it successfully?)
  - Why you need to regain access to your Apache account -- e.g., if it is to work on a <a href="https://www.apache.org/foundation/" target="_blank">foundation project</a>, name that project; or if you are a <a href="https://www.apache.org/foundation/members" target="_blank">foundation member</a>, state that.
  - SSH access to a project VM via public-key authentication.
  - Whether you ever set up Orthrus/OPIE on any `*.apache.org` box. (This is only applicable to people who had root permissions on PMC VMs.)
  - Whether you have access to the private part of a PGP key associated with your Apache account.
  - Whether the contact information on your ICLA is valid.
  - For (<a href="https://www.apache.org/foundation/members" target="_blank">ASF Members</a> only, whether the contact information in your `members.txt` entry is valid.
  - Whether you are able to send a new ICLA, with the same signature as your original one, which specifies new contact information.
  - Whether there is any other way in which we (Infra) might satisfy ourselves that you are the legitimate owner of that account.

**Note**: please do not ask other ASF committers or Members to email root@ to vouch for you.

### Multi Factor Authentication
Infra will soon provide multi-factor authentication (MFA) for account logins. Documentation related to setting up and using multi-factor authentication will be provided here when the service is ready.

You are welcome to review the <a href="https://infra.apache.org/mfa.html">draft MFA policy</a> and the related draft policy on <a href="https://infra.apache.org/mfa-reset.html">resetting MFA if access has been lost</a>.

**Note**: If you are using GitHub, you must also use GitHub's MFA, which is separate from the Apache MFA. If you are having trouble logging in to GitHub (or some other service) or to Apache, make sure you are using the correct entries for the MFA in question.

## Account removal 
Occasionally we need to remove an account - either by request or because the committer is deceased or, in rare cases, because the ASF is forcibly removing the committer. 

In practice, we almost never actually remove an LDAP account; we just remove the committer from all LDAP groups and mailing lists they have belonged to.

An exception would be responding to a GDPR/PII request by a committer. If you wish to make such a request, open an [Infra Jira](https://issues.apache.org/jira/projects/INFRA/issues/) ticket, state the circumstances, and provide your account information (not the password).
