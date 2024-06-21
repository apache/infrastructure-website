title: Inside Infra June 2024 
date: '2024-06-24' 
permalink: newsletter0624
layout: post 

Welcome to _Inside Infra_ for June, 2024.

**A change to website creation and builds for projects**

Many ASF projects, and the Infrastructure team, have been using the ASF-pelican template and service to build and deploy their websites. Infra has decided to deprecate its customized buildsite offerings in favor of those provided by GitHub Pages. A GitHub Action provides the same Pelican features and workflow as the former service did.

Infra is offering support to help projects move from the former buildsite tool to the GitHub Action, providing a run-once migration script that adapts the website repository. 

The documentation about building websites with Pelican that starts at <a href="https://infra.apache.org/asf-pelican.html" target="_blank">infra.apache.org/asf-pelican.html</a> is being updated.

To read more about migration methods, please visit: <a href="https://cwiki.apache.org/confluence/display/INFRA/Moving+from+Infrastructure-pelican+to+GitHub+Actions" target="_blank">Moving from Infrastructure-pelican to GitHub Actions</a>, and the GHA's README file: <a href="https://github.com/apache/infrastructure-actions/blob/main/pelican/README.md" target="_blank">github.com/apache/infrastructure-actions/blob/main/pelican/README.md</a>. 

We are expecting to wrap up disabling our Pelican buildsite offerings by the end of 2024. If you have any questions regarding this migration, please email us at private@infra.apache.org or message us on #asfinfra in the-asf Slack space.


**Apache and HSTS**

Infra is adding apache.org to Chrome's HTTP Strict Transport Security (HSTS) preload list, upping the security measures for the majority of visitors to our sites. This change will go into effect on July 1st.


**Your good ideas for Infrastructure**

Members of the ASF community have lots of good ideas for services Infra could provide, or improvements the team should make to existing services. To this point, there has not been a convenient way to get those ideas to where people can respond to them by supporting them, suggesting tweaks to the original idea, or explaining why they think the service or fix is not necessary.

Infra has set up "Infrastructure-ideas" (<a href="https://github.com/apache/infrastructure-ideas" target="_blank">github.com/apache/infrastructure-ideas</a>), a GitHub repository to host, discuss, and get consensus on people's ideas for ASF infrastructure. For now, we will mainly be making use of the repo's "Discussions" tab.

  -Start a new discussion in the category that best matches it:
    - Enhancements
    - General
    - New ideas for services
    - Polls
    - Q&A
  - If you see a suggestion that you agree with, you can upvote it. This helps to demonstrate how broadly the community supports the idea, and that, in turn, could help Infra decide which ideas to devote resources toward implementing.
  - If you want to flesh out a suggestion, feel free to add a comment, a question, a challenge, a tweak to it.
We look forward to your ideas!


**The new ASF distribution platform**

Infra developing the Artifacts Distribution Platform (ADP). The idea is to consolidate dist.apache.org, downloads.apache.org, rsync.apache.org and archive.apache.org into one service that will free up resources and:

  - simplify backups of release artifacts
  - remove the need to "police" projects about their release pages by no longer requiring them to manually archive older releases
  - ensure that all new releases follow our release policies by only allowing policy-compliant artifacts to be released
  - make it easier for product users to verify that what they are about to download is a certified ASF artifact

We have assembled lists of necessary features, 'good to have' features, and ambitious pipe dreams, and value input from all across the The ASF's communities, and development is well underway. We expect to bring the distribution platform on-line in stages, with the first stage becoming available late in 2024 or early in 2025.

  - Join the `artifacts@infra.apache.org` mailing list.
  - Ask to be invited to the `artifact-platform-dev` channel in the `the-ASF` workspace on Slack.
  - Review the <a href="https://cwiki.apache.org/confluence/display/INFRA/Artifacts+Distribution+Platform" target="_blank">current collection of ideas and issues</a> related to the ADP. Add your thoughts/concerns/insights in the editable pages linked to from that main page. (Note: we have already blue-skied a very complex application. If you suggest another component, we may invite you to help develop it.)
    
**Note**: the name of the platform may change before it goes live.


**Roundtable summary**

The June, 2024 Roundtable reviewed and discussed tools and resources that every PMC should consider using:

  - Virtual machines - the bread and butter of The ASF. Each project can use an Infra-supported virtual machine for free.
  - <a href="https://github.com/apache/infrastructure-asfyaml" target="_blank">.asf.yaml</a> - Lets project manage their own website development and many other things. .
  - self-serve - Provides many tools for Committers, project leaders, and ASF Members.
Confluence and Jira - Wiki and ticketing system from Atlassian.
  - Apache STeVe - Voting tool for the ASF and for projects. It is its own top level project.
  - Slack - A project channel in the 'the-asf' space can be a communications hub for a project rather than, say, IRC.
  - <a href="https://infra-reports.apache.org" target="_blank">Infra Reports</a> - Dashboard covering resource uptime, public download statistics, use of GitHub Actions, the project website resource checker, and so on.
  - <a href="https://github.com/apache/infrastructure-actions" target="_blank">Infrastructure Actions repo</a> - hosts Infrastructure-approved GH Actions that all projects can use. This generated a lot of interest and suggestions from those present, so we are devoting the next Roundtable to talking through how we will manage this repository and curate its contents.

We also touched on Non-Infra tools:

  - Reporter (ComDev)
  - Apache Whimsy

The full notes of the meeting are at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2024-06-05%2C+17%3A00+UTC" target="_blank"Infra Roundtable 2024-06-05, 17:00 UTC</a>.

The next Roundtable will be **July 3, 2024, 1700UTC**. We will discuss how to manage the new repository to host ASF-approved GitHub Actions.

More soon!
