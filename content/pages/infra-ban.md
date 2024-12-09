Title: Site-wide ban policy
license: https://www.apache.org/licenses/LICENSE-2.0

## Policy

The Apache Software Foundation provides a robust and extensive system for serving the needs of the Foundation, of our projects as they create and deploy product releases, and of people all around the world who wish to download and use those products. These services are free of charge; but we offer them with the assumption that everyone uses them appropriately. 

If you abuse the system by overloading it in one way or another, you make it harder for others to do what they need to do. The Infrastructure team will take steps to prevent abuse and restore normal access to all who rely on the ASF.

### PMCs and committers

Projects misusing ASF resources may see their access to those resources suspended without warning. Examples of misuse include:

  - overuse of disk space.
  - neglecting maintenance or security for project virtual machines.
  - over-consuming Travis minutes.


### Those visiting the ASF to download products or for other reasons

If you break one of these rules, **your IP will be banned** from all services across the ASF.

  - Slow Loris-like abuse (too many request timeouts).
  - More than 200,000 pageviews on any box per 12 hours.
  - More than 50,000 requests to downloads.apache.org per 24 hours. (tip: use a caching proxy instead)
  - More than 50,000 JIRA requests per 24 hours.
  - More than 50 Gibibytes traffic per 12 hours.
  - More than 25,000 visits to archive.apache.org per 24 hours.
  - More than 40GB downloaded from archive.apache.org per week.
  - More than 100 mebibits/second sustained traffic for an hour or more.
  - More than 25,000 JIRA pageviews per hour
  - More than 2,000 viewvc requests per 24 hours.
  - More than 100,000 Confluence (`cwiki.apache.org`) page visits per 24 hours.
  - More than 10,000 Bugzilla requests per 24 hours.
  - More than 1,000 Gitbox requests per hour.
  - More than 25,000 `repository.apache.org` visits per 24 hours.
  - More than 100,000 `builds.apache.org` visits per 12 hours.
  - More than 2,500 code `429` (rate-limited) responses not respected per 12 hours. Services like Gitbox, Jira, Confluence, and Bugzilla have rate limits imposed. Abusing these services will result in a `429 HTTP` response code. Not respecting the HTTP response may result in a **permanent ban**.
  - Excessive 404 result codes on `repository.apache.org` or `people.apache.org`. Neither repository.apache.org nor people.apache.org are general purpose Maven repositories, and should **only be used for the testing of pre-production ASF code artifacts**. <a href="https://mvnrepository.com/repos/central">Maven Central</a> is the correct public java artifact repository service.

Please evaluate your systems and update your configuration to use maven central, not repository.apache.org or people.apache.org

If you think we banned your IP address by mistake, or if you have been banned but have an explanation why we should bend the rules for your specific case (for instance, if you have a NAT IP address that a lot of people use), contact us at `abuse@infra.apache.org` or through the "asfinfra" <a href="https://the-asf.slack.com/" target="_blank">Slack channel</a>. We will consider leniency and allow-listing on a case-by-case basis.
