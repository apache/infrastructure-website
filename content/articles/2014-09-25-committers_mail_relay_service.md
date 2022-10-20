
layout: post
title: Committers mail relay service
date: '2014-09-25T22:57:44+00:00'
permalink: committers_mail_relay_service

<p>For a very long time now we have allowed committers to send email from their @apache.org email address from any host. &nbsp;10 years ago this was less of an issue than it is today. &nbsp;In the current world of mass spam and junk flying around, mail server providers are trying to find better ways to implement a sense of safety from this for their users. &nbsp;One such method is SPF [1]. These methodologies check that incoming email actually originated via a valid mail server for the senders domain.&nbsp;</p> 
  <p>For example if you send from myuserid@apache.org, but you just send that via your ISP at home, it could be construed as being junk as it never came via an apache.org mail server. &nbsp;Some time ago we setup a service on people.apache.org to cater for this, but it was never enforced and it seems that the SMTP daemon running the service is not 100% RFC compliant and thus some people have been unable to use this service.</p> 
  <p>As of today, we have stood up a new service on host mail-relay.apache.org that will allow committers to send their apache.org emails via a daemon that is RFC compliant and uses your LDAP credentials. You can read here [2] what settings you will need to be able to use this service.&nbsp;</p> 
  <p>On Friday October 10th, at 13:00 UTC the old service on people.apache.org will be terminated, and the updates to the DNS to enforce sending of all apache.org email to have originated via an ASF mail server will be enabled. This means that as of this time if you do not send your apache.org email via mail-relay it is very likely that the mail will not reach it's destination. &nbsp;</p> 
  <p>When we say 'send your apache.org email' &nbsp;- we mean that when you send *<b>from</b>* your userid@apache.org email. &nbsp; Emails sent *<b>to</b>* any apache.org email address will not affected by this.&nbsp;</p> 
  <p> </p> 
  <p>[1] - <a href="http://en.wikipedia.org/wiki/Sender_Policy_Framework" title="http://en.wikipedia.org/wiki/Sender_Policy_Framework">http://en.wikipedia.org/wiki/Sender_Policy_Framework</a></p> 
  <p>[2] - <a href="https://reference.apache.org/committer/email#sendingemailfromyourapacheorgemailaddress" title="https://reference.apache.org/committer/email#sendingemailfromyourapacheorgemailaddress">https://reference.apache.org/committer/email#sendingemailfromyourapacheorgemailaddress</a> </p>
