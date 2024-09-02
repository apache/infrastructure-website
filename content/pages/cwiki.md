Title: Confluence Wiki space for your project
license: https://www.apache.org/licenses/LICENSE-2.0

  - <a href="#overview">Overview</a>
  - <a href="#getting">Getting your project cwiki space</a>
  - <a href="#managing">Managing your cwiki space</a>
  - <a href="#watching">Watching a cwiki page</a>
  - <a href="#faqs">FAQs</a>

<h2 id="overview">Overview<a class="headerlink" href="#overview" title="Permanent link">&para;</a></h2>
Every Apache Software Foundation project can establish, manage, and populate a space on the <a href="https://cwiki.apache.org/confluence/" target="_blank">Confluence Wiki</a> (cwiki) that Infra maintains for the ASF. Projects can use this space to share and store important information, code snippets, and project procedures. Some projects also use their wiki space to provide product documentation for end users.

Many thanks to <a href="http://www.atlassian.com/" target="_blank">Atlassian Software Systems</a> for providing to the ASF a free license for this service.

**Note** To deal with the creation of spammy accounts and risks to ASF and project information on the wiki, we have limited account-creation: committers and ASF members can automatically log in to the ASF Confluence Wiki without creating an account. At the moment people who do not have an ASF LDAP account **cannot** create an account in the wiki.

<h2 id="getting">Getting your project cwiki space<a class="headerlink" href="#getting" title="Permanent link">&para;</a></h2>
Your ASF Project PMC can request creation of a new space.

  - On the <a href="https://selfserve.apache.org/" target="_blank">Self-Service portal</a> select _Create a new Confluence space_.
  - Include the cwiki account name of a PMC member (preferably the PMC chair) who will help administer the space.
  - Specify the key name for the space. The key name cannot be changed. If you use Jira, you might want to use the same key name.

When Infra creates the space, it sets up a $project-committer group (or equivalent) with full rights to the project's space.

<h2 id="managing">Managing your cwiki space<a class="headerlink" href="#managing" title="Permanent link">&para;</a></h2>

  - Each project community manages its own cwiki space and can decide how best to arrange and populate its pages.
  - Your cwiki space has a permissions feature that lets you set access levels for various areas of the space or its individual pages. If your project is using part of the space for end-user documentation, it can leave that section without access restrictions, while restricting access to other areas to project committers.
  - Editing access to your project's space is restricted to Project committers and individuals who have filed a <a href="http://www.apache.org/licenses/" target="_blank">Contributor's License Agreement</a> with the ASF.
  - You can create user groups in addition to the standard groups:
  
<h2 id="watching">Watching a cwiki page<a class="headerlink" href="#watching" title="Permanent link">&para;</a></h2>
Cwiki users, including those not involved in a project, can 'watch' pages in a project's space to receive update notices when information on that page changes. 

To watch a page: 
  
  - Log in in to the ASF cwiki.
  - Locate the page you want to watch.
  - Click **Watch** on the top menu bar. 

To stop watching a page:

  - Log in in to the ASF cwiki.
  - Click your profile icon at the top right of the wiki page.
  - From the dropdown menu that appears, select **Watches**. 
  - The list of pages you are watching appears, and you can remove those you no longer want to watch.
  
Infra can help you set up a role account that can watch for any changes in your space and send notices about them to an email list. This can lead to a large amount of traffic, so you can choose a digest option that provides a daily summary of changes.
  
<h2 id="faqs">FAQs<a class="headerlink" href="#faqs" title="Permanent link">&para;</a></h2>

**Can anyone add to a page?** As noted above, editing a page is restricted to people who have submitted a signed CLA to the ASF. This is to make clear that the individual intends to contribute the copyright on the documentation to the ASF.

However, your cwiki space supports comments, and any logged-in page visitor can add suggestions or ask questions.

**What if the site is down?** If the cwiki is down, first check the <a href="http://monitoring.apache.org/status/" target="_blank">ASF Public Network Status page</a>. If the service seems to be down, but Monitoring reports it as OK, then please email `infra@` or post a Jira ticket.

If the Monitoring status shows that the service is offline, then the appropriate people have already been contacted. If the service stays offline for 24 hours, then please file a Jira ticket.

**Is the cwiki backed up?** Yes, we store backups of the cwiki so we can restore all content if something bad happens.
