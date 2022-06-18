Title: Mailing List Migration Project

<h3 id="migration">Hermes &#x2192 Mailgw</h3>
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
<h4>What are hermes and mailgw, and why are we migrating?</h4>
<p>
Hermes and mailgw are hostnames for the servers that process mail to
@apache.org email addresses. They also process mailing list traffic
for all ASF projects, e.g. "users@httpd.apache.org".
<p>
Hermes is a nearly 10 year old legacy server that pre-dates Infra's modern 
configuration management strategy, and pre-dates many modern email 
technologies like TLS encryption.
<p>
Mailgw is a modern server using currently available technology, and
under full configuration management, greatly improving reliability and
reproducibility of the service in case of failures.
<p>
The migration process moves @apache.org and @$project.apache.org email 
services from hermes onto mailgw, ensuring that email services remain 
compliant with modern standards to the greatest extent possible.
<p>
<h4>Will we lose any email?</h4>
<p>
No. Despite a list being migrated from hermes to mailgw, mail which was 
'in flight' to hermes will still be delivered to the list subscribers on 
hermes. Once the list is fully migrated, we will reroute email to mailgw 
automatically. This process is transparent to users.
<p>
<h4>Will this affect official archives?</h4>
<p>
No. We manage archives through mailing list subscriptions to the PonEE 
archival service and list subscriptions to the mbox-vm archiver. Mail
delivered via either hermes or mailgw will make it to the official archives.
<p>
<h4>What about unofficial mbox archives?</h4>
<p>
hermes-based ~apmail/lists/project.a.o/archives acessible via ezmlm's 
archive commands (get/index/thread/etc) will not be transferred to mailgw. 
They will be archived for posterity and we can provide them upon 
Member request. Access all mailing list archives via the 
official URL <a href="https://lists.apache.org">https://lists.apache.org</a>.
<p>
<h4>Will the system preserve queued moderation mail?</h4>
<p>
Yes.
<p>
<h4>Will the system preserve settings and subscribers/mods?</h4>
<p>
Yes.
<p>
<h4>What do I do if there is a problem?</h4>
<p>
Email users@infra.apache.org or open an Infra Jira ticket.
<p>
### APMAIL Volunteer Specific Information

#### Will apmail volunteers be able to access the new server?

Yes, apmail access will be re-granted upon request. Ask Infra if you
wish to continue as an apmail volunteer, and we will add you to the new
server.

#### What is the actual hostname of the new server?

mailgw-he-de.apache.org

#### How do we know if a list has been migrated?

The list will exist on mailgw-he-de.apache.org, and the list directory 
on hermes will contain a flag file called 'migrated-to-mailgw'.

#### Do apmail processes remain the same?

For the most part, tools in ~apmail/bin will perform as expected, and 
ezmlm commands (subscriptions, moderation, etc.,) work as expected. 
Contact Infra if anything doesn't work.


