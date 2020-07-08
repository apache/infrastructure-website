Title: Committers' FAQs

A committer is an individual who has write access to the codebase of an Apache project. 

The main information resource for you in this role, apart from the wisdom of your project colleagues, is the [New Committers Guide](new-committers-guide.html).

If you are not an Apache committer, but wish to become one, the instructions on [how to contribute](contributors.html) to Apache projects will be more useful to you.</p>

<h3 id="frequently-asked-questions">Frequently asked questions<a class="headerlink" href="#frequently-asked-questions" title="Permanent link">&para;</a></h3>
<ul>
<li><a href="#general">General</a></li>
<li><a href="#technical">Technical</a></li>
<li><a href="#svn">Version control</a></li>
<li><a href="#mail">Mail</a></li>
<li><a href="#mailmod">Mailing list moderation</a></li>
<li><a href="#legal">Legal and organizational</a></li>
</ul>

<h3 id="general">General<a class="headerlink" href="#general" title="Permanent link">&para;</a></h3>

<h4 id="apachecon">What is ApacheCon?<a class="headerlink" href="#apachecon" title="Permanent link">&para;</a></h4>

The Apache Software Foundation periodically organizes <a href="https://www.apachecon.com">conferences</a> focusing on software developed at Apache and on the way that Apache develops its software. Learn about what's happening at Apache, hack code and meet the faces associated with the names!

<h4 id="hackathon">What is a Hackathon?<a class="headerlink" href="#hackathon" title="Permanent link">&para;</a></h4>

A face-to-face or shared online gathering for hacking code together. Hackathons are generally held at ApacheCons, as well as at other times.

<h4 id="infrathon">What is an Infrathon?<a class="headerlink" href="#infrathon" title="Permanent link">&para;</a></h4>

A face-to-face gathering for work on Apache infrastructure by our amazing infra contractors and volunteers.

<h4 id="volunteer">How do I manage my volunteer energy?<a class="headerlink" href="#volunteer" title="Permanent link">&para;</a></h4>

Heed the warnings in these two email threads about what it means to be a committed person at the ASF and how to deal with the pressures that arise from such dedication:

  - <a href="https://mail-archives.apache.org/mod_mbox/www-community/200311.mbox/%3c3FC1C5BD.3060406@apache.org%3e" target="_blank">What is a member?</a>
  - <a href="https://mail-archives.apache.org/mod_mbox/www-community/200311.mbox/%3c4A16CAE8-2130-11D8-9668-000393753936@gbiv.com%3e" target="_blank">volunteeritis</a>.

We each need to re-read these important messages from time to time and remind our communities of the need for self-care and care of others.

<h4 id="new-project">How do I start a new ASF project or migrate an existing project?<a class="headerlink" href="#new-project" title="Permanent link">&para;</a></h4>

Contact the <a href="https://incubator.apache.org/" target="_blank">Incubator Project</a>. They will assist you in starting a project or moving an existing one into the ASF.</p>

<a href="https://labs.apache.org/" target="_blank">Apache Labs</a> could also be for you if you want to start something new.

<h4 id="committer-responsibilities">What are the responsibilities of a Committer?<a class="headerlink" href="#committer-responsibilities" title="Permanent link">&para;</a></h4>

**Note**: this is an incomplete collection and not authoritative.

As an Apache volunteer, you have the right to set your own priorities and do the work that scratches your own itch. As a Committer, you have a responsibility to the community to help create a product that will outlive the interest of any particular volunteer, including yourself. For example, he code that you commit should be clear enough that others not involved in its current development will be able to maintain and extend it. It also means that you are responsible for helping to grow and maintain the health of the Apache community.

