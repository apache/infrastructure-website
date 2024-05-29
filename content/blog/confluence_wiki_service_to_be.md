title: Confluence Wiki service to be restarted
date: '2015-06-10T08:32:13+00:00'
permalink: confluence_wiki_service_to_be
layout: post

Hi All,<br /><br />There will be a planned reboot of Confluence on Friday 12th June at 18:00 UTC+1<br /><br />This is a blog post notice as recommended in our Core Services planned downtime SLA.<br /><br />The Confluence wiki service configuration is stored in our Puppet configuration.<br /><br />We have made some modifications to the Puppet Manifest affecting the Module that<br />Confluence uses (cwiki_asf). Some code is being moved out from the module and <br />into a host specific YAML file. This will make it easier for future hosts to reuse the <br />module (such as an upgrade host currently awaiting these changes.)<br />A twitter notification will be posted 1 hour before.<br />A planned maintenance notice will be posted on status.apache.org.<br /><br />If necessary we will make use this outage window to apply any OS updates and reboot <br />the host VM.<br /><br />Actual downtime should be no more than 1 hour all being well.<br /><br />An email about this will be sent to infrastructure@ after the service has resumed from the planned downtime.
