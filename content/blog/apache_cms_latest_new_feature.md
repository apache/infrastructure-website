title: Apache CMS: latest new feature is SPEED!
date: '2012-02-26T02:23:56+00:00'
permalink: apache_cms_latest_new_feature
layout: post

<hr/>
**Note**: Projects and the ASF itself used the Apache Content Management System from 2010 to 2021. It is no longer available.

Links to suggestions for setting up a project website, and website guidelines, are available under "PMC resources" in the general <a href="https://infra.apache.org/doc.html" target="_blank">Infrastructure documentation page</a>.
<hr/>
<p>Over the past few months the&nbsp;<a href="http://www.apache.org/dev/cms">Apache CMS</a> has seen lots of new improvements, all under the general theme of making the system more performant.&nbsp; Supporting very large sites like the <a href="http://www.openoffice.org/">Apache OpenOffice User Site</a> with almost 10 GB of content has presented new challenges, met largely with the introduction of zfs clones for generating per-user server-side working copies, changing what was an O(N) rsync job to an O(1) operation.&nbsp; We've also moved the update processing out-of-band to further cut down on the time it takes for the bookmarklet to produce a page, eliminating all O(N) algorithms from the process.</p> 
  <p>&nbsp;More recent work focuses on the merge-based publication process, which for large changesets took a considerable amount of time to process.&nbsp; That too has been recoded based on svnmucc and is now another O(1) operation- essentially a perfect copy of staging with a few adjustments for &quot;external&quot; paths.</p> 
  <p>Combine that with the activity around parallelizing the build system and you have a completely different performance profile compared to the way the system worked in 2011.&nbsp; In short, if you haven't tried the CMS lately, and were a bit offput by the page rendering times or build speeds, have another look! <br /></p> 
  <p> </p> 
  <p>Next up: describing the work done around external build support, focusing first on maven based sites.<br /></p> 
  <p><br /></p>