More specific responsibilities of Committers include:

  - **Deciding on release plans and releases**: A prime committer responsibility is to help decide when a version of product code is ready for release. A release is not to be taken lightly; each release must uphold the Apache tradition of quality. Each Project Management Committee PMC) formally authorizes the distribution of releases to the public.
  - **Applying patches**: To grow and maintain healthy communities, committers need to discuss, review and apply patches submitted by contributors and other committers. Committers are also responsible for the quality and IP clearance of the code that goes into ASF repositories.
  - **Helping users**: Committers should monitor both the `dev` and `user` or `users` email lists for the projects they work on and together provide prompt and useful
 responses to questions from users and their developer colleagues.
  - **Monitoring commits and issues**: Committers should review commit email messages for their projects and point out anything that looks funny or that may point to IP issues. Committers also monitor the project's issue-tracking system (Bugzilla or Jira or something else) for bug reportss or enhancement requests.
  - **Helping out with the website**: The main Apache website and the project websites are in constant need of maintenance. Committers on a project are expected to
 collectively maintain the project's web site. Apache committers as a group share the responsibility to maintain the main Apache site.

<h4 id="committer-set-term">Is there a set term for acting as a Committer? Will I have to be elected again?<a class="headerlink" href="#committer-set-term" title="Permanent link">&para;</a></h4>

Committer status and merit never expire. If you become inactive for a time (usually six months or more), your account may be deactivated for security reasons. Most
projects allow reactivation of committer status by application to the PMC.

Some projects use the concept of <em>emeritus committer</em> for those who have contributed to the project but can no longer can give much time to it.

<h4 id="code-import">How do I bring code developed outside Apache into an existing project?<a class="headerlink" href="#code-import" title="Permanent link">&para;</a></h4>

For any substantial codebase that has been developed outside the ASF, there is a process to complete before the code can be committed. The <a href="https://incubator.apache.org" target="_blank">Incubator</a> team manages this. The first step is to contact your <a href="https://www.apache.org/dev/pmc.html#import" target="_blank">PMC</a>.

<h4 id="private-or-public">Where should I discuss ASF project business?<a class="headerlink" href="#private-or-public" title="Permanent link">&para;</a></h4>

Apache project business should almost always be on your public `dev@` mailing list, unless there is a specific reason to use `private@`. See the <a href="https://www.apache.org/dev/pmc.html#private-or-public" target="_blank">discussion about private vs. public lists</a>.

<h4 id="first-commit">I just made my first commit. Why don't I see a commit message?<a class="headerlink" href="#first-commit" title="Permanent link">&para;</a></h4>

The most likely explanation is that the commit message is awaiting moderation. Messages will be delivered promptly without moderation once the moderator approves posts from your `apache.org` address.

<h3 id="technical">Technical<a class="headerlink" href="#technical" title="Permanent link">&para;</a></h3>

<h4 id="infrastructure-change-request">How do I make infrastructure requests?<a class="headerlink" href="#infrastructure-change-request" title="Permanent link">&para;</a></h4>

You might notice something that needs changing, for example the configuration for a mailing list. The request to the `users@infra` list or the `apmail@` alias needs to come from your Project Management Committee. That ensures that the requests are official, and not just an individual's desire. 

There are many things that the PMC or PMC chair can do directly, thereby easing the load on the infrastructure team (Infra).

<h4 id="infrastructure-public-communications">How does Infra communicate with the public?<a class="headerlink" href="#infrastructure-public-communications" title="Permanent link">&para;</a></h4>

Infra uses the `users@infra.apache.org` mailing list to discuss new infrastructure developments at the ASF. For service downtime announcements and current information on operations, we use <a href="https://twitter.com/infrabot" target="_blank">Infrabot</a>. For general announcements regarding services and the like, Infra has a <a href="https://blogs.apache.org/infra" target="_blank">blog</a>.

<h4 id="machines">What hosts/machines at Apache can I access?<a class="headerlink" href="#machines" title="Permanent link">&para;</a></h4>

