Title: Committers' FAQs
license: https://www.apache.org/licenses/LICENSE-2.0

A committer is an individual who has write access to the codebase of an Apache project.

The main information resource for you in this role, apart from the wisdom of your project colleagues, is the [New Committers Guide](new-committers-guide.html).

If you are not an Apache committer, but wish to become one, the instructions on [how to contribute](contributors.html) to Apache projects will be more useful to you.</p>

<h3 id="frequently-asked-questions">Frequently asked questions<a class="headerlink" href="#frequently-asked-questions" title="Permanent link">&para;</a></h3>
<ul>
<li><a href="#general">General</a></li>
<li><a href="#technical">Technical</a></li>
<li><a href="#svn">Version control</a></li>
<li><a href="#mail">Email</a></li>
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
  - <a href="https://mail-archives.apache.org/mod_mbox/www-community/200311.mbox/%3c4A16CAE8-2130-11D8-9668-000393753936@gbiv.com%3e" target="_blank">volunteeritis</a>

We each need to re-read these important messages from time to time and remind ourselves and our communities of the need for self-care and care of others.

<h4 id="new-project">How do I start a new ASF project or migrate an existing project?<a class="headerlink" href="#new-project" title="Permanent link">&para;</a></h4>

Contact the <a href="https://incubator.apache.org/" target="_blank">Incubator Project</a>. They will assist you in starting a project or moving an existing one into the ASF.</p>

<a href="https://labs.apache.org/" target="_blank">Apache Labs</a> could also be for you if you want to start something new.

<h4 id="committer-responsibilities">What are the responsibilities of a Committer?<a class="headerlink" href="#committer-responsibilities" title="Permanent link">&para;</a></h4>

**Note**: this is an incomplete collection and not authoritative.

As an Apache volunteer, you have the right to set your own priorities and do the work that scratches your own itch. As a Committer, you have a responsibility to the community to help create a product that will outlive the interest of any particular volunteer, including yourself. For example, the code that you commit should be clear enough that others not involved in its current development will be able to maintain and extend it. It also means that you are responsible for helping to grow and maintain the health of the Apache community.

More specific responsibilities of Committers include:

  - **Deciding on release plans and releases**: A prime committer responsibility is to help decide when a version of product code is ready for release. A release is not to be taken lightly; each release must uphold the Apache tradition of quality. Each Project Management Committee PMC) formally authorizes the distribution of releases to the public.
  - **Applying patches**: To grow and maintain healthy communities, committers need to discuss, review and apply patches submitted by contributors and other committers. Committers are also responsible for the quality and IP clearance of the code that goes into ASF repositories.
  - **Helping users**: Committers should monitor both the `dev@` and `user@` or `users@` email lists for the projects they work on and together provide prompt and useful
 responses to questions from users and their developer colleagues.
  - **Monitoring commits and issues**: Committers should review commit email messages for their projects and point out anything that looks funny or that may point to IP issues. Committers also monitor the project's issue-tracking system (Bugzilla or Jira or something else) for bug reports or enhancement requests.
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
Note that you do <strong>only</strong> have SFTP access. There is no shell access. RSA SSH keys are required for SFTP access, which you can update via <a href="https://whimsy.apache.org" target="_blank">Whimsy</a> or <a href="https://id.apache.org" target="_blank">id.apache.org</a>.

Here is a <a href="/machines.html" target="_blank">list of other Apache services/hosts and their public keys</a>.

<h4 id="can-cant">What can and can't I do on those machines?<a class="headerlink" href="#can-cant" title="Permanent link">&para;</a></h4>

