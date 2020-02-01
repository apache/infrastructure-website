Title: Guidelines for creating a Jira ticket

## Jira

<a href="https://issues.apache.org/jira" target="_blank">Jira</a> is a proprietary issue tracking product developed by Atlassian that allows bug tracking and agile project management. Atlassian provides Jira services to Apache projects. The tool's name is a short form of the name of the Japanese movie monster, Godzilla, and was an early developer nickname for the application.

Anyone can review existing Jira tickets, or "issues". You must register and log in if you want to create, comment or vote on, or watch issues. Only developers can edit, prioritize, schedule and resolve issues.

### Setting a ticket's priority

Follow these guidelines when assigning a priority to a Jira ticket. Infra uses these priorities to triage operations, and if we feel a ticket is mis-prioritized, we will change it or put it on hold.

- **Blocker**: A time-sensitive issue that is hindering the basic functions of a project.
  - *Example*: Our web site has been defaced and we just sent out a press release.

- **Critical**: A time-sensitive issue that causes disruption for a project, but is not hindering the basic functionality
  - *Example*: We just announced a new release, but SVN is not allowing us to upload or move the artifacts.

- **Major**: A (large) issue that needs attention soon, but is not time-sensitive in terms of basic project functionality. This includes asking for new resources to be set up. *Examples*:
   - Set up a new podling.
   - Add a Git repository.
   - Set up svn/git-pubsub.

- **Minor**: An issue that needs attention within a reasonable amount of time, but is not time-sensitive nor critical to a project's basic functionality or ongoing daily business. *Examples*:
  - Retire a project's resources.
  - Fix a JavaScript error on a web site.
  - Add GitHub integration for a repository.

- **Trivial**: A task that should be solved, but has minimal or no constraints in time
  - *Example*: Fix the copyright year on a web site.
