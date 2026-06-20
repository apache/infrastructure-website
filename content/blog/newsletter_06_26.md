title: Inside Infra June 2026 
date: '2026-06-20' 
permalink: newsletter0626 layout: post

**Welcome to _Inside Infra_ for June, 2025**

### Roundtable

The June Roundtable focused on **release automation**, with Piotr Karwasz presenting, using the Apache Log4j release process as an example. A PDF of his slide deck is attached to the minutes page at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2026-06-03" target="_blank">Infra Roundtable 2026-06-03</a>.

The coming roundtables will be

  - July 1, 1700 UTC. Clay Johnson of Gradle will present on **predictive test analysis**.
  - August 5, 1700 UTC. The Tooling team will present the current state of the **Apache Trusted Releases (ATR) platform**.

Details about joining a roundtable, and what goes on at one, are here: <a href="https://infra.apache.org/roundtable.html" target="_blank">infra.apache.org/roundtable.html</a>.

### CAP - active beta seeks testers

Work is in progress to streamline and automate procedural/technical decision votes that relate to infra, security, and tooling, using a service called the **Contingent Approval Platform (CAP)**. CAP is intended to provide a single, uniform workflow for establishing proof of consensus in a project or committee for a given action, whether this is a social/manual thing or an automated task that requires approval.

A demo version is up and running at <a href="https://cap-test.apache.org" target="_blank">cap-test.apache.org</a>, and <a href="https://cap-test.apache.org/#/about" target="_blank">cap-test.apache.org/#/about</a> has documentation and the tool's rationale in great detail.

Infra is looking for people to log in to CAP and participate in an existing vote, or create a new voting instance, and to share feedback, bug reports, and enhancement requests.

**Note:** All email communication in the CAP demo goes to `gnomes@infra.apache.org`, our spam inbox, for these tests, so check that list instead of where things go for a tool that is fully functional, like a dev@ or private@ list.

The source code is at <a href="https://github.com/apache/infrastructure-cap" target="_blank">github.com/apache/infrastructure-cap</a> if you want to file a bug report or feature request.

### Infra at C/C Glasgow

The Infrastructure team will present a full track at Community over Code Glasgow, October 11-14:

  - Apache Trusted Releases: Securing the Open Source Supply Chain (with the Tooling team)
  - CI Workshop
  - Defending the Foundation: Implementing Automated Integrity Validation (AIV) Gates for Apache Projects
  - Distributed Denial of Service: Traffic characterization and mitigation
  - How To Infra
  - Infra Deployment Workshop
  - IRL Roundtable
  - Where are we going with ASF Infra?

Additionally, Infra will be hosting **Games Night**, which was very popular at the 2025 convention.

More details are at <a href="https://communityovercode.org/" target="_blank">communityovercode.org/</a>. We hope to see you there! 

### Infra 101: Use of build resources

The ASF has a limited number of self-hosted runners to support build processes. Processes that run more often than they need to, or for longer than is reasonable, prevent other projects from doing their builds. Committers and ASF Members can see, for the projects they are involved in, use of GitHub Actions resources (times ranging from the past hour to the past 30 days) at <a href="https://infra-reports.apache.org/#ghactions" target="_blank">infra-reports.apache.org/#ghactions</a>. 

There is on-going community discussion on a Slack channel, `project-workflow-optimisations`, about how projects can optimize GitHub Actions workflows to minimize

  - the number of concurrent jobs drawing on our limited allocation of runners
  - the number of long-running jobs

To share best practices, we encourage projects to contribute to this CWiki page: <a href="https://cwiki.apache.org/confluence/display/INFRA/GitHub+Actions+Recommended+Practices" target="_blank">cwiki.apache.org/confluence/display/INFRA/GitHub+Actions+Recommended+Practices</a>.

A project can maintain its own self-hosted runners if it can provide a suitable VM or on-premises hardware to execute the runners: <a href="https://cwiki.apache.org/confluence/display/INFRA/GitHub+self-hosted+runners" target="_blank">cwiki.apache.org/confluence/display/INFRA/GitHub+self-hosted+runners</a>.

**More next month!**
