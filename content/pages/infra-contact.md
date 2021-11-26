Title: Details on contacting Infra

Here is detailed information on how to contact Infra in a wide range of situations.

<h2 id="how">How should I make contact?<a class="headerlink" href="#how" title="Permanent link">&para;</a></h2>

That depends on your role and what you want to do. If this chart doesn't help, Infra maintains a publicly accessible channel (`#asfinfra`) within the <a href="https://the-asf.slack.com/#asfinfra" target="_blank">ASF presence on Slack</a>, and you can ask there whether to create a bug report or do something else.

| If you... | and want to... | then contact... | Notes |
|-----|-----|-----|-----|
| are anyone | report a **security vulnerability** in a service that runs on apache.org | `root@apache.org` | You may optionally encrypt the email to this <a href="https://home.apache.org/keys/group/infrastructure-root.asc" target="_blank">set of keys</a>. |
| are anyone | report a **security vulnerability** in an Apache project | the <a href="https://www.apache.org/security/" target="_blank">Apache Security Team</a> | The Security Team is not part of Infra. |
| are anyone | 	report that a **service is down** _if_ <a href="https://status.apache.org/" target="_blank">status.apache.org</a> doesn't show it | Infra's <a href="https://the-asf.slack.com/#asfinfra" target="_blank">Slack channel</a> | Email to `users@infra.apache.org` is an acceptable alternative. The <a href="https://twitter.com/infrabot/" target="_blank">infrabot</a> Twitter feed may contain information about current outages and maintenances. |
| are a **newly-invited** commmitter | ask a question about your committership | `private@$project` |  |
| are a **committer** |	**regain access** to your account | See <a href="https://infra.apache.org/infra-contact.html#regain-account" target="_blank">Regaining account access</a> | If commits fail, double-check that you are using `https://` (not `http://`). |
| are a **supplier** (you donate or sell hardware or services to Apache) | anything | `private@infra.apache.org` | <a href="https://home.apache.org/keys/group/infrastructure-root.asc" target="_blank">Encrypt</a> passwords or send them by other means. |
| submitted an **ICLA** in the past | change your **contact details** of record | `secretary@apache.org` | Snail mail is possible too; see <a href="https://www.apache.org/foundation/contact" target="_blank">apache.org/foundation/contact</a>. |
| are anyone | **unsubscribe** from a mailing list | See <a href="https://www.apache.org/foundation/mailinglists#subscribe" target="_blank">unsubscription instructions</a>. |  |
| are a **committer** | change your **account details** | <a href="https://id.apache.org/" target="_blank">Self-serve</a> |  |
| are a **PMC** | request **account creation** for a newly-elected committer | <a href="https://whimsy.apache.org/officers/acreq" target="_blank">Whimsy</a> | Instructions are <a href="https://www.apache.org/dev/pmc#newcommitter" target="_blank">here</a> |
| are a newly-accepted **podling** | create podling infrastructure (site, lists, etc.) | <a href="https://infra.apache.org/infra-contact.html#requesting-podling" target="_blank">Requesting podling</a> |  |
| are a podling that has just **graduated** | migrate resources from Incubator locations to TLP locations | <a href="https://infra.apache.org/infra-contact.html#requesting-graduation" target="_blank">Requesting graduation</a> |  |
| are a PMC or podling | request **mailing list creation** | <a href="https://selfserve.apache.org/mail.html" target="_blank">Self-serve</a> | Only Members and Officers (including PMC chairs) can submit the form. |
| are a committer or PMC | change **Jenkins** build settings | `builds@apache.org` | Project members having hudson-jobadmin **karma** can perform some tasks; ask your `dev@` list. |
| are a PMC | ask Infra to do something | <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">Create a Jira ticekt</a> | See <a href="https://infra.apache.org/infra-contact.html#requesting-action" target="_blank">On Requests</a> and <a href="https://infra.apache.org/infra-contact.html#what-we-need-to-know" target="_blank">What we need to know</a>. |
| are an **Officer** of the ASF | ask an organizational (as opposed to technical) question | VP Infrastructure, or `private@infra.apache.org` | The target audience for this item is the Apache Board of Directors, the VP of Fundraising, etc. |
| posted to an Apache mailing list | **edit** the mail archives | <a href="https://www.apache.org/foundation/public-archives" target="_blank">Public forum archive policy</a> | We deny almost all requests. |
| are anyone | discuss something publicly with Infra, or ask Infra a question | `users@infra.apache.org` | Consider this as a semi-public list, as many people subscribe to it. The discussion archives are available for ASF Members only. |
| are anyone | get your **IP** unblocked |  `users@infra.apache.org` |  |

