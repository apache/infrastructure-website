Title: Mail Rejection Policy

license: https://www.apache.org/licenses/LICENSE-2.0

### "Not authorized" message

People emailing ASF addresses may see this message: 

``Recipient address rejected: ASF gnomes rejected your message: SPF fail - not authorized. See https://infra.apache.org/mail-rejection.html``

The apache.org MX servers reject messages under many of the following circumstances:

- SPF (Sender Policy Framework) hard fail for domains which have it configured (-all)
- SPF hard fail for major spam targets despite ~all (gmail.com, yahoo.com)
- SPF hard fail for inbound mail from apache.org addresses which do NOT originate from apache.org servers 
- Various RBL provider match
- Invalid HELO hostname (hostname does not exist)
- Invalid HELO domain (domain does not exist)
- Unauthorized destination (no relaying)
- Unauthorized SMTP pipelining (common spam-burst technique)
- Reverse DNS does not match sender domain
- Header checks for known spam phrases
- Sender_access bans per envelope from address
- And many more

SPF hard fail for the apache.org domain has been implemented for incoming apache.org mail. This will require people using an apache.org mail address in their envelope "from" to be sending from an authorized host via mail-relay.a.o. See [Committer email](committer-email.html).

Infra takes a hard-line approach to prolific spammers, and will block all mail traffic from spam domains with a rejection message of ``550 Domain Blocked - Spam. Contact abuse@infra.apache.org``. If you receive this message, you may contact that address (using a different domain) to request review.

Refer to <a href="https://blogs.apache.org/infra/entry/committers_mail_relay_service" target="_blank">this blog post</a> for additional information.

[Contact Infra](/contact.html) via an alternate email address, or <a href="https://issues.apache.org/jira/" target="_blank">file a Jira ticket</a> with any questions.

If you feel your email has been blocked or rejected in error, please open a ticket at https://issues.apache.org/jira and include your external IP address and the To: header.

### Issue related to reporting ASF mail as spam

Please read [Dealing with spam in your ASF email account](spam-reporting.html) and **do not** flag valid ASF-related email as spam.
