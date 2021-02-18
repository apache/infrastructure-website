Title: Details on contacting Infra

Here is detailed information on how to contact Infra in a wide range of situations.

<h2 id="how">How should I make contact?<a class="headerlink" href="#how" title="Permanent link">&para;</a></h2>

That depends on your role and what you want to do. If this chart doesn't help, Infra maintains a publicly accessible channel (`#asfinfra`) within the <a href="https://the-asf.slack.com/#asfinfra" target="_blank">ASF presence on Slack</a>, and you can ask there whether to create a bug report or do something else.
<table width="100%">
<thead>
<tr>
<th>If you are...</th>
<th>and want to...</th>
<th>then contact...</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>anyone</td>
<td>report a <strong>security vulnerability</strong> in a service that runs on apache.org</td>
<td>`root@apache.org`</td>
<td>You may optionally encrypt the email to <a href="https://home.apache.org/keys/group/infrastructure-root.asc" target="_blank">this set of keys</a>.</td>
</tr>
<tr>
<td>anyone</td>
<td>report a <strong>security vulnerability</strong> in an Apache project</td>
<td><a href="https://www.apache.org/security/" target="_blank">Apache Security Team</a></td>
<td>The Security Team is not part of Infra.</td>
</tr>
<tr>
<td><!-- TODO: status.a.o is sorted by physical name; would be useful to explain that asomewhere, but not here in the bulleted list --> anyone</td>
<td>report that a <strong>service is down</strong> and <a href="https://status.apache.org/" target="_blank">status.apache.org</a> doesn't show it</td>
<td><a href="https://the-asf.slack.com/#asfinfra" target="_blank">Slack</a> channel</td>
<td>Slack preferred, email to `users@infra.apache.org` is an acceptable alternative. The <a href="https://twitter.com/infrabot/" target="_blank">infrabot Twitter feed</a> may contain information about current outages and maintenances.</td>
</tr>
<tr>
<td>a <strong>newly-invited committer</strong></td>
<td>ask a question about your committership</td>
<td>`private@$project`</td>
<td></td>
</tr>
<tr>
<td>a committer</td>
<td>regain <strong>access to your account</strong>; <a href="https://id.apache.org/reset/enter" target="_blank">resetting your password</a> didn't work</td>
<td>See <a href="#regain-account">Regaining account access</a></td>
<td>If commits fail, double-check that you are using `https://` (not `http://`).</td>
</tr>
<tr>
<td>a <strong>supplier</strong> (you donate or sell hardware or services to Apache)</td>
<td>anything</td>
<td>`private@infra.apache.org`</td>
<td>Passwords should be <a href="https://home.apache.org/keys/group/infrastructure-root.asc" target="_blank">encrypted</a> or sent by other means</td>
</tr>
<tr>
<td><strong>submitted an ICLA</strong> in the past</td>
<td>change your contact details of record</td>
<td>`secretary@apache.org`</td>
<td>Fax or snail mail are possible too; see <a href="https://www.apache.org/foundation/contact" target="_blank">apache.org/foundation/contact</a></td>
</tr>
<tr>
<td>prospective official download mirror</td>
<td>request being listed as an official download mirror</td>
<td>see <a href="how-to-mirror.html" target="_blank">the "new mirror" documentation</a></td>
<td>Please email <code>mirrors@apache.org</code> if you have any questions.</td>
</tr>
<tr>
<td>existing official download mirror</td>
<td>ask a question concerning your mirror</td>
<td>`mirrors@apache.org`</td>
<td>Questions not suitable for public discussion may be sent to `apmirror@apache.org` (an alias with limited distribution).</td>
</tr>
<tr>
<td>anyone</td>
<td>report a problem with a download mirror (other than it being out of date</td>
<td>the Apache project whose product you were trying to download</td>
<td>The project will escalate to infra if necessary.</td>
</tr>
<tr>
<td>anyone</td>
<td><strong>unsubscribe</strong> from a mailing list</td>
<td>See <a href="https://www.apache.org/foundation/mailinglists#subscribe" target="_blank">unsubscription instructions</a></td>
<td></td>
</tr>
<tr>
<td>a committer</td>
<td>change <strong>your account details</strong></td>
<td><a href="https://id.apache.org/" target="_blank">Self-serve</a></td>
<td>Details include forwarding email address, password, and SSH or PGP public keys of record.</td>
</tr>
<tr>
<td>a PMC</td>
<td>request <strong>account creation</strong> for a newly-elected committer</td>
<td><a href="https://whimsy.apache.org/officers/acreq" target="_blank">Whimsy</a></td>
<td>See <a href="https://www.apache.org/dev/pmc#newcommitter" target="_blank">docs</a> for details</td>
</tr>
<tr>
<td>a newly-accepted <strong>podling</strong></td>
<td>create podling infrastructure (site, lists, etc.)</td>
<td><a href="#requesting-podling">Requesting podling</a></td>
<td></td>
</tr>
<tr>
<td>a podling that has just <strong>graduated</strong></td>
<td>migrate resources from Incubator locations to TLP locations</td>
<td><a href="#requesting-graduation">requesting graduation</a></td>
<td></td>
</tr>
<tr>
<td>an existing PMC or podling</td>
<td>request <strong>mailing list</strong> creation</td>
<td><a href="https://selfserve.apache.org/mail.html" target="_blank">Self-serve</a></td>
<td>Only Members and Officers (this includes all PMC chairs) can submit the form.</td>
</tr>
<tr>
<td>a committer or PMC</td>
<td>add/remove mailing list <strong>moderators</strong></td>
<td><a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">create a JIRA ticket</a></td>
<td>Feel free to follow up via the Slack channel or file a Jira ticket if no reply after 48 hours</td>
</tr>
<tr>
<td>a committer or PMC</td>
<td>change <strong>Jenkins</strong> build settings</td>
<td>builds@apache.org</td>
<td>Project members having <a href="https://cwiki.apache.org/confluence/display/INFRA/Jenkins#Jenkins-HowdoIgetanaccount" target="_blank"><code>hudson-jobadmin</code> karma</a> can perform some tasks; ask your dev@ list</td>
</tr>
<tr>
<td>a PMC</td>
<td>request Infra to <strong>do</strong> something</td>
<td><a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">create a Jira ticket</a></td>
<td>See <a href="#requesting-action">"On Requests"</a> and <a href="#what-we-need-to-know">"Providing needed information"</a>.</td>
</tr>
<tr>
<td>an <strong>Officer</strong> of the ASF</td>
<td>ask an organizational (as opposed to technical) question</td>
<td>VP Infrastructure, or private@infra.apache.org</td>
<td>The target audience for this item is the Apache Board of Directors, the VP of Fundraising, etc.</td>
</tr>
<tr>
<td>posted to an Apache mailing list</td>
<td>edit the <strong>mail archives</strong></td>
<td><a href="https://www.apache.org/foundation/public-archives" target="_blank">Public Forum Archive Policy</a></td>
<td>Virtually all requests are denied.</td>
</tr>
<tr>
<td>anyone</td>
<td><strong>discuss</strong> something publicly with Infra</td>
<td>users@infra.apache.org</td>
<td>Archives: <a href="https://lists.apache.org/list.html?users@infra.apache.org" target="_blank">discussion archives</a>  - for <a href="https://www.apache.org/foundation/how-it-works.html#asf-members" target="_blank">ASF Members</a> only!</td>
</tr>
<tr>
<td>anyone</td>
<td>ask Infra a <strong>question</strong></td>
<td>users@infra.apache.org</td>
<td>Consider the users@infra mailing list as a semi-public list as many <a href="https://www.apache.org/foundation/how-it-works.html#committers" target="_blank">Apache committers</a> subscribe to it.</td>
</tr>
<tr>
<td>anyone</td>
<td>get your IP unblocked</td>
<td>users@infra.apache.org</td>
<td>Consider the users@infra mailing list as a semi-public list as many <a href="https://www.apache.org/foundation/how-it-works.html#committers" target="_blank">Apache committers</a> subscribe to it.</td>
</tr>
</tbody>
</table>

<h2 id="what-we-need-to-know">Providing needed information<a class="headerlink" href="#what-we-need-to-know" title="Permanent link">&para;</a></h2>

<table class="table">
<thead>
<tr>
<th>If you ask us to...</th>
<th>then we need to know...</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Promote a <strong>podling to TLP</strong></td>
<td>See <a href="#requesting-graduation">requesting podling graduation</a></td>
<td></td>
</tr>
<tr>
<td>Create a <strong>podling</strong></td>
<td>See <a href="#requesting-podling">requesting a podling</a></td>
<td></td>
</tr>
<tr>
<td>Load <strong>Subversion history</strong></td>
<td>URL and checksum (or PGP signature) of a dumpfile; proof of <a href="https://www.apache.org/legal/resolved#category-a" target="_blank">IP rights</a></td>
<td>Produce with <code>svnadmin dump --incremental --deltas</code> or <code>svnrdump</code>. The paths within the dumpfile should be relative to the project root (e.g., to <code>/repos/asf/incubator/MyPodling</code>).</td>
</tr>
<tr>
<td>Load <strong>Git history</strong></td>
<td>URL and of a repository or an export stream; proof of <a href="https://www.apache.org/legal/resolved#category-a" target="_blank">IP rights</a></td>
<td>If linking to a file, provide PGP signature or checksum. If to a remote repository, you must review and sign off on the import ("Yes, that is the repository and history we asked to import and have IP rights for") before it will be writable.</td>
</tr>
<tr>
<td>Create an <strong>svnpubsub-based site</strong></td>
<td>SVN URL of the compiled site (directory containing HTML files)</td>
<td><a href="https://infra.apache.org/project-site.html" target="_blank">SvnPubSub</a> does not support Git. Use the <a href="http://home.apache.org/committers-by-project.html#infrastructure-root" target="_blank">webreq app</a></td>
</tr>
<tr>
<td>Create an <strong>svnpubsub-based Dist area</strong></td>
<td>Create or ask Infra to create a dist release directory. Specify release area only or release and dev areas. If you omit a list of emails for commit notices to go to, the default is the  project commits list.</td>
<td>Any existing release dir will be blown away (archive releases remain). Infra will ask for a release or KEYS/NOTICE file once the directory is in place.</td>
</tr>
<tr>
<td>Create a <strong>project blog</strong></td>
<td>project name, brief one-line description of the project, and Apache usernames (and fullnames) of 1+ editors</td>
<td></td>
</tr>
<tr>
<td>Create a <strong>blog account</strong> for an editor</td>
<td>The Apache username (and fullnames) of the editor</td>
<td>Non-PMC members need to demonstrate PMC consensus (link to a lazy consensus thread suffices).</td>
</tr>
<tr>
<td>Create a <strong>moin wiki</strong></td>
<td>Moin is deprecated and no more Moin wikis are being created.</td>
<td>Plan on using Confluence instead. See the next entry.</td>
</tr>
<tr>
<td>Create a <strong>Confluence wiki</strong></td>
<td>wiki name, destination for commit mails, and Confluence usernames of two+ community members - volunteer space admins</td>
<td>Go to <a href="https://selfserve.apache.org/confluence.html" target="_blank">selfserve</a> and follow the prompts.</td>
</tr>
<tr>
<td>Set up your project on <a href="https://reviews.apache.org/" target="_blank"><strong>Review Board</strong></a></td>
<td>Project name, which svn/git branches to support</td>
<td>Review Board is a web-based collaborative code review tool, available as free software under the MIT License.</td>
</tr>
<tr>
<td>Create a <strong>Jira project</strong></td>
<td>Key name (e.g., <code>INFRA</code>), Jira user names of 1-2 project members - volunteer project admins, mailing list address to which Jira notifications should go</td>
<td>Go to <a href="https://selfserve.apache.org/jira.html" target="_blank">selfserve</a> and follow the prompts.</td>
</tr>
<tr>
<td>Migrate your project's <strong>SVN to Git</strong></td>
<td>n/a</td>
<td>Please use <a href="https://selfserve.apache.org"  target="_blank">self-serve</a> to create your intended Git repo(s). Run svn2git locally using this <a href="https://git-wip-us.apache.org/authors.txt"  target="_blank">authors file</a> and push once the conversion result is confirmed. File an Infra ticket to mark your SVN repository readonly. Optionally, file a ticket to temporarily disable commit emails for when you push your converted clone.</td>
</tr>
</tbody>
</table>
<p>Don't see here what you're looking for? See above for <a href="#requesting-where">other cases</a>.</p>

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
  - >Whether there is any other way in which we (infra) might satisfy ourselves that you are the legitimate owner of that account.

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
