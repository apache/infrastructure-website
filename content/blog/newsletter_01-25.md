title: Inside Infra January 2025 
date: '2025-01-21' 
permalink: newsletter0125 layout: post

Welcome to **Inside Infra** for January, 2025

The January **roundtable** took place Wednesday, January 8, 2025. The main topic was a deep dive into **asf.yaml**, the Swiss Army Knife of ASF build utilities.

The next version of .asf.yaml addresses a number of headaches with the first version, such as cumbersome design and the difficulty in testing changes to your .asf.yaml before going live with it. It centralizes data brokering, pre-validates schemes to ensure inter-feature cooperation, and puts in place a number of other improvements.

The summary of the presentation and discussion are <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2025-01-08+1700+UTC" target="_blank">here</a>, along with several useful links.

The new version of .asf.yaml should be live by the start of February, 2025.

The next roundtable will be **Wednesday, February 5, 2025, 1700 UTC**. The main topic will be creation, review and management of **custom GitHub Actions** that projects can use in their compile and build processes, and the self-serve way to add custom GitHub Actions to the GHA Allowlist.

See <a href="https://infra.apache.org/roundtable.html" target="_blank">this page</a> for details about how to join a roundtable, and what happens at it. 


## Global CSP brownout

Staring March 1, 2025, the ASF will be enforcing a **Content Security Policy** (CSP) for all project websites. 

  - External trackers from 3rd party providers are NO LONGER allowed
  - External resources from providers with which we do not have a Data Processing Agreement (DPA) are NO LONGER allowed

This policy will bring project websites into alignment with The ASF's security and privacy parameters.

The full policy, with links to important resources, is <a href="https://infra.apache.org/csp" target="_blank">here</a>.


## Reminder: Removing Blue Ocean

At the end of February, 2025, ASF Infra will remove all <a href="https://plugins.jenkins.io/blueocean/">Blue Ocean</a> and related plugins from our Jenkins ci-* controllers.

Cloudbees have removed the Blue Ocean plugin from their <a href="https://docs.cloudbees.com/docs/cloudbees-ci-kb/latest/troubleshooting-guides/admin-monitor-blueocean-removal" target="_blank">Cloudbees Assurance Program</a> (CAP), which our Jenkins Controllers use to maintain plugin integrity and compatibility. The Jenkins Open Source program also removed the plugin(s) from their own instances. The plugin is only receiving security updates from here on, and Cloudbees recommend that users switch to the <a href="https://docs.cloudbees.com/plugins/ci/cloudbees-pipeline-explorer" target="_blank">Pipeline Explorer</a> plugin. Infra has already installed Pipeline Explorer on all ASF controllers.

If you have questions about Blue Ocean replacements, email `users@infra.apache.org` or post your question on the #asfinfra channel in the the-ASF workspace on Slack.


More next month!
