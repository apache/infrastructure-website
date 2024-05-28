title: MoinMoin Service - User Account Tidy Up
date: '2014-11-21T12:17:17+00:00'
permalink: moinmoin_service_user_account_tidy
layout: post

<hr/>
**Note**: We no longer use the MoinMoin service. Projects can create a wiki in the <a href="https://infra.apache.org/cwiki.html" target="_blank">ASF Confluence Wiki</a>.
<hr/>
<p>In recent months we have become increasingly aware of a slowing down of our MoinMoin wiki service. &nbsp;We have attributed this, at least in part, due to the way MoinMoin stores some data about user accounts. &nbsp;</p>
  <p>Across all of our wiki instances (in the farm) we had a little over 1.08 million distinct user accounts. &nbsp;Many of which have never been used (spam etc). &nbsp;So we have decided to archive all users who have not accessed any of the wiki sites they were registered for in more than 128 days. &nbsp;</p>
  <p>This has resulted in us being able to archive a little over 800k users. &nbsp;This leaves us with around 200k users across 77 wikis. This still feels very high, and in the coming weeks we will investigate further still in how we can better understand if those remaining accounts are making valid changes, or are they just link farm home pages.</p>
  <p>If you think your account was affected by this, and you would like to have your account restored, then please contact the Infra team using this page&nbsp;<a href="http://www.apache.org/dev/infra-contact">http://www.apache.org/dev/infra-contact</a> <br /><br /><br />Thanks,<br />ASF Infra Team<br /><br /></p>
