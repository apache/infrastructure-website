Title: Guidelines for creating a Jira ticket
license: https://www.apache.org/licenses/LICENSE-2.0

## Jira tickets


<a href="https://issues.apache.org/jira" target="_blank">Jira</a> is a proprietary issue tracking product developed by Atlassian that allows bug tracking and agile project management. Atlassian provides Jira services to Apache projects. The tool's name is a short form of the name of the Japanese movie monster, <a href="https://en.wikipedia.org/wiki/Jira_(software)" target="_blank">Godzilla</a>, and was an early developer nickname for the application.

Anyone can review existing Jira tickets, or issues. You must register and log in if you want to create, comment or vote on, upload attachments to, or watch issues. Only <a href="https://www.apache.org/foundation/how-it-works.html#committers" target="_blank">committers</a> can edit, prioritize, schedule and resolve issues.

ASF and many of its projects use Jira to keep track of work to be done. The largest group of tickets assigned to Infra are requests for Infra to perform a task of one sort or another. The next largest category is reports of possible bugs in the Infrastructure system.


<ul>
<li><a href="#who">Who can create a ticket</a></li>
<li><a href="#account">Creating an account for a non-ASF reporter</a>
<li><a href="#before">Before you create a ticket</a></li>
<li><a href="#writing">Writing a good Jira ticket</a></li>
<li><a href="#followup">Jira tickets for Infra</a></li>

</ul>

<h3 id="who">Who can create a ticket<a class="headerlink" href="#who" title="Permanent link">&para;</a></h3>

Any person with an ASF Jira account can open a ticket for any ASF project.

In November, 2022, due to an influx of false Jira accounts creating a flood of spam tickets, Infra ended public signups to ASF Jira accounts. This <a href="https://infra.apache.org/blog/jira-public-signup-disabled.html" target="_blank">blog post</a> discusses the decision.

If you need to open a Jira ticket for a particular project and do not have an ASF Jira account, you can use the <a href="https://selfserve.apache.org/jira-account.html" target="_blank">Jira account request</a> feature in our <a href="https://selfserve.apache.org" target="_blank">self-serve portal</a> to request an account. The project which you specify in your request will review your information and either approve or reject the application. You will get a notification of their decision.

If your application is approved, you receive an email with a link to where you can request a password for your Jira account. Once you have logged in, you can create Jira tickets for ASF projects, for Infra, or for the ASF in general.

<h3 id="account">Approving an account request for a non-ASF reporter<a class="headerlink" href="#account" title="Permanent link">&para;</a></h3>

When someone who is not part of the ASF community requests a Jira account so they can submit tickets related to a project's product, the PMC of the project they specify in their application receives a notice that the application is pending. Please review the [policy on approving Jira accounts](jira-approve-account.html) for people who are not members of the ASF community before reviewing the application.

Review the applicant's information and either approve or deny the request. If you deny the request, you have the option of adding an explanation for the denial. The system sends an email with your decision (including any explanation you provide for a denial) to the applicant.

<h3 id="before">Before you create a ticket<a class="headerlink" href="#before" title="Permanent link">&para;</a></h3>

**Note**: Do not use Jira to submit a ticket about a security vulnerability. Review <a href="https://www.apache.org/security/#reporting-a-vulnerability" target="_blank">the guidelines on reporting vulnerabilities</a> to learn how to report such issues.

  1. Browse the existing Jira tickets to see if others have already reported the bug you noticed or have requested the task or additional feature that you were going to ask for. If you find a ticket that covers what you wanted to report, you can add a comment and maybe some more relevant information to the existing ticket.
  2. Decide whether an Apache Jira ticket is the proper venue for your concern. For example, the Infrastructure team installs and operates multiple third party services on behalf of the ASF and its projects. Examples include Jira itself, GitHub, TravisCI, JFrog, BitWarden, PonEE, Okta, Nexus, Confluence, and Statuspage. If you have a problem with the core functions of a third party service, it will be more efficient to file a bug report with that service, rather than with Infra or any ASF project. Infra will **close as invalid** any bug report or enhancement request about a third party service that does not relate to the ASF's interaction with or configuration of that service.
  3. If the ticket is not to report an issue, but to request that **Infra** make a configuration change, add a service, create a virtual machine, or perform some other work for your project, _unless you are a committer or a PMC member of the project_, include in the ticket a reference to the email thread in which the PMC agreed to that request. Infra will **reject** Jira tickets submitted on behalf of a PMC by someone who is not a committer for that project and cannot in some other way establish a) their connection to the project and b) PMC approval for the request.
  4. **Note**: If the ticket is for Infra, and is for a major request, such as to set up a virtual machine for the project, the ticket **should** demonstrate PMC approval of the request, no matter what status the ticket-creator has.

