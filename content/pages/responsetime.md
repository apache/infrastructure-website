Title: Response time
license: https://www.apache.org/licenses/LICENSE-2.0

The Infra team takes seriously all work requests submitted to it and all reports it receives about issues in the Apache system. We triage such reports according to severity, and seek to resolve them in a timely fashion.

## Account creation

The ASF follows the procedure outlined at <a href="https://infra.apache.org/managing-committers.html" target="_blank">Managing Project Committers</a> for creation of committer accounts. When the ASF Secretary approves the account-creation request, they inform Infra. Infra commits to creating the account within **seven business days**, although in practice it usually happens more quickly than that.

## Services

Currently, Apache services are operating at an uptime rate of over 99%.

For the current status of services, see <a href="https://status.apache.org/" target="_blank">the ASF status page</a> and the Infra <a href="https://www.apache.org/uptime/" target="_blank">response graphs</a>.

### Jira issue reports and service requests

Here is how we triage issue reports and service requests submitted as Jira tickets:

#### Blocker
A time-sensitive issue that is hindering a project's basic functions.

  - **Goal**: 24 hours to respond, 3 days (72h) to resolve. Weekend hours count against this goal.
  - **Example**: Web site has been defaced and we just sent out a press release.

#### Critical
A time-sensitive issue that causes disruption for a project, but is not hindering basic functionality.

  - **Goal**: 36 hours to respond, 4 days (96h) to resolve. Weekend hours count against this goal.
  - **Example**: We just called a new release, but SVN is not allowing us to upload or move the artifacts.

#### Major
This is the default Jira issue priority. It fits a large issue that Infra should resolve quickly, but is not time-sensitive or related to basic project functions. This includes requesting new resources.

  - **Goal**: 2 days (48h) to respond, 5 days (120h) to resolve. Weekends do not count against this goal.
  - **Examples**:
    - Set up a new podling.
    - Add a git repository.
    - Set up py/svn/git-pubsub.

#### Minor 
An issue that Infra should resolve within a reasonable time, is not time-sensitive and is not critical to a project's basic functionas or ongoing daily business.

  - **Goal**: 3 days (72h) to respond, 2 weeks (336h) to resolve. Weekends do not count against this goal.
  - **Examples**:
    - Retire a project's resources.
    - Fix a JavaScript error on a web site.
    - Add GitHub integration for a repository.
    - Refine Jira settings for a project.

#### Trivial
A task that Infra should resolve, but that has minimal or no time constraints.

  - **Goal**: 3 days (72h) to respond, 4 weeks (672h) to resolve. Weekends do not count against this goal.
  - **Example**: Fix copyright year on a web site.
  
### Notes

  - Response time is counted as first reply (from someone else) or assignment.
  - Tickets marked as `Planned Work` do not have a response-time goal.
  - Tickets marked as `Waiting for user` have no response time goal until the user responds.
  - Weekends do not count toward response time for all tickets except those marked `Blocker` or `Critical`.
  - Tickets only appear in response statistics once resolved or if exceeding the goal for their category.
  - Ticket velocity (user engagement and interaction) is important.
