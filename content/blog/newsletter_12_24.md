title: Inside Infra December 2024 
date: '2024-12-21' 
permalink: newsletter1224 layout: post

**Welcome to Inside Infra for December, 2024**

The **December roundtable** did not take place due to presenter illness. We have pushed its topic to next month. That roundtable will be **Wednesday, January 8, 2025, 1700 UTC**. The main topic will be a deep dive into **asf.yaml**, the Swiss Army Knife of ASF build utilities.

See <a href="https://infra.apache.org/roundtable.html" target="_blank">this page</a> for details about how to join a roundtable, and what happens at it. 

## Removing Blue Ocean and related plugins

At the end of February, 2025, ASF Infra will remove all <a href="https://plugins.jenkins.io/blueocean/" target="_blank">Blue Ocean</a> and related plugins from our Jenkins ci-* controllers.

Cloudbees have removed the Blue Ocean plugin from their <a href="https://docs.cloudbees.com/docs/cloudbees-ci-kb/latest/troubleshooting-guides/admin-monitor-blueocean-removal" target="_blank">Cloudbees Assurance Program</a> (CAP), which our Jenkins Controllers use to maintain plugin integrity and compatibility. The Jenkins Open Source program also removed the plugin(s) from their own instances. The plugin is only receiving security updates from here on, and Cloudbees recommend that users switch to the <a href="https://docs.cloudbees.com/plugins/ci/cloudbees-pipeline-explorer" target="_blank">Pipeline Explorer</a> plugin. Infra has already installed Pipeline Explorer on all ASF controllers.

If you have questions about Blue Ocean replacements, email `users@infra.apache.org` or post your question on the `#asfinfra` channel in the `the-ASF` workspace on Slack.

## Naming of repositories for podlings

In the past, the names of Git repositories for projects in the Incubator were supposed to start with 'incubator-', and then the project's name. We no longer follow this pattern, so there is no need to request the 'incubator-' prefix for a new Git repository for a project, or when migrating an existing repository to the project.


**More in the new year!**
