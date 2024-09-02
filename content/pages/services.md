Title: Services and Tools

license: https://www.apache.org/licenses/LICENSE-2.0

Infra maintains a wide range of tools for PMCs, project committers, and the Apache Board to use. Parts of our toolkit are only available to people who have specific duties or roles. Others, like the monitoring tools that show the status of various parts of the Apache infrastructure, are available to everyone.

  - <a href="#tlps">Services for Top-Level Projects (TLPs)</a>
    - <a href="#web-sites">Websites</a>
    - <a href="#email">Email</a>
    - <a href="#self-serve">ASF self-service platform</a>
    - <a href="#account-mgmt">ASF account management</a>
    - <a href="#notices">Getting notices of infrastructure events</a>
    - <a href="#ldap">LDAP-enabled services</a>
  - <a href="#podlings">Services for incubating projects (podlings)</a>
  - <a href="#tools">Tools for ASF projects</a>
    - <a href="#source-repository">Version control</a>
    - <a href="#issue-tracking">Issue tracking and feature requests</a>
    - <a href="#repository-to-issue-tracker-integrations">Integrating your repository with Jira tickets</a>
    - <a href="#source-repository-publishersubscriber-services">Source repository publisher/subscriber services</a>
    - <a href="#build">Build services</a>
    - <a href="#product-naming">Product naming</a>
    - <a href="#code-signing">Code signing</a>
    - <a href="#qa">Code quality</a>
    - <a href="#code-dist">Code distribution</a>
    - <a href="#virtual-servers">Virtual servers</a>
    - <a href="#voting">Online voting</a>
  - <a href="#other">Other tools</a>
    - <a href="#dns">DNS</a>
    - <a href="#url-shortener">URL shortener</a>
    - <a href="#sharing">Sharing snippets</a>
    - <a href="#logging">Logging</a>
    - <a href="#machines">Machine list</a>
    - <a href="#whimsy">Whimsy</a>

<h2 id="tlps">Services for Top-Level Projects (TLPs)<a class="headerlink" href="#tlps" title="Permanent link">&para;</a></h2>

<h3 id="web-sites">Websites<a class="headerlink" href="#web-sites" title="Permanent link">&para;</a></h3>

  - <a href="https://apache.org">`www.apache.org`</a> is the main ASF website.
  - <a href="https://apache.org/dev/#web" targety="_blank">ASF project websites</a>.
  - <a href="https://infra-reports.apache.org/site-source/">ASF project website sources</a>
  - An index of <a href="https://projects.apache.org/projects.html?name" target="_blank">all ASF projects</a> (if they have set up a DOAP).
  - Any ASF project can use the [ASF-Pelican template](asf-pelican.html) as the basis for their project website.
  - Details about individual <a href="https://home.apache.org/" target="_blank">ASF Committers</a>.
  - Notes about committers' <a href="/new-committers-guide.html#public_html" target="_blank">personal web spaces</a>.
  - The <a href="https://whimsy.apache.org/site/" target="_blank">Apache Project Website Checker</a> periodically reviews all TLP websites and reports whether they comply with Apache's <a href="https://www.apache.org/foundation/marks/pmcs#navigation" target="_blank">policies for TLP websites</a>.
  
<h3 id="email">Email<a class="headerlink" href="#email" title="Permanent link">&para;</a></h3>

  - All requests for new email lists should go through the <a href="https://selfserve.apache.org/mailinglist-new.html" target="_blank">self-serve system</a>. Remember not to mark a list as private if you want it publicly archived.
  - Email server - QMail/QSMTPD
  - <a href="https://www.apache.org/foundation/mailinglists.html" target="_blank">email lists</a> - EZMLM
  - Searchable <a href="https://lists.apache.org/" target="_blank">email list archives</a>. ASF Members have full access to private emails; PMC members have access to their PMC's archives only.
  - Spam control - Spamfilter + SpamAssassin
  - Email forwarding: See <a href="https://id.apache.org" target="_blank">id.apache.org</a>
  - <a href="https://lists.apache.org/" target="_blank">PonyMail</a> lets you browse Apache email archives by certain categories, by user, or by project. You must log in if you want to respond to an email, or write a new one, through this interface.
  - Infra maintains and uses a series of <a href="https://infra.apache.org/infra-mail.html" target="_blank">email lists</a>, some of which are open to committers.