Committers may access `home.apache.org`. See the related information in the [New committers' guide](new-committers-guide.html).
Note that you do <strong>only</strong> have sftp access.  There is no shell access.</p>

Here is a <a href="https://apache.org/dev/machines.html" target="_blank">list of other Apache services/hosts and their public keys</a>.

<h4 id="can-cant">What can and can't I do on those machines?<a class="headerlink" href="#can-cant" title="Permanent link">&para;</a></h4>

You can publish a small personal website in `public_html`, as described in the [New committers' guide](new-committers-guide.html). **Never** store secret/private keys (the private half of an SSH keypair, or a PGP private key) on any ASF machines.

<h4 id="statistics">Is there a way to see a graph of loads (CPU, I/O, network)?<a class="headerlink" href="#statistics" title="Permanent link">&para;</a></h4>

  - Infra publishes top-level statistics on the <a href="https://status.apache.org/" target="_blank">status page</a>.
  - Vadim Gritsenko provides <a href="http://home.apache.org/~vgritsenko/stats/">statistics and cool charts</a>.

<h4 id="host-key-change">What should I do if Host Key has changed when logging into an Apache server?<a class="headerlink" href="#host-key-change" title="Permanent link">&para;</a></h4>

Take any message about a change to the host key or any "Error validating server certificate" very seriously: it may indicate a man-in-the-middle attack is in progress. **Do not ignore this message**.

Before contacting the Apache infrastructure team, check that you are logging in to the correct machine, and verify the currently published SSH fingerprints for Apache hosts, as described under "Identity theft" in the  [New committers' guide](new-committers-guide.html).

<h4 id="help-i-forgot-my-password">Help, I Forgot My Password!<a class="headerlink" href="#help-i-forgot-my-password" title="Permanent link">&para;</a></h4>

See if you get an authorization failure (see below) when accessing SVN, or try the 'forgot password' link on the <a href="https://id.apache.org/" target="_blank">Apache Account site https://id.apache.org/</a>.

<h4 id="nexus-repositoryapacheorg-locked-me-out-when-i-tried-to-stage-a-rc">Nexus (<code>repository.apache.org</code>) locked me out when I tried to stage a RC<a class="headerlink" href="#nexus-repositoryapacheorg-locked-me-out-when-i-tried-to-stage-a-rc" title="Permanent link">&para;</a></h4>
<p>Nexus is LDAP based authorization. If you have changed your LDAP password recently it is possible
you have a cached version of your old password stored, perhaps in a <code>settings.xml</code> file 
locally. Maven makes repeated attempts to try this authorization and within 10 seconds 
you might find your LDAP account locked as a result.</p>
<p>Try accessing another LDAP-based service to test the theory.</p>
<p>The cure is to go to <a href="https://id.apache.org/reset/enter">https://id.apache.org/reset/enter</a> and reset your LDAP password to
clear the locked account. Change any cached credentials locally and try staging to Nexus again.</p>
<h2 id="svn">Version control<a class="headerlink" href="#svn" title="Permanent link">&para;</a></h2>
<h4 id="svn-authorization-failure">Why do I get an authorization failure when I try to access Subversion?<a class="headerlink" href="#svn-authorization-failure" title="Permanent link">&para;</a></h4>
<p>The most common reason is that you've forgotten your password!</p>
<p>The password you use for Subversion is the same as the password you use
for access to LDAP <code>id.apache.org</code>. You will not be prompted to enter it
frequently. This makes it is easy to forget.</p>
<p>Apache employs a number of different HTTP authentication realms. You will
need to enter your password whenever you access a new realm. (Subversion
prints information about the realm when you are prompted for the password.)</p>
<p>Of course, it is also possible that you're accessing a URL which is
restricted. That's probably for a good reason so unless you know that you
should have access, don't bother the infrastructure team.</p>
<p>If you do forget your password please visit <code>https://id.apache.org/</code> to reset it. </p>
<h4 id="committers-module">Where is the committers/ module?<a class="headerlink" href="#committers-module" title="Permanent link">&para;</a></h4>
<p>In Subversion, url: <code>https://svn.apache.org/repos/private/committers</code> </p>
<h4 id="commit-403">Why do I get a 403 When I try to commit?<a class="headerlink" href="#commit-403" title="Permanent link">&para;</a></h4>
<p>See the <a href="version-control.html">Version Control FAQ</a>.</p>
<h4 id="lock">When do I need to use svn lock?<a class="headerlink" href="#lock" title="Permanent link">&para;</a></h4>
<p>Very rarely if ever. Please read <a href="version-control.html#lock">this</a> for why you shouldn't lock.</p>
<h4 id="version-control-faq">Where can I find more information?<a class="headerlink" href="#version-control-faq" title="Permanent link">&para;</a></h4>
<p>The <a href="version-control.html">Version Control FAQ</a>.</p>
<h2 id="mail">Mail<a class="headerlink" href="#mail" title="Permanent link">&para;</a></h2>
<h4 id="email-setup">How do I set up my Apache email account?<a class="headerlink" href="#email-setup" title="Permanent link">&para;</a></h4>
<p>See these <a href="https://reference.apache.org/committer/email">instructions</a>.</p>
<h4 id="subscribe">How do I subscribe to a mailing list?<a class="headerlink" href="#subscribe" title="Permanent link">&para;</a></h4>
<p>If it is a public list, email the <code>-subscribe</code> address (such as
<code>dev-subscribe@httpd.apache.org</code>) from the address you want subscribed, and
reply to the confirmation mail.  For more information see the 
<a href="https://www.apache.org/dev/#mail">detailed mailing list guide</a>.</p>
<p>Private lists use the same procedure, but it's recommended to use <a href="https://whimsy.apache.org/committers/subscribe">the
self-subscribe app</a> instead;
that avoids needing to wait for the human moderators to check and green-light
your subscription request.</p>
<p>At the time of writing the self-subscribe app lets <a href="../foundation/members">ASF
Members</a> subscribe to any ASF list (see
&lt;../foundation/governance/members&gt; for the rationale behind this) and other
committers to subscribe to a few foundation-wide lists. Committers
who wish to subscribe to other lists (such as a private@ list of their project)
should still email the <code>-subscribe</code> address.</p>
<h4 id="subscriptions">How do I find out my subscriptions?<a class="headerlink" href="#subscriptions" title="Permanent link">&para;</a></h4>
<p>Committers can use <a href="https://whimsy.apache.org/roster/committer/__self__">Whimsy</a> to check their details, including subscription information.</p>
<h4 id="new-mailing-list">How do I request creation of a new mailing list?<a class="headerlink" href="#new-mailing-list" title="Permanent link">&para;</a></h4>
<p>Mailing lists are the virtual room where the communities live, form and grow.
It is wiser to keep the number of mailing lists per codebase the smallest
possible to allow the community to reach that critical mass that is
necessary to bootstrap a codebase and keep it in good shape.</p>
<p>At the same time, as communities grow, the need for more specialized mailing
lists appears. If you think your project requires a new list:</p>
<ul>
<li>Float the idea in the <code>dev@</code> or <code>users@</code> mailing list.</li>
<li>If there seems to be some support for the idea, request a community vote.</li>
<li>If creation is aporoved, your Project Management Committee needs to
send in a request (more details <a href="infra-contact#requesting-action">here</a>).</li>
</ul>
<p><strong>WARNING:</strong> Creating of a user mail list can be a dangerous thing
for a project community if the developers don't pay attention to their users and if
users don't have developers who reply to their emails. One would expect a well-behaving user community to reply to one
another in a civil, adult manner that is focused on whatever the list was created for, but it can take time for a community to learn and take to heart such good behavior.</p>
<h4 id="list-subscribers">How do I find out who is subscribed to a mailing list?<a class="headerlink" href="#list-subscribers" title="Permanent link">&para;</a></h4>
<p>Information on list subscriptions is private, so is not available to all committers.</p>
<p>Moderators can send an email to:</p>
<p><tt><var>listname</var>-list@<var>tlp</var>.apache.org</tt></p>
<p>Anyone with
access to the apmail account can run the following command to get a count
of the subscribers.</p>
<p><tt>ezmlm-list ~apmail//lists/<var>project</var>/<var>listname</var>| wc -l</tt></p>
<p>Remember that there often are people subscribed to the digest version
too:</p>
<p><tt>~apmail/lists/<var>project</var>/<var>listname</var>/digest</tt></p>
<p>However, most committers do not have access to apmail.</p>
<h4 id="mail-forward">Mail forwarding<a class="headerlink" href="#mail-forward" title="Permanent link">&para;</a></h4>
<p>Your forwarding address(es) are now stored in LDAP and maintained by the use of the
<a href="https://id.apache.org/">Self Serve</a> app. </p>
<p>Forwarding is now done directly from LDAP.</p>
<h4 id="mail-download">How can I download my old mail?<a class="headerlink" href="#mail-download" title="Permanent link">&para;</a></h4>
<p>Some older mailboxes may still exist on the <code>people.apache.org</code> server. Here is how to move the mail from there
into a <a href="http://www.mozilla.org/products/thunderbird/">Thunderbird</a> mail
client: </p>
<p>Copy the mailbox from your <code>people.apache.org</code> directory to your
local machine. For example:</p>
<p><code>$ scp USER@people.apache.org:/home/USER/Mailbox /tmp/Mailbox</code></p>
<p>Then copy it into your Thunderbird Mail folder. For example:</p>
<p><code>$ mv /tmp/Mailbox "thunderbird/profile/Mail/Local Folders"</code></p>
<p>The name of the directory might differ depending on your Thunderbird
version and configuration.</p>
<h2 id="mailmod">Mailing list moderation<a class="headerlink" href="#mailmod" title="Permanent link">&para;</a></h2>
<h4 id="mailing-list-moderators">How do I request changes for moderators?<a class="headerlink" href="#mailing-list-moderators" title="Permanent link">&para;</a></h4>
<p>File an INFRA Jira ticket or ask your PMC to send a request to the apmail@ alias (apache.org)</p>
<p>If you have access to apmail, you can just change the list of subscribers
to list/mod. For example, for the <code>mod_perl</code> developers' list that is in</p>
<p><code>~apmail/lists/perl.apache.org/dev/mod/</code> </p>
<p>Use <code>ezmlm-list</code> , <code>ezmlm-sub</code> and <code>ezmlm-unsub</code> to do that.</p>
<p>To determine who the existing moderators are, any committer can use the
technique described in the "committers" SVN module at <a href="https://svn.apache.org/repos/private/committers/docs/resources.txt" target="_blank">resources.txt</a>.</p>
<h4 id="mail-moderate">What should I do with "MODERATE" emails?<a class="headerlink" href="#mail-moderate" title="Permanent link">&para;</a></h4>
<p>Review the mail to see if it is spam (or other severely misguided
mail). If it is spam, just ignore the mail to have it silently dropped
after 5 days. </p>
<p>To bounce non-spam with a notice to the sender, reply to the <strong>-reject</strong> address in the mail header. If you wish to include a comment
with the rejection, the body of the message should look like this:</p>
<pre>
%%% Start comment
Your message goes here...
%%% End comment
</pre>

<p>If it is legitimate mail from a non-subscriber (or someone sending with a
different envelope sender than the one subscribed), reply to the <strong>-accept</strong> address. If you also send mail to the <strong>-allow</strong>
address (i.e. reply to all), future postings from that address will be
allowed through automatically.</p>
<p>If there is no <strong>-allow</strong> address in the moderate requests, the list is
misconfigured. Contact
<code>apmail@apache.org</code> and get them to enable remote administration.</p>
<p>See the <a href="http://www.ezmlm.org/">EZMLM</a> "Moderator's and Administrator's
Manual". You can also send a request for advice to {listname}-help@tlp.apache.org from
your moderation address (there are extra details for moderators).</p>
<p>Some lists are only open to ASF committers. The moderators have methods to
ensure that subscribers are committers, so subscribers can use whatever
email address that they want. Moderators see the tips described in the
"committers" SVN module at <a href="https://svn.apache.org/repos/private/committers/docs/resources.txt" target="_blank">resources.txt</a>.</p>
<h4 id="allowing_posts">Allowing posts from non-subscribers<a class="headerlink" href="#allowing_posts" title="Permanent link">&para;</a></h4>
<p>Most lists require people to subscribed in order to post messages. However, subscribers receive copies of all mails (or digests).
This is obviously unsuitable for bots, or for private lists which need to accept posts from non-subscribers.</p>
<p>A moderator can fix this by using 'Reply All' to a moderation message from the poster.
This will both 'accept' the message and 'allow' further posts.</p>
<p>It's also possible to set this up in advance, by subscribing the poster to the 'allow' list.
E.g. if you want mailbot@host.com to be able to post, use:</p>
<p><code>{listname}-allow-subscribe-mailbot=host.com@tlp.apache.org</code></p>
<p>Note that the '@' in the sender email must be replaced by '='</p>
<h4 id="problem_posts">Dealing with problem posts<a class="headerlink" href="#problem_posts" title="Permanent link">&para;</a></h4>
<p>If you have a troublesome poster, you can un-subscribe them from the
list using </p>
<p><code>{listname}-unsubscribe-badboy=menace.com@tlp.apache.org</code></p>
<p>Send a courtesy email to them to let them know they have been unsubscribed, and why.</p>
<p>Occasionally you will get someone with a poorly-configured spam filter
sending automated replies to the list. You can deny their postings using</p>
<p><code>{listname}-deny-subscribe-badposter=menace.com@tlp.apache.org</code></p>
<p>Send a courtesy email suggesting how they can resolve the problem.</p>
<p>If an unsubscribed user was added to the moderation list and is sending spam to
the list, remove them by sending an email to:</p>
<p><code>{listname}-allow-unsubscribe-badposter=menace.com@tlp.apache.org</code></p>
<p>To see a list of who is allowed to post on the moderation list, send an email to:</p>
<p><code>{listname}-allow-list@tlp.apache.org</code></p>
<p>There is now an <em>opt-in</em> configuration for problem posters, where you can 
subscribe him or her to a 'sendsubscribertomod' list. It works in exactly
the same way as adding or removing someone from an 'allow' or 'deny' list.
  <strong>File an INFRA ticket to have it enabled for your list</strong> (you don't have to 
use it, but having it enabled adds an option for you to consider.)</p>
<p>To use it (once it has been enabled) do this:</p>
<p><code>{listname}-sendsubscribertomod-subscribe-badposter=menace.com@tlp.apache.org</code></p>
<p>All emails from this person now go to a moderator for approval before they appear in the mailing list.
It does not matter if they are already a subscriber of the list 
or even if they are on the allow list.</p>
<p>Once a bad poster starts behaving in the proper manner again, feel free to 'unsubscribe' them from the 'sendsubscriberstomod' list so they can resume 
normal operations.</p>
<p>You mus send these moderation commands <strong>from your moderator address</strong>.  You can tell if
you're sending from the right address by emailing the <code>-help</code> address (e.g.,
<code>dev-help@tlp.apache.org</code>) and checking if the subject of the reply contains
the word "Moderator help".</p>
<h4 id="missing">Dealing with reports of "missing" mail<a class="headerlink" href="#missing" title="Permanent link">&para;</a></h4>
<p>If a subscriber reports that they are not receiving some e-mails, check which ones are involved.
If they are not seeing their own e-mails, note that GMail hides duplicates.
Also check whether the emails could have been treated as SPAM by their e-mail client.</p>
<h4 id="bounce">Dealing with reports of message "bounces"<a class="headerlink" href="#bounce" title="Permanent link">&para;</a></h4>
<p>If a subscriber reports getting a  bounce message from ezmlm, ask them to provide the details.
For example:</p>
<p>```</p>
<div class="codehilite"><pre><span class="n">Hi</span>! <span class="n">This</span> <span class="n">is</span> <span class="n">the</span> <span class="n">ezmlm</span> <span class="n">program</span><span class="p">.</span>
<span class="n">I</span><span class="o">&#39;</span><span class="n">m</span> <span class="n">managing</span> <span class="n">the</span> <span class="n">user</span><span class="p">@</span><span class="n">tlp</span><span class="p">.</span><span class="n">apache</span><span class="p">.</span><span class="n">org</span> <span class="n">mailing</span> <span class="n">list</span><span class="p">.</span>

<span class="n">Messages</span> <span class="n">to</span> <span class="n">you</span> <span class="n">from</span> <span class="n">the</span> <span class="n">user</span> <span class="n">mailing</span> <span class="n">list</span> <span class="n">seem</span> <span class="n">to</span>
<span class="n">have</span> <span class="n">been</span> <span class="n">bouncing</span>
<span class="p">...</span>
<span class="n">Here</span> <span class="n">are</span> <span class="n">the</span> <span class="n">message</span> <span class="n">numbers</span><span class="p">:</span>
    12345
</pre></div>


<p>```</p>
<p>This can occur if the recipient's mail system has strict SPAM detection rules.
One way to find such emails is to request an index listing from ezmlm, for example
by sending an email to</p>
<p><code>dev-index-12345@tlp.apache.org</code></p>
<p>This will show the subject, timestamp and sender of the email. That may be sufficient to identify it as spam.
If not, the subject and date should make it easy to find the email in the archives.</p>
<h4 id="spam">Dealing with "MODERATE" requests for SPAM<a class="headerlink" href="#spam" title="Permanent link">&para;</a></h4>
<p>If the content of the MODERATE request is clearly SPAM, the simplest solution
is just to delete the request. Do not reject it. However, if you are receiving a lot of such requests, it may perhaps be worth taking
additional action.</p>
<p>Some SPAM mails have an opt-out link. Whether this will actually do anything useful is another matter, but it might be worth
trying if the spam seems to be from a legitimate business. </p>
<p>To avoid revealing your personal IP address, you may wish to use an anonymizing service such as Tor.</p>
<p>If the SPAM mails are all sent from the same address (you can find the sender's address in the ), try adding them to the 'deny' list:</p>
<p><code>{listname}-deny-subscribe-badposter=menace.com@tlp.apache.org</code></p>
<p>You can find the sender's address in the moderation request in the <code>cc:</code> area:</p>
<div class="codehilite"><pre><span class="n">Cc</span><span class="p">:</span> <span class="p">{</span><span class="n">listname</span><span class="p">}</span><span class="o">-</span><span class="n">allow</span><span class="o">-</span><span class="n">tc</span><span class="p">.</span><span class="o">&lt;</span><span class="n">digits</span><span class="o">&gt;</span><span class="p">.</span><span class="o">&lt;</span><span class="n">alphanumeric</span><span class="o">&gt;-</span><span class="n">badposter</span><span class="p">=</span><span class="n">menace</span><span class="p">.</span><span class="n">com</span><span class="p">@</span><span class="n">tlp</span><span class="p">.</span><span class="n">apache</span><span class="p">.</span><span class="n">org</span>
</pre></div>


<p>The sender e-mail address is contained between the '-' (hyphen) immediately following the "alphanumerics" and the '@' sign.</p>
<p>This is already in the correct form for use in the 'deny' subscription request, i.e. the '@' has been changed to '='. In the example above this is:</p>
<p><code>badposter=menace.com</code></p>
<p>If this address contains random alphanumerics then it is probably a short-lived address, in which case there is no point trying to use the deny list.</p>
<h2 id="legal">Legal and organizational<a class="headerlink" href="#legal" title="Permanent link">&para;</a></h2>
<h4 id="apache-way">What are the core beliefs of The Apache Way?<a class="headerlink" href="#apache-way" title="Permanent link">&para;</a></h4>
<p><strong>Note:</strong> While there is not an official list, the following six
principles have been cited as the core beliefs of The Apache Way:</p>
<ul>
<li>collaborative software development</li>
<li>commercial-friendly standard license</li>
<li>consistently high quality software</li>
<li>respectful, honest, technical-based interaction</li>
<li>faithful implementation of standards</li>
<li>security as a mandatory feature</li>
</ul>
<p>A non-official <a href="http://theapacheway.com/">The Apache Way</a> website is available.</p>
<h4 id="projectindependence">Are Apache projects really independent?<a class="headerlink" href="#projectindependence" title="Permanent link">&para;</a></h4>
<p>Yes, Apache projects must always be managed <a href="https://community.apache.org/projectIndependence.html">independently</a> of undue commercial influence.</p>
<h4 id="free">Are Apache projects really always free to download and use?<a class="headerlink" href="#free" title="Permanent link">&para;</a></h4>
<p>Yes, Apache software products are always available to download and use <a href="https://www.apache.org/free/">at no cost</a>.</p>
<h4 id="applying-patches">How should I apply patches from a contributor?<a class="headerlink" href="#applying-patches" title="Permanent link">&para;</a></h4>
<p>You need to make sure that the commit message contains at least the name of
the contributor and ideally a reference to the Bugzilla or Jira issue with which
the patch was submitted. This preserves the legal trail and
makes sure that contributors are recognized. You can also list the names of all contributors somewhere
on the project website. To make it easier to "grep" for commits with patches from
contributors, always use the same pattern in the commit message.
Traditionally, we use "Submitted by: &lt;name&gt;" or "Obtained from:
&lt;name&gt;".</p>
<p>Here's an example of what such a commit message could look like:
<code><pre>
Bugzilla #43835:
Added some cool new feature.
Submitted by: John Doe &lt;john.doe.at.null.org&gt;</pre></code></p>
<h4 id="cla-registration">How long does it take to register a CLA?<a class="headerlink" href="#cla-registration" title="Permanent link">&para;</a></h4>
<p>It depends on variables including staff workload. You shouldn't be worried until a week or
two has passed since the date you expected the document to arrive.</p>
<p>When a <a href="http://www.apache.org/licenses/#clas">CLA</a> is submitted, there are
several stages to the process.</p>
<ul>
<li>First, it has to arrive in the hands of an Officer of the ASF.
For emailed and faxed documents, this is quick. For snail-mailed documents,
this is sometimes slow and often very slow if the mail is posted from outside the US.</li>
<li>Second, the ASF Secretary has to acknowledge the document in the appropriate file in the
Foundation repository.</li>
<li>Third, you wait until you know that the ASF has registered the
document. ASF members can watch the commit records or check the file.
PMC members can watch their private@ list for a notice from <code>secretary@</code> (this
only happens if the ICLA mentioned which TLP to notify) .
Others will need to check the <a href="https://home.apache.org/unlistedclas.html">list of ICLAs</a>
This is automatically generated, about once an hour, from the file maintained by the Secretary.</li>
</ul>
<h4 id="trademarks">How can I report issues with Apache brand or trademark use?<a class="headerlink" href="#trademarks" title="Permanent link">&para;</a></h4>
<p>PMCs are responsible for managing their own Apache project brands, and committers 
are encouraged to assist. If you spot any potential misuse or infringement of 
Apache brands or trademarks by third parties, please follow our 
<a href="../foundation/marks/reporting.html">Apache Trademark Use Reporting Guidelines</a>.</p></div>
