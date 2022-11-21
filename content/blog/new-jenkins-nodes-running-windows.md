
layout: post
title: New Jenkins Nodes running Windows
date: '2019-11-21'
permalink: new-jenkins-nodes-running-windows

This afternoon, I rolled out two new Shared Jenkins Nodes, jenkins-win-azr-7 and 8. They are both in rotation, using the labels Windows and Windows-Docker. The second label was put in place as the older nodes can't run Docker Desktop. I've also tried setting these up by cloning disks instead of from the ground up.
Feel free to test them out, all the usual tools are in place (as well as Docker). 
