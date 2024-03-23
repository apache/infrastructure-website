layout: post 
title: Inside Infra March 2024 
date: '2024-03-23' 
permalink: newsletter0324

Welcome to **Inside Infra** for March, 2024.

### Policy change on use of GitHub Actions

Due to misconfigurations in their builds, some projects have been using unsupportable numbers of GitHub Actions. As part of fixing this situation, Infra has added a 'resource use' section to the policy on GitHub Actions. This section of the policy will come into effect on **April 20, 2024**:

  - All workflows MUST have a job concurrency level less than or equal to 20. This means a workflow cannot have more than 20 jobs running at the same time across all matrices.
  - All workflows SHOULD have a job concurrency level less than or equal to 15. Just because 20 is the max, doesn't mean you should strive for 20.
  - The average number of minutes a project uses per calendar week MUST NOT exceed the equivalent of 25 full-time runners (250,000 minutes, or 4,200 hours).
  - The average number of minutes a project uses in any consecutive five-day period MUST NOT exceed the equivalent of 30 full-time runners (216,000 minutes, or 3,600 hours).
  - Projects whose builds consistently cross the maximum use limits will lose their access to GitHub Actions until they fix their build configurations.

The full policy is at <a href="https://infra.apache.org/github-actions-policy.html" target="_blank">https://infra.apache.org/github-actions-policy.html</a>.


### Roundtable summary

In the Roundtable of March 3, 2024, Clay Johnson of Gradle outlined the testing features that come with Develocity, focussing on their use with Gradle and Maven. For instance:

  - The build scan gives insights into what goes on in a build, and can help a project quickly focus on tests that are failing or flaky, and address related code issues.
  - Predictive test selection can speed up certain types of builds by skipping the tests that are not relevant to the build.

A fuller summary of this discussion, and conversation about GitHub Runners and other topics, is at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2024-03-06%2C+17%3A00+UTC" target="_blank">https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2024-03-06%2C+17%3A00+UTC</a>, and is available to ASF Members and Committers.

**Note**: There will be **no April 2024 Roundtable**. The series will resume in May.


### The end of Apache Paste Bucket?

In 2013 Infra rolled out Apache Paste Bucket (`http://paste.apache.org/`). In a blog entry at the time, we described it as an "ASF-driven site for posting snippets, scripts, logging output, configurations and much more and sharing them with the world."

The tool has seen some use over the past decade, but has had very little traffic in the last couple of years. To keep Apache Paste Bucket available, the code would require a significant upgrade. Unless we hear that the tool is important to some part of the ASF community, we plan to shut down Apache Paste in the near future.
<hr/>
The next newsletter will appear toward the end of April, 2024.
