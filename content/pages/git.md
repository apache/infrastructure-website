Title: Git access to Apache Subversion codebases
license: https://www.apache.org/licenses/LICENSE-2.0

The Apache Software Foundation projects use <a href="https://subversion.apache.org/" target="_blank">Subversion</a> (SVN) or <a href="https://git-scm.com/" target="_blank">Git</a> for [version control](version-control.html) of their software and documentation assets. This page is about _read-only_ Git mirrors of Apache SVN codebases. [Writable Git repositories](project-repo-policy.html) are also available.


<h2 id="git-mirrors">Read-only Git mirrors<a class="headerlink" href="#git-mirrors" title="Permanent link">&para;</a></h2>

We maintain read-only Git mirrors of many Apache codebases at <a href="https://git.apache.org/" target="_blank">https://git.apache.org/</a>. These mirrors contain the full version histories (including all branches and tags) of the mirrored codebases and are updated in near real time based on the latest svn commits.

You can clone the mirrors or download them using both the Git and HTTP protocols. Less frequently updated copies of the
mirrors are also available on GitHub.

Please file an <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">INFRA</a> ticket (component: Git) to request a new codebase to be mirrored or to change the settings of an existing mirror. When requesting a new mirror, please include the following information:

  - Name of the codebase, for example "Apache Tika"
  - Name of the requested Git mirror, for example "tika.git"
  - Subversion path of the codebase, for example "/lucene/tika"
  = Subversion layout, in case it is different from the standard "trunk, branches, tags" structure.

<h2 id="workflow">Workflow<a class="headerlink" href="#workflow" title="Permanent link">&para;</a></h2>

Here is how to use Git with an Apache codebase. This workflow is mainly targeted to contributors who don't already have commit
access to a project.

Once you have cloned or pulled the latest changes to your local Git repository of an Apache codebase, you can start working on it. Whenever you make some changes to the codebase, it's good to have a related issue filed in the issue tracker of the project and to use a similarly named branch in your Git repository. For example, to create a branch for an issue with the key `TIKA-123`:

`git branch TIKA-123 origin/trunk`

With per-issue branches you can easily switch back and forth between different issues without worrying about unwanted side-effects from
unfinished changes to other issues. Whenever you want to work on the TIKA-123 example issue, simply check out that branch and start making your changes:

`git checkout TIKA-123`

It's a good idea to commit your changes whenever you have finished one logical part of the issue. For example when refactoring, make a new commit for each refactoring step you take:

`git commit`

Once you're ready to share your changes with the rest of the project team, you can use the git `format-patch` command to produce a nice set of patches to attach to the relevant issue:

`git format-patch origin/trunk`

The sooner you share your work, the better. 

You can repeat the steps of this workflow as often as you like, producing more patches to be attached to the issue tracker. Once some of your patches are accepted and committed to svn, you can rebase your work against the latest trunk. Alternatively, if you're asked to make some changes, you can go back to the original Git commit and modify it until the project team accepts your changes.
