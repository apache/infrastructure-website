Title: Application upgrades policy and workflow
license: https://www.apache.org/licenses/LICENSE-2.0

This policy encompasses Infra's approach to upgrades of Jenkins, Confluence and Jira and their respective plugins.

# Upgrades

### Jenkins

**Main Jenkins instance**
_Upgrades once a quarter_

Infra follows the <a href="https://jenkins.io/download/lts/" target="_blank">LTS line of releases</a>, which the Jenkins Project releases on a 12 week cycle. Once every three months, on the last Saturday or Sunday of the month following the Jenkins LTS release, ASF Infra upgrades the main instance. 

**Jenkins plugins**
_Upgrades once a month_

We upgrade all plugins (there are more than 200!) before and after the main instance upgrade, as appropriate, and at the end of each month when there is no main instance upgrade to perform.

### Jira

**Main Jira instance**
_Upgrades every six months_

Jira gets a new release every two to six weeks, far too often (and unpredictable) for us to upgrade every release they make. Infra upgrades our Jira instance to whatever the latest release is every six months.

**Jira plugins**
_Upgrades every two months_

We upgrade Jira plugins before or after each main instance upgrade, as appropriate, and once every two months between main instance upgrades. 

### Confluence

**Main Confluence instance**
_Upgrades every six months_

Our goal is to upgrade Confluence to the latest version twice a year.

**Confluence plugins**
_Upgrades every two months_ 

Every two months we perform upgrades to plugins that are compatible with the version of the main Confluence instance we are running.

# Documentation

Infra documents what we upgraded and when, from what version to what version, on these pages:

  - <a href="https://cwiki.apache.org/confluence/display/INFRA/Jenkins+Upgrades" target="_blank">Jenkins upgrades</a>
  - <a href="https://cwiki.apache.org/confluence/display/INFRA/Jenkins+Plugin+Upgrades" target="_blank">Jenkins plugin upgrades</a>
  - <a href="https://cwiki.apache.org/confluence/display/INFRA/Jira+Upgrades" target="_blank">Jira upgrades</a>
  - <a href="https://cwiki.apache.org/confluence/display/INFRA/Jira+Plugin+Upgrades" target="_blank">Jira plugin upgrades</a>
  - <a href="https://cwiki.apache.org/confluence/display/INFRA/Confluence+Upgrades" target="_blank">Confluence upgrades</a>
  - <a href="https://cwiki.apache.org/confluence/display/INFRA/Confluence+Plugin+Upgrades" target="_blank">Confluence plugin upgrades</a>

# Notifications

Since Jenkins, Jira and Confluence are **Core Services**, Infra issues a notice of a planned upgrade at least 72 hours ahead of the event on the wiki or a web page and by emails to the `builds@apache.org` and `users@infra.apache.org` mailing lists. We add a Twitter notification by `ASF Infrabot` one hour before upgrades begin.

# In case of emergencies

Occasionally things go wrong with a main or plugin upgrade, and security issues may arise. If we determine that there is an issue, we will work on it immediately until we resolve it. We will send an email to the relevant list and a notice on X (the former Twitter) about any unexpected downtime.
