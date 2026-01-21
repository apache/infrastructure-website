title: Responding to the 2024 Infra survey
date: '2026-01-21 T02:23:56+00:00'
permalink: responding_to-2024_survey
layout: post

At the end of 2023, Infra conducted a survey, looking for feedback on how the team and the ASF infrastructure are working. It was good to see that, for instance, 95% of respondents felt that Infra offers adequate technical services for their project. The full report on responses is at [2023 Infra Survey Results](2023%20Infra%20Survey%20Results.html).

Many respondents took the time to add comments identify areas which needed improvement, and the Infra team never got around to acknowledging and responding to those comments and suggestions, until now. (Note, some comments were a little unclear or too terse for us to figure out how to answer them. Apologies for omitting them in this following list.) 

The comments and suggestions fell into several broad categories:

### Communications

  - **Periodic newsletter** -"Inside Infra" goes monthly to all members of the users@infra mailing list and is available here in the Infra Blog.
  - **Periodic publication** of the basic stuff, such as 'Where is self-serve?' - We include handy hints in the newsletter.
  - **Email announcements of important matters to all members** - We try to balance keeping people informed and not flooding inboxes.
  - **Better connection of each Infra service with its documentation** - Reviewing ...<a href="https://issues.apache.org/jira/browse/INFRA-27577" target="_blank">INFRA-27577</a>
  - **News box on the landing page at infra.a.o needs to be updated more frequently**  - implemented
  - **Questions to `users@infra.a.o` seem to go unanswered** - Questions seem to get a response within 24 hours in almost all cases
  - **Be more consistent in showing latest and earlier versions of info on the wiki pages** - We have the most current information at the top of the wiki page, and display any older information (perhaps related to a still-valid but no longer recommended process) that we feel is necessary to preserve at the bottom of the page, with a note indicating the build or situation this older information relates to. We have no policy of retaining wiki information that is no longer needed.
  - **Public archive containing summaries of all main points in all roundtables**  - this exists at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable" target="_blank">Infra Roundtable</a>
  - **Archived blog content is greatly bit rotted with no way to fix; no good modern blogging options** - Blog content is intended to be permanent. 'Archived' is archived and dated. When there is a possibility of confusion due to statements in a past blog entry, Infra adds a note at the top to indicate the current state of play.
  - **Mailing list noise from GitHub/GitBox. Drop messages from some bots** - "Projects can set their notification targets for commits and GitHub issues/PRs/actions and discussions via .asf.yaml." See <a href="https://github.com/apache/infrastructure-asfyaml?tab=readme-ov-file#notif" target="_blank">github.com/apache/infrastructure-asfyaml?tab=readme-ov-file#notif</a>

### Technical services

  - **Proactively improve the security posture of all ASF projects** - Infra is working on many fronts to enhance the security of all ASF and ASF project assets and servers. This work is never complete, because the threats constantly evolve. VP-Security is responsible for creating security policies for ASF projects to follow.
  - **Automating releases** - this is coming in 2026 with the Apache Trusted Release service.
  - **FreeBSD runners and CI builder on GitHub** - It may be an option to think about if GitHub can provide hosting, or if projects needing this can bring their own runners.
  - **More docs and examples for VM setup via puppet** - ASF committers can consult the `infrastructure-p6` GitHub repository for code examples.
  - **Password management solution** - Infra has not made progress on this service.
  - **More powerful GitHub Action runners for all platforms** - More powerful comes at a cost: GitHub charges for those. if projects can get donated self-hosted or 'runs-on' runners, Infra can hook them up.
  - **Video call service** - Desirable. Neither Infra nor Tooling are working on such a service at the moment.
  - **ASF project websites vary widely in visual appeal and functionality. How to make it easier to quickly set up ‘modern looking’ websites?** - Perhaps for a new ASF project, or community.a.o , or another, a global provided style that can built in different ways would indeed be nice (such as Forrest from old, Maven, etc.). We do have Pelican-enabled builds that can build a consistent look, but the tool remains hard to use currently.
  - **Fix tool sprawl – self-serve, whimsy, reporter, cveprocess...** - These are separate tools for separate services, and often run by different volunteer projects or committees. Infra is not in charge of many of these services.
  - **Issue tracking – automated scripts to migrate existing issues from Jira to GitHub Issues** - Infra offers a service to do this for projects using the jira-issues-importer tool, and projects like Maven and others have written their own tools.
  - **Research an official Stack Overflow integration as an alternative to users’ lists?** - Infra has been looking into this. But nothing determined yet.
  - **Easy to use and secure package and releasing platform** - the Apache Trusted Release service, which will provide this, is in the beta-test phase
  - **FreeBSD/BSD** - They are no longer an option.
  - **Automated voting tool** - Apache STeVe is available for PMC votes; the Apache Trusted Release service, which will have this feature for voting on releases, is in the beta-test phase.

### Jenkins

There were a number of questions for which the most accurate answers are available at `https://www.jenkins.io/doc/`

  - **In CI/CD, we don’t really have any CD. Where can we deploy test apps?** – Infra does not offer CD at the moment. Some projects may be able to host a test version of their apps on their virtual machines, but this may not be practical for our more complex products, and not meaningful for others.
  - **Need a simple build caching solution for Jenkins so we can cache Maven repositories between builds** – Maven has a build cache tool now.
  - **Jenkins builds should be containerized and isolated from one another, so one build does not bring down a node for everybody else. Need guaranteed minimum performance for performance-sensitive build tests.** – Some projects have secured donations of resources to ensure exclusive build controller and nodes. The rest of us have to share our limited resources.
  - **Long build queues on ASF Jenkins; problems with GHA builds** - Long build queues are not common any more. We have managed huge improvements to Jenkins build nodes in particular.
  - **Jenkins seems outdated. Would prefer something like Concourse.** - Opinions differ. Infra offers Jenkins, but it is not compulsory to use.
  - **More stability for Ubuntu Jenkins nodes** - We have made great strides in the Jenkins CI arena over the last two years and build nodes are pretty stable these days.

### Docker

  - **More control over Docker Hub repos** - A selfserve tool for creating dockerhub repos, adding/removing members, etc. is in the works.
  - **CI stability** - We have made huge improvements, and we continue to improve and expand our CI offering.
  - **Docker Images** - Docker Hub repos managed by infra for projects, and self service, coming for this.

### Builds

  - **Builds are sometimes flaky because of disk-full error, broken hardware, missing build tools...** - The Tooling team is hoping to help with these issues in the new Apache Trusted Release platform, which is in beta-test.
  - **Builds are very slow for projects with a large number of modules and different workflows for different test suites. Such projects need more dedicated resources.** - Projects that need additional resources may need to search for a donor or take the request to the Board. Infra does not have sufficient resources to get every project's builds into the comfort zone.
  - **Struggling to find good documentation on Buildbot hosts, in particular for setting up a Windows build.** - Agree - we do have Buildbot documentation, but it can do with improvements.

Infra plans to run the next version of its survey sometime in 2026.
