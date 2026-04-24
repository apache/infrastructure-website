title: Inside Infra April 2026 
date: '2026-04-24' 
permalink: newsletter0426 layout: post

## Welcome to Inside Infra for April, 2026

### Roundtable

The April 1 Roundtable focused on the migration of the ASF's Confluence Wiki and Jira services from local instances to the cloud. This move is necessary because our use of both services far outstrips what the local instances were designed to handle.

There are significant technical challenges in the migration:

  - We have 1.2 million Confluence pages related to The ASF, its committees, and most of its projects.
  - We have a similar number of Jira tickets related to 682 ASF projects. We have to migrate them all, even the tickets related to retired projects, to maintain project development history.
  - We have over 150,000 user accounts for Jira and almost 100,000 for Confluence (many ASF-related people have one of each, of course). Many of these are inactive. We have to get our combined number of accounts down to 75,000.

The migration task needs more projects to volunteer to take part so we can address any issues that come up before we do the migration. Project PMCs can express their interest in a message to `users@infra`, in an Infra Jira ticket, or in the conversation on the `#atlassian-cloud-migration` channel in the `the-asf` Slack space.

A summary of the presentation and discussion is at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2026-04-1" target="_blank">cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2026-04-1</a>.

The next roundtable will be **May 6, 1700 UTC**. The timely topic for discussion is **AI coding - infrastructure implications**.

Details about joining a roundtable, and what goes on at one, are at: <a href="https://infra.apache.org/roundtable.html" target="_blank">infra.apache.org/roundtable.html</a>.

### MFA

Infra has integrated and deployed **Authentik**, an open source identity platform, as the Foundation's new multi-factor authentication (MFA) service. The platform is operational and we are now in a soft launch, working with the Tooling team to integrate the first production services: ASF Trusted Release platform (ATR) and the Board Agenda Tool (BAT).

These early integrations will help to validate the end-to-end authentication flow before broader rollout.

Further information is at <a href="https://cwiki.apache.org/confluence/display/INFRA/MFA+User+Guide" target="_blank">MFA User Guide</a>.

### Rulesets and CoPilot code reviews in GitHub

Rulesets and CoPilot code reviews are now available for ASF project repositories. You make both available through settings in the repository's .asf.yaml file.

  - **Rulesets** help you control how people can interact with branches and tags in a repository. See <a href="https://github.com/apache/infrastructure-asfyaml?tab=readme-ov-file#rulesets" target="_blank">the section on rulesets in the `.asf.yaml` README file</a>.
  - **CoPilot code review** can review code written in any coding language and provide feedback. It reviews your code from multiple angles to identify issues and suggest fixes, which you can apply with a couple of clicks. See <a href="https://github.com/apache/infrastructure-asfyaml?tab=readme-ov-file#copilot_code_review" target="_blank">the section on Copilot code review in the `.asf.yaml` README file</a>.

### Infra at C/C Glasgow

The Infrastructure team will present a full track of talks, discussions, workshops, games and an in-person Roundtable at Community over Code Glasgow, **October 11-14**. The <a href="https://communityovercode.org/wp-content/uploads/2026/02/Community-Over-Code-Prospectus-2026.pdf" target="_blank">conference prospectus</a> is available now, and the detailed schedule of keynotes, tracks, and talks–-and Games Night!--will be available soon.

### Phishing attempts

Projects are seeing a large number of phishing attempts in Slack workspaces. The attacker, using a fake account, pretends to be someone in an important role in The ASF or the larger coding world, and sends direct messages to members to try to lure them to phishing websites. If you receive a message like this that is outside your normal experience on Slack, do not click on any link it includes. First confirm by another channel that it came from the supposed sender.

### Infra 101

**Your project has a person who isn't a committer that they wish to be able to review pull requests** 

The project can assign the Triage (or collaborator) role to a user who is not a committer or ASF Member in the repository's <a href="https://github.com/apache/infrastructure-asfyaml">`.asf.yaml`</a> file with an entry like this:

```
github:
  collaborators:
    - externalgithubuserhere 
```

**More next month!**
