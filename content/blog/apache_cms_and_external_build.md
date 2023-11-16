
layout: post
title: Apache CMS and external build support
date: '2012-03-10T17:28:05+00:00'
permalink: apache_cms_and_external_build

<hr/>
**Note**: Projects and the ASF itself used the Apache Content Management System from 2010 to 2021. It is no longer available.

Links to suggestions for setting up a project website, and website guidelines, are available under "PMC resources" in the general <a href="https://infra.apache.org/doc.html" target="_blank">Infrastructure documentation page</a>.
<hr/>

<p>Recently we've been working with the maven team to facilitate migration of <a href="http://maven.apache.org">maven.apache.org</a> to the Apache CMS, using maven as the core build system instead of the standard perl build scripts.&nbsp; A mockup has been created at <a href="http://maventest.apache.org/">maventest.apache.org</a>&nbsp; to see how this will work.&nbsp;&nbsp; Once the site is completed, there will be roughly 5GB of data to service, spanning dozens of maven components.&nbsp; Each component will be self-contained and managed externally from the CMS site using a local maven svnpubsub plugin written mainly by Benson Margulies.&nbsp; The CMS will glue all the components together into a single common site using the <a href="http://www.apache.org/dev/cmsref#generated-docs">extpaths.txt</a> file to configure the paths.</p> 
  <p>The doxia subproject requires special treatment as an independent CMS subproject which is also using maven as it's core build system.&nbsp; Special logic was introduced into the CMS to properly redirect subproject links based on maven source tree layouts, and the system has worked seamlessly so far.</p> 
  <p>Other recent news includes the migration of the main <a href="http://incubator.apache.org/">incubator.apache.or</a><a href="http://incubator.apache.org/">g</a> site to the CMS.&nbsp; There the CMS relies on Ant/Anakia to produce site builds instead of the standard perl build scripts, providing an easy migration path for folks accustomed to the old way of building the site.</p> 
  <p>Essentially we've made good on the promise that the CMS is simply CI for websites with an easy way of editing pages within your browser.&nbsp; Support for forrest builds is planned but hasn't been fleshed out with any live examples to date.&nbsp; That would round out the major java site-building technologies currently deployed by Apache projects- volunteers welcome!<br /></p>
