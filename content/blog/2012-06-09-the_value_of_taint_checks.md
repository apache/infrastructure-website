
layout: post
title: The value of taint checks in CGI scripts
date: '2012-06-09T21:45:27+00:00'
permalink: the_value_of_taint_checks

<p>Consider the following snippet taken from a live CGI script running on the host that serves www.apache.org:</p> 
  <pre>#!/usr/bin/perl

use strict;
use warnings;

print "Content-Type: text/html\n\n";
my $artifact = "/apache-tomee/1.0.1-SNAPSHOT/";
$artifact = $ENV{PATH_INFO} if $ENV{PATH_INFO};

$artifact = "/$artifact/";
$artifact =~ s,/+,/,g;
$artifact =~ s,[^a-zA-Z.[0-9]-],,g;
$artifact =~ s,\.\./,,g;

my $content = `wget -q -O - http://repository.apache.org/snapshots/org/apache/openejb$artifact`;
... 
</pre> 
  <p> </p><hr width="100%" size="2" /> 
  <p> </p> 
  <p>Looks pretty good right?&nbsp; Any questionable characters are removed from $artifact before exposing it to the shell via backticks... hmm, well turns out that's not so easy to determine.</p> 
  <p>The first warning sign that was given to the author of this script was that he hadn't enabled taint checks- if he had this is how things probably would have looked:</p> 
  <pre>#!/usr/bin/perl -T

use strict;
use warnings;

print "Content-Type: text/html\n\n";
my $artifact = "/apache-tomee/1.0.1-SNAPSHOT/";
$artifact = $ENV{PATH_INFO} if $ENV{PATH_INFO};

$artifact = "/$artifact/";
$artifact =~ s,/+,/,g;
$artifact =~ m,^([a-zA-Z.[0-9]-]*)$, or die "Detainting regexp failed!";
$artifact = $1;
$artifact =~ s,\.\./,,g;

my $content = `wget -q -O - http://repository.apache.org/snapshots/org/apache/openejb$artifact`;
... </pre><hr width="100%" size="2" /> 
  <p>Which doesn't look like much of a change, but the impact on the actual logic is massive: we've gone from a substitution that strips unwanted chars to a fully-anchored pattern that matches only a string full of wanted chars only, and dies on pattern match failure.&nbsp; Sadly the developer in question did not heed this early advice.<br /></p> 
  <p>As it turns out, there is a bug (well several) in the core pattern that renders the original substitution ineffective.&nbsp; However the impact on the taint-checked version causes the detainting match to fail and renders the script harmless!&nbsp; The practical difference is that instead of a script with a working remote shell exploit, we have script that serves no useful purpose.&nbsp; To the Apache sysadmins this is a superior outcome, even though to the developer the original, essentially working script is preferable- worlds are colliding here, but guess who wins?<br /></p> 
  <p>At the ASF the sysadmins almost invariably refuse to run perl or ruby CGI scripts without taint-checking enabled, and will always prefer CGI scripts be written in languages that support taint checks as they tend to enforce good practice in dealing with untrusted input.&nbsp; This example, which is in fact one of the first times we've even considered allowing Apache devs to deploy non-download CGI scripts on the <a href="http://www.apache.org">www.apache.org</a>&nbsp; server, serves as a useful reminder to Apache devs as to why using languages that support taint checks is an essential component of scripting on the web.</p> 
  <p><br /></p> 
  <p><br /></p>
