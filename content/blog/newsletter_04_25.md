title: Inside Infra April 2025 
date: '2025-04-23' 
permalink: newsletter0425 layout: post

## Welcome to Inside Infra for April, 2025

### Roundtable

The April roundtable was an 'open mic' session, to which people were encouraged to bring their fascinating or festering issues. Topics included:

  - the dynamics in choirs and voluntary organizations in general and how they map to the dynamics in ASF Member interrelations
  - where project VMs are hosted
  - how to find the APIs of services Infra provides
  - what a pipservice is, and whether a pipservice sandbox would be useful to project committers
  - the allowlist for custom GitHub Actions
  - whether custom GHAs need to include Apache licenses (short answer is 'no')
  - how to find out if the ASF has blocked your IP address, and why (see below)

There is **no roundtable in May**. The next roundtable will be **Wednesday, June 4, 2025, 1700 UTC**. The main topic will be a presentation on **JFrog and Artifactory**, a universal binary repository manager that enables teams to store, manage, and organize software packages throughout the development lifecycle.

### .asf.yaml improvements

Recent enhancements to .asf.yaml make it easier for projects to manage their development environments, including:

  - identifying required reviewers for the release
  - create a display between when you trigger a release and when the release process actually starts
  - an option to allow deploying from all protected branches
  - improvements to the branch and tagging processes

More details are available in this part of the .asf.yaml README file: [https://github.com/apache/infrastructure-asfyaml?tab=readme-ov-file#environments](github.com/apache/infrastructure-asfyaml?tab=readme-ov-file#environments) 

### Removal of Maven integration plugin

At the end of May, 2025, Infra will be removing the deprecated <a href="https://plugins.jenkins.io/maven-plugin/" target="_blank">Cloudbees Maven Integration Plugin (Maven job type)</a> from all ci-* Controllers here at the ASF. We recommend that projects that have been using this plugin migrate to a Pipeline job or a Freestyle job with Maven steps. There is a <a href="https://docs.cloudbees.com/plugins/ci/declarative-pipeline-migration-assistant" target="_blank">tool</a> already installed in ASF Controllers so that you can easily migrate to a pipeline job.

Further information is available:

  - <a href="https://docs.cloudbees.com/docs/cloudbees-ci-kb/latest/troubleshooting-guides/help-bulk-migration-maven-jobs" target="_blank">Bulk migration Maven jobs</a>
  - <a href="https://plugins.jenkins.io/pipeline-maven/" target="_blank">Pipeline</a>
  - <a href="https://www.youtube.com/watch?v=u0_sIo9I7CE" target="_blank">Video: Darin Pope, Cloudbees Advocate, goes through the steps to migrate</a>

Infra's Gavin McDonald has checked all project controllers, and sees that very few projects are still using the Maven type job, so this removal should affect almost nobody. If, however, you have concerns or would like help with migrating your project's Maven-type job, Infra is only to happy to help.

The end of May is only five weeks away, Please do create an INFRA Jira ticket right away if you need help or clarification.

### Jira accounts

Over the years, the ASF has accumulated, on top of Jira accounts created by ASF Members and committers, a huge number of Jira accounts created primarily by people who want to submit a ticket for one of our many projects. Most of these accounts don't see reuse after the issue the person wanted to report is resolved, and the account becomes inactive.

We now have 99,115 Jira accounts that have been inactive for more than three years, and 111,917 accounts that have been inactive for more than a year (interestingly, the number of accounts that have been inactive for the past 90 days is almost the same, 117,186).

This volume of accounts puts an unnecessary burden on our system, and Infra will be taking steps to reduce the account count:

  - We will **delete** accounts that are more than a year old and have never had any activity.
  - We will **disable and anonymize** accounts that have been inactive for the past three years, retaining the record of their activity before that time. 

ASF Members and project committers can help lighten the load by making sure to always use a Jira account with your ASF credentials (username, email address as they appear in the ICLA you submitted) whenever creating or commenting on a ticket for the ASF, or related to any of our projects.

### If your IP address seems to be blocked

If you cannot access one or more ASF repositories or services, your IP address may have been blocked. Before contacting Infra, review <a href="https://infra.apache.org/abc/" target="_blank">Abuse and Connectivity Issues at the ASF</a> (ABC). The page lists the common overuse (or abuse) issues that affect our site's work and cause an automatic IP address block, and recommends steps to get such a block removed. ABC also provides a channel to contact Infra if you need more information than the page provides.

### Jobs!

The Apache Software Foundation (ASF) is seeking an Infrastructure Systems Administrator who will contribute to the stability, security, and growth of its globally-distributed infrastructure. The successful candidate will demonstrate strong system administration skills in diverse environments, proven experience with open source tools and methodologies, and a deep understanding of F/OSS project dynamics. This role is 100% remote, but availability for once-yearly travel to the United States for a multi-day Team Meetup is highly encouraged. The candidate must be based in the UK or Europe. Applicants from nations embargoed or sanctioned by the United States cannot be accepted. Salary commensurate with experience.

<a href="https://s.apache.org/infra-hiring-2025" target="_blank">s.apache.org/infra-hiring-2025</a>


**More next month!**
