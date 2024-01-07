
layout: post
title: SVN performance enhancements
date: '2010-02-17T00:41:04+00:00'
permalink: svn_performance_enhancements

<p>Tonight we enabled a pair of Intel X25-M's to serve as <a href="http://blogs.sun.com/brendan/entry/test">l2arc cache</a> for the zfs array which contains all of our svn repositories.&nbsp; Over the next few hours as these SSD's start serving files from cache, the responsiveness and overall performance of svn on eris (our master US-based server) should be noticeably better than it has been lately.</p><p>In addition we are planning to install 16GB of extra RAM into eris to improve zfs performance even further, but for now we are hopeful that committers will appreciate the performance we've added tonight.</p><p><br />&nbsp;</p>