<h3 id="self-serve">ASF self-service platform<a class="headerlink" href="#self-serve" title="Permanent link">&para;</a></h3>

One of Infra's goals is to empower ASF members, PMCs, and committers to do much of what they need to do without having to request help from Infra. The <a href="https://selfserve.apache.org" target="_blank">Self-Service Platform</a>, for example, provides a number of handy tools that **people who have an Apache email address** (basically, project committers, PMC members, and ASF Members) can use to:

  * Create a Jira or Confluence project, Git repository, or email list (PMC Chairs and Infra members).
  * Edit your ASF identity or update your ASF password. If you are updating your password, you need access to the email account associated with your Apache account. A reset key is only valid for 15 minutes, so be sure to use it as soon as it arrives.
  * Synchronize Git repositories.
  * Use the OTP Calculator to generate one-time passwords for the OTP or S/Key one-time-password systems (generally, PMC members).
  * Archive a Confluence Wiki space and make it read-only.

People who are not part of the ASF community but wish to file a Jira ticket about an ASF project's product can use the platform to <a href="https://infra.apache.org/jira-guidelines.html#who" target="_blank">request a Jira account</a>.
  
<h3 id="account-mgmt">ASF account management<a class="headerlink" href="#account-mgmt" title="Permanent link">&para;</a></h3>

[ASF account management](account-mgmt.html) provides guidance if you want to update your account details, or have lost access to your account.
  
<h3 id="notices">Getting notices of infrastructure events<a class="headerlink" href="#notices" title="Permanent link">&para;</a></h3>
You can subscribe to notices of infrastructure events that you want to know about, ranging from Subversion commits to emails to specific lists. [Learn more here](pypubsub.html).

<h3 id="ldap">LDAP-enabled services<a class="headerlink" href="#ldap" title="Permanent link">&para;</a></h3>

Infra supports many ASF <a href="https://cwiki.apache.org/confluence/display/INFRA/LDAP+enabled+services+at+the+ASF" target="_blank">LDAP-enabled services</a>. You can log in to them with your LDAP credentials. 

<h2 id="podlings">Services for incubating projects (podlings)<a class="headerlink" href="#podlings" title="Permanent link">&para;</a></h2>

Infra supports incubating projects, or podlings. 

  - An introduction to [Infra and the Incubator](infra-incubator.html), showing the steps for setting up a new podling.
  - Guidance for [selecting a project or product name](project-names.html)
  
<h2 id="tools">Tools for ASF projects<a class="headerlink" href="#tools" title="Permanent link">&para;</a></h2>

Infra supports an array of tools and services to help projects develop and support both their applications and their community, including:

- Every project can use a dedicated space on the [Confluence wiki](cwiki.html).
  - How to <a href="https://cwiki.apache.org/confluence/display/INFRA/Managing+permissions+on+your+project%27s+Confluence+Space" target="_blank">manage user permissions</a> in your project's wiki space.
  - How to <a href="https://cwiki.apache.org/confluence/display/INFRA/Giving+a+user+edit+access+to+Confluence" target="_blank">give a user edit access</a> to the wiki space.
- <a href="https://reporter.apache.org/" target="_blank">Reporter</a> provides actvitity statistics and other information about your project, and editing tools to help you write and submit your project's quarterly Board reports.
- You can create and run a [project blog](project-blogs.html).
- You can establish a [Slack channel](slack.html) for real-time team discussions. Once you have your Slack channel, Infra can set up a _Slack-Jira bridge_ so that you get notices in your channel of new or updated Jira tickets. open a Jira ticket for INFRA to get this feature for your TLP's Slack channel.
- Teams can conduct and record meetings through Internet Relay Chat (IRC) using [ASFBot](asfbot.html). However, you must conduct formal votes on decisions in the appropriate project email list, following the <a href="https://www.apache.org/foundation/voting.html" target="_blank">Apache voting process</a>.
- [Localization tools](localization.html).
- The Apache <a href="https://creadur.apache.org/rat/" target="_blank">Release Audit Tool (RAT)</a> can help you confirm that your proposed product release complies with all ASF requirements.
- The ASF <a href="https://oauth.apache.org/api.html" target="_blank">OAuth</a> system provides a focal point for services wishing to make use of authentication without security implications around storing sensitive user data. Many Apache services use it to validate that the user requesting access is a committer within the project and has lawful access to the systems in question. <a href="https://cwiki.apache.org/confluence/display/INFRA/ASF+OAuth+Service" target="_blank">Read more about Apache OAuth</a>.

