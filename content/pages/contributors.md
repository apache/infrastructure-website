Title: Guide for new project contributors

<p>This guide provides tips and suggestions for new <strong>contributors</strong> to Apache projects.
A contributor is anyone who wants to contribute code, documentation, tests, ideas, anything to any project 
hosted here at the Apache Software Foundation (ASF). </p>
<p><strong>Note</strong>: if you are interested in contributing <strong>financially</strong>, please see <a href="https://www.apache.org/foundation/contributing.html" target="_blank">Sponsorship and Donations</a>.</p>
<p>There is a separate <a href="new-committers-guide">New Committer Guide</a> and <a href="committers">FAQ</a>.</p>
<h2 id="links">Contents<a class="headerlink" href="#links" title="Permanent link">&para;</a></h2>
<p><ul>
  <li><a href="#comdev">Community Development is here to help</a></li>
  <li><a href="#mail">Everything happens on mailing lists</a></li>
  <li><a href="#howitworks">How open-source works at Apache</a></li>
  <li><a href="#svnbasics">Source code repositories</a><ul>
     <li><a href="#svn">Using Subversion</a></li>
     <li><a href="#git">Using Git</a></li>
     </ul></li>
  <li><a href="#providingfeedback">Providing feedback to Apache projects</a></i></p>
</ul>

