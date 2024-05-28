
layout: post
Title: id.apache.org  --  New Password Service
date: '2011-01-14T16:36:42+00:00'
permalink: https_id_apache_org_new

Folks, <br /> <br />

The infrastructure team are pleased to announce the availability of <a href="https://id.apache.org">id.apache.org</a> the new password management tool for all ASF committers and members.  This new service will allow users to: 
<ol> 
 <li>Reset forgotten LDAP passwords themselves, no need to contact the Infra team anymore.</li>
 <li>The ability to change their LDAP password.</li>
 <li> The ability to update your LDAP record, i.e. change forename, surname or mail attributes. [1].</li>
</ol>

Users should note that this service will only allow you to manage your LDAP password,  thus controlling access to those resources currently protected by LDAP authnz.   <br /> <br />
Once logged in you will note that some fields are not editable, this is by design and are there merely to show you your LDAP entry.  You are currently only allowed to edit your Surname, Given name (Forename), and Mail attributes.  This list may be extended as we make more features available, and they will be announced as and when.<br /> <br />

<p>Users of this service should note that we have a few small bugs to iron out, and this will be done as soon as possible.  For example if you attempt to modify your details and do no re-enter your password you will currently see a generic HTTP 500 error. </p>

<p>Thanks must go to Ian Boston (ieb), and Daniel Shahaf (danielsh) for making this work.  Ian provided the initial code (his first ever attempt at Python too). Daniel then took it and implemented several changes and generally improved the backend.</p>

<p>[1]  - It should be noted that updating your mail record in LDAP will not currently have any affect on where your apache.org email is forwarded on too.  This is planned to take place later this year. </p>
