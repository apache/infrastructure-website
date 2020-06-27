Title: Confluence Wiki space for your project

Every Apache Software Foundation project can establish, manage, and populate a space on the Confluence Wiki (cwiki) that Infra maintains for the ASF. Projects can use this space to share and store important information, code snippets, and project procedures. Some projects use their wiki space to provide product documentation for end users.

Many thanks to <a href="http://www.atlassian.com/" target="_blank">Atlassian Software Systems</a> for providing to the ASF a free license for this service.

## Getting your project cwiki space ##

Your ASF Project PMC can request creation of a new space.

  - On the <a href="https://selfserve.apache.org/" target="_blank">Self-Service portal</a> select _Create a new Confluence space_.
  - Include the cwiki account name of a PMC member (preferably the PMC chair) who will help administer the space.
  - Specify the key name for the space. The key name cannot be changed. If you use Jira, you might want to use the same key name.

When Infra creates the space, it sets up a $project-committer group (or equivalent) with full rights to the project's space.

## Managing your cwiki space ##

  - Each project community manages its own cwiki space and can decide how best to arrange and populate its pages.
  - Your cwiki space has a permissions feature that lets you set access levels for various areas of the space or its individual pages. If your project is using part of the space for end-user documentation, it can leave that section without access restrictions, while restricting access to other areas to project committers.
  - Editing access to your project's space is restricted to Project committers and individuals who have filed a <a href="http://www.apache.org/licenses/" target="_blank">Contributor's License Agreement</a> with the ASF.
  - You can create user groups in addition to the standard groups:
  
## Watching a cwiki page ##

Cwiki users, inckluding those not involved in a project, can 'watch' pages in a project's space to receive update notices when information on that page changes, To watch a page, login in to the ASF cwiki, locate the page you want to watch, and click **Watch** on the top menu bar. 

To stop watching a page:

  - Click your profile icon at the top right if the wiki page.
  - From the dropdown menu that appears, select **Watches**. 
  - The list of pages you are watching appears, and you can remove those you no longer want to watch.
  
Infra can help you set up a role account that can watch for any changes in your space and send notices about them to an email list. This can lead to a large amount of traffic, so you can choose a digest option that provides a daily summary of changes.
  
## FAQs ##

**Can anyone add to a page?** As noted above, editing a page is restricted to people who have submitted a signed CLA to the ASF. This is to make clear that the individual intends to contribute the copyright on the documentation to the ASF.

However, your cwiki space supports comments, and any logged-in page visitor can add suggestions or ask questions.

**What if the site is down?** If the cwiki is down, first check the <a href="http://monitoring.apache.org/status/" target="_blank">ASF Public Network Status page</a>. If the service seems to be down, but Monitoring reports it as OK, then please email `infra@` or post a Jira ticket.

If the Monitoring status shows that the service is offline, then the appropriate people have already been contacted. If the service stays offline for 24 hours, then please file a Jira ticket.

**Is the cwiki backed up?** Yes, we store backups of the cwiki so we can restore all content if something bad happens.
