Title: Site-wide ban policy

Infra has a very specific set of rules in place to prevent abuse of Apache services. If you break one of these rules, your IP will be banned from all services across the ASF.

The following behaviors are **not permitted** on ASF services:

- Slow Loris-like abuse (too many request timeouts).
- More than 200,000 pageviews on any box per 12 hours.
- More than 50,000 JIRA requests per 24 hours.
- More than 10,000 download page views per 24 hours.
- More than 10,000 visits to our backup dist/ area on `www.apache.org` per 24 hours.
- More than 50 Gibibytes traffic per 12 hours (does not include mirrors, but does include `archive.apache.org`!).
- More than 50,000 visits to archive.apache.org per 12 hours.
- More than 100 mebibits/second sustained traffic for an hour or more.
- More than 2,000 viewvc requests per 24 hours.
- More than 100,000 Confluence (`cwiki.apache.org`) page visits per 24 hours.
- More than 10,000 Bugzilla requests per 24 hours.
- More than 1,000 Gitbox requests per hour.
- More than 75,000 `repository.apache.org` visits per 24 hours.
- More than 100,000 `builds.apache.org` visits per 12 hours.
- More than 2,500 code 429 (rate-limited) responses not respected per 12 hours. Services like Gitbox, Jira, Confluence, and Bugzilla have rate limits imposed. Abusing these services will result in a **429 HTTP** response code. Not respecting the HTTP response may result in a permanent ban.

If you think we banned your IP address by mistake, or if you have been banned but have an explanation why we should bend the rules for your specific case (for instance, if you have a NAT IP address that a lot of people use), contact us at `abuse@infra.apache.org` or through the "asfinfra" <a href="https://the-asf.slack.com/" target="_blank">Slack channel</a>. We will consider leniency and whitelisting on a case-by-case basis.
