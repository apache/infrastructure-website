Title: Apache Infrastructure Mailing List Migration Project

<h2 id="migration">Mailing List Migration</h2>

As part of the Apache Infrastructure team's goals of modernization and
service improvement, we are pleased to announce the general availability
of "mailgw", the long-awaited replacement for hermes.

This document addresses common questions related to the migration of mail 
and mailing lists to the new server.

<h2 id="faq">Frequently Asked Questions</h2>

Will any mail be lost?
No. Despite being migrated to mailgw from hermes, mail which was 'in flight' 
to hermes will still be delivered to the list on hermes. Once fully migrated, 
email will be routed to mailgw automatically.

Will official archives be affected?
No. Archival is managed through subscriptions to the PonEE archival service 
as well as the mbox-vm archiver.

What about unofficial (hermes-based ~/lists/project.a.o/archives) archives?
These will not be transferred to mailgw in-situ. They will be archived for 
posterity and can be made available upon request.

Will queued moderation mails be preserved?
Yes
