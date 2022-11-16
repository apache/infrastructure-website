
layout: post
title: Improved integration between Apache and GitHub
date: '2014-02-12T01:16:30+00:00'
permalink: improved_integration_between_apache_and

<p>After a few weeks of hard work and mind-boggling debugging, we are pleased to announce tighter and smarter integration between GitHub and the Apache Software Foundation's infrastructure.</p> 
  <p>These new features mean a much higher level of replication and retention of what goes on on GitHub, which in turns both help projects maintain control over what goes on within their project, as well as keeping a record of everything that's happening in the development of a project, whether it be on ASF hardware or off-site on GitHub. </p> 
  <p>To be more precise, these new features allows for the following:</p> 
  <ul> 
    <li>Any Pull Request that gets opened, closed, reopened or commented on now gets recorded on the project's mailing list</li> 
    <li>If a project has a JIRA instance, any PRs or comments on PRs that include a JIRA ticket ID will trigger an update on that specific ticket</li> 
    <li>Replying to a GitHub comment on the dev@ mailing list will trigger a comment being placed on GitHub (yes, it works both ways!)</li>
    <li>GitHub activity can now be relayed to IRC channels on the Freenode network.<br /></li> 
  </ul> 
  <p>As with most of our things, this is an opt-in feature. If you are in a project that would like to take advantage of these new features, please contact infrastructure, preferably by filing a <a title="JIRA" target="_blank" href="https://issues.apache.org/jira/browse/INFRA">JIRA ticket</a> with the component set to Git, and specifying which of the new features you would like to see enabled for your project.<br /></p> 
  <p>On behalf of the Infrastructure Team, I hope you will find these new features useful and be mindful in your use of them.<br /></p>
