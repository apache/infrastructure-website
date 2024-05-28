title: ASF JIRA Outages and Troubleshooting
date: '2016-06-30T16:25:30+00:00'
permalink: continued_outages_for_the_asf
layout: post

<p>As people have noticed, our JIRA instance (arguably the largest public instance in the world) has been suffering from a yet unknown issue as of late.&nbsp;We are reasonably sure that this is related to specific queries being made against the instance (possibly automated queries from scrapers), but have yet to identify the exact cause of the problem.</p> 
  <p>The failure condition arises when the database connection pool is exhausted, despite being configured and sized appropriately. These connections all appear idle, but when the pool is full, no new connections can be established, and the instance falls over, requiring a restart.&nbsp;</p> 
  <p>We are working closely with Atlassian, the creator of JIRA, to remedy the situation. Unfortunately, this requires running diagnostics on the production JIRA instance, which in and of itself causes performance degradation and downtime. Over the past several days, we've identified and implemented some changes to the pool parameters which we hope will help stabilize the instance while we continue our diagnostic work.</p> 
  <p>We expect that there may still be some moments of downtime and occasional restarts. Any longer duration outages will be announced via Twitter/infrabot and status.apache.org.</p>
