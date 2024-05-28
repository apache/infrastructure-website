
layout: post
Title: Scaling down the CMS to modest but intricate websites
date: '2014-03-25T18:23:50+00:00'
permalink: scaling_down_the_cms_to

<hr/>
**Note**: Projects and the ASF itself used the Apache Content Management System from 2010 to 2021. It is no longer available.

Links to suggestions for setting up a project website, and website guidelines, are available under "PMC resources" in the general <a href="https://infra.apache.org/doc.html" target="_blank">Infrastructure documentation page</a>.
<hr/>

<p>The original focus of the CMS was to provide the tools necessary for handling <a href="http://www.apache.org/">http://www.apache.org/</a>&nbsp;and similar Anakia-based sites. &nbsp;The scope quickly changed when <a href="http://www.openoffice.org/">Apache OpenOffice</a> was accepted into the incubator... handling over 9GB of content well was quite an undertaking and will be soon discussed at Apachecon in Denver during <a href="http://apacheconnorthamerica2014.sched.org/event/041f72d553e8414e68180854cc62dc68#.UzHCItzoaRs">Dave Fisher's talk</a>. &nbsp;From there the build system was extended to allow builds using multiple technologies and programming languages.</p> 
  <p>Since that time in late 2012 the CMS codebase has sat still, but recently we've upped the ante and decided to offer features aimed at parity with other site building technologies like jekyll, nanoc and middleman. &nbsp;You can see some of the new additions to the Apache CMS in action at <a href="http://thrift.apache.org/">http://thrift.apache.org/</a>. The Apache Thrift website was originally written to use nanoc before being ported to the newly improved Apache CMS. They kept the YAML headers for their markdown pages and converted from a custom preprocessing script used for inserting code snippets to using a fully-supported snippet-fetching feature in the Apache CMS.&nbsp;</p> 
  <p>&quot;The new improvements to the Apache CMS allowed us to quickly standardize the build process and guarantee repeatable results as well as integrate direct code snippets into the website from our source repository.&quot;<br />- Jake Farrell, Apache Thrift PMC Chair</p> 
  <p>Check out the Apache Thrift website&nbsp;<a href="http://svn.apache.org/repos/asf/thrift/cms-site/trunk/">cms sources</a> for sample uses of the new features found in <a href="https://svn.apache.org/repos/infra/websites/cms/build/lib/ASF/View.pm">ASF::View</a> and <a href="https://svn.apache.org/repos/infra/websites/cms/build/lib/ASF/Value/Snippet.pm">ASF::Value::Snippet</a>.</p>
