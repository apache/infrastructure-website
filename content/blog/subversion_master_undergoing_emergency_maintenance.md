title: Subversion master undergoing emergency maintenance
date: '2014-12-03T17:52:32+00:00'
permalink: subversion_master_undergoing_emergency_maintenance
layout: post

<p>
The primary master machine that hosts the Apache Software Foundation's subversion repositories is currently undergoing some emergency maintenance due to disk errors.<br />
We do not currently have an ETA on when this will be fixed.<br /> <br />
In the meantime, there will be no access to commit to SVN.<br />
The read-only mirror at <a target="_blank" href="http://svn.eu.apache.org">svn.eu.apache.org</a> is still working.</p> 
  <p><u><b>UPDATE: 18:30 UTC, 3 December 2014</b></u></p> 
  <p>The machine that hosts the SVN master suffered root filesystem corruption. This corruption led to a severe degradation of the SVN service, and to repair the issue the service was taken down. </p> 
  <p>This filesystem is separate from the filesystem that hosts the SVN repositories. We expect no data loss from this issue. (And we have multiple copies of this data available to us.)&nbsp;</p> 
  <p>We'll be keeping this blog post updated with more details as they become available. </p> 
  <p><b><u>UPDATE: 21:30 UTC, 3 December 2014</u></b></p> 
  <p>We've removed the master from DNS rotation, so read-only access remains accessible everywhere. </p> 
  <p>Commits to SVN remain disabled while we work on restoring the service.&nbsp;</p> 
  <p> </p> 
  <p><b><u>UPDATE: 04:45 UTC, 4 December 2014</u></b></p> 
  <p>&nbsp;The service remains offline while we work on moving the service to a new host. &nbsp;During the work to resolve the failed disks on eris (the previous host) it became apparent that it would not be the best use of our time to keep working on this (and we had frankly lost faith in the disks).&nbsp;</p> 
  <p>We are now several hours into this move. &nbsp;The data has been synchronised to the new host, and now we are working on porting the configuration of the old host into puppet and making it fit the new setup on which it will be run. &nbsp;We don't currently have an exact time when we think it will be finished, but we are hopeful it will be during Thursday 4th December 2014.</p> 
  <p>We'd like to apologise the downtime, but we are taking actions that we feel are in the best interests of a key piece of foundation infrastructure. &nbsp;As always you can come and find us in the Hipchat channel #asfinfra -&nbsp;<a title="https://www.hipchat.com/gdAiIcNyE" href="https://www.hipchat.com/gdAiIcNyE">https://www.hipchat.com/gdAiIcNyE</a>&nbsp;if you have any questions.&nbsp;</p> 
  <p> --pctony</p> 
  <p> </p> 
  <p><b><u>UPDATE: 11:18 UTC, 4 December 2014</u></b></p> 
  <p>&nbsp;We are performing sanity checks on the new puppetized configuration. For historical reasons, our svn system has relied on specially crafted versions of svn, which we are attempting to replace with canonical release versions instead, so as to easier set up a new host, should we experience another major outage. This entails a lot of rewriting of scripts, but we expect most of this to have been done now, pending a full system check.<br /></p> 
  <p>Once all this is done, we will be performing authorization checks to make sure everything is as it should be, and when satisfied, we will reopen the svn repo for committers.<br /></p> 
  <p>The ETA is still uncertain, but remains a hopeful &quot;today&quot; (Thursday, December 4th). </p> 
  <p>--humbedooh <br /></p> 
  <p><b><u>UPDATE: 16:15 UTC, 4 December 2014</u></b></p> 
  <p>We are nearly there. We are currently putting the finishing touches to the config, and we will begin closed testing within the infrastructure group very soon. Assuming this goes well we will aim to open the service as soon as possible after this. &nbsp;</p> 
  <p>The delay will come when we ensure that no data could be lost as a result of re-starting the service. &nbsp;Data security and provenance is our utmost concern.&nbsp;</p> 
  <p>More news to follow in the next couple of hours hopefully. </p> 
  <p>--pctony&nbsp;</p>
  <p> </p>
  <p><b><u>UPDATE: 03:01 UTC, 5 December 2014 &nbsp;[FINAL UPDATE]&nbsp;</u></b></p>
  <p>Well. As of 5 minutes ago the main subversion service was restored. Only one repository is currently not available, the dist repository used by projects to stage dev and release outputs. This will be fixed ASAP.&nbsp;</p>
  <p>If you spot any issues with the service, in the first instance please hop onto HipChat and chat to us - <a href="https://www.hipchat.com/gdAiIcNyE">https://www.hipchat.com/gdAiIcNyE</a>.&nbsp; Or you can use the usual email address <a href="mailto:infrastructure@apache.org">infrastructure@apache.org</a>&nbsp; if you prefer that.</p>
  <p>This outage has forced us to review the setup of the primary subversion host and as a result of this we have made many changes to bring it inline with our current practice and standards. This involved re-engineering quite a lot of things that had accumulated over the years, and like many a good onion the more layers we peeled back the more we sobbed.&nbsp;</p>
  <p>We are happy to report that this host is now completely managed with puppet, and is delivering metrics to our instance of Circonus very happily. </p>
  <p>Once again thank you for your patience and we hope that the service feels a lot more sprightly on it's new host.&nbsp;</p>
  <p>Cheers,<br />On behalf of the Apache Infrastructure Team</p>
  <p>--pctony&nbsp;</p> 
  <p> </p>
