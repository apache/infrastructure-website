
layout: post
title: Infrastructure Team Adopting an On-Call Rotation
date: '2014-08-18T13:00:00+00:00'
permalink: infrastructure_team_adopting_an_on

<p>As the Apache Software Foundation (ASF) has grown, the infrastructure required to support its diverse set of projects has grown as well. To care for the infrastructure that the ASF depends on, the foundation has hired several contractors to supplement the dedicated cadre of volunteers who help maintain the ASFs hardware and services. To best utilize the time of our paid contractors and volunteers, the Infrastructure team will be adopting an on-call rotation to meet requests and resolve outages in a timely fashion.&nbsp;</p> 
  <h3>Why We're Establishing an On-Call Rotation
</h3> 
  <p>
In groups, especially groups that are charged with overlapping duties, there's occasionally a sense of <a href="http://en.wikipedia.org/wiki/Diffusion_of_responsibility" target="_blank">diffusion of responsibility</a>. There tends to be a good number of tasks or incidents that routinely occur that need a clear owner. We've also tried to set expectations around our service levels relative to the importance of a service. In example, a new mailing list can be set up as convenient, but a failing mail service needs to be addressed immediately.

</p> 
  <p>The technical side of this has been that we have historically alerted via email and/or SMS about any urgent issues that came up. Of course those alerts went to everyone on the team. If the alert occurs at an inconvenient time, either everyone responds, which is likely wasteful, or no one responds thinking someone else will.

</p> 
  <p>At the Infrastructure team's face to face meeting in July we decided we'd adopt an on-call rotation for the contractors so that everyone wasn't responsible for everything all of the time.  We then went looking for something to let us sanely (and without building it ourselves) deal with that. </p> 
  <p>

We ended up choosing <a href="https://pagerduty.com" target="_blank">PagerDuty</a>, which has a number of ways of receiving alerts. More importantly, it allows us to set a schedule, easily override it for holidays or illnesses, and do so programmatically. It also seamlessly integrates with <a href="https://hipchat.com">HipChat</a>, which Infrastructure is running a trial of and communicates with our mobile devices. </p> 
  <p>

PagerDuty also supports a clear escalation path that begins alerting other people about issues if the person on-call fails to respond in a timely manner. Additionally, PagerDuty's mobile apps are built with <a href="https://cordova.apache.org">Apache Cordova</a>, which is an interesting circle. We've finished our trial and decided to adopt PagerDuty. PagerDuty&nbsp;was especially gracious and made our account gratis.

</p> 
  <p>Adopting an on-call rotation will allow us to provide a better service and response time, while also clearly setting expectations around contractor availability so they can relax on their off weeks. </p> 
  <p>

If you have questions or want to get involved, feel free to join us on the infrastructure mailing list infrastructure@apache.org or joining us in our <a href="http://www.hipchat.com/gw4Cfp7JY" target="_blank">Hipchat room</a>. 
</p>
