title: What can the ASF Buildbot do for your project?
date: '2009-11-09T13:01:12+00:00'
permalink: what_can_the_asf_buildbot
layout: post

<p>The below information has just been published to the main&nbsp; ASF Buildbot URI <a href="http://ci.apache.org/buildbot.html" title="ASF Buildbot">ci.apache.org/buildbot.html</a>.</p><p>A summary of just some of the things the ASF Buildbot can do for your project:
	</p><ul><li>Perform per commit build &amp; test runs for your project</li><li>Not just svn! - Buildbot can pull in from your Git/Mercurial branches too!</li><li>Build and Deploy your website to a staging area for review</li><li>Build and Deploy your website to mino (people) for syncing live</li><li>Automatically Build and Deploy Snapshots to Nexus staging area.</li><li>Create Nightly and historical zipped/tarred snapshot builds for download</li><li>Builds can be triggered manually from within your own freenode #IRC Channel</li><li>An IRCBot can report on success/failures of a build instantly</li><li>Build Success/Failures can go to your dev/notification mailing list</li><li>Perform multiple builds of an svn/git commit on multiple platforms asynchronously</li><li>ASF Buildbot uses the latest <a href="http://incubator.apache.org/rat" title="Incubating RAT project">RAT</a> build to check
		for license header issues for all your files.
		  </li><li>RAT Reports are published live instantly to ci.apache.org/$project/rat-report.[txt|html]</li><li>As indicated above, plain text or HTML versions of RAT reports are published.</li><li>[Coming Soon] - RAT Reports sent to your dev list, only new failures will be listed.</li><li>[Coming Soon] - Email a patch with inserted ASL 2.0 Headers into your failed files!!</li><li>Currently Buildbot has Ubuntu 8.04, 9.04 and Windows Server 2008 Slaves</li><li>[Coming Soon] - ASF Buildbot will soon have Solaris, FreeBSD 8 and Windows 7 Slaves</li></ul>

	<p>Dont see a feature that you need? Join the <a href="mailto:builds-subscribe@apache.org" title="Email Link to the builds subscribe list">builds.at.apache.org</a>
	mailing list and request it now, or file a <a href="http://issues.apache.org/jira/browse/INFRA/component/12312782">Jira Ticket.</a></p>
	<p>Help is always on hand on the <a href="mailto:builds@apache.org">builds.at.apache.org</a> mailing list for any problems or
	build configuration issues/requests. Or try the #asftest channel on irc.freenode.net for live support.</p>

	<p>So now you want your project to use Buildbot? No problem, best way is to file a <a href="http://issues.apache.org/jira/browse/INFRA/component/12312782">Jira Ticket.</a>
           and count to 10 (well maybe a bit longer but it won't be long before you are up and running).</p>
