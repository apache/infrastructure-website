Title: Mail Rejection Policy

People emailing ASF addresses sometimes see this rejection message: 

``_550 5.7.23 Recipient address rejected: Message rejected due to: Receiver policy for SPF Softfail_``

The apache.org MX servers reject messages under the following circumstances:

- SPF (Sender Policy Framework) hard fail for domains which have it configured (-all)
- SPF hard fail for major spam targets despite ~all (gmail.com, yahoo.com)
- SPF hard fail for inbound mail from apache.org addresses which do NOT originate from apache.org servers (despite the DNS SPF record currently set to softfail)
- Failed <a href="http://www.postfix.org/POSTSCREEN_README.html" target="_blank">Postscreen checks</a>
- Barracuda central RBL match
- Invalid HELO hostname (hostname does not exist)
- Invalid HELO domain (domain does not exist)
- Unauthorized destination (no relaying)
- Unauthorized SMTP pipelining (common spam-burst technique)
- Reverse DNS does not match sender domain
- Header checks for known spam phrases
- Sender_access bans per envelope from address

SPF hard fail for the apache.org domain has been implemented for incoming apache.org mail. This will require people using an apache.org mail address in their envelope "from" to be sending from an authorized host via mail-relay.a.o: `https://reference.apache.org/committer/email`

Refer to <a href="https://blogs.apache.org/infra/entry/committers_mail_relay_service" target="_blank">this blog post</a> for additional information.

[Contact Infra](/pages/contact.html) via an alternate email address, or <a href="https://issues.apache.org/jira/" target="_blank">file a Jira ticket</a> with any questions.