<h2 id="what-we-need-to-know">What we need to know<a class="headerlink" href="#what-we-need-to-know" title="Permanent link">&para;</a></h2>

| If you ask us to... | we need to know... | Notes |
|-----|-----|-----|
| **promote** a podling to TLP | see <a href="https://infra.apache.org/infra-contact.html#requesting-graduation" target="_blank">Requesting podling graduation</a> |  |
| **create** a podling | see <a href="https://infra.apache.org/infra-contact.html#requesting-podling" target="_blank">Requesting a podling</a> |  |
| load **Subversion history** | URL and checksum (or PGP signature) of a dumpfile; proof of <a href="https://www.apache.org/legal/resolved#category-a" target="_blank">IP rights</a> | Produce with `svnadmin dump --incremental --deltas` or `svnrdump`. The paths within the dumpfile should be relative to the project root (e.g., to `/repos/asf/incubator/MyPodling`). |
| load **Git history** | URL of a repository or an export stream; proof of <a href="https://www.apache.org/legal/resolved#category-a" target="_blank">IP rights</a> | If linking to a file, provide PGP signature or checksum. If to a remote repository, you must review and sign off on the import ("Yes, that is the repository and history we asked to import and have IP rights for") before it will be writable. |
| create an **svnpubsub-based site** | SVN URL of the compiled site (directory containing HTML files) | For Git-based web sites, refer to <a href="https://cwiki.apache.org/confluence/display/INFRA/Git+-+.asf.yaml+features" target="_blank">Git-.asf.yaml features</a> for instructions on publishing. |
| create a **project blog** | project name, brief one-line description of the project, and Apache usernames (and fullnames) of at least two editors |  |
| create a **blog account** for an editor | The Apache username (and fullname) of the editor | Non-PMC members need to demonstrate PMC consensus (a link to a lazy consensus thread suffices). |
| create a project **Confluence wiki** | wiki name, destination for commit mails, and Confluence usernames of at least two community members who will be space admins | Go to <a href="https://selfserve.apache.org/confluence.html" target="_blank">Self-serve</a> and follow the prompts. |
| set up your project on **Review Board** | project name, which svn/git branches to support | <a href="https://reviews.apache.org/" target="_blank">Review Board</a> is a web-based collaborative code review tool, available as free software under the MIT License. |
| create a **Jira project** | Key name (e.g., INFRA), Jira user names of 1-2 project members who will be project admins, mailing list address to which Jira notifications should go | Go to <a href="https://selfserve.apache.org/confluence.html" target="_blank">Self-serve</a> and follow the prompts. |
| migrate your project's SVN repository to Git |  | Use <a href="https://selfserve.apache.org/confluence.html" target="_blank">Self-serve</a> to create your intended Git repo(s). Run `svn2git` locally using this <a href="https://git-wip-us.apache.org/authors.txt" target="_blank">authors file and push once the conversion result is confirmed. Submit a Jira ticket for Infra to mark your SVN repository 'readonly'. Optionally, file a ticket to temporarily disable commit emails for when you push your converted clone. |

Don't see here what you're looking for? See above for <a href="#requesting-where">other cases</a>.

<h2 id="requesting-podling">Requesting podling creation<a class="headerlink" href="#requesting-podling" title="Permanent link">&para;</a></h2>

The podling creation process is as follows:

1. The IPMC vote passes.
1. The podling is added to the IPMC's <code>podlings.xml</code> summary file with <code>status=current</code>.
(See <a href="https://incubator.apache.org/guides/mentor.html#Overview" target="_blank">notes</a> about that, and other initial tasks.)
1. Create a <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">Jira ticket</a> asking Infra to create a DNS for your new podling (include the podling's name).
1. After the DNS is created, an ASF Member or PMC chair files <a href="https://selfserve.apache.org/mail.html" target="_blank">mailing list creation requests</a>.
1. Infra creates the lists, which also notifies the IPMC of the mailing list creation.
1. An Incubator PMC member who is also an ASF member or a PMC chair edits the <a href="https://github.com/apache/infrastructure-puppet/blob/deployment/modules/subversion_server/files/authorization/asf-authorization-template" target="_blank">asf-authorization-template</a> and adds an <code>[/incubator/podling]</code> section. If the section refers to an <code>@podling</code> group, add a definition of that group as a comma-separated list of availids (usernames), to the <code>[groups]</code> section.  Alternatively, just set <code>@incubator = rw</code> as the section's body.
1. If the podling wants to use SVN, an Incubator PMC member runs <code>svn mkdir ^/incubator/podling</code>. The commit
mail goes to the mailing list created earlier.
1. If the podling wants to use GIT, one of the mentors submits a request via <a href="https://selfserve.apache.org/" target="_blank">Self-Serve</a>.
1. The podling community sets up a <a href="https://infra.apache.org/project-site#intro" target="_blank">project site</a>.
1. An ASF Member or PMC chair files a <a href="https://home.apache.org/committers-by-project.html#infrastructure-root" target="_blank">website creation request</a>.