You can publish a small personal website in `public_html`, as described in the [New committers' guide](new-committers-guide.html). **Never** store secret/private keys (the private half of an SSH keypair, or a PGP private key) on any ASF machines.

<h4 id="statistics">Is there a way to see a graph of loads (CPU, I/O, network)?<a class="headerlink" href="#statistics" title="Permanent link">&para;</a></h4>

  - Infra publishes top-level statistics on the <a href="https://status.apache.org/" target="_blank">status page</a>.

<h4 id="host-key-change">What should I do if Host Key has changed when logging into an Apache server?<a class="headerlink" href="#host-key-change" title="Permanent link">&para;</a></h4>

Take any message about a change to the host key or any "Error validating server certificate" very seriously: it may indicate a <a href="https://en.wikipedia.org/wiki/Man-in-the-middle_attack" target="_blank">man-in-the-middle attack</a> is in progress. **Do not ignore this message**.

Before contacting the Apache infrastructure team, check that you are logging in to the correct machine, and verify the currently published SSH fingerprints for Apache hosts, as described under "Identity theft" in the [New committers' guide](new-committers-guide.html).

<h4 id="help-i-forgot-my-password">Help, I forgot my password!<a class="headerlink" href="#help-i-forgot-my-password" title="Permanent link">&para;</a></h4>

See if you get an authorization failure (see below) when accessing SVN, or try the 'forgot password' link on the <a href="https://id.apache.org/" target="_blank">Apache Account site https://id.apache.org/</a>.

<h4 id="nexus-repositoryapacheorg-locked-me-out-when-i-tried-to-stage-a-rc">Nexus (`repository.apache.org`) locked me out when I tried to stage a RC<a class="headerlink" href="#nexus-repositoryapacheorg-locked-me-out-when-i-tried-to-stage-a-rc" title="Permanent link">&para;</a></h4>

Nexus uses LDAP-based authorization. If you have changed your LDAP password recently it is possible you have a cached version of your old password stored, perhaps in a `settings.xml` file locally. Maven makes repeated attempts to try this authorization and within 10 seconds you might find your LDAP account locked as a result. Try accessing another LDAP-based service to test the theory.

The cure is to go to <a href="https://id.apache.org/reset/enter" target="_blank">https://id.apache.org/reset/enter</a> and reset your LDAP password to clear the locked account. Change any cached credentials locally and try staging to Nexus again.

<h3 id="svn">Version control<a class="headerlink" href="#svn" title="Permanent link">&para;</a></h3>

<h4 id="svn-authorization-failure">Why do I get an authorization failure when I try to access Subversion?<a class="headerlink" href="#svn-authorization-failure" title="Permanent link">&para;</a></h4>

The most common reason is that you've forgotten your password! The password you use for Subversion is the same as the password you use for access to LDAP `id.apache.org`. You will not be prompted to enter it frequently. This makes it easy to forget.

Apache employs a number of different HTTP authentication realms. You will need to enter your password whenever you access a new realm. (Subversion prints information about the realm when you are prompted for the password.)

Of course, it is also possible that you're accessing a URL which is restricted. That's probably for a good reason, so unless you know that you should have access, don't bother the infrastructure team about being locked out.

If you do forget your password please visit `https://id.apache.org/` to reset it.

<h4 id="committers-module">Where is the committers/ module?<a class="headerlink" href="#committers-module" title="Permanent link">&para;</a></h4>

In Subversion, URL: `https://svn.apache.org/repos/private/committers` .

<h4 id="lock">When do I need to use `svn lock`?<a class="headerlink" href="#lock" title="Permanent link">&para;</a></h4>

Very rarely if ever. See the [version control FAQ](version-control.html) for more details.

<h2 id="mail">Email<a class="headerlink" href="#mail" title="Permanent link">&para;</a></h2>

<h4 id="email-setup">How do I set up my Apache email account?<a class="headerlink" href="#email-setup" title="Permanent link">&para;</a></h4>

See these [instructions](committer-email.html).

<h4 id="subscribe">How do I subscribe to a mailing list?<a class="headerlink" href="#subscribe" title="Permanent link">&para;</a></h4>

If it is a public list, email the `-subscribe` address (such as `dev-subscribe@httpd.apache.org`) from the address you want subscribed, and reply to the confirmation mail. For more information see the <a href="https://www.apache.org/dev/#mail" target="_blank">mailing list guide</a>.

Private lists use the same procedure, but it's recommended to use <a href="https://whimsy.apache.org/committers/subscribe" target="_blank">the
self-subscribe app</a>. That avoids needing to wait for a human moderator to check and green-light your subscription request.

At the time of writing the self-subscribe app lets <a href="https://www.apache.org/foundation/members" target="_blank">ASF Members</a> subscribe to any ASF list and other committers to subscribe to a few foundation-wide lists. Committers who wish to subscribe to other lists (such as a `private@` list of their project) should still email the `-subscribe` address.

<h4 id="subscriptions">How do I find out my subscriptions?<a class="headerlink" href="#subscriptions" title="Permanent link">&para;</a></h4>

Committers can use <a href="https://whimsy.apache.org/roster/committer/__self__" target="_blank">Whimsy</a> to check their details, including subscription information.

<h4 id="list-subscribers">How do I find out who is subscribed to a mailing list?<a class="headerlink" href="#list-subscribers" title="Permanent link">&para;</a></h4>

Information on list subscriptions is private, so is not available to all committers.

**Note**: to use the examples below, replace `listname` with the name of the mailing list, and `tlp` with the name of the ASF project the list belongs to.

Moderators can send an email to: `listname-list@tlp.apache.org`

Anyone with access to the apmail account can run the following command to get a count of subscribers:

`ezmlm-list ~apmail/lists/tlp/listname| wc -l`

Remember that there often are people subscribed to the digest version of the list, too:

`~apmail/lists/tlp/listname/digest`

Note that moderators can get a log of changes to the subscriber list by emailing `listname-log@tlp.apache.org`.

<h4 id="mail-forward">Mail forwarding<a class="headerlink" href="#mail-forward" title="Permanent link">&para;</a></h4>

Your forwarding address(es) are stored in LDAP and maintained through the <a href="https://id.apache.org/" target="_blank">Self Serve</a> app. Forwarding is done directly from LDAP.

<h3 id="mailmod">Mailing list moderation<a class="headerlink" href="#mailmod" title="Permanent link">&para;</a></h3>

This information has moved [here](mailing-list-moderation.html).

<h3 id="legal">Legal and organizational<a class="headerlink" href="#legal" title="Permanent link">&para;</a></h3>

<h4 id="apache-way">What are the core beliefs of The Apache Way?<a class="headerlink" href="#apache-way" title="Permanent link">&para;</a></h4>

**Note:** While there is not an official list, the following principles have been cited as the core beliefs of The Apache Way:

  - collaborative software development
  - commercial-friendly standard license
  - consistently high quality software
  - respectful, honest, technical-based interaction
  - faithful implementation of standards
  - security as a mandatory feature

A non-official <a href="http://theapacheway.com/" target="_blank">The Apache Way</a> website is available.</p>

<h4 id="projectindependence">Are Apache projects really independent?<a class="headerlink" href="#projectindependence" title="Permanent link">&para;</a></h4>

Yes, Apache projects must always be managed <a href="https://community.apache.org/projectIndependence.html" target="_blank">independently</a> of undue commercial influence.

<h4 id="free">Are Apache project products really always free to download and use?<a class="headerlink" href="#free" title="Permanent link">&para;</a></h4>

Yes, the software products Apache produce are always available to download and use <a href="https://www.apache.org/free/" target="_blank">at no cost</a>.

<h4 id="applying-patches">How should I apply patches from a contributor?<a class="headerlink" href="#applying-patches" title="Permanent link">&para;</a></h4>

Consult with the PMC of the product involved, and see [how to submit a patch for project code](patch.html).

<h4 id="cla-registration">How long does it take to register a CLA?<a class="headerlink" href="#cla-registration" title="Permanent link">&para;</a></h4>

It depends on variables including staff workload. You shouldn't be worried until a week or two has passed since the date you expected the document to arrive.

When a <a href="https://www.apache.org/licenses/#contributor-license-agreements" target="_blank">CLA</a> is submitted, there are several stages to the approval process.

1. It has to arrive in the hands of an Officer of the ASF. As it happens via email, that is usually quick.
2. Second, the ASF Secretary has to acknowledge the document in the appropriate file in the Foundation repository.
3. Wait until you know that the ASF has registered the document. ASF members can watch the commit records or check the file. PMC members can watch their `private@` list for a notice from `secretary@` (this only happens if the ICLA mentioned which TLP to notify). Others will need to check the <a href="https://whimsy.apache.org/officers/unlistedclas.cgi" target="_blank">list of ICLAs</a>. This is automatically generated, about once an hour, from the file maintained by the Secretary.

<h4 id="trademarks">How can I report issues with Apache brand or trademark use?<a class="headerlink" href="#trademarks" title="Permanent link">&para;</a></h4>

PMCs are responsible for managing their own Apache project brands, and committers are encouraged to assist. If you spot any potential misuse or infringement of Apache brands or trademarks by third parties, please follow our  <a href="https://www.apache.org/foundation/marks/reporting.html" target="_blank">Apache Trademark Use Reporting Guidelines</a>.
