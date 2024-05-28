
layout: post
Title: Git based websites available
date: '2015-04-29T21:29:31+00:00'
permalink: git_based_websites_available

<p>If you have worked on a web site for an Apache project, you've probably come across the fact that everything has to be in Subversion for web sites. The reason for this has been the desire to have a unified standard for publishing web site contents across all projects. The current workflow is handled by two components, svnpubsub - a pubsub service for subversion - and svnwcsub, the client for svnpubsub. In&nbsp;2013 we added a similar method for Git, called gitpubsub. Nowadays, gitpubsub is used for a ton of different service messages in the ASF; Git commits, JIRA notifications, GitHub communication and so on, and as of today, we have added gitwcsub, a gitpubsub client similar to svnwcsub, <b>enabling projects to use git as their repository for web site content.</b></p>
  <p>&nbsp;In order to use git as your web site repository, you must have your web site in a git repo. This can either be an existing repository or a new one created just for your web site. gitwcsub will, by default, pull content from the <i>asf-site</i> branch of any repo set up for it, so all that needs to be done is to have this branch in a repo on <a href="http://git-wip-us.apache.org">git-wip-us.apache.org</a> and you can have your projects site published via git.</p>
  <p>To have your site transferred to a git based workflow, please file a JIRA ticket with infrastructure.</p>
  <p>Lastly, we want to thank the CouchDB project for being guinea pigs in this process!<br /></p>
