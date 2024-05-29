title: 2023 Infra Survey Results 
date: '2024-02-13' 
permalink: 2023_infra_survey_results
layout: post 

More than 50 people posted responses to our 2023 'year in review' survey. Here is a summary of the responses to questions and the comments added in each section.

We're grateful to those who took the time to fill out the survey. Without feedback like this, the Infra team can feel a bit like it is flailing around in the dark.

## Summary of responses

### Infra Roundtables

82% of survey respondents have attended an Infra Roundtable

Some reasons for not having attended include:

  - Time constraints (most frequent response)
  - Was not aware it existed
  - Do not need it / no pressing issues
  - Timezone issues (the roundtables frequently happen at a time which is more convenient to people in Europe and North American than in Asia)

88.9% say the roundtables ‘provide value’.

Topics respondents would like roundtables to address:

  - Things Infra is working on that might be useful to PMCs
  - Vulnerability scanning
  - Automation of
    - voting
    - policy compliance verification
    - releases
  - Ways to make it easier for contributors to projects to contribute to Infra coding tasks
  - Periodic hackathons Infra hackathons open to all contributors
  - Series of FAQs / tutorials on common tasks at the ASF

### Communication

81% agreed that Infra is getting better at open communication.

Further communications improvement suggestions included:

  - Periodic newsletter (implemented!)
  - Email announcements of important matters to all members
  - Better connection of each Infra service with its documentation
  - News box on the landing page at `infra.a.o` needs to be updated more frequently
  - Questions to `users@infra.a.o` seem to go unanswered
  - Be more consistent in showing latest and earlier versions of info on the wiki pages
  - Public archive containing summaries of all main points in all roundtables
  - Periodic publication of the basic stuff, such as 'Where is self-serve?'

### Technical services

95% feel Infra offers adequate technical services for their project.

Service improvement suggestions:

  - Proactively improve the security posture of all ASF projects
  - Automating releases (this is coming!) and dependency upgrades for CVE mitigation
  - Free BSD runners and CI builder on GitHub
  - More docs and examples for VM setup via puppet
  - Password management solution
  - More powerful GitHub Action runners for all platforms
  - Video call service

We asked which existing services need improvement. These areas got the most votes:

  - CI/CD (Jenkins, BuildBot, GitHub Actions – 62%
  - Issue Tracking (Jira, GitHubIssues, Bugzilla) – 31%
  - Documentation / Wiki pages – 31%
  - Source control (GitHub/GitBox, SVN) – 19%
  - Messaging (Slack, mailing lists) – 19%	

Comments:

  - Archived blog content is greatly bit rotted with no way to fix; no good modern blogging options
  - ASF project websites vary widely in visual appeal and functionality. How to make it easier to quickly set up ‘modern looking’ websites?
  - Issue tracking – automated scripts to migrate existing issues from Jira to GitHub Issues.
  - Fix tool sprawl – self-serve, whimsy, reporter, cveprocess...
  - Jenkins seems outdated. Would prefer something like Concourse.
  - Research an official Stack Overflow integration as an alternative to users’ lists?
  - In CI/CD, we don’t really have any CD. Where can we deploy test apps?
  - Docker Images.
  - More control over Docker Hub repos.
  - Builds are sometimes flaky because of disk-full error, broken hardware, missing build tools...
  - Builds are very slow for projects with a large number of modules and different workflows for different test suites. Such projects need more dedicated resources.
  - It’s easy for projects to configure build pipelines that don’t work well.
  - I shouldn’t have to create a filter to understand the context of an email from the ASF.
  - Struggling to find good documentation on Buildbot hosts, in particular for setting up a Windows build.
  - In a multilanguage project, Kotlin is not counted.
  - Mailing list noise from GitHub/GitBox. Drop messages from some bots.
  - Need a simple build caching solution for Jenkins so we can cache Maven repositories between builds
  - Need a good template for the static part of project websites. (Working on it!)
  - There is no documentation on cleanup after a build and main + subpath deployment of a website, nor an example to start with.
  - Long build queues on ASF Jenkins; problems with GHA builds
  - Jenkins builds should be containerized and isolated from one another, so one build does not bring down a node for everybody else. Need guaranteed minimum performance for performance-sensitive build tests.
  - Improve the messaging of Jira to the mailing lists.

### New Year’s resolutions for projects:

  - Hope to make more frequent releases (multiple mentions).
  - Get it fully, reproducibly built with OID integration to release it via Trusted Publishing to PyPI.
  - Reduce ‘onboarding barriers’ and bridging projects for more synergy.
  - Add documentation tutorials.
  - Attracting more people to work on the documentation.

### New Year’s hopes to get from Infra, the ASF, from your project

  - Easy to use and secure package and releasing platform (Working on it!)
  - More reliability
  - An arrangement with medium or substack
  - FreeBSD/BSD
  - More stability for Ubuntu Jenkins nodes
  - automated voting tool (Working on it!)
  - CI stabiity
  - More powerful GitHub Runners for all platforms

### Feedback for the Infra team:

Most of the comments were positive, with thanks for our efforts and good wishes for the new year.

And there was one “Well, there is that one guy...” (working on it!)
