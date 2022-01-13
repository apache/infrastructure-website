Title: Guidelines for creating a Jira ticket

## Jira tickets

<a href="https://issues.apache.org/jira" target="_blank">Jira</a> is a proprietary issue tracking product developed by Atlassian that allows bug tracking and agile project management. Atlassian provides Jira services to Apache projects. The tool's name is a short form of the name of the Japanese movie monster, <a href="https://en.wikipedia.org/wiki/Jira_(software)" target="_blank">Godzilla</a>, and was an early developer nickname for the application.

Anyone can review existing Jira tickets, or issues. You must register and log in if you want to create, comment or vote on, upload attachments, or watch issues. Only <a href="https://www.apache.org/foundation/how-it-works.html#committers" target="_blank">committers</a> can edit, prioritize, schedule and resolve issues.

ASF and many of its projects use Jira to keep track of work to be done. The largest group of tickets assigned to Infra are requests for Infra to perform a task of one sort or another. The next largest category is reports of possible bugs in the Infrastructure system.

### Before you create a ticket

  1. Browse the existing Jira tickets to see if others have already reported the bug you noticed or have requested the task or additional feature that you were going to ask for. If you find a ticket that covers what you wanted to report, you can add a comment and maybe some more relevant information to the existing ticket.
  2. Decide whether an Apache Jira ticket is the proper venue for your concern. For example, the Infrastructure team installs and operates multiple third party services on behalf of the ASF and its projects. Examples include Jira itself, GitHub, TravisCI, JFrog, LastPass, PonEE, Okta, Nexus, Confluence, and Statuspage. If you have a problem with the core functions of a third party service, it will be more efficient to file a bug report with that service, rather than with Infra or any ASF project. Infra will **close as invalid** any bug report or enhancement request about a third party service that does not relate to the ASF's interaction with or configuration of that service.
  3. If the ticket is not to report an issue, but to request that Infra makes a simple or minor configuration change, add a service, or perform some other work for your project, **unless you are a <a href="https://www.apache.org/foundation/how-it-works.html#committers" target="_blank">committer</a> or a <a href="https://www.apache.org/foundation/how-it-works.html#pmc-members" target="_blank">PMC member</a> of the project**, you **MUST** include in the ticket a reference to the email thread in which the PMC agreed to that request. Infra will **reject** any Jira tickets submitted on behalf of a PMC by anyone who is not a <a href="https://www.apache.org/foundation/how-it-works.html#committers" target="_blank">committer</a> for that project and cannot in some other way establish **a)** their connection to the project and **b)** PMC approval for the request.
  4. If the ticket is for a major request, such as setting up a virtual machine, granting elevated access or changes to project Infrastructure, you **MUST** be a <a href="https://www.apache.org/foundation/how-it-works.html#committers" target="_blank">committer</a> for that project and the ticket **MUST** demonstrate PMC approval of the request.

### Writing a good Jira ticket
If there is nothing in Jira already that covers what's on your mind, and the topic seems related to Apache services or an Apache project rather than a third party, click "Create" to display a form where you can describe your issue or request. Providing as much relevant information as you can helps Infra respond quickly and appropriately.

The form is pretty clear, so the focus here is on a couple of key fields.

#### Project
This is the group you want to take a look at the ticket. Select "Infra" for an infrastructure issue or request. Select a specific project if the issue is something like a problem in the project's documentation or website.

#### Issue type
There's a good list of issue types to choose from. Make sure you select the most appropriate one.

#### Project (again)
Maybe you want Infra to look at a problem with the Apache Widget project. Then in this field you would select Widget. Most of the time, for an Infra ticket, you will select Infra again.

#### Summary
This is your quick statement of your problem or request. "Infra is broken!" would not be a useful statement. Something like "Self-serve site hangs, then crashes" is more likely to get the right person's attention and a prompt resolution to the problem.

#### Priority
Make your best guess at how urgent this thing is. Infra triages Jira tickets by their prioritiesm, and may adjust the priority of a ticket if we feel its current setting is too high or too low.

The options are

  - **Blocker**: a time-sensitive issue that is hindering a basic function of a project. (_example: "We just announced a new release, but SVN is not allowing us to upload or move the artifacts."_)
  - **Critical**: a time-sensitive issue that is disrupting the project, but does not hinder basic functions. (_"Our website has been defaced."_)
  - **Major**: this issue needs attention soon, but is not hindering basic functions. Most requests for new resources fall into this category. (_"Add a Git repository."_)
  - **Minor**: this issue needs attention, but is not time-sensitive and does not hinder basic functions. (_"Fix a JavaScript error on our website."_)
  - **Trivial**: this issue is minimal and has no time constraints. ( _"The copyright year on Infra web page bla.html is incorrect."_)

#### Component/s
Select one or more components that this issue or request relates to. If you cannot figure out what to pick, select "Other/misc".

#### Fix Version/s
This an optional field, useful if your issue concerns a specific Infra tool or service and you know the version you are using.

#### Assignee
If you specify someone here, that person receives an alert about the issue. You can accept the default (Automatic) to put the issue in the queue for the Infra team.

#### Environment
This is an optional field where you can describe your operating system, software platform and/or hardware specifications if they are relevant to the bug, task, or feature request.

#### Description
Provide the juicy details here. For example, for a bug report, Infra needs to know how to reproduce the thing you ran into. Describe what you were doing ("I was logged in to bla.html using Firefox"), what you wanted to do ("I wanted to do xxx"), what you expected to happen, and what you actually experienced.

For a feature request, it helps if you can not only describe the feature, but explain why the project needs it.

#### Other fields
There are many more optional fields that you can probably skip.

When you have completed entering the useful information, click **Create** to create the ticket.
