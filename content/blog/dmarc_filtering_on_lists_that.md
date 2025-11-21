title: DMARC filtering on lists that munge messages
date: '2014-06-03T21:57:08+00:00'
permalink: dmarc_filtering_on_lists_that
layout: post

<hr/>

**Note**: This page, including the update note, were correct when written, but are now <b>out of date</b>. A description of the situation related to DMARC and DKIM as of November, 2025 is available on this wiki page: <a href="https://cwiki.apache.org/confluence/display/INFRA/DMARC+and+DKIM+for+ASF+mail" target="_blank">cwiki.apache.org/confluence/display/INFRA/DMARC+and+DKIM+for+ASF+mail</a>.

<hr/>

**Note**: The solution described below has been incorporated into ezmlm. However, it creates a new problem, generating double 'Reply-To:' headers in the case of lists with a `reply-to` set to something other than the list name. A complete rewrite of this function is under consideration. You can follow the discussion on Jira ticket <a href="https://issues.apache.org/jira/browse/INFRA-24849" target="_blank">INFRA-24849</a>.
<hr/>

<p>Since Yahoo! switched their DMARC policy in mid-April 2014, we've seen an increase in undeliverable messages sent from our mail server for Yahoo! accounts subscribed to our lists. &nbsp; Roughly half of Apache's mailing lists do some form of message munging, whether it be Subject header prefixes, appended message trailers, or removed mime components. &nbsp;Such actions are incompatible with Y!'s policy for its users, which has meant more bounces and more frustration trying to maintain inclusive discussions with Y! users.</p> 
  <p>Since Y!'s actions are likely just the beginning of a trend towards strong DMARC policies aimed at eliminating forged emails, we've taken the extraordinary step of munging Y! user's From headers to append a spec-compliant .INVALID marker on their address, and dropping the DKIM-Signature: header for such messages. &nbsp;We are an ezmlm shop and maintain a heavily customized .ezmlmrc file, so carrying this action out was relatively straightforward with a 30-line perl header filter prepended to certain lines in the &quot;editor&quot; block of our .ezmlmrc file. &nbsp;The filter does a dynamic lookup of DMARC &quot;p=reject&quot; policies to inform its actions, so we are prepared for future adopters beyond the early ones like Yahoo!, AOL, Facebook, LinkedIn, and Twitter. &nbsp; Interested parties in our solution may visit <a href="http://www.sunstarsys.com/essays/mailing-lists">this page</a> for details and the Apache-licensed code.</p> 
  <p>Of course this filter only applies to half our lists- the remainder that do no munging are perfectly compatible with DMARC rejection policies without modification of our list software or configuration. &nbsp;Apache projects that prefer to avoid munging may file a Jira ticket with infrastructure to ask that their lists be set to &quot;ezmlm-make -+ -TXF&quot; options.</p> 
  <p> </p>
