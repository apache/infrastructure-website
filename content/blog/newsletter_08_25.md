title: Inside Infra August 2025 
date: '2025-08-26' 
permalink: newsletter0825
layout: post 

## Welcome to *Inside Infra* for August, 2025

### Roundtable

The August Roundtable discussed the impact of **AI scraping** on The ASF, and what responses to it might be useful. 

The main impacts on ASF infrastructure are:

  - Overuse of resources - effectively, distributed denial of service
  - Increased downtime
  - Valid requestors unable to reach resources
  - Alerts at all hours of the day and night for limited staff
  - Possible legal exposure relative to PII being scraped

The full summary, including many helpful comments and suggestions, is at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2025-08-06+1700+UTC" target="_blank">Infra Roundtable 2025-08-06 1700 UTC</a>

The September roundtable will be a **face-to face event on September 14** at <a href="https://communityovercode.org/" target="_blank">**Community Over Code**</a>, the ASF conference in Minneapolis, Minnesota, USA. The entire Infra and Tooling team track is on the 14th, the last day of the event; and if you are attending, we hope you can join us.

Information about how to take part in the online roundtables is at <a href="https://infra.apache.org/roundtable.html" target="_blank">infra.apache.org/roundtable.html</a>.

### DKIM

As part of our ongoing efforts to improve mail deliverability and align with modern email authentication standards, Infra enabled DKIM (DomainKeys Identified Mail) signing for all personal (non-list) email sent via mail-relay.apache.org. An explanation of DKIM is at <a href="https://www.mimecast.com/content/dkim/" target="_blank">mimecast.com/content/dkim/</a>.

This means that when committers send individual emails via the ASF relay using their @apache.org addresses, those messages will now include a DKIM signature. This change helps ensure delivery to domains that are increasingly rejecting unsigned mail, such as Outlook.com and other major providers.

**Please note**: Mailing list messages remain unchanged. Outgoing email sent through ASF mailing lists will not be DKIM signed at this time. Individual mail signing is an incremental step, and Infra is evaluating future options for signing list traffic in a way that preserves functionality and compatibility. This change should improve deliverability for many of you using @apache.org addresses in day-to-day correspondence, particularly when reaching users on stricter mail platforms.

If you have questions or encounter any issues, feel free to reach out to `users@infra.apache.org`.

### New Infra staffer

**Ricardo Anguiano** joined the ASF Infra team on August 5, 2025.

Ricardo is a curious technology professional. He started his career at CodeSourcery, an open source software development services company, where he focused on IT and Python-based tool maintenance. He spent his career so far collaborating with globally distributed teams in technical marketing and application engineering roles (Mentor Graphics), and sales and marketing roles (Odaseva, Cognition Factory). He has far more rss feeds than he can keep up with, an abundance of open wikipedia tabs, and engages in recreational system administration.
His non-nerdy pursuits include growing tomatoes, hiking, cycling and visiting friends and family. He is based in the Sacramento, California area in the United States.

_What attracted you to the ASF and to this ASF Infra job?_

"It boils down to alignment, interest, ability, curiosity and familiarity. I’ve been a fan of open-source software environments and methods for a long time. The mission of The Apache Software Foundation and what the Foundation enables is very appealing to me.

"I’ve never really stopped doing the IT sorts of things that I started my career on. These are the things that I call recreational system administration: Purchase a domain; set up DNS, mail, web, etc.; write small, useful utilities for myself to solve some problem or automate something.

"After some time away from professional IT and professional software development, I was curious to see the state of things now. The distributed, collaborative, and technical environment within ASF Infra has a lot in common with jobs I had early in my career, and I’ve sought to replicate elements of that environment repeatedly, where I could, in later roles."


**More next month!**
