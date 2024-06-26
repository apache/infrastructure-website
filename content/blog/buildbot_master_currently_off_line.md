title: Buildbot master currently off-line
date: '2015-06-29T21:17:45+00:00'
permalink: buildbot_master_currently_off_line
layout: post

<p><b>Update (2015-06-30 ~12.00 UTC):</b></p> 
  <p>The replacement buildbot master is now live. The CMS service and the <a href="http://ci.apache.org">ci.apache.org</a>&nbsp; website have been restored. The project CI builds are mostly working but builds that upload docs, snapshots etc. to the buildmaster for publishing are likely to fail at the upload stage while we ensure all the necessary directory structures are in place to receive the uploads. Work to resolve these final few issues is ongoing.<br /></p> 
  <p>We continue to try and contact the owner of the account where the IRC proxy was running. In case their account has been compromised, it remains locked. In addition, all their commits have been reviewed by other project committers and that review has confirmed that no malicious commits have been made by the account in question.</p> 
  <p>The review of <a href="http://aegis.apache.org">aegis.apache.org</a>&nbsp; is ongoing. No evidence of compromise beyond the possible compromise of the single, non-privileged user account has been found.<br /></p> 
  <p><b>Original post (2015-06-29 ~21.00 UTC):</b></p> 
  <p>As per the e-mails to committers@ earlier today, <a href="http://aegis.apache.org">aegis.apache.org</a> is currently offline after a report was received that suspicious network traffic had been observed from that host. This blog post will be updated as more information becomes known.</p> 
  <p><b>What we know:</b></p> 
  <ul> 
    <li>At ~16.00 UTC 28 June 2015 a report of suspicious network activity from a buildbot host was reported to the Apache security team.</li> 
    <li>Further information was requested and at ~18.00 UTC 28 June 2015 the Apache Infrastructure team received a copy of network logs that showed a number of suspicious IRC connections originating from aegis.apache.org</li> 
    <li>These IRC connections were traced to a non-privileged user account on <a href="http://aegis.apache.org">aegis.apache.org</a>&nbsp; running an open IRC proxy</li> 
    <li>At ~20.00 UTC 28 June 2015 the user account concerned was locked for all ASF services and the proxy process terminated.</li> 
    <li>At ~10.00 UTC 29 June 2015, after further discussion within the infrastructure team, aegis.apache.org was taken off-line as a precaution.</li> 
  </ul> 
  <p>It remains unclear whether the open IRC proxy was installed by the user that owned the account or whether their account was compromised and the IRC proxy was installed by an unauthorized user. <br /></p> 
  <p>It is worth stressing that no further information came to light between 20.00 UTC 28 June 2015 and 10.00 UTC 29 June 2015 that triggered the decision to take the host off-line. The host was taken off-line purely as a precaution while we reviewed the available information. That process is ongoing. So far we have found no evidence to even suggest anything more than a user account being used to run an IRC proxy and plenty of evidence that suggests that this was the only activity this account was used for.<br /></p> 
  <p><b>Risks:</b></p> 
  <p>There is no risk to released source or binaries for any ASF project. There are multiple reasons for this:</p> 
  <ul> 
    <li>buildbot is a CI system used to build snapshots, not releases</li> 
    <li>no builds are performed on <a href="http://aegis.apache.org">aegis.apache.org</a></li> 
  </ul> 
  <p>Buildbot is used to build some project web sites and / or project documentation. The risk of compromise here is viewed as very low for the following reasons:</p> 
  <ul> 
    <li>the builds do not take place on aegis.apache.org</li> 
    <li>diffs of every change are sent to the relevant project team's mailing list for review and an unexpected / malicious change would be spotted</li> 
  </ul> 
  <p><b>Project impact:</b></p> 
  <p> The following services are currently off-line and will remain so until the buildbot master is restored</p> 
  <ul> 
    <li>All buildbot builds</li> 
    <li>Projects that use the CMS will be unable to update their web sites (the CMS uses buildbot to build web site updates)<br /></li> 
    <li>the <a href="http://ci.apache.org">ci.apache.org</a>&nbsp; website<br /></li> 
  </ul> 
  <p><b>Work in progress:</b></p> 
  <p>Analyzing <a href="http://aegis.apache.org">aegis.apache.org</a>&nbsp; is going to take time and, while we view the chances of a wider compromise of this host as very, very small, we are not willing to bring the host back on line at this point. This host was due for replacement so the decision has been taken to pull this work forward and rebuild the buildbot master on a new host now. We have taken this decision not because we believe <a href="http://aegis.apache.org">aegis.apache.org</a>&nbsp; to be compromised, but because it is possible to complete this work far more quickly than it is possible to confirm our view that <a href="http://aegis.apache.org">aegis.apache.org is not compromised.</a>&nbsp; We currently estimate that the rebuild of the new buildbot master host will be completed by 1 July 2015.<br /></p> 
  <p>We continue to analyze the information we have obtained from <a href="http://aegis.apache.org">aegis.apache.org</a>&nbsp; and from other sources and will update this blog post as more information becomes available.</p> 
  <p><b>Questions:</b></p> 
  <p>Questions, concerns, comments etc. should be directed to infrastructure@apache.org <br /></p>