<hr />
<h2 id="comdev">Community Development is here to help!<a class="headerlink" href="#comdev" title="Permanent link">&para;</a></h2>
<p>Apache values "Community over code", and is full of volunteers who want to help you! Guideposts and helpful information and mentors for 
newcomers to Apache can be found in <a href="http://community.apache.org/">Community Development</a>.</p>
<h2 id="mail">Everything happens on mailing lists<a class="headerlink" href="#mail" title="Permanent link">&para;</a></h2>
<p>Virtually everything at Apache happens on one of our publicly archived mailing lists. 
Find the <a href="http://www.apache.org/dev/#mail">right Apache mailing list</a>, and 
read some <a href="http://www.apache.org/dev/contrib-email-tips">tips on asking questions</a>.</p>
<h2 id="howitworks">How open-source works at Apache<a class="headerlink" href="#howitworks" title="Permanent link">&para;</a></h2>
<p>There are many books, presentations, and academic papers about the way open-source software development
works and how you can become a valuable member of the open source/free software community. For an overview of how it works at Apache, see </p>
<ul>
<li>the <a href="http://www.apache.org/">ASF front page</a></li>
<li>the <a href="../foundation/how-it-works.html">ASF How it works</a> document</li>
<li>the <a href="http://jakarta.apache.org/site/understandingopensource.html">Apache Jakarta: Understanding Opensource</a>
document</li>
<li>the <a href="https://www.fsf.org/" target="_blank">FSF website</a></li>
<li>the <a href="https://www.opensource.org/" target="_blank">Open Source Initiative website</a></li>
<li><a href="http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/" target="_blank">The Cathedral and the Bazaar</a></li>
</ul>
<h2 id="svnbasics">Source code repositories<a class="headerlink" href="#svnbasics" title="Permanent link">&para;</a></h2>
<p>Apache projects use either <a href="https://subversion.apache.org" target="_blank">Subversion</a> or <a href="https://infra.apache.org/git.html" target="_blank">Git</a> for their source code repositories.</p>
<h3 id="bleeding-edge">Nightly code / Development code<a class="headerlink" href="#bleeding-edge" title="Permanent link">&para;</a></h3>
<p>Getting the source directly from the source repository usually gives you
the latest, or "bleeding edge" version of that particular project. </p>
<h3 id="svn">Using Subversion<a class="headerlink" href="#svn" title="Permanent link">&para;</a></h3>
<p>In the Subversion repository, there are usually three separate top-level directories:</p>
<ul>
<li>The <code>trunk</code> directory contains the current source code, and thus it's
usually used in the source code access URLs the project provides.</li>
<li>The <code>tags</code> directory contains specific versions of the project that were
tagged with some name. These were created for some specific reason. For
instance, you usually find a tag for each released version of the project.</li>
<li>The <code>branches</code> directory contains versions of the project that are
different in some respect, such as experimental or former released versions.</li>
</ul>
<p>If you are looking to download the source code for <strong>stable</strong> versions
of the ASF projects, you should go to a normal <a href="http://www.apache.org/dyn/closer.cgi/">mirror site</a>
and simply download it from there. Only if you want the bleeding edge source
(from the <code>trunk</code> folder, or if you need an older version for which you don't
get the source code from the mirrors anymore, use the source repository.</p>
<p>Before you start using source code from the source repository, you need to
check out a local copy of the remote repository. Here's how.</p>
<p>Subversion, which is the technology/tool Apache uses to maintain a <a href="https://subversion.apache.org/" target="_blank">source repository</a>. For more details about the Subversion client, the <a href="http://svnbook.red-bean.com" target="_blank">Subversion book</a> is the place to start.</p>
<h4 id="svn-cygwin">Getting SVN source code on Windows with cygwin<a class="headerlink" href="#svn-cygwin" title="Permanent link">&para;</a></h4>
<p><a href="https://www.cygwin.com/ target="_blank">Cygwin</a> is a free software suite of ports of
popular Linux tools and utilities that runs natively on Windows. It includes a port of the svn application for checking out source code from the Apache source repositories. If you use cygwin, please follow the Unix/Linux instructions below.</p>
<h4 id="svn-cli">Getting SVN source code on Windows with the command-line<a class="headerlink" href="#svn-cli" title="Permanent link">&para;</a></h4>
<p>The Subversion utilities are available as native Windows binaries. Get them
from <a href="https://subversion.apache.org" target="_blank">the Subversion home page</a>). To use these
tools, open a command window (click Start &gt; Run..., then type 'cmd'),
then enter the following commands:</p>
<p>(Note: you can use any directory in place of <code>C:\checkout</code>. Replace <code>%SVNUTILS%</code> with where you installed the
svn binary, e.g. with, <code>C:\svn-win32-1.3.2\bin</code>, or with nothing if you added
the SVN utility to your PATH.)</p>
<p>```
    mkdir C:\checkout
    cd /D C:\checkout
    %SVNUTILS%\svn.exe svn checkout ^
        http://svn.apache.org/repos/asf/infrastructure/site/trunk/ site</p>
<p>```</p>
<p>This will check out the ASF website into a sub-directory called <code>site</code>. When the process is done, you should have checked out the
sources for the website you're reading now. (To recreate the site from the sources, you need <a href="http://ant.apache.org/" target="_blank">Apache Ant</a>. Install Ant now if you
haven't already.)</p>
<p>You can enter these URLs into a browser and actually look at the
sources before checking out anything. However, for this you should probably
use the Web view at <code>http://svn.apache.org/viewvc/</code> as it is much nicer to
use than the raw view. The above URL gives you read-only access. If you're a
committer, then you should use <code>svn checkout --username [username]
https://...</code>. The https access requires authentication and allows you to
commit your changes.</p>
<h4 id="svn-tortoise">Getting SVN source code from on Windows with TortoiseSVN<a class="headerlink" href="#svn-tortoise" title="Permanent link">&para;</a></h4>
<p><a href="https://tortoisesvn.net/" target="_blank">TortoiseSVN</a> is a neat extension for the
Windows Explorer which integrates SVN. Using it is very simple:</p>
<p>After you've created a folder to which you want to check out the sources,
right-click the folder and select <code>SVN Checkout...</code> :</p>
<p><img alt="screenshot of SVN checkout" src="images/tortoisesvn-checkout.jpg" title="screenshot of SVN checkout" />
Fill out the settings as in the screenshot below, and click OK.</p>
<p><img alt="screenshot of SVN settings" src="images/tortoisesvn-settings.jpg" title="screenshot of SVN settings" /></p>
<p>This checks out the source of the site that you're looking at.</p>
<h4 id="svn-nix-cli">Getting SVN source code on Linux using command-line tools<a class="headerlink" href="#svn-nix-cli" title="Permanent link">&para;</a></h4>
<p>The Subversion utilities are available as native Unix and Linux binaries.
Chances are you already have them installed. Try it by opening a console
and typing 'svn'. If you get an error along the lines of <code>bash: svn:
command not found</code>, then you need to install the utilities. How you do that
depends on what version of Unix or Linux you have. For instance, with Debian or
Ubuntu, you can install the utilities by opening a console window and entering the
commands:</p>
<p><code>su -
    # enter the root password when prompted
    apt-get update
    apt-get install svn
    exit</code></p>
<p>Other systems have graphical installers or use the rpm tool. Please refer
to the documentation of your system for instructions on how to install
software</p>
<p>Once you have these tools installed, open a command window, then enter the
following commands:</p>
<p><code># you can use any directory in place of ~/checkout
    mkdir ~/checkout
    cd ~/checkout
    svn checkout http://svn.apache.org/repos/asf/infrastructure/site/trunk/ site</code></p>
