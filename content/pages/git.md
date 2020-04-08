Title: Git access to Apache codebases

<p>The Apache Software Foundation uses <a href="https://subversion.apache.org/" target="_blank">Subversion</a> (SVN) as the main [version control](version-control.html) infrastructure, but we also provide some level of support to users of the <a href="https://git-scm.com/" target="_blank">Git</a> version control system.

This page as about _read-only_ Git mirrors of Apache codebases. [Writable Git repositories](writable-git.html) are also available.
<a href="writable-git">Writable Git repositories</a> are also available.</p>
<div class="toc">
<ul>
<li><a href="#git-mirrors">Read-only Git mirrors</a></li>
<li><a href="#workflow">Proposed workflow</a></li>
</ul>
</div>
<h1 id="git-mirrors">Read-only Git mirrors<a class="headerlink" href="#git-mirrors" title="Permanent link">&para;</a></h1>
<p>We maintain read-only Git mirrors of many Apache codebases at
<a href="http://git.apache.org/">http://git.apache.org/</a>. These mirrors contain the
full version histories (including all branches and tags) of the mirrored
codebases and are updated in near real time based on the latest svn
commits.</p>
<p>The mirrors can be cloned or pulled from git.apache.org using both
the Git and HTTP protocols. Less frequently updated copies of the
mirrors are also available on Github. See the mirror page for the
available clone URLs.</p>
<p>Please file an <a href="https://issues.apache.org/jira/browse/INFRA">INFRA</a> issue
(component: Git) to request a new codebase to be mirrored or to change the
settings of an existing mirror. When requesting a new mirror, please
include the following information:</p>
<ul>
<li>
<p>Name of the codebase, for example "Apache Tika"</p>
</li>
<li>
<p>Name of the requested Git mirror, for example "tika.git"</p>
</li>
<li>
<p>Subversion path of the codebase, for example "/lucene/tika"</p>
</li>
<li>
<p>Subversion layout, in case it is different from the standard "trunk,
branches, tags" structure.</p>
</li>
</ul>
<h1 id="workflow">Proposed workflow<a class="headerlink" href="#workflow" title="Permanent link">&para;</a></h1>
<p>This is a proposed workflow for using Git with an Apache codebase. This
workflow is mainly targeted to contributors who don't already have commit
access to a project.</p>
<p>Once you have cloned or pulled the latest changes to your local Git
repository of an Apache codebase, you can start working on it. Whenever you
make some changes to the codebase, it's good to have a related issue filed
in the issue tracker of the project and to use a similarly named branch in
your Git repository. For example, to create a branch for an issue with the
key TIKA-123.</p>
<p><code>git branch TIKA-123 origin/trunk</code> </p>
<p>With per-issue branches you can easily switch back and forth between
different issues without worrying about unwanted side-effects from
unfinished changes to other issues. Whenever you want to work on the
TIKA-123 example issue, simply checkout that branch and start making your
changes.</p>
<p><code>git checkout TIKA-123</code> </p>
<p>It's a good idea to commit your changes whenever you have finished one
logical part of the issue. For example when refactoring, make a new commit
for each refactoring step you take.</p>
<p><code>git commit</code> </p>
<p>Once you're ready to share your changes with the rest of the project team,
you can use the git format-patch command to produce a nice set of patches
to attach to the relevant issue.</p>
<p><code>git format-patch origin/trunk</code> </p>
<p>The sooner you share your work the better. You can repeat the steps of this
workflow as often as you like, producing more patches to be attached to the
issue tracker. Once some of your patches are accepted and committed to svn,
you can rebase your work against the latest trunk. Alternatively, if you're
asked to make some changes, you can go back to the original Git commit and
modify it until the project team accepts your changes.</p></div>

_migrating information from https://www.apache.org/dev/git.html_
