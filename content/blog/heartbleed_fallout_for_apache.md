
layout: post
title: heartbleed fallout for apache
date: '2014-04-11T20:25:44+00:00'
permalink: heartbleed_fallout_for_apache

<p>Remain calm.</p> 
  <p>What we've learned about the heartbleed incident is that it is hard, in the sense of perhaps only viable to a well-funded blackhat operation, to steal a private certificate and key from a vulnerable service. &nbsp;Nevertheless, the central role Apache projects play in the modern software development world require us to mitigate against that circumstance. &nbsp;Given the length of time and exposure window for this bug's existence, we have to assume that some/many Apache passwords may have been compromised, and perhaps even our private wildcard cert and key, so we've taken a few steps as of today:</p> 
  <p> </p> 
  <ol> 
    <li>We fixed the vulnerability in our openssl installations to prevent further damage,</li> 
    <li>We've acquired a new wildcard cert for apache.org that we have rolled out prior to this blog entry,</li> 
    <li>We will require that all committers rotate their LDAP passwords (committers visit <a href="https://id.apache.org/reset/enter">id.apache.org</a> to reset LDAP passwords once they've been forcibly reset),</li> 
    <li>We are encouraging all service administrators to all non-LDAP service like jira to rotate those passwords as well.</li> 
  </ol> 
  <div> 
    <p>Regarding the cert change for svn users- we'd also like to suggest that you remove your existing apache.org certs from your .subversion cache to prevent potential MITM attacks using the old cert. &nbsp;Fortunately it is relatively painless to do this:</p> 
    <p>&nbsp;% grep -l apache.org ~/.subversion/auth/svn.ssl.server/* | xargs rm</p> 
    <p> </p> 
    <p>NOTE: our openoffice wildcard cert was never vulnerable to this issue as it was served from an openssl-1.0.0 host.&nbsp;</p> 
    <p> </p> 
  </div> 
  <p> </p>
