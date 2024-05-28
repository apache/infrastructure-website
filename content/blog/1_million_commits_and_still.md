
layout: post
Title: 1 million commits and still going strong
date: '2010-09-23T11:55:55+00:00'
permalink: 1_million_commits_and_still

<p>Yesterday, the main ASF SVN code repository passed the 1 million commit mark.  Shortly thereafter one of the ASF members enquired as to how he could best grab the SVN log entries for all of these commits.  As always, there were a bunch of useful replies, but they were all set to take quite some time; mainly because if anyone just simply runs</p>

<pre>svn log http://svn.apache.org/repos/asf -r1:1000000 </pre>

<p>It will not only take several hours, it will also cause high levels of load on one of the two geo-balanced SVN servers.  Also, requesting that many log entries will likely result in your IP address being banned.</p>

<p>So I decided to create the log set locally on one of the SVN servers.  This is now available for download  [<a href="http://s.apache.org/1m-svnlog">http://s.apache.org/1m-svnlog</a>]  [<a href ="people.apache.org/~pctony/asf-svnlog-1-1000000.tgz.md5">md5</a>] <br />
This is a 50Mb tar/gz file.  It will uncompress to about 240Mb.   The log 'only' contains the log entries from 1 -> 1,000,000  - if you want the rest you can run:</p>

    <pre>svn log http://svn.apache.org/repos/asf -r1000001:HEAD</pre>

<p>This will give you all the log entries from 1M+1 to current</p>
