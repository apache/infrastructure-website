title: paste.apache.org sees the light of day
date: '2013-03-06T18:37:42+00:00'
permalink: paste_apache_org_sees_the
layout: post

<em>Note</em>: As of May, 2024, Apache Paste is no longer available.

<hr/>
<p>Today, the Apache Infrastructure team launched <a href="http://paste.apache.org">http://paste.apache.org</a>, a new ASF-driven site for posting snippets, scripts, logging output, configurations and much more and sharing them with the world.
</p> 
  <p><br /><b><i>&nbsp;Why yet another paste bin, you ask?</i></b></p> 
  <p>Well, for starters, this site is different in that is it run by the ASF, for the ASF, in that we fully control what happens to your data when you post it, or perhaps more important, what does NOT happen to it. The site enforces a &quot;from committers to everyone&quot; policy, meaning only <u>committers</u> may post new data on the site, but everyone is invited to watch the result. While this is not a blanket guarantee that the data is accurate or true, it is nonetheless a guarantee that <i><b>what you see is data posted by an Apache committer</b></i>.</p> 
  <p>Secondly, committers have the option to post something as being &quot;committers only&quot;, meaning only committers within the ASF can see the paste. This is much like the &quot;private&quot; pastes offered by many other sites, but with the added benefit that it prevents anyone snooping around from watching whatever you paste, unless they are actually a committer.</p> 
  <p> </p> 
  <p><b><i>&nbsp;Great, so how does it work?</i></b></p> 
  <p> It works like most other paste sites, in that you go to <a href="http://paste.apache.org">http://paste.apache.org,</a>&nbsp; paste your data, select which type of highlighting to use, and you get an URL with your paste. For text-only clients, raw data will be displayed, while regular browsers will enjoy a full web page with the ability to download or edit a paste. Currently we have support for httpd configurations, C/C++, Java, Lua, Erlang, XML/HTML, PHP, Shell scripts, Diff/Patch, Python and Perl syntax highlighting. If you want to have any other type of highlighting added, don't hesitate to ask!<br /></p> 
  <p>Since this site enforces the &quot;from committers to everyone&quot; policy, you are required to use your LDAP credentials when making a paste. To allow for the use of the service within console applications (shells etc) that might not (or should not) provide authentication credentials (on public machines you'd want to avoid storing your committer credentials for instance!), we have equipped the site with a token generator, that both allows you to pipe any output you may have directly to the site as well as gives you some hints on how you may achieve this.</p> 
  <p>Imagine you have a directory listing that you'd only want your fellow committers to see. Publishing this, using the token system, is as easy as doing:<br /><span style="background-color: #b5ffb4;">$&gt; ls -la | privpaste&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br />http://paste.apache.org/p/1234</span><br /></p> 
  <p>And there you have it, the command returns a URL ready for sharing with your fellow committers. Had you wanted for everyone to be able to see it, you could have used the <i>pubpaste</i> alias instead (click on &quot;generate token&quot; on the site to get more information about tokens and the useful aliases).</p> 
  <p> </p> 
  <p> We hope you'll enjoy this new service, and use it wisely as well as often. Should you have any questions or suggestions, we'd be most happy to receive them through any infra channel you want to use. <br /></p> 
  <p><br /></p> 
  <p> <br /></p>