<p>This will check out this very documentation that you're reading into a
sub-directory called <code>site</code>. Depending on your connection, this may
take a while.</p>
<h4 id="svn-ide">Using an IDE for SVN repository access<a class="headerlink" href="#svn-ide" title="Permanent link">&para;</a></h4>
<p>Most decent IDEs provide Subversion integration. For Java IDEs, you might have to install a plugin to get SVN
support:</p>
<table class="table">
<thead>
<tr>
<th>IDE</th>
<th>Plugin/Extension</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.eclipse.org">Eclipse</a></td>
<td><a href="ext:tigris/subclipse">Subclipse</a></td>
</tr>
<tr>
<td><a href="https://www.jetbrains.com/idea">JetBrains IDEA before version 5</a></td>
<td><a href="https://svnup.tigris.org">svn-up</a></td>
</tr>
<tr>
<td><a href="https://www.netbeans.org">NetBeans</a></td>
<td><a href="https://vcsgeneric.netbeans.org/profiles/index.html">Subversion profile</a></td>
</tr>
</tbody>
</table>
<p>Please refer to the documentation of the IDE and the plugin/extension for how to install and use the plugin/extension.</p>
<h4 id="svn-update">How to update your checked-out SVN module<a class="headerlink" href="#svn-update" title="Permanent link">&para;</a></h4>
<p>You don't need to check out an entire module every time something is changed.
To synchronize your local copy with the remote repository, use the <code>svn
update</code> which goes like this:</p>
<p>```
    # location where the module is stored
    cd checkout</p>
<div class="codehilite"><pre><span class="c"># either you call the update in the module&#39;s directory</span>
<span class="c"># or you supply the list of modules to update, like this</span>
<span class="n">svn</span> <span class="n">update</span> <span class="n">site</span>
</pre></div>


<p>```</p>
<p>With graphical clients, the process is similar. For example, in TortoiseSVN
you can right-click on any subversion checkout directory and select the
"SVN Update" option.</p>
<h3 id="git">Using Git<a class="headerlink" href="#git" title="Permanent link">&para;</a></h3>
<p>Links to information to help you get started with Git are <a href="https://infra.apache.org/version-control.html" target="_blank">here</a>.</p>
<h2 id="providingfeedback">Providing feedback to Apache projects<a class="headerlink" href="#providingfeedback" title="Permanent link">&para;</a></h2>
<p>A valuable way to contribute to ASF projects is to use the software and
then provide feedback about it to its developers. Different Apache software
projects have different preferences about how you should submit feedback. Check out the project website for more information. In the
absence of information on how to provide feedback,
follow these guidelines.</p>
<p>A vital part of the ASF projects are the project mailing lists. Most projects have a
users' list named <code>users@${project}.apache.org</code> or <code>user@${project}.apache.org</code>. Subscribe to it by sending an
e-mail to <code>users-subscribe@${project}.apache.org</code>, then follow the
instructions. We have many <a href="https://www.apache.org/dev/contrib-email-tips" target="_blank">tips how on asking questions in a way that gets answers</a>.</p>
<p>Tell the developer and user community about your use of the software
product, your experiences in setting it up, issues you encountered, and any general feedback you may have. Don't forget to include any positive observations that will show you appreciate the effort the team is making.</p>
<p>Your story will likely be very welcome if you write it clearly, in a friendly tone, and
Read The Manual before asking for answers that you could find there. You'll probably receive
enthusiastic responses from some of the developers and other users (although responses may not appear right away: everybody is busy). If you
found specific issues or have a specific idea about how things should work,
the project may ask you to submit a detailed bug report or patch to improve things</p>
<p>Many projects also have a developer-focused mailing list named 
<code>dev@${project}.apache.org</code> for discussion of technical project details.</p>
<h4 id="bugreports">How to send in a bug report<a class="headerlink" href="#bugreports" title="Permanent link">&para;</a></h4>
<p>Projects take bug reports very seriously. To help a team fix the bug quickly, include as much information with your report as possible, such as your
platform, version numbers of the application you were using, error logs, configuration, etc. If you are not
sure whether a piece of information is relevant, include it.</p>
<p>Before you submit a bug report, make sure the bug hasn't been reported
before, fixed in a newer version of the software, or fixed in the current
development version. Then file a report. Different projects have different
preferences for this. Usually you enter the bug information into a bug
tracking database, which is normally either
<a href="https://issues.apache.org/bugzilla/enter_bug.cgi" target="_blank">Bugzilla</a> or <a href="https://issues.apache.org/jira" target="_blank">Jira</a>.
Some projects don't use an issue tracker. In that case, send the bug report
to the appropriate mailing list.</p>
<p>If you have the knowledge to supply a patch that fixes the issue, please do
so...</p>
<p>Most issue trackers also support submitting requests for enhancements. If you do so, make sure to set the appropriate flags in
the issue tracker to indicate that your request is not about a bug.</p>
<h4 id="patches">How to send in patches<a class="headerlink" href="#patches" title="Permanent link">&para;</a></h4>
<p>A patch is a computer-generated file that describes differences between
different versions of one or more source files, with the intention of improving the current application code. Different
software projects have different preferences about how to submit a patch. Check out the project website for more information.</p>
<p>In the absence of information on how to provide feedback on any specific 
Apache project's own website, follow these guidelines. For an example, 
see the Apache Subversion project's <a href="https://subversion.apache.org/docs/community-guide/general.html#patches" target="_blank">patch guide</a>.</p>
<p>Patches are generated using the unix utility <code>diff</code> or the <code>svn diff</code>
command. They can be applied using the unix utility <code>patch</code>. When you want
to contribute a change or addition to existing source code, you should:</p>
<ul>
<li>
<p>check out the latest copy of the sources from the project's code repository.</p>
</li>
<li>
<p>change the source files to incorporate your change or addition. Make sure
you also provide appropriate source code documentation (like javadoc for
Java sources), and follow the project's coding conventions.</p>
</li>
<li>
<p>check the software still compiles and runs correctly on your local machine.</p>
</li>
<li>
<p>run any unit or regression tests the software may have.</p>
</li>
</ul>
<p>If this works, you can create your patch. Remove all build products and
remnants (like any 'build', 'dist' or 'bin'
directories)  from the module tree, then build the actual patch. Here's how to do it using the
command line SVN client under unix:</p>
<p>Apache projects prefer the unified diff format. The subversion tool creates
that automatically. If you use other tools, please refer to their
documentation for details on set the diff format.</p>
<p>```
    # location where the modules are stored
    cd checkout</p>
<div class="codehilite"><pre><span class="c"># directory of the module</span>
<span class="n">cd</span> <span class="n">site</span>

<span class="c"># creation of the diff</span>
<span class="n">svn</span> <span class="nb">diff</span> <span class="o">&gt;</span> <span class="n">site</span><span class="p">.</span><span class="nb">patch</span>
</pre></div>


<p>```</p>
<p>The Subversion client now examines all subdirectories for changed files,
then compares the changed file to the one on the server. It generates the
patch. The '&gt;' redirection results in the resulting patch being put in a
text file named (in this case) <code>site.patch</code>.</p>
<p>With your patch generated, you need to send it to the developers. Different
projects have different preferences for this. Usually you add
it as an attachment to the relevant bug report in the bug tracking
database. If a relevant bug report
doesn't exist yet, create one. </p>
<p>A very few projects don't use an issue tracker. In
that case, send the patch as an attachment to an e-mail with a subject
prefixed with "<code>[PATCH]</code>", to the appropriate
development mailing list. If the patch is large, please ask before e-mailing it
in case there is a better way to provide it.</p>
<p>Supply a different patch per issue. A patch can span multiple
files but you should normally try not to fix multiple bugs in a single
patch, unless those bugs are intimately related.</p>
<p>Be patient if your patch is not applied
as fast as you'd like or a developer asks you to make changes to the patch.
If you do not receive any feedback in a reasonable amount of time (say, a week or two),
feel free to send a follow-up e-mail to the developer list. Open source developers are all
volunteers, often doing the development in their spare time.</p>
<h4 id="websites">How to suggest changes to project websites<a class="headerlink" href="#websites" title="Permanent link">&para;</a></h4>
<p>One of the simplest ways to contribute to Apache projects is by suggesting 
improvements to the project's website or product documentation. If something doesn't make 
sense to you, or if you have a better way to explain something, send the 
project a patch!</p>
<p>Projects use many different content management systems for their websites. systems have a web-based editor that makes it relatively simple to provide improvements, once you have access rights. Ask the PMC for such rights, explaining how you would like to help, or simply provide your suggestions in an email.</p></div>
