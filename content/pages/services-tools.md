Title: Services and Tools

Infra maintains a wide range of tools for PMCs, project committers, and the Apache Board to use. Parts of our toolkit are only available to people who have specific duties or roles. Others, like the monitoring tools that show the status of various parts of the Apache infrastructure, are available to everyone.

<h2 id="web-sites">Web sites<a class="headerlink" href="#web-sites" title="Permanent link">&para;</a></h2>

  - <a href="https://apache.org/dev/#web" targety="_blank">ASF websites</a>.
  - An index of <a href="https://projects.apache.org/projects.html?name" target="_blank">all ASF projects</a>.
  - `www.apache.org` is the main ASF website. Build instructions are <a href="https://apache.org/dev/infra-site" target="_blank">here</a>.
  - Details about individual <a href="https://home.apache.org/" target="_blank">ASF Committers</a>.
  - Notes about committers' <a href="https://apache.org/dev/new-committers-guide.html#public_html" target="_blank">personal web spaces</a>.
  
<h2 id="email">Email<a class="headerlink" href="#email" title="Permanent link">&para;</a></h2>

  - Mail server - QMail/QSMTPD
  - <a href="https://www.apache.org/foundation/mailinglists.html" target="_blank">mailing lists</a> - EZMLM
  - Searchable <a href="https://lists.apache.org/" target="_blank">private mailing list archives (mod_mbox)</a>. ASF Members have full access; PMC members have access to their PMC's archives only.
  - Spam control - Spamfilter + SpamAssassin
  - Mail forwarding: See <a href="https://id.apache.org" target="_blank">id.apache.org</a>
  - <a href="https://lists.apache.org/" target="_blank">PonyMail</a> lets you browse Apache email archives by certain categories, by user, or by project. You must log in if you want to respond to an email, or write a new one, through this interface.
  - Infra maintains and uses a series of <a href="https://infra.apache.org/infra-mail.html" target="_blank">mailing lists</a>, some of which are open to committers.

## ASF Self-Service Platform

One of Infra's goals is to empower ASF members, PMCs, and committers to do much of what they need to do without having to request help from Infra. The <a href="https://selfserve.apache.org" target="_blank">Self-Service Platform</a>, for example, provides a number of handy tools that **people who have an Apache email address** (basically, project committers, PMC members, and ASF Members) can use:

  * Create a new Jira or Confluence project, Git repository, or mailing list (PMC Chairs and Infra members).
  * Edit your ASF identity or update your ASF password.
  * Synchronize Git repositories.
  * Use the OTP Calculator to generate passwords for the OTP or S/Key one-time-password systems (generally, PMC members).
  
### Getting notices of infrastructure events
You can subscribe to notices of infrastructure events that you want to know about, ranging from Subversion commits to emails to specific lists. [Learn more here](pypubsub.html).

### LDAP-enabled services
Infra supports many ASF <a href="https://cwiki.apache.org/confluence/display/INFRA/LDAP+enabled+services+at+the+ASF" target="_blank">LDAP-enabled services</a>. You can log in to them with your LDAP credentials. 
  
## Tools for ASF projects

### PMC tools

- <a href="https://reporter.apache.org/" target="_blank">Reporter</a> provides actvitity statistics and other information about your project, and editing tools to help you write and submit your project's quarterly Board reports.
- You can create and run a [project blog](project-blogs.html).
- Teams can conduct and record meetings through Internet Relay Chat (IRC) using [ASFBot](asfbot.html).
- The <a href="https://translate.apache.org/" target="_blank">ASF Translation Service</a> provides the Pootle localization tool to help projects that want to provide documentation and user-interface text in multiple languages. *NOTE*: While several ASF projects continue to use Pootle, AFS is not approving new Pootle use. As of March, 2020, Infra is testing a replacement translation service.
- The Apache <a href="https://creadur.apache.org/rat/" target="_blank">Release Audit Tool (RAT)</a> can help you confirm that your proposed product release complies with all ASF requirements.

<h4 id="source-repository">Version control<a class="headerlink" href="#source-repository" title="Permanent link">&para;</a></h2>

Apache provides, and Infra maintains, [code repositories](version-control.html) that Apache projects can use to keep their project code safe, accessible to team members, and under version control.

  - <a href="https://svn.apache.org/repos/asf/" target="_blank">Subversion (SVN) repositories</a>
  - <a href="https://svn.apache.org/viewvc/" target="_blank">ViewVC (Browser interface to the main repository)</a>
  - [Read-only Git mirrors of SVN codebases](git.html)
  - [Writable Git repositories](wr8taboe-git.html)


<h4 id="issue-tracking">Issue tracking and feature requests<a class="headerlink" href="#issue-tracking" title="Permanent link">&para;</a></h4>

Projects can use either of these bug-tracking  and feature request tools:

* <a href="https://issues.apache.org/jira" target="_blank">Jira</a>
* <a href="https://bz.apache.org/bugzilla/" target="_blank">Bugzilla</a>

For historical reasons, some projects have their own instances of Jira or Bugzilla. See <a href="https://issues.apache.org/" target="_blank">issues.apache.org</a> for a list.

Review Apache's <a href="https://issues.apache.org/bugwritinghelp.html" target="_blank">bug reporting guidelines</a>.

### Build services

Apache supports and models continuous integration and continuous deployment, or *CI/CD*. The <a href="https://ci.apache.org" target="_blank">Apache Build services site</a> provides more information, and links to these build tools:

* BuildBot
* Gump
* Jenkins

Other tools to consider:

* <a href="https://travis-ci.org/" target="_blank">Travis CI</a>
* <a href="https://www.appveyor.com" target="_blank">Appveyor</a>


### Code Distribution

Use the ASF <a href="https://repository.apache.org/" target="_blank">Nexus Repository Manager</a> to browse for and review code distributions by ASF projects.



### Sharing Snippets

<a href="https://paste.apache.org/" target="_blank">Paste</a> is a service that lets ASF members post code snippets or similar file extracts they want to share to illustrate a code issue or make available for reuse, usually with other project members. You can post content as plain text, or formatted for a number of coding and scripting languages.

### Logging

* <a href="https://uls.apache.org/app/kibana#/discover?_g=()" target="_blank">Kibana</a>

### Machine List

* <a href="https://www.apache.org/dev/machines.html" target="_blank">Host Keys and Fingerprints</a>

### Whimsy

* <a href="https://whimsy.apache.org/roster/committer/" target="_blank">Committer search</a>

