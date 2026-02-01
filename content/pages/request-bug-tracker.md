Title: Requesting or changing an issue and feature-request tracker for a project
license: https://www.apache.org/licenses/LICENSE-2.0

The ASF recommends these options for tracking issues and feature requests:

* <a href="https://issues.apache.org/jira" target="_blank">Jira</a>
* The <a href="https://guides.github.com/features/issues/" target="_blank">GitHub issue tracking feature</a>

### Requesting a Jira instance

Infra itself uses Jira, so to request a Jira instance for your project, create a <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">Jira ticket</a>. Set the issue type to 'New Jira Project' and provide the necessary details:

  - A list of committers with access to modify/close tickets
  - A list of committers who will act as Jira administrators
  - A notification scheme (to which email address do JIRA notifications go?)
  - A name and description for the Jira instance
  
### Response

Infra will respond within a couple of days, either with a request for clarification of some point or to let you know that the instance is set up and ready for your project to use.

### Using GitHub Issue tracking
Enabling GitHub Issue tracking for your project is self-serve. In the .asf.yaml file for your repository, locate the `github` section and set the `issues` option to true, as in the example below. 

```
github:
  features:
    # Enable wiki for documentation
    wiki: true
    # Enable issue management
    issues: true
    # Enable projects for project management boards
    projects: true
```

You can review your .asf.yaml settings for Git at <a href="https://github.com/apache/infrastructure-asfyaml/blob/main/README.md" target="_blank">Git .asf.yaml features</a>.

### Switching from Jira to GitHub Issue tracking

If your project switches from Jira to GitHub for receiving issue reports and feature requests, you will want to change the existing Jira tickets to read-only, and prevent people from trying to open new tickets. This will eliminate time and effort you will otherwise have to spend on rejecting new tickets and explaining the change.

Once GitHub issue tracking is active for the project, open what will probably be your final Jira ticket for Infra, requesting Infra to:

  - Change all existing Jira tickets for the project to read-only
  - Remove the project name from the drop-down list of projects that a person can choose from when creating a Jira ticket.

Infra will let you know when this has been completed.

We recommend that you inform your dev and user communities of the change.
