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
| are a **committer** |	**regain access** to your account | See <a href="https://infra.apache.org/account-mgmt.html">ASF account management</a> | If commits fail, double-check that you are using `https://` (not `http://`). |
| are a **supplier** (you donate or sell hardware or services to Apache) | anything | `private@infra.apache.org` | <a href="https://home.apache.org/keys/group/infrastructure-root.asc" target="_blank">Encrypt</a> passwords or send them by other means. |
| submitted an **ICLA** in the past | change your **contact details** of record | `secretary@apache.org` | Snail mail is possible too; see <a href="https://www.apache.org/foundation/contact" target="_blank">apache.org/foundation/contact</a>. |
| are anyone | **unsubscribe** from a mailing list | See <a href="https://www.apache.org/foundation/mailinglists#subscribe" target="_blank">unsubscription instructions</a>. |  |
| are a **committer** | change your **account details** | <a href="https://id.apache.org/" target="_blank">Self-serve</a> |  |
| are a **PMC** | request **account creation** for a newly-elected committer | <a href="https://whimsy.apache.org/officers/acreq" target="_blank">Whimsy</a> | Instructions are <a href="https://www.apache.org/dev/pmc#newcommitter" target="_blank">here</a> |
| are a newly-accepted **podling** | create podling infrastructure (site, lists, etc.) |  | See [Infra and the Incubator](infra-incubator.html) |
| are a podling that has just **graduated** | migrate resources from Incubator locations to TLP locations |  | See [Infra and the Incubator](infra-incubator.html) |
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
| **promote** a podling to TLP |  | See [Infra and the Incubator](infra-incubator.html) |
| **create** a podling |  | See [Infra and the Incubator](infra-incubator.html) |
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

<h2 id="requesting-action">Other Requests<a class="headerlink" href="#requesting-action" title="Permanent link">&para;</a></h2>

<h4 id="requesting-menu">What can I ask for?<a class="headerlink" href="#requestin-menu" title="Permanent link">&para;</a></h4>

See the list of [Services and tools](https://infra.apache.org/services-tools.html) Infra provides for projects. If you want something that isn't listed, get in touch. It might be possible to support it, especially if the feature request includes a list of [volunteers](volunteer.html) who will help maintain it hint, hint.</p>

<h4 id="requesting-where">Where should I submit my request?<a class="headerlink" href="#requesting-where" title="Permanent link">&para;</a></h4>

The short answer: If there is a <a href="https://selfserve.apache.org/" target="_blank">dedicated webapp</a>, use it. If not, file a <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">Jira ticket</a> for Infra. 

The more <a href="#how">complete answer</a> is in the table above. Please review the table before filing a ticket - often you or someone in your PMC can effect the change without involving infra at all.

<h5 id="request-checklist">Before you press `Send` on your ticket:<a class="headerlink" href="#request-checklist" title="Permanent link">&para;</a></h5>

  - **Ask** in your project</strong> whether someone has the karma to implement the  requested change. This eases the load on the infra team. The moderators and volunteer admins of the project's issue tracker and wiki can often address issues with those services.
  - **Aggregate requests**: instead of sending five emails, each asking for one more moderator to be added, send one email asking for five moderators to be added.
  - **CC your PMC** on emails. When creating Jira tickets, some cases **SHOULD** or even **MUST** demonstrate PMC consensus. In such cases, not succeeding to demonstrate such PMC consensus, Jira tickets will be **closed as invalid** or even **rejected**. For more details, please refer to our [Jira Guidelines](jira-guidelines.html).
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
