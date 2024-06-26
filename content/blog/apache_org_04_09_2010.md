title: apache.org incident report for 04092010
date: '2010-04-13T05:04:50+00:00'
permalink: apache_org_04_09_2010
layout: post

<p>Apache.org services recently suffered a direct, targeted attack against our infrastructure, specifically the server hosting our issue-tracking software.</p> 
  <p>The Apache Software Foundation uses a donated instance of <a href="http://www.atlassian.com/software/jira/">Atlassian JIRA</a> as an issue tracker for our projects. Among other projects, the ASF Infrastructure Team uses it to track issues and requests. Our JIRA instance was hosted on brutus.apache.org, a machine running Ubuntu Linux 8.04 LTS.</p> 
  <h2>Password Security</h2> 
  <p><strong><font color="red">If you are a user of the Apache hosted JIRA, Bugzilla, or Confluence, a hashed copy of your password has been compromised.</font></strong></p> 
  <p>JIRA and Confluence both use a SHA-512 hash, but without a random salt.  We believe the risk to simple passwords based on dictionary words is quite high, and most users should rotate their passwords.</p> 
  <p>Bugzilla uses a SHA-256, including a random salt. The risk for most users is low to moderate, since pre-built password dictionaries are not effective, but we recommend users should still remove these passwords from use. </p> 
  <p>In addition, if you logged into the Apache JIRA instance between April 6th and April 9th, you should consider the password as compromised, because the attackers changed the login form to log them.</p> 
  <h2>What Happened?</h2> 
  <p>On April 5th, the attackers via a compromised <a href="http://www.slicehost.com">Slicehost</a> server opened a new issue, INFRA-2591.  This issue contained the following text:</p> 
  <blockquote>
ive got this error while browsing some projects in jira
http://tinyurl.com/XXXXXXXXX [obscured]
</blockquote> 
  <p>Tinyurl is a URL redirection and shortening tool.  This specific URL redirected back to the Apache instance of JIRA, at a special URL containing a <a href="http://en.wikipedia.org/wiki/Cross-site_scripting">cross site scripting (XSS) attack</a>. The attack was crafted to steal the session cookie from the user logged-in to JIRA. When this issue was opened against the Infrastructure team, several of our administrators clicked on the link. This compromised their sessions, including their JIRA administrator rights.</p> 
  <p>At the same time as the XSS attack, the attackers started a brute force attack against the JIRA login.jsp, attempting hundreds of thousands of password combinations.</p> 
  <p>On April 6th, one of these methods was successful. Having gained administrator privileges on a JIRA account, the attackers used this account to disable notifications for a project, and to change the path used to upload attachments. The path they chose was configured to run JSP files, and was writable by the JIRA user. They then created several new issues and uploaded attachments to them. One of these attachments was a JSP file that was used to browse and copy the filesystem. The attackers used this access to create copies of many users' home directories and various files.  They also uploaded other JSP files that gave them backdoor access to the system using the account that JIRA runs under.</p> 
  <p>By the morning of April 9th, the attackers had installed a JAR file that would collect all passwords on login and save them. They then sent password reset mails from JIRA to members of the Apache Infrastructure team. These team members, thinking that JIRA had encountered an innocent bug, logged in using the temporary password sent in the mail, then changed the passwords on their accounts back to their usual passwords.</p> 
  <p>One of these passwords happened to be the same as the password to a local user account on brutus.apache.org, and this local user account had full sudo access. The attackers were thereby able to login to brutus.apache.org, and gain full root access to the machine. This machine hosted the Apache installs of JIRA, Confluence, and Bugzilla.</p> 
  <p>Once they had root on brutus.apache.org, the attackers found that several users had cached Subversion authentication credentials, and used these passwords to log in to minotaur.apache.org (aka people.apache.org), our main shell server. On minotaur, they were unable to escalate privileges with the compromised accounts.</p> 
  <p>About 6 hours after they started resetting passwords, we noticed the attackers and began shutting down services. We notified Atlassian of the previously unreported XSS attack in JIRA and contacted SliceHost.  Atlassian was responsive.  Unfortunately, SliceHost did nothing and 2 days later, the <strong>very</strong> same virtual host (slice) <a href="http://blogs.atlassian.com/news/2010/04/oh_man_what_a_day_an_update_on_our_security_breach.html">attacked Atlassian directly</a>.</p> 
  <p>We started moving services to a different machine, thor.apache.org. The attackers had root access on brutus.apache.org for several hours, and we could no longer trust the operating system on the original machine.</p> 
  <p>By April 10th, JIRA and Bugzilla were back online.</p> 
  <p>On April 13th, Atlassian provided a patch for JIRA to prevent the XSS attack. See 
