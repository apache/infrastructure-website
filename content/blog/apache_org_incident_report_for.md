title: apache.org incident report for 05292012
date: '2012-05-29T16:59:09+00:00'
permalink: apache_org_incident_report_for
layout: post

<p>Last week, internal audit activity discovered that the access logs of some committer-only Apache services contained passwords but had been available to every Apache committer.<br /></p> 
  <h3> </h3> 
  <h3>The problem</h3> 
  <p>The httpd logs of several ASF services are aggregated and archived on minotaur.apache.org.&nbsp; Minotaur is also people.apache.org, the shell host for committers, and committers were encouraged to analyse the logs and <a href="http://mail-archives.apache.org/mod_mbox/subversion-dev/201205.mbox/%3CCABD8fLV30-YaFaYt21GuCJX+_xqqPCB+S+XpW_G1aydyTrgkug@mail.gmail.com%3E">produce aggregated data</a>.<br /><br />However, for two services, the archived logs included <a href="http://httpd.apache.org/docs/current/mod/mod_log_forensic.html">forensic logs</a>, which are extra-verbose logs that include all HTTP request headers.&nbsp; (The logs are never encrypted, even if the HTTP connection was wrapped by SSL encryption.)&nbsp; Both of these services  <a href="http://s.apache.org/">http://s.apache.org</a> and <a href="http://svn.apache.org/">http://svn.apache.org</a>  allow anyone to use them in a read-only manner anonymously, and allow further operations (such as creating shortlinks) to LDAP-authenticated committers.&nbsp; Authentication is usually done by embedding the username and password, encoded in base64, in the &quot;Authorization:&quot; HTTP header, under SSL encryption.<br /><br />Base64 is a reversible transform.&nbsp; (It is an encoding, not a cipher.)<br /><br />Consequently, any Apache committer could learn the passwords of any other committer by reading the log files and reversing the base64 encoding.<br /></p> 
  <h3>Shutting the barn door</h3> 
  <p>The logs archive directory was made readable by the root user only.&nbsp; Forensic logging was disabled, and past forensic logs deleted.&nbsp; ZFS snapshots containing those logs were destroyed, too.<br /></p> 
  <h3>Finding the horse<br /></h3> 
  <p>We know that several committers had on one occasion or another copied the logs in order to analyse them, so we operated on the assumption that copies of the sensitive forensic logs were circulating on hardware we do not control.&nbsp; We therefore opted to have all passwords changed, or reset.<br /><br />Several Apache committers whose passwords grant very high access were advised privately to change their passwords.&nbsp; The root@ team ensured the follow-through and, before announcing the vulnerability any further, changed the passwords of those whom had not done so themselves.&nbsp; The root@ team also changed the passwords of all non-human (role) accounts on those services.<br /><br />The vulnerability was then announced to all Apache committers with the same instructions: 'Your passwords may be compromised; change them &quot;now&quot;; we will explain the problem later.'.&nbsp; This notice was authenticated via a PGP signature and via acknowledging it in a root-owned file on people.apache.org.<br /><br />Finally, passwords that have not been changed after forensic logs had been disabled  and, therefore, were presumed to be contained in compromised forensic logs  were changed by the root@ team to random strings.</p> 
  <h3>Implications<br /></h3> 
  <p>Were some committer to have compromised another Apache account using this vulnerability prior to these steps being taken, note that root access to all apache.org hosts is only available using one-time-passwords (otp) for certain privileged sudo users.&nbsp; Such account holders have been instructed not to use the same password for otp as for LDAP, so this would not have resulted in an attacker gaining root privileges without our knowledge.&nbsp; All of our commit activity is peer-reviewed and logged to various commit lists, and no reports of unusual commit activity have been received during the time frame in which this exposure was effective.&nbsp; In fact no unusual activity has ever been reported regarding any of our LDAP-based services, so there is no reason for us to suspect malicious activity has occurred as a result of this vulnerability.<br /></p> 
  <h3>Preventing recurrence</h3> 
  <p>No code changes were needed to the software that s.apache.org and
svn.apache.org run; the software was behaving correctly according to
its configuration, but the configuration itself  and the in-house
log archiving scripts  were incorrect.<br /><br />A member of the infrastructure team will be approaching the Apache HTTPD PMC with a documentation patch for mod_log_forensic.</p> 
  <h3>Epilogue</h3> 
  <p>There were no malicious parties involved here (to our knowledge); we just made a configuration error.&nbsp; The nature of the error meant we had to assume all passwords were compromised, and that was costly to fix.<br /><br />We hope our disclosure has been as open as possible and true to the ASF spirit.&nbsp; Hopefully others can learn from our mistakes.&nbsp; See our <a href="http://www.apache.org/info/20010519-hack.html">prior</a> <a href="https://blogs.apache.org/infra/entry/apache_org_downtime_report">incident</a> <a href="https://blogs.apache.org/infra/entry/apache_org_04_09_2010">reports</a> from the Apache Infrastructure Team.<br /><br />Committers  please address questions to root@apache.org only.<br /><br />Queries from the press should be sent to press@apache.org.<br /><br />Happy hacking!<br /><br /> </p>
