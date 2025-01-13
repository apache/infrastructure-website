title: s.apache.org - uri shortening service
date: '2010-06-11T17:17:46+00:00'
permalink: s_apache_org_uri_shortening
layout: post

<p>
Today we've brought <a href="http://s.apache.org/">s.apache.org</a> online.  It's a url shortening service that's limited to Apache committers- the people who write all that Apache software!   One of the main reasons we're providing this service is to allow committers to use shortened links whose provenance is known to be a trusted source, which is a big improvement over the generic shorteners out there in the wild.  It is also meant to provide permanent links suitable for inclusion in board reports, or more generally email sent to our mailing lists - which will be archived, either publicly or privately, for as long as Apache is around.
</p> 
  <p>
The service is easy to use, and being from Apache the <a href="http://s.apache.org?action=source">source code</a> for the service is readily available.    The primary author of the code is Ulrich Stärk (uli).  Some of the more interesting features you can pick up from the source is the ability to &quot;display&quot; a link before doing a redirect by tacking on &quot;?action=display&quot; to any shortened url. For the truly paranoid there is the &quot;?action=display;cookie=1&quot; query string to force <strong>all</strong> shortened urls to display by default before redirecting. That feature may be turned off again with the &quot;?action=display;cookie=&quot; query string.  Again, look over the source code for other interesting features you may wish to take advantage of.
</p> 
  <p>Committers: here's some JavaScript you might consider placing in a bookmark, courtesy of Doug Cutting. To use create a new bookmark and set the link url to</p> 
  <blockquote style="margin: 0px 0px 0px 40px; border: none; padding: 0px;"><code>javascript:void(location.href='https://s.apache.org/?action=create&amp;search=ON&amp;uri='+escape(location.href)) </code></blockquote>
