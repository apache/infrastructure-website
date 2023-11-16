
layout: post
title: apache.org incident report for 8282009
date: '2009-09-02T08:56:09+00:00'
permalink: apache_org_downtime_report

<p>Last week we <a href="https://blogs.apache.org/infra/entry/apache_org_downtime_initial_report">posted about the security breach</a> that caused us to temporarily suspend some services.&nbsp; All services
have now been restored. We have analyzed the events that led to the breach, and continued to work on improving the security of our systems.<br /></p>

**NOTE**: At
no time were any Apache Software Foundation code repositories, downloads, or users put at risk by this intrusion. However, we believe that providing a detailed account
of what happened will make the internet a better place, by allowing others to learn from our mistakes.</h3>

<h2>What Happened?</h2>
<p>Our initial running theory was correct--the server that hosted
the apachecon.com (dv35.apachecon.com) website had been compromised. The machine was running CentOS, and we
suspect they may have used the recent local root exploits <a href="https://rhn.redhat.com/errata/RHSA-2009-1222.html">patched in RHSA-2009-1222</a> to escalate their privileges on this machine. The attackers fully compromised
this machine, including gaining root privileges, and destroyed most of
the logs, making it difficult for us to confirm the details of
everything that happened on the machine.&nbsp;</p><p>This machine is owned by the ApacheCon conference production company,
not by
the Apache Software Foundation. However, members of the ASF
infrastructure team had accounts on this machine, including one used to
create backups.</p><p>The
attackers attempted unsuccessfully to use passwords from the compromised ApacheCon
host to log on to our production webservers.&nbsp; Later, using the SSH Key of the backup account, they were able to access
people.apache.org (minotaur.apache.org). This account was an unprivileged user, used
to create backups from the ApacheCon host.<br /></p><p>minotaur.apache.org runs FreeBSD 7-STABLE, and acts as the staging machine for our mirror
network. It is
our primary shell account server, and provides many other services for Apache developers. None of our Subversion (version control) data is kept on this machine, and there was never any risk to any Apache source code.<br /></p><p>Once
the attackers had gained shell access, they added CGI scripts to the document root folders of
several of our websites. A regular, scheduled rsync process copied these scripts to our
production web server, eos.apache.org, where they became externally
visible. The CGI scripts were used to obtain remote shells, with information sent using HTTP POST commands. </p><p>Our download pages are
dynamically generated, to enable us to present users with a local mirror of our software. This means that all of our domains have <a href="http://httpd.apache.org/docs/2.2/mod/core.html#options">ExecCGI enabled</a>, making it harder for us to protect against an attack of this nature.<br /></p><p>After
discovering the CGI scripts, the infrastructure team decided to shutdown
any servers that could potentially have been affected. This included people.apache.org, and both the EU
and US website servers. All website traffic was redirected to a known-good
server, and a temporary security message was put in place to let people
know we were aware of an issue.</p><p>One by one, we brought the potentially-affected servers up, in single user mode, using our out of band access. It quickly became clear that aurora.apache.org, the EU website server, had not been affected. Although the CGI scripts had been rsync'd to that machine, they had never been run. This machine was not included in the DNS rotation at the time of the attack.</p><p>aurora.apache.org runs Solaris 10, and we were
able to restore the box to a known-good configuration by cloning
and promoting a ZFS snapshot from a day before the CGI scripts were synced
over. Doing so enabled us to bring the EU server back online, and to rapidly restore our main websites. Thereafter, we continued to analyze the cause of the breach, the method of access, and which, if any, other machines had been compromised.<br /></p><p>Shortly after bringing up
aurora.apache.org we determined that the most likely route of the breach was
the backup routine from dv35.apachecon.com. We grabbed all the
available logs from dv35.apachecon.com, and promptly shut it down.<br /></p><p>Analysis continued on minotaur.apache.org and eos.apache.org (our US
server), until we were confident that all remants of the attackers had been removed. As each server was declared clean, it was brought back online.<br /></p><h2>What worked?</h2><ul><li>The use of ZFS snapshots enabled us to restore the EU production web server to a known-good state.</li><li>Redundant
services in two locations allowed us to run services from an alternate
location while continuing to work on the affected servers and services.</li><li>A non-uniform set of compromised machines
(Linux/CentOS i386, FreeBSD-7 amd_64, and Solaris 10 on sparc) made it
difficult for the attackers to escalate privileges on multiple machines.</li></ul><h2>What didn't work?</h2><ul><li>The
use of SSH keys facilitated this attack. In hindsight, our implementation left a lot to be
desired--we did not restrict SSH keys appropriately, and we were
unaware of their misuse.<br /></li><li>The rsync setup, which uses people.apache.org to manage the deployment of our websites, enabled the attackers to get their files onto the US mirror, undetected.</li><li>The ability to run CGI scripts in any virtual host, when most of our websites do not need this functionality, made us unneccesarily vulnerable to an attack of this nature.<br /></li><li>The lack of logs from the ApacheCon host prevents us from conclusively determining the full
course of action taken by the attacker. All but one log file were deleted by the attacker, and logs were not kept off the machine.</li></ul><br /><h2>What changes we are making now?</h2>As a result of
this intrusion we are making several changes, to help further secure our
infrastructure from such issues in the future. These changes include the following:<ul><li>Requiring all users with <a href="http://www.freebsd.org/doc/en/books/handbook/one-time-passwords.html">elevated privileges to use  OPIE for sudo</a> on certain machines.&nbsp; We already require this in some places, but will expand its use as necessary.<br /></li><li>Recreating
and using new SSH keys, one per host, for backups.&nbsp; Also enforcing use of the
from=&quot;&quot; and command=&quot;&quot; strings in the authorized keys file on the
destination backup server. In tandem with access restrictions which only allow connections
from machines that are actually backing up data, this will prevent 3rd party
machines from being able to establish an SSH connection.&nbsp; <br /></li><ul><li>The
command=&quot;&quot; string in the authorized_keys file is now explicit, and only allows one way rsync traffic, due to the paths and flags used.</li><li>New keys have been generated for all hosts, with a minimum key length of at least 4096 bits .</li></ul><li>The
VM that hosted the old apachecon.com site remains powered down, awaiting
further detailed analysis.&nbsp; The apachecon.com website has been re-deployed on a
new VM, with a new provider and different operating system.<br /></li><li>We are looking at disabling CGI support on most of our website systems.&nbsp; This has led to the creation of <a href="https://svn.apache.org/repos/infra/infrastructure/trunk/projects/mod_asf_mirrorcgi/mod_asf_mirrorcgi.c">a new httpd module</a> that will handle things like mirror locations for downloads.<br /></li><li>The
method by which most of our public facing websites are deployed to our production servers will also change, becoming a much more automated process. We hope to have switched over to a <a href="https://svn.apache.org/repos/infra/infrastructure/trunk/projects/svnpubsub/svnpubsub.py">SvnSubPub</a> / <a href="https://svn.apache.org/repos/infra/infrastructure/trunk/projects/svnpubsub/svnwcsub.py">SvnWcSub</a> based system within the next few weeks. <br /></li><li>We will re-implement measures such as IP banning after several failed logins, on all machines.&nbsp;</li><li>A
proposal has been made to introduce centralized logging. This would include all system logs, and possibly also services such as smtpd and httpd.<br /></li></ul><p><br /><br /></p>
