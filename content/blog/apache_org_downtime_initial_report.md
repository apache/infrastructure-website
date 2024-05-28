
layout: post
Title: apache.org downtime - initial report
date: '2009-08-28T12:33:19+00:00'
permalink: apache_org_downtime_initial_report

<p>This is a short overview of what happened on Friday August 28 2009
to the apache.org services.&nbsp; A more detailed post will come at a later
time after we complete the audit of all machines involved.</p><p> On August 27th, starting at
about 18:00 UTC an account used for automated backups for the ApacheCon
website hosted on a 3rd party hosting provider was used to upload files
to minotaur.apache.org.&nbsp; The account was accessed using SSH key
authentication from this host.<br /></p><p><b>To the best of our knowledge at this time, no end users were affected by this incident,&nbsp; and the attackers were not able to escalate their
privileges on any machines.</b></p><b>While we have no evidence that downloads were affected, users are always advised to check digital
signatures where provided.</b><p>minotaur.apache.org runs
FreeBSD 7-STABLE and is more widely known as people.apache.org.&nbsp;
Minotaur serves as the seed host for most apache.org websites, in
addition to providing shell accounts for all Apache committers.</p><p>The
attackers created several files in the directory containing files for
www.apache.org, including several CGI scripts.&nbsp; These files were then
rsynced to our production webservers by automated processes.&nbsp; At about
07:00 on August 28 2009 the attackers accessed these CGI scripts over
HTTP, which spawned processes on our production web services. </p><p>At about 07:45 UTC we noticed these rogue processes on eos.apache.org, the Solaris 10 machine that normally serves our websites.</p><p>Within the next 10 minutes we decided to shutdown all machines involved as a precaution.</p><p>After
an initial investigation we changed DNS for most apache.org services to
eris.apache.org, a machine not affected and provided a basic downtime
message.</p><p>After investigation, we determined that our European fallover and backup machine, aurora.apache.org, was not affected.&nbsp;&nbsp; While
the some files had been copied to the machine by automated rsync
processes, none of them were executed on the host, and we restored from
a ZFS snapshot to a version of all our websites before any accounts
were compromised.</p><p>At this time several machines remain offline, but most user facing websites and services are now available.</p><p>We will provide more information as we can.<br /></p><p>&nbsp;</p>