If the project needs additional services (issue tracker, Wiki, blog, etc.), file a ticket via <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">Jira</a> using appropriate categories and providing as much information as possible. To save everyone's time, consult <a href="#what-we-need-to-know">"Providing needed information"</a>
before filing each ticket.

<h2 id="requesting-graduation">Requesting podling graduation to top level project (TLP)<a class="headerlink" href="#requesting-graduation" title="Permanent link">&para;</a></h2>

Once your podling has <a href="https://incubator.apache.org/guides/graduation.html#project-first-steps" target="_blank">graduated</a> to a TLP, create the following Jira tickets:

1. A "Graduate Foo to TLP" parent ticket.
1. A "Foo TLP: common tasks" ticket as a sub-task of (1). This ticket handles DNS entry, Unix/LDAP group creation, PMC Chair karma,
mailing list migration, native Git repository migrations (but not git-svn mirrors), Subversion public tree migration, buildbot config
changes, and website migration. <strong>There is no need to file individual tickets for these tasks.</strong> In the ticket, specify <strong>the LDAP name of the TLP</strong> --- that is, the <code>foo</code> in <code>dev@foo.apache.org</code>.
1. For each additional service that needs configuration changes as the result of the migration, create another sub-task. If you have N services, create N sub-tasks. "Services" here includes everything indicated <a href="#requesting-menu">below</a>, such as Subversion private tree, git-svn mirrors, issue trackers, wikis, and <a href="https://ci.apache.org/" target="_blank">continuous integration</a> (Jenkins, Buildbot, Continuum etc.). See <a href="https://issues.apache.org/jira/browse/INFRA-5688" target="_blank">Flex's graduation tickets</a> for a good example.

Note that the new PMC chair is still responsible for using Whimsy as appropriate. The group membership is initialized on a best-guess basis, but the chair must check that it's accurate and add and remove people as needed. Infra intializes the Committee data directly from the information in the Board resolution.

<h2 id="regain-account">Regaining access to a committer account<a class="headerlink" href="#regain-account" title="Permanent link">&para;</a></h2>

If you forgot your password, try...

  1. to reset it at <a href="https://id.apache.org/reset/enter" target="_blank">id.apache.org/reset/enter</a>. That will email
your @apache.org address (which forwards to your non-apache email account) a short-lived password reset link. The link may be encrypted to <a href="https://home.apache.org/keys/committer/" target="_blank">your PGP key</a>.
  1. decrypting the e-mail - one way to do this is to sve the e-mail contents as a text file, e.g. `password.txt`. Open a shell command window, and run the following command:

```
gpg -d password.txt</code>
```

