
layout: post
title: New monitoring system: nagios is dead long live circonus
date: '2014-05-23T22:29:12+00:00'
permalink: new_monitoring_system_nagios_is

<p>23 may 2014 the old monitoring system &quot;nagios&quot; was put to sleep, and &quot;circonus&quot; was given production status.</p> 
  <p>The new monitoring system is sponsored by circonus and most of the monitoring as well as the central database runs on <a href="www.circonus.com" target="_blank">www.circonus.com</a>. The infrastructure team have built and deployed logic around the standard circonus system:<br />
- A private broker, to monitor internal services&nbsp; without exposing them on internet<br /> - A dedicated broker (inhouse development) that monitor special ASF systems (like svn compare US - EU)<br />
- A configuration system, that are based on svn.<br />
- A new status page <a target="_blank" href="status.apache.org">status.apache.org</a> <br />
- A new team structure (all committers with sudo karma on a vm, get an email when something happens with the vm)<br /> </p> 
  <p> </p> 
  <p>The new system is a lot faster and we can therefore offer projects monitoring of project URLs, of course the project also need to have a team that handles the alerts.</p> 
  <p>The current version has approx. the same facilities as Nagios, but we are planning (and actively programming) a version.2 that will allow us to better predict problems before they occur.</p> 
  <p>Some of the upcoming features are:<br />
- disk monitoring<br />
- vital data statistic from core system (like size of mail queues)</p> 
  <p>The change of monitoring system is a vital component in our transition to automate services and thereby enable infra to more effectively secure the stability of the infrastructure as well as make early detection of potential problems.</p> 
  <p>The system was presented in Apachecon denver 2014, slides can be found&nbsp; <a href="http://people.apache.org/~jani/circonus.pdf">here</a>. We hope to present the live version at apachecon budapest 2014.</p> 
  <p>On behalf of the infrastructure team</p> 
  <p> jan I.<br /></p> 
  <p> </p> 
  <p><br /></p> 
  <p> </p> 
  <p><br /></p>
