title: Committer shell access to people.apache.org
date: '2014-09-25T23:38:41+00:00'
permalink: committer_shell_access_to_people
layout: post

<p>Apache committers are granted shell access to a host known as either people.apache.org or minotaur. As you may know, there has been a two year grace period in which we have advertised the upcoming change away from password logins to SSH key only.</p> 
  <p>Due to a significant recent increase in security issues, the Infrastructure team has taken steps to complete the implementation of key-only logins to protect ASF computing resources.&nbsp;</p> 
  <p>If you can't access the host anymore then it is very likely you do not have your key stored in LDAP. &nbsp;Please check your LDAP data in https://id.apache.org - and add your key(s) if they are not present.&nbsp; If necessary, ensure your keys are loaded locally (for linux see <a href="http://linux.die.net/man/1/ssh-add">http://linux.die.net/man/1/ssh-add</a>&nbsp; and <a href="http://linux.die.net/man/1/ssh-agent">http://linux.die.net/man/1/ssh-agent</a>)<br /></p> 
  <p>The host will pick up this change within 5 minutes of you making your change and you should be able to get in again. </p> 
  <p>As always if you have any issues please open a JIRA issue in the INFRA project and we will help you as soon as we can. &nbsp;</p> 
  <p> </p>
<p>Update 2024-08: <a href="end_of_home.html">You can't go home again</a>...</p>
