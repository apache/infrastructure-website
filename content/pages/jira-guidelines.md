Title: Guidelines for creating a Jira ticket

## Jira tickets

<a href="https://issues.apache.org/jira" target="_blank">Jira</a> is a proprietary issue tracking product developed by Atlassian that allows bug tracking and agile project management. Atlassian provides Jira services to Apache projects. The tool's name is a short form of the name of the Japanese movie monster, Godzilla, which was an early developer nickname for the application.

Anyone can review existing Jira tickets, or issues. You must register and log in if you want to create, comment or vote on, or watch issues. Only developers can edit, prioritize, schedule or resolve issues.

ASF and many of its projects use Jira to keep track of work to be done. The largest group of tickets assigned to Infra are requests for Infra to perform a task of one sort or another. The next largest category is reports of possible bugs in the Infrastructure system.

<ul>
<li><a href="#before">Before you create a ticket</a></li>
<li><a href="#writing">Writing a good Jira ticket</a></li>
<li><a href="#followup">Follow-up</a></li>

</ul>


<h3 id="before">Before you create a ticket<a class="headerlink" href="#before" title="Permanent link">&para;</a></h3>

  1. Browse the existing Jira tickets to see if others have already reported the bug you noticed or have requested the task or additional feature that you were going to ask for. If you find a ticket that covers what you wanted to report, you can add a comment and maybe some more relevant information to the existing ticket.
  2. Decide whether an Apache Jira ticket is the proper venue for your concern. For example, the Infrastructure team installs and operates multiple third party services on behalf of the ASF and its projects. Examples include Jira itself, GitHub, TravisCI, JFrog, LastPass, PonEE, Okta, Nexus, Confluence, and Statuspage. If you have a problem with the core functions of a third party service, it will be more efficient to file a bug report with that service, rather than with Infra or any ASF project. Infra will **close as invalid** any bug report or enhancement request about a third party service that does not relate to the ASF's interaction with or configuration of that service.
  3. If the ticket is not to report an issue, but to request that Infra make a configuration change, add a service, create a virtual machine, or perform some other work for your project, _unless you are a committer or a PMC member of the project_, include in the ticket a reference to the email thread in which the PMC agreed to that request. Infra will **reject** Jira tickets submitted on behalf of a PMC by someone who is not a committer for that project and cannot in some other way establish a) their connection to the project and b) PMC approval for the request.

**Note**: If the ticket is for a major request, such as to set up a virtual machine for the project, the ticket **should** demonstrate PMC approval of the request, no matter what status the ticket-creator has.

<h3 id="writing">Writing a good Jira ticket<a class="headerlink" href="#writing" title="Permanent link">&para;</a></h3>
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

<h3 id="followup">Follow-up<a class="headerlink" href="#followup" title="Permanent link">&para;</a></h3>

Once you have submitted your ticket, allow a reasonable time for Infra to respond to you. A team member will probably respond within 24 hours for an urgent issue, but might take a great deal longer for a low-priority request. After that time has passed, feel free to write a reminder email to `users@infra.apache.org`, including the Jira ticket number.

Infra may respond in a number of ways, including:

  - Closing the ticket as **invalid**. Review "Before you create a ticket", above, for reasons that may generate this response.
  - Asking for **further details**. You may then see that the status of the ticket has changed to _waiting for user_. Provide the details as best you can in a comment, and change the status to _waiting for Infra_.
  - Reporting the issue **resolved**. Please verify the fix or that the requested service is now available. If all is well, and Infra has not changed the status to _closed_ or one of its variants, feel free to do so yourself.

**Note**: If the ticket's status is _waiting for user_, Infra may ignore it for now and work on other tickets.
