title: Inside Infra March 2025 
date: '2026-03-20' 
permalink: newsletter0326 layout: post

## Welcome to **Inside Infra** for March, 2026

### Roundtable

The presenter for the March roundtable was unavailable at the last moment, so Drew Foulks took the chair with a series of questions under the heading: "How can Infra present itself even better than it is doing now?"

People made suggestions and proposed initiatives in response to these questions:

   1. If you were the ASF president or a board member, what would your priorities for Infra be?
   2. In your ideal ASF of tomorrow, how much should we incorporate AI contributions, internal tooling, and vibe code submissions?
   3. In The ASF of tomorrow, how should Infra better support Top Level Projects in what they do?

Notes on the full discussion are at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2026-03-4" target="_blank">Infra Roundtable 2026-03-4</a>.

The next Roundtable will be **April 1, 1700 UTC** on the roundtable channel in the the-asf Slack space, and the topic (not a joke!) is the coming **migration of the Atlassian tools most projects rely on, Jira, and the Confluence Wiki**, from on-premises instances to the cloud. We will cover the why and the when, and what the impact will be on projects and on the ASF as a whole.

Looking ahead:

  - The May Roundtable will be **May 6, 1700 UTC** with the topic: **What is the impact on our infrastructure of AI coding?**
  - On **June 3, 1700 UTC**, Piotr P. Karwasz presents at the roundtable on **release automation**

Information on roundtables, and how to take part in one, is at <a href="https://infra.apache.org/roundtable.html" target="_blank">infra.apache.org/roundtable.html</a>

### Subversion migration

To address ongoing stability problems with the primary ASF Subversion server (svn.apache.org/dist.apache.org), Infra will be migrating the SVN service to new hardware on **March 22**. The service will be offline during the migration, which should take place between **1400 and 1700 UTC**.

### MFA

Infra is near the point of being able to begin a soft launch of the new multi-factor authentication (MFA) system that will eventually improve security for many ASF services and sites. The intention is to make the service available to a small beta-test group at first so that any issues that turn up do not cause inconvenience for the whole Foundation while they are being corrected. There will be a detailed announcement well in advance of the new MFA system going live.

### Infra at C/C Glasgow

The Infrastructure team will present a full track of talks, discussions, workshops, games and an in-person Roundtable at Community over Code Glasgow, **October 11-14**. The conference prospectus is at <a href="https://communityovercode.org/wp-content/uploads/2026/02/Community-Over-Code-Prospectus-2026.pdf" target="_blank">communityovercode.org/wp-content/uploads/2026/02/Community-Over-Code-Prospectus-2026.pdf</a> and the detailed schedule of keynotes, tracks, and talks–-and Games Night!-- will be available soon.

### Infra 101

If your website doesn't update after you have made and committed a change, the process may be stalled. Try making a **whitespace commit**. A large commit may not traverse all the parts of the process correctly and a small one after it will, and will thus trigger the publish process.

_BUT_

If you have made a change to your **.asf.yaml** file and it has not taken effect in a reasonable time, a whitespace commit will not help. Instead, commit a **semantic change**, such as adding a labels entry under GitHub, to encourage the build process. See <a href="https://github.com/apache/infrastructure-asfyaml" target="_blank">github.com/apache/infrastructure-asfyaml</a>.

**More next month!**
