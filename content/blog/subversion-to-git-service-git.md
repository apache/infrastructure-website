title: Subversion-to-Git service (git.apache.org) post mortem, and the path forward
date: '2019-09-10T21:36:35+00:00'
permalink: subversion-to-git-service-git
layout: post

<h2>What happened<br /></h2> 
  <p>On August 31st 2019, the machine hosting our subversion-to-git mirrors and synchronization process for GitHub suffered a catastrophic drive error due to a power failure at our data center in Virginia. The power failure was, unfortunately, of such a nature, that recovering the disk data was not possible. Four days into the failure, on September 4th 2019, we received confirmation from the data center that the data redundancy had also failed, meaning we had no measure of restoring to a new disk.</p> 
  <h2>What this means right now</h2> 
  <p> Currently, all GitHub mirrors that originate in subversion, and thus relied on this service, are not being synchronized with their subversion source. As git relies on on-disk subversion meta-data, as opposed to in-repo, we are not able to obtain the meta-data and continue synchronizing unless a full recreation of the mirrors is performed. This means starting from the first revision in any given subversion repository and working towards the most current one, a process that may well take a few days or weeks, depending on the size of the repository (by number of commits) and the number of running jobs at that time.<br /></p> 
  <h2>What we intend to do, going forward </h2> 
  <p>Our most immediate action has been to revisit off-site backup strategies to ensure that our services are as resilient as possible, as well as re-assess and re-categorize various machines with regards to backup strategies.</p> 
  <p>With backups revisited, and on the more long-term side of things, discussions have been centered around what we want to offer, and how that will shape our design of the system. We want to balance the need for features against robustness and speed at the core of the service, as well as perform some fall cleaning of the service, and as such, the Infrastructure team has decided to restart the service with a blank slate, incorporating features as the needs arise and are discussed. We will also be reaching out to the projects with subversion-to-git mirrors currently on GitHub, and ask for a positive confirmation that they wish to continue with this service, so as to clean up the number of repositories that are no longer in use. We are also redesigning the core service, coupling it tighter with our subversion offerings. <br /></p> 
  <p>We estimate the git mirror service to be revamped and rebooted in a matter of weeks, as cycles allow (this is occurring in tandem with other service upgrades, which puts the timeline somewhat into the future), and will add mirror repositories on an ad-hoc basis as requests come in.</p> 
  <h2>Notable changes to service offering</h2> 
  <p>As we are starting with a blank slate, please be advised of the following changes to the service as it starts back up:</p> 
  <ul> 
    <li>There will no longer be a <a href="http://git.apache.org">git.apache.org</a>&nbsp; URL for git mirrors, to lessen the confusion with <a href="http://gitbox.apache.org">gitbox.apache.org.</a>&nbsp; Projects wishing to point to a git copy of their subversion repository should use their respective GitHub URLs.</li> 
    <li>Repositories are re-created from scratch. As such, it may take days from a recreation is started till the sync process begins to kick in.</li> 
  </ul>