<h3 id="source-repository">Version control<a class="headerlink" href="#source-repository" title="Permanent link">&para;</a></h3>

Apache provides, and Infra maintains, [code repositories](version-control.html) that Apache projects can use to keep their project code safe, accessible to team members, and under version control.

  - Information about [using Git](git-primer.html)
    - [Read-only Git mirrors of SVN codebases](git.html)
    - [Writable Git repositories](project-repo-policy.html)
    - [Apache and GitHub](apache-github.html)
    - [Access roles for GitHub repositories](github-roles.html)
  
  - Information about [using Subversion](svn-basics.html)
    - <a href="https://svn.apache.org/repos/asf/" target="_blank">Subversion (SVN) repositories</a>
    - <a href="https://svn.apache.org/viewvc/" target="_blank">ViewVC (Browser interface to the main SVN repository)</a>
  

<h3 id="issue-tracking">Issue tracking and feature requests<a class="headerlink" href="#issue-tracking" title="Permanent link">&para;</a></h3>

The ASF supports these options for tracking issues and feature requests:

* <a href="https://issues.apache.org/jira" target="_blank">Jira</a> (Note: [qbot](qbot.html) is a tool that can integrate Jira notifications with a project's channel in the `the-asf` [Slack](slack.html) workspace.)
* The <a href="https://guides.github.com/features/issues/" target="_blank">GitHub issue tracking feature</a>

For historical reasons, some projects use <a href="https://bz.apache.org/bugzilla/" target="_blank">Bugzilla</a>. We continue to support Bugzilla, but will not set it up for projects that do not already use it.

<a href="https://allura.apache.org/" target="_blank">Apache Allura</a> is another issue-tracking option. If you feel it may meet your project's needs, consult directly with the Allura project through their `users@allura.apache.org` email list.

See <a href="https://issues.apache.org/" target="_blank">issues.apache.org</a> for a list of what each project uses.

Here is how to [request a bug and issue tracker for your project](request-bug-tracker.html).

Here are some guidelines for [writing a good bug report](bug-writing-guide.html).

<h3 id="repository-to-issue-tracker-integrations">Integrating your repository with Jira tickets<a class="headerlink" href="#repository-to-issue-tracker-integrations" title="Permanent link">&para;</a></h3>

Infra can activate a [Subversion and Git integration with Jira tickets](svngit2jira.html) for your project.

<h3 id="source-repository-publishersubscriber-services">Source repository publisher/subscriber services<a class="headerlink" href="#source-repository-publishersubscriber-services" title="Permanent link">&para;</a></h3>

  - SvnPubSub
  - [PyPubSub](pypubsub.html)

<h3 id="build">Build services<a class="headerlink" href="#build" title="Permanent link">&para;</a></h3>

Apache supports and models continuous integration and continuous deployment, or *CI/CD*. The [ASF build and supported services](build-supported-services.html) page provides information about, and links to, the CI services the ASF provides and/or supports.

Other tools to consider:

* <a href="https://travis-ci.org/" target="_blank">Travis CI</a>
* <a href="https://www.appveyor.com" target="_blank">AppVeyor</a>

<h3 id="product-naming">Product naming<a class="headerlink" href="#product-naming" title="Permanent link">&para;</a></h3>

See [guidance for choosing a product name](project-names.html)

<h3 id="code-signing">Code signing<a class="headerlink" href="#code-signing" title="Permanent link">&para;</a></h3>

  - Digicert
      - Requesting access to the [Digicert code signing service](digicert-access.html)
      - [Using Digicert](digicert-use.html)
  - For <a href="https://cwiki.apache.org/confluence/display/INFRA/Distribution+via+the+Apple+App+Store" target="_blank">distribution via the Apple App Store</a>
  - More information on <a href="https://cwiki.apache.org/confluence/display/INFRA/Code+Signing+and+Publishing" target="_blank">code signing and publishing</a>

<h3 id="qa">Code quality<a class="headerlink" href="#qa" title="Permanent link">&para;</a></h3>

<a href="https://sonarcloud.io/" target="_blank">**SonarCloud**</a> is a code quality and security tool that is free to open-source projects. It permits continuous inspection of code quality so your project can perform automatic reviews with static analysis of code to detect bugs, code smells, and security vulnerabilities in 20+ programming languages.

You can <a href="https://sonarcloud.io/organizations/apache/projects" target="_blank">check the status of many Apache project repositories</a>.

Guidance for using SonarCloud with an ASF project is <a href="https://cwiki.apache.org/confluence/display/INFRA/SonarCloud+for+ASF+projects" target="_blank">here</a>.

<h3 id="code-dist">Code distribution<a class="headerlink" href="#code-dist" title="Permanent link">&para;</a></h3>

Use the ASF <a href="https://repository.apache.org/" target="_blank">Nexus Repository Manager</a> to browse for and review code distributions by ASF projects.

<h4 id="distributions">Distributions<a class="headerlink" href="#distributions" title="Permanent link">&para;</a></h4>

  - <a href="https://www.apache.org/dyn/closer.lua" target="_blank">Current distributions</a>
  - <a href="https://archive.apache.org" target="_blank">Historical distribution archives</a>
  - [Rsync for distribution mirrors](how-to-mirror.html)
  - <a href="https://repository.apache.org" target="_blank">Nexus</a>

<h3 id="virtual-servers">Virtual servers<a class="headerlink" href="#virtual-servers" title="Permanent link">&para;</a></h3>

Infra can provide Ubuntu virtual machines for projects. See:

  - [Virtual machine policy](vm-policy.html)
  - [Process for requesting a vm](vm-for-project.html)

<h3>Use of nightlies.a.o</h3>

nightlies, as implied by its name, is designed as a 'short term' storage solution. See the [nightlies use policy](nightlies.html).

<h3 id="voting">Online voting<a class="headerlink" href="#voting" title="Permanent link">&para;</a></h3>

Projects can use the <a href="https://steve.apache.org" target="_blank">Apache STeVe</a> voting system instance (offline when not in use). The tool name refers to the <a href="https://en.wikipedia.org/wiki/Single_transferable_vote" target="_blank">single transferable vote</a> system that is one of its voting options. Open a Jira ticket for Infra to provide assistance in preparing STeVe for your project's use.

<h2 id="other">Other tools<a class="headerlink" href="#other" title="Permanent link">&para;</a></h2>

<h3 id="dns">DNS<a class="headerlink" href="#dns" title="Permanent link">&para;</a></h3>

Infra manages the ASF DNS, which is registered with Namecheap.

<h3 id="url-shortener">URL shortener<a class="headerlink" href="#url-shortener" title="Permanent link">&para;</a></h3>

<a href="https://s.apache.org" target="_blank">URL shortener</a>

<h3 id="sharing">Infra Reporting Dashboard<a class="headerlink" href="#infra-reports" title="Permanent link">&para;</a></h3>

The <a href="https://infra.apache.org/infra-reports.html" target="_blank">ASF Infrastructure Reporting Dashboard</a> contains a collection of reports on the overall health and activity of the infrastructure at the ASF. Some reports are available only for ASF Members and Infra team members.

<h3 id="machines">Machine list<a class="headerlink" href="#machines" title="Permanent link">&para;</a></h3>

<a href="/machines.html" target="_blank">Host Keys and Fingerprints</a>

<h3 id="whimsy">Whimsy<a class="headerlink" href="#whimsy" title="Permanent link">&para;</a></h3>

<a href="https://whimsy.apache.org/" target="_blank">Apache Whimsy</a> describes itself as "providing organizational information about the ASF and our projects in easy to consume ways, and to help automate corporate processes at the ASF to make the paperwork behind the scenes easier for our many volunteers."

There are many Whimsy tools useful for PMCs and individual committers, such as <a href="https://whimsy.apache.org/roster/committer/" target="_blank">Committer search</a>.
