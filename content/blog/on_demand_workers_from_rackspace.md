
layout: post
title: On-demand workers from Rackspace added to builds.apache.org
date: '2014-09-04T13:00:00+00:00'
permalink: on_demand_slaves_from_rackspace

<div>A couple of weeks ago, Apache's Infrastructure team added a new feature to our Jenkins server, <a href="http://builds.apache.org">builds.apache.org</a> to help deal with the at times overwhelming queues of builds waiting for an executor. While this has been improved dramatically by the increase in workers generously provided by Yahoo! on physical hosts, we're always trying to look forward and be prepared for increased usage in the future.&nbsp;</div> 
  <div><br /></div> 
  <div>To that end, we've set up worker images on Rackspace, generated using the fantastic tool <a href="http://packer.io" target="_blank">Packer</a>. Using the <a href="http://jclouds.apache.org">Apache jclouds</a> <a href="https://wiki.jenkins-ci.org/display/JENKINS/JClouds+Plugin">plugin for Jenkins</a>, Ubuntu workers will be spun up dynamically on Rackspace using those images when there's a queue of pending builds that are able to run on the “ubuntu” label. Up to five of these workers can be running at a time, and they're automatically removed from Jenkins and destroyed on Rackspace once they've been idle a set period of time. This burst capacity will help us prevent a long wait for builds to run on <a href="http://builds.apache.org">builds.apache.org</a>.</div> 
  <div><br /></div> 
  <div>We're able to do this thanks to Rackspace generously donating resources to the Apache Software Foundation. We're extremely grateful for this, and if any other public cloud providers are also interested in donating compute cycles to the Foundation, please contact the Infrastructure team.</div> 
  <div><br /></div> 
  <div>One thing to note - the worker image we're using is still new and may have bugs in it. If you see your build suddenly failing for mysterious reasons, please take a look at the worker it ran on - if it's a worker named something like “jenkins-ubuntu-1404-4gb-abc”, please open a BUILDS JIRA at <a href="https://issues.apache.org">issues.apache.org</a> with a link to the failing build and we'll investigate.</div> 
  <div><br /></div> 
  <div>We've got more improvements for <a href="http://builds.apache.org">builds.apache.org</a> planned for the future, and we're looking forward to sharing them with all of you - there'll be a talk at ApacheCon EU this November on the current status of Jenkins at the ASF, what we've done to stabilize and improve the developer experience on <a href="http://builds.apache.org">builds.apache.org</a>&nbsp;this year, and what's planned for the future - hope to see you there!</div>
