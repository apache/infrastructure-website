title: Inside Infra March 2025 
date: '2025-03-27' 
permalink: newsletter0325 layout: post

Welcome to **Inside Infra** for March, 2025

The next **Infra roundtable** will be **Wednesday, April 2, 2025, 1700 UTC**. This will be an "ask us anything" day, so feel free to bring any infrastructure issue that you find interesting/puzzling/scary.

For details about how to join a roundtable, and what happens at it, see <a href="https://infra.apache.org/roundtable.html" target="_blank">infra.apache.org/roundtable.html</a>

## GHA allowlist

Infra and a team of volunteers have been developing an automated self-serve solution that will enable Dependabot to scan our allowlist approved GitHub Actions, as well as help projects add third-party Actions to the list. 

The team is debugging the complex flow of commits and action triggers to our pubsub-based watcher service. For the moment, you still need to submit a Jira ticket to Infra if you want to add an Action to the allowlist.

Remaining tasks include

  - dependabot update bundling
  - watcher service re-scanning
  - polishing up workflow triggers

If you are interested in following this work more closely, or contributing to it, please join our email list (`ghactions@infra.apache.org`) and/or the **#asf-ghactions** channel in the the-apache space on Slack.

## GitHub Discussions

Projects that are using GitHub Discussions and have suddenly found that feature is missing. Please see <a href="https://github.com/apache/infrastructure-asfyaml?tab=readme-ov-file#repo_features" target="_blank">github.com/apache/infrastructure-asfyaml?tab=readme-ov-file#repo_features</a>.

GitHub Discussions are now managed entirely through .asf.yaml, and will default to being disabled unless your project enables them in your .asf.yaml file. If you do not have a valid 'discussions' entry in the notifications section in the configuration, that will also disable GitHub Discussions.

To enable Discussions, include these settings into the .asf.yaml file in your default branch:

```
notifications:
   discussions: issues@foo.apache.org  (use your own mailing list name here)
...
github:
   features:
     discussions: true
```

## Jobs!

The Apache Software Foundation (ASF) is seeking an Infrastructure Systems Administrator who will contribute to the stability, security, and growth of its globally-distributed infrastructure. The successful candidate will demonstrate strong system administration skills in diverse environments, proven experience with open source tools and methodologies, and a deep understanding of F/OSS project dynamics. This role is 100% remote, but availability for once-yearly travel to the United States for a multi-day Team Meetup is highly encouraged. The candidate must be based in the UK or Europe. Applicants from nations embargoed or sanctioned by the United States cannot be accepted. Salary commensurate with experience.

<a href="https://www.indeed.com/job/infrastructure-systems-administrator-036d1005bc664243" target="_blank">indeed.com/job/infrastructure-systems-administrator-036d1005bc664243" target="_blank"</a>

**More next month!**
