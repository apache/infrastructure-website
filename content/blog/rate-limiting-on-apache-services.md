
layout: post
Title: Rate-limiting on Apache services
date: '2019-01-27T18:20:54+00:00'
permalink: rate-limiting-on-apache-services

<p>Over the past few days we have implemented rate limiting on selected services across the ASF.</p> 
  <p>As our foundation grows, so do the number of users and robots utilizing our services. In order to accommodate as many as possible with what resources we have, we have opted to implement rate-limiting to ensure that everyone can get their fair share of use of our services across the globe. The first services to have rate-limiting implemented are:</p> 
  <ul> 
    <li>JIRA (issues.apache.org)</li> 
    <li>MoinMoin Wiki (wiki.apache.org)</li> 
    <li>BugZilla (bz.apache.org)</li> 
  </ul> 
  <div><br /></div> 
  <h3>If you are a normal user of our services:</h3>This very likely will never affect you, and you can go about your business just like normal :) If you DO experience errors or 429 (rate limited) response codes, please do let us know.<br /><br /> 
  <h3>If you are a robot or otherwise automated tool:</h3> 
  <p>There are now limits in place for how much CPU time you can use, varying from service to service. If you get limited, you will receive a HTTP 429 response instead of the normal 200, and a short text blob will explain that you have crossed our resource limits and have been rate-limited. It will also explain why, and when you can expect to be unblocked again (generally within two minutes time). Scrapers, bots etc using our services should check for a 429 response code and act accordingly (or just slow down the discovery pace in general, as that benefits all of us).</p> 
  <p> </p> 
  <h3>A general note about the rate limiting system, now and in the future:<br /></h3> 
  <p>Rate limits are applied across IP blocks to discourage distributed abuse, thus if you have 1.2.3.4 abusing a service, 1.2.3.5 would potentially also be affected by the rate limits till they expire.</p> 
  <p>Later this year, we will be rolling out rate limits on more services, and we encourage people automating tasks to honor the 429 responses across all ASF services.</p> 
  <p>We would also like to point out that there are, as before, additional global limits in place regarding the use of our services, which can be found at: <a href="http://www.apache.org/dev/infra-ban.html">https://www.apache.org/dev/infra-ban.html</a> <br /></p>
