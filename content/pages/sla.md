Title: Service Level Agreement (SLA)

A service-level agreement, or SLA, is a service provider's commitment to its clients. The Infra team commits to these targets for the services it maintains for the Apache community.

### Services ###

Currently, Apache services are operating at an uptime rate of over 99%.

For current status of services, see <a href="https://status.apache.org/" target="_blank">the ASF status page</a> and the Infra <a href="https://www.apache.org/uptime/" target="_blank">SLA graphs</a>.

### Jira issue reports and service requests ###

Here is how we calculate SLAs and Infra's response for issue reports and service requests submitted as Jira tickets:

#### Blocker ####
A time-sensitive issue that is hindering a project's basic functions.

  - **SLA**: 24 hours to respond, 3 days (72h) to resolve. Weekends count against SLA hours.
  - **Example**: Web site has been defaced and we just sent out a press release.

#### Critical ####
A time-sensitive issue that causes disruption for a project, but is not hindering basic functionality.

  - **SLA**: 36 hours to respond, 4 days (96h) to resolve. Weekends count against SLA hours.
  - **Example**: We just called a new release, but SVN is not allowing us to upload or move the artifacts.

#### Major #### 
This is the default Jira issue priority. It fits a large issue that Infra should resolve quickly, but is not time-sensitive or related to basic projct functions. This includes requesting new resources.

  - **SLA**: 2 days (48h) to respond, 5 days (120h) to resolve. Weekends do not count against SLA hours.
  - **Examples**:
    - Set up a new podling.
    - Add a git repository.
    - Set up py/svn/git-pubsub.

#### Minor #### 
An issue that Infra should resolve within a reasonable time, is not time-sensitive and is not critical to a project's basic functionas or ongoing daily business.

  - **SLA**: 3 days (72h) to respond, 2 weeks (336h) to resolve. Weekends do not count against SLA hours
  - **Examples**:
    - Retire a project's resources.
    - Fix a JavaScript error on a web site.
    - Add GitHub integration for a repository.
    - Refine Jira settings for a project.

#### Trivial ####
A task that Infra should resolve, but that has minimal or no time constraints.

  - **SLA**: 3 days (72h) to respond, 4 weeks (672h) to resolve. Weekends do not count against SLA hours.
  - **Example**: Fix copyright year on a web site.
