title: The ASF CMS
date: '2010-12-02T04:25:43+00:00'
permalink: the_asf_cms
layout: post

<hr/>
**Note**: Projects and the ASF itself used the Apache Content Management System from 2010 to 2021. It is no longer available.

Links to suggestions for setting up a project website, and website guidelines, are available under "PMC resources" in the <a href="https://infra.apache.org/doc.html" target="_blank">general Infrastructure documentation page</a>.
<hr/>
<p>
Over the past 3 months, the Infrastructure Team has developed and deployed a custom CMS for Apache projects to use to manage their websites.  There is a  <a href="http://www.apache.org/dev/cms.html">document</a> available which explains the rationale, role, and future plans for the CMS.  We have opened up the ACLs for the <a href="http://www.apache.org/">www.apache.org</a> site for all committers to now be able to edit content on the site using the cms (while still restricting live publication to the Apache membership and the Infrastructure Team).
</p>
<p>
The basic workflow for committers is easy to describe:  first install the <a href="https://cms.apache.org/#bookmark">JavaScript bookmarklet</a> on your browser toolbar.  Next visit a webpage on the <a href="http://www.apache.org/">www.apache.org</a> website.  When you've located a page you'd like
to edit, click on the installed bookmarklet: you'll be taken to a working copy of the markdown source for the page in question.  To edit the content click
on the [Edit] link.  A markdown editor will show you a preview of your changes while you work.  When you have finished, submit your changes and [Commit] them.
</p>
<p>
Your commit will trigger <a href="http://ci.apache.org/#buildbot">buildbot</a> to build a staging version of your changes.  You can follow the build while it is ongoing, and once it has completed you can click on the [Staged] link to see the results.  Members and Infrastructure Team members can continue on and publish those changes once they are satisfied with them.  Other committers may need to send a note to the site-dev@ mailing list to request publication of their changes.
</p>
<p>
The publication links in the CMS are essentially merge + commit operations in subversion which are tied into the live site via svnpubsub.  That means
publishing in the CMS is virtually instantaneous.
</p>
<p>
The CMS is now open to all top-level and incubating projects.  Interested projects should contact the infrastructure@ mailing list or simply file an <a href="https://issues.apache.org/jira/browse/INFRA">INFRA</a> ticket against the CMS component.  Early adopters are encouraged to collaborate on
the <a href="http://wiki.apache.org/general/ApacheCms2010">wiki page</a> for working out usage and adoption issues.
</p>
