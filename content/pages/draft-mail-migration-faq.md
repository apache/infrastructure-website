Title: Mailing List Migration Project

<h3 id="migration">Hermes -> Mailgw</h3>
<p>
As part of the Apache Infrastructure team's goals of modernization and
service improvement, we are pleased to announce the general availability
of "mailgw", the long-awaited replacement for hermes.
<p>
This document addresses common questions related to the migration of mail 
and mailing lists to the new server.
<p>
<h3 id="faq">Frequently Asked Questions</h3>
<p>
<h4>Will any mail be lost?</h4>
<p>
No. Despite being migrated to mailgw from hermes, mail which was 'in flight' 
to hermes will still be delivered to the list on hermes. Once fully migrated, 
email will be routed to mailgw automatically. This process is transparent to 
users.
<p>
<h4>Will official archives be affected?</h4>
<p>
No. Archival is managed through subscriptions to the PonEE archival service 
as well as the mbox-vm archiver.
<p>
<h4>What about unofficial mbox archives?</h4>
<p>
hermes-based ~/lists/project.a.o/archives acessible via ezmlm's archive 
commands (get/index/thread/etc) will not be transferred to mailgw. 
They will be archived for posterity and can be made available upon 
request. All mailing list archives should be accessed via the official
URL <a href="https://lists.apache.org">https://lists.apache.org</a>
<p>
<h4>Will queued moderation mails be preserved?</h4>
<p>
Yes.
<p>
<h4>What do I do if there is a problem?</h4>
<p>
Email users@infra.apache.org or open an Infra Jira ticket.
<p>