<a href="http://jira.atlassian.com/browse/JRA-20994">JRA-20994</a> and <a href="http://jira.atlassian.com/browse/JRA-20995">JRA-20995</a> for details.
</p> 
  <p>Our Confluence wiki remains offline at this time. We are working to restore it.</p> 
  <h2>What worked?</h2> 
  <ul> 
    <li>Limited use passwords, especially <a href="http://en.wikipedia.org/wiki/One-time_password">one-time passwords</a>, were a real lifesaver. If JIRA passwords had been shared with other services/hosts, the attackers could have caused widespread damage to the ASF's infrastructure. Fortunately, in this case, the damage was limited to rooting a single host.</li> 
    <li>Service isolation worked with mixed results. The attackers must be presumed to have copies of our Confluence and Bugzilla databases, as well as our JIRA database, at this point. These databases include hashes of all passwords used on those systems. However, other services and hosts, including LDAP, were largely unaffected.</li> 
  </ul> 
  <h2>What didn't work?</h2> 
  <ul> 
    <li>The primary problem with our JIRA install is that the JIRA daemon runs as the user who installed JIRA. In this case, it runs as a jira role-account. There are historical reasons for this decision, but with 20/20 hindsight, and in light of the security issues at stake, we expect to revisit the decision!</li> 
    <li>The same password should not have been used for a JIRA account as was used for sudo access on the host machine.</li> 
    <li>Inconsistent application of one time passwords; We required them on other machines, but not on brutus.  PAM was configured to allow optional use of OPIE, but not all of our sudoers had switched to it.</li> 
    <li>SSH passwords should not have been enabled for login over the Internet. Although the Infrastructure Team had attempted to configure the sshd daemon to disable password-based logins, having <code>UsePAM yes</code> set meant that password-based logins were still possible.</li> 
    <li>We use <a href="http://www.fail2ban.org">Fail2Ban</a> for many services, but we did not have it configured to track JIRA login failures.</li> 
  </ul> 
  <h2>What are we changing?</h2> 
  <ul> 
    <li>We have remedied the JIRA installation issues with our reinstall. JIRA is now installed by root and runs as a separate daemon with limited privileges.</li> 
    <li>For the time being we are running JIRA in a httpd-tomcat proxy config with the following rules:

      
      <pre>
<code>
   ProxyPass /jira/secure/popups/colorpicker.jsp !
   ProxyPass /jira/secure/popups/grouppicker.jsp !
   ProxyPass /jira/secure/popups/userpicker.jsp !
   ProxyPass /jira        http://127.0.0.1:18080/jira
</code>
</pre>
Sysadmins may find this useful to secure their JIRA installation until an upgrade is feasible.
    
    </li> 
    <li>We will be making one-time-passwords mandatory for all super-users, on all of our Linux and FreeBSD hosts.</li> 
    <li>We have disabled caching of svn passwords, and removed all currently cached svn passwords across all hosts ast the ASF via the global config <code>/etc/subversion/config</code> file:

      
      <pre>
<code>
[auth]
store-passwords = no
</code>
</pre> 
    </li>  
    <li>Use Fail2Ban to protect web application login failures from brute force attacks</li> 
  </ul> 
  <p>We hope our disclosure has been as open as possible and true to the ASF spirit. Hopefully others can learn from our mistakes.</p>
