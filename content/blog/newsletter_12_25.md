title: Inside Infra December 2025 
date: '2025-12-30' 
permalink: newsletter1224 layout: post

**Welcome to Inside Infra for December, 2025**

The December **roundtable** was about the massive DDOS (distributed denial of service) attack the ASF experienced starting November 10. There was a massive increase in access attempts to Jira, Confluence and other services. For example, The ASF's Jira instance normally has 1000 connections open at a given time. On November 11 there were more than 100,000 connections. The attacks were different from the scraping attacks we experience, in which perhaps there are 2000 nodes trying to scrape all the ASF email. In this case, almost all the nodes just attempted to gain access and then...sat there, holding the connection open.

Infra had to create a bunch of tools to augment the existing blocking processes and to improving analysis of attacks on ASF machines. It will probably be necessary to create a wrapper around our firewall, because the level of the firewall's activity itself was causing our system to overload.

The full discussion is available at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2025-12-03+1800+UTC" target="_blank">Infra Roundtable 2025-12-03 1800 UTC</a>

The next Roundtable will be **Wednesday, February 4, 2026, 1800 UTC**. Jarek Potiuk will be presenting on the **software dependency tracker** he developed, and on **using AI in code development**.



More next year!
