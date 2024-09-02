Title: Content Moderation Policies
license: https://www.apache.org/licenses/LICENSE-2.0

This page lists the most common questions and answers surrounding content moderation 
policies at ASF Infrastructure, including, but not limited to:

- Data Privacy (GDPR, CCPA, CPPA/PIPEDA, etc.)
- Accidental exposure of credentials or other sensitive data
- Spam removal

The content the Infrastructure team can moderate includes text on ASF web pages, in Jira tickets, in emails to and from ASF addresses, in code comments, and in comments on commits to Git or Subversion code repositories.

See also the guidelines for <a href="https://infra.apache.org/mailing-list-moderation" target="_blank">mailing list moderation</a>.

## Personal Data Privacy Requests
Requests regarding exposure of PII (Personal Identifiable Information) **MUST** be sent to our 
Data Privacy Officer at `privacy@apache.org`. For more information on personal data privacy, 
see https://privacy.apache.org/.

## Accidental exposure of credentials or company-sensitive data

**TL;DR:** If you or your company experience accidental exposure of sensitive data or credentials in one of the types of content listed above, 
you should always assume that the data is now public, and immediately invalidate those credentials.

Depending on the context and circumstances of your request, we _may_ be able to remove the 
following items:

- Specific emails from our mailing list archives*
- Public comments on PRs/issues*
- Web pages or packages with compromised data

`*`Removing emails from public archives is not likely to be approved, as propagation of email to multiple hosts and locations makes it 
   virtually impossible to enact.

We are **not** able to, and will not spend time with the following:

- Deleting pull requests from GitHub (cannot be done)
- Deleting LDAP or other governance records that pertain to existing committers to ASF project repositories

## Dealing with spam

If you are a **mailing list moderator**, see this <a href="https://infra.apache.org/mailing-list-moderation#spam">guidance on spam management</a>.

If you have an ASF email account and are receiving what you believe to be spam on it:

  - Review <a href="https://infra.apache.org/spam-reporting.html" target="_blank">this guidance on possible spam</a>. 
  - If you still have an issue, report it to `users@infra.apache.org`.

If you seem to be receiving spam from an ASF email account, report the issue to `abuse@infra.apache.org`.

We make a good-faith effort to remove obvious spam from our email archives; however, given that our mailing lists are archived in many places, 100% certainty of spam removal is impossible.