<h3 id="writing">Writing a good Jira ticket<a class="headerlink" href="#writing" title="Permanent link">&para;</a></h3>
If there is nothing in Jira already that covers what's on your mind, and the topic seems related to Apache services or an Apache project rather than a third party, click "Create" to display a form where you can describe your issue or request. Providing as much relevant information as you can helps Infra respond quickly and appropriately.

The form is pretty clear, so the focus here is on a couple of key fields.

#### Project
This is the group you want to take a look at the ticket. Select "Infra" for an infrastructure issue or request. Select a specific project if the issue is something like a problem in the project's documentation or website.

#### Issue type
There's a good list of issue types to choose from. Make sure you select the most appropriate one.

#### Project (again)
For an Infra ticket, if you want Infra to look at a problem with the Apache Widget project, in this field select `Widget`. Most of the time, for an Infra ticket, select `Infra`.

#### Summary
This is your quick statement of your problem or request. "Things are broken!" would not be a useful statement. Something like "Self-serve site hangs, then crashes" is more likely to get the right person's attention and a prompt resolution to the problem.

#### Priority
Make your best guess at how urgent this thing is. Infra, and many projects, triage Jira tickets by their priorities, and may adjust the priority of a ticket if its current setting seems too high or too low.

The options are

  - **Blocker**: a time-sensitive issue that is hindering a basic function of a project. (_example: "We just announced a new release, but SVN is not allowing us to upload or move the artifacts."_)
  - **Critical**: a time-sensitive issue that is disrupting the project, but does not hinder basic functions. (_"Our website has been defaced."_)
  - **Major**: this issue needs attention soon, but is not hindering basic functions. Most requests for new resources fall into this category. (_"Add a Git repository."_)
  - **Minor**: this issue needs attention, but is not time-sensitive and does not hinder basic functions. (_"Fix a JavaScript error on the website."_)
  - **Trivial**: this issue is minimal and has no time constraints. ( _"The copyright year on Infra web page bla.html is incorrect."_)

#### Component/s
Select one or more components that this issue or request relates to. If you cannot figure out what to pick, select `Other/misc`.

#### Fix Version/s
This an optional field, useful if your issue concerns a specific Infra tool or service and you know the version you are using.

#### Assignee
If you specify someone here, that person receives an alert about the issue. You can accept the default (Automatic) to put the issue in the queue for the Infra or project team's attention.

#### Environment
This is an optional field where you can describe your operating system, software platform and/or hardware specifications if they are relevant to the bug, task, or feature request.

#### Description
Provide the juicy details here. For example, for an infrastructure bug report, Infra needs to know how to reproduce the thing you ran into. Describe what you were doing ("I was logged in to bla.html using Firefox"), what you wanted to do ("I wanted to do xxx"), what you expected to happen, and what you actually experienced.

For a feature request, it helps if you can not only describe the feature, but explain why the ASF or the specific project needs it.

#### Other fields
There are many optional fields that you can probably skip.

When you have completed entering the useful information, click **Create** to create the ticket.

<h3 id="followup">Jira tickets for Infra<a class="headerlink" href="#followup" title="Permanent link">&para;</a></h3>

You cannot read or comment on existing Jira tickets for Infra without having logged in with your Apache credentials. See the "Who can create a ticket" section, at the top of this page, for details.

The largest group of tickets assigned to Infra are requests for Infra to perform a task of one sort or another. The next largest category is reports of possible bugs in the Infrastructure system.

Infra may respond in a number of ways, including:

  - Closing the ticket as **invalid**. Review "Before you create a ticket", above, for reasons that may generate this response.
  - Asking for **further details**. You may then see that the status of the ticket has changed to _waiting for user_. Provide the details as best you can in a comment, and change the status to _waiting for Infra_.
  - Reporting the issue **resolved**. Please verify the fix or that the requested service is now available. If all is well, and Infra has not changed the status to _closed_ or one of its variants, feel free to do so yourself.

**Note**: A ticket in the status of _Waiting for User_, will not generally be worked on until the ticket status is set to _Waiting for Infra_. Be sure to set the ticket to _Waiting for Infra_ if the ticket needs follow-up!

Here are details about Infra's typical <a href="https://infra.apache.org/responsetime.html" target="_blank">response times</a> to Jira tickets and other requests, which largely depend on the severity of the issue. 
