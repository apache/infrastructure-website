title: Inside Infra May 2025 
date: '2025-05-23' 
permalink: newsletter0525 layout: post

## Welcome to Inside Infra for May, 2025

### Roundtable

There was no roundtable in May. The next roundtable will be **Wednesday, June 4, 2025, 1700 UTC**. The main topic will be a presentation on **JFrog and Artifactory**, a universal binary repository manager that enables teams to store, manage, and organize software packages throughout the development lifecycle.

Information about how to take part in a roundtable is at <a href="https://infra.apache.org/roundtable.html" target="_blank">infra.apache.org/roundtable.html</a>.

### Which Infra email address??

Infra monitors and participates in these email addresses:

  - `users@infra.apache.org` is for general infrastructure discussions and suggestions, and for questions related to ASF infrastructure and the Infra team that do not rise to the level of a Jira ticket. Only committers and ASF members can subscribe to the list.
  - `private@infra.apache.org` is for communications that may involve PII, personnel issues, or other information that should not be widely shared. Only ASF Members can subscribe to the list.
  - `root@apache.org` is an unarchived alias that goes to Infra staff only for Infra-related security issues or other private matters that don't fit other lists. See the second entry on <a href="https://infra.apache.org/infra-contact.html" target="_blank">Contacting Infra</a> about reporting a security issue specific to an ASF project or a project's product.

In the past there was the `infrastructure@apache.org` mailing list. This address is no longer in use.

### Reminder: removal of Maven integration plugin

At the end of May, 2025, Infra will be removing the deprecated Cloudbees Maven Integration Plugin (<a href="https://plugins.jenkins.io/maven-plugin/" target="_blank">Maven job type</a>) from all ci-* Controllers here at the ASF. We recommend that projects that have been using this plugin migrate to a Pipeline job or a Freestyle job with Maven steps. There is a <a href="https://docs.cloudbees.com/plugins/ci/declarative-pipeline-migration-assistant" target="_blank">tool</a> already installed in ASF Controllers so that you can easily migrate to a pipeline job.

For further information, see:

  - <a href="https://docs.cloudbees.com/docs/cloudbees-ci-kb/latest/troubleshooting-guides/help-bulk-migration-maven-jobs" target="_blank">help-bulk-migration-maven-jobs</a>
  - <a href="https://plugins.jenkins.io/pipeline-maven/" target="_blank">plugins.jenkins.io/pipeline-maven/</a>
  - a YouTube video: <a href="https://www.youtube.com/watch?v=u0_sIo9I7CE" target="_blank">Darin Pope, Cloudbees Advocate, goes through the steps to migrate</a>

Gavin McDonald has checked all project controllers, and sees that very few projects are still using the Maven type job, so this removal should affect almost nobody. If, however, you have concerns or would like help with migrating your project's Maven-type job, Infra is only to happy to help.

Please do create an INFRA Jira ticket right away if you need help or clarification.

### ViewVC access

In a response to the massive increase in abusive requests that caused our Subversion ViewVC service to buckle under the pressure, we have implemented **authorization checks for ViewVC**. In essence, this means ViewVC is now only accessible to ASF committers.

We understand that this will cause frustration for some project participants, and we took this step because, at the moment, no other option is available.

### GitHub repo branch protection rule updates

In early May, Infra made a change to GitBox, the service that hosts our Git repositories and keeps everything in sync with GitHub. This changes the way we synchronize our own Git repositories with GitHub, in order to allow for branch protection rules on GitHub to be enforced even on GitBox. In essence, this means your project can set up branch protection rules on GitHub and have the same rules go into effect on GitBox.

For most projects, this should not involve any change in your workflow or the way you push commits, though some projects or individual committers may find that previously-allowed pushes are no longer allowed due to the harmonization of GitHub and GitBox branch rules. In those cases, we advise that projects set clear guidelines for how they want their workflows and protections set up, and how to modify any existing workflows or guides that would no longer be permissible.

As we move ever-closer towards more scrutiny and security in the open source software community, we hope this will help make projects more confident in their security setup (and any other procedures that revolve around branches and protections).

As always, if you have any questions or encounter any issues related to this change, please reach out to the Infrastructure team, either on `users@infra.apache.org`, on our Slack channel, `#asfinfra`, or by opening an Infra Jira ticket.

### Did you know?

You can add and remove external collaborators to your GitHub repository using .asf.yaml! (see <a href="https://github.com/apache/infrastructure-asfyaml#assigning-the-github-triage-role-to-external-collaborators" target="_blank">Assigning the GitHub tirage role to external collaborators</a>).

If you invited a collaborator and they missed the invitation (they're only valid for seven days), simply

  - remove them from the collaborator section in your .asf.yaml
  - commit and push the change
  - re-add them to the collaborator section
  - commit and push that change

They will receive a new invitation.

You must do this in two separate pushes, as a push is what constitutes a binding change in .asf.yaml.

**More next month!**
