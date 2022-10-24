
layout: post
title: Changes to email service for all committers
date: '2011-02-24T21:13:18+00:00'
permalink: changes_to_email_service_for

<p>In the near future the Infrastructure team will be implementing a change to the way we handle emails for all committers. </p>

<p>
Historically we have allowed users to choose how to handle their apache.org email.  However we will be making the following changes:
<ol>
 <li>Making LDAP authoritative for all mail forwarding addresses.</li>
 <li>Users will no longer be allowed to store their apache.org email locally on people.apache.org (minotaur)</li>
 <li>The Infra team will take the mail address currently held in either your .qmail or .forward file (.qmail is authoritative if they both exist) and inject this into LDAP</li>
 <li>We will no longer allow users to configure mail filtering, but you can configure your SpamAssassin threshold as per <a href="https://blogs.apache.org/infra/entry/controlling_your_spamassassin_threshold1"> our recent blog post</a>.</li>
 <li>We will make committers ~/.forward and ~/.qmail files read-only, there will still be at least one of these files, but it will be owned by the mail daemon user.  </li>
</ol>
</p>

<p>This means that all committers will be required to forward their apache.org email to an email address outside of the foundation. </p>

<p>We are doing this to simplify the email infrastructure, and to help reduce the current level of complexity of maintaining people.apache.org.  Also, making LDAP authoritative means we can move some of the work straight out to the MXs, and thus avoid sending it through several mail servers.  In the new architecture if someone emails you directly at your apache.org mail address it will only be handled by one apache.org MX. </p>

<p>Of course, we wont delete any email you currently have on people.apache.org.  Should you want to edit your LDAP record you should use <a href="https://id.apache.org">https://id.apache.org</a> to do this.</p>