This should decrypt the file and display the output in the window.

  3. If you have lost access to your registered email address, file an additional ICLA with Secretary. Follow the directions for <a href="https://www.apache.org/licenses/#submitting" target="_blank">submitting an ICLA</a>. Include your current Apache ID and mention in your cover email that you are requesting a change to your email address.

  4. If that didn't work, email root@. In your email, mention the following information:
 
  - Your username.
  - The fact that you have tried a self-service password reset, and why it didn't work. (Was the mail received? Did you decrypt it successfully?)
  - Why you need to regain access to your Apache account --- e.g., if it is   to work on a <a href="https://www.apache.org/foundation/" target="_blank">foundation project</a>, name that project; or if you are a <a href="https://www.apache.org/foundation/members" target="_blank">foundation member</a>, state that.
  - Whether you have SSH access to <code>minotaur.apache.org</code> or to a PMC jail/zone/VM via public-key authentication<
  - Whether you ever set up OPIE on any `*.apache.org` box. (This is only applicable to people who had root permissions on PMC VMs.)
  - Whether you have access to the private part of a PGP key associated with your Apache account.
  - Whether the contact information on your ICLA is valid.
  - For (<a href="https://www.apache.org/foundation/members" target="_blank">ASF Members</a> only, whether the contact information in your `members.txt` entry is valid.
  - Whether you are able to send a new ICLA, with the same signature as your original one, which specifies new contact information.
  - Whether there is any other way in which we (infra) might satisfy ourselves that you are the legitimate owner of that account.

**Note**: please do not ask other ASF committers or Members to email root@ to vouch for you.

<h2 id="requesting-action">Other Requests<a class="headerlink" href="#requesting-action" title="Permanent link">&para;</a></h2>

<h4 id="requesting-menu">What can I ask for?<a class="headerlink" href="#requestin-menu" title="Permanent link">&para;</a></h4>

See the list of [Services and tools](https://infra.apache.org/services-tools.html) Infra provides for projects. If you want something that isn't listed, get in touch. It might be possible to support it, especially if the feature request includes a list of [volunteers](volunteer.html) who will help maintain it hint, hint.</p>

<h4 id="requesting-where">Where should I submit my request?<a class="headerlink" href="#requesting-where" title="Permanent link">&para;</a></h4>

The short answer: If there is a <a href="https://selfserve.apache.org/" target="_blank">dedicated webapp</a>, use it. If not, file a <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">Jira ticket</a> for Infra. 

The more <a href="#how">complete answer</a> is in the table above. Please review the table before filing a ticket - often you or someone in your PMC can effect the change without involving infra at all.

<h5 id="request-checklist">Before you press `Send` on your ticket:<a class="headerlink" href="#request-checklist" title="Permanent link">&para;</a></h5>

  - **Ask** in your project</strong> whether someone has the karma to implement the  requested change. This eases the load on the infra team. The moderators and volunteer admins of the project's issue tracker and wiki can often address issues with those services.
  - **Aggregate requests**: instead of sending five emails, each asking for one more moderator to be added, send one email asking for five moderators to be added.
  - **CC your PMC** on emails. In Jira tickets, it is helpful to link to a thread that demonstrates PMC consensus. (If you request a significant or major configuration change, we will probably ask for that link if you don't provide it.)
  - If you create a Jira ticket, create it in the **right Jira component**. This helps the team spot pending tasks in their areas. If it's not obvious which component is the right one, report a bug in the documentation.
  - **Be patient**. It may take a few days for someone to respond.
  - **Research your topic**. See the <a href="https://www.apache.org/dev/" target="_blank">developer information section</a>.
  
**Thanks**. Making requests following these guidelines might require a little effort, but saves time for all involved.


<h4 id="reopen">My issue got closed with a request to reopen it<a class="headerlink" href="#reopen" title="Permanent link">&para;</a></h4>

Then reopen it. Usually we ask that you do something as you reopen it, so do that too (or say why you didn't).

Background: we tend to close issues that we cannot act on for an extended period, since we use the <code>INFRA</code> queue as a to-do list. In our workflow, this kind of close/reopen cycle is a matter of ordinary routing (much like <a href="https://subversion.apache.org/docs/community-guide/building#revert" target="_blank">reverting a commit that broke the build
system</a>).

<h4 id="ignored">My issue got ignored<a class="headerlink" href="#ignored" title="Permanent link">&para;</a></h4>

There could be a few reasons: some areas have longer turn-around times than others; sometimes we're busy on backend projects like installing new hardware and have little time for user-facing tasks; sometimes an issue blocks on prerequisite new hardware to get
shipped, installed, and configured, which takes time; sometimes we're just backlogged and are working on issues ahead of yours in the
queue; and sometimes we do tickets of a certain category in batch, and yours will be done in the next batch in a few days.

To make sure your issue doesn't get lost, feel free to add a comment to the relevant Jira issue, or email the <code>users@infra</code> list with a question. If the matter remains unresolved after that, feel free to escalate it to <a href="https://www.apache.org/foundation/" target="_blank">the VP, Infrastructure</a> or to the <code>operations@</code> privately-archived mailing list (everyone may post to it).

<h4 id="emergency">In case of emergency<a class="headerlink" href="#emergency" title="Permanent link">&para;</a></h4>

The following describes how to page root@ people when there is an absolutely urgent problem, such as a malicious cracker having an active root shell on `archive.apache.org`.  **This is only for urgent, ASF-wide problems
that must be handled at once, even if that means waking people up in the middle
of the night or having them miss their flight**

Normally, pinging <code>#asfinfra</code> or emailing <code>root@</code> or <code>private@infra</code> suffices. We discourage pinging people privately (via email, Slack, or Twitter) as then only a single person is aware of a request. 

If you have exhausted these options, the last resort is to look 
up root@ people the list of names (see <a href="https://home.apache.org/committers-by-project.html#infrastructure-root" target="_blank">here</a> or <a href="https://svn.apache.org/repos/private/committers/board/committee-info.txt" target="_blank">here</a>) and call them or SMS them.

Finally, the VP Infrastructure has the authority to contact third parties directly. The contact information is available
to him via <code>docs/vp/littleblackbook.txt</code>.

**Reminder**: this facility is for emergency use only. It wakes people up.
