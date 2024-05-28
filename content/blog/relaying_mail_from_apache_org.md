
layout: post
Title: Relaying mail from apache.org.
date: '2009-08-01T12:24:57+00:00'
permalink: relaying_mail_from_apache_org

<p>One of the more common issues committers face at Apache is in trying to send mail from their apache.org account.&nbsp; We've just made that process a whole lot easier by setting up an SSL-enabled, smtp-auth based mail submission service on people.apache.org port 465; which is compatible with gmail's <a href="http://gmailblog.blogspot.com/2009/07/send-mail-from-another-address-without.html">recently announced feature</a> to allow outbound mail from your apache.org address to be directed to people.apache.org, instead of to a gmail server, for delivery.&nbsp; Say goodbye to all the ezmlm moderation battles: your SMTP envelope sender will now match your From header!<br /></p><p>In the future we may wish to tighten up the SPF records for apache.org, so please take advantage of this new service for all outbound delivery of your personal apache.org email.<br />&nbsp;</p>
