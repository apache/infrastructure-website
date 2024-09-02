Title: Source Code Repositories at Apache

license: https://www.apache.org/licenses/LICENSE-2.0

Apache project contributors are in countries all around the world. To help them work together, projects keep their source code in an Internet-accessible revision control system, either <a href="https://subversion.apache.org/" target="_blank">Subversion (SVN)</a> or <a href="https://git-scm.com/" target="_blank">Git</a>. Apache committers have _write access_ to the repositories for their projects, so they can edit existing code and add new files. 

## Contents ##

  - <a href="#general">In general</a>
  - <a href="#git">Git repositories</a>
    - <a href="#create">Creating repositories</a>
    - <a href="#asfyaml">.asf.yaml for Git repositories</a>
  - <a href="#svn">SVN repositories</a>
    - <a href="#commandline">Command-line SVN access</a>
    - <a href="#commandlinecommit">Committing code through the command line</a>
    - <a href="#configuring">Configuring the SVN client</a>
    - <a href="#svnssl">SVN SSL server certificate</a>
    - <a href="#errormessages">Typical SVN error messages</a>
    - <a href="#svnfaqs">SVN FAQs</a>
  - <a href="#migrating">Migrating an SVN code repository to Git</a>

<h2 id="general">In general<a class="headerlink" href="#general" title="Permanent link">&para;</a></h2>

**Note**: please review the [Project Code Repository Policy](project-repo-policy.html).

Everyone has *read access* to the repositories and can download the most up-to-date development version of any project's software to review or compile. 

- If you want a stable release of the source code, download it from the <a href="https://www.apache.org/dyn/closer.lua/" target="_blank">distribution directory</a>. 
- Only download the code directly from your project's code repository if you are participating in the development effort. The latest version of the code is what your colleagues have most recently checked in, and they may or may not have confirmed that it compiles correctly and does what they want it to do.
- If you want a release version of the project's compiled application, visit the project's website and find its download page. It may offer both stable releases and "bleeding-edge" or "nightly" builds that compile properly but include the latest, possibly-unstable, features.

<h2 id="git">Git repositories<a class="headerlink" href="#git" title="Permanent link">&para;</a></h2>

How-to guides, documentation, and a list of projects using Git for revision control are at <a href="https://git.apache.org/" target="_blank">git.apache.org</a>.

Many Git users manage their source code through one of these tools:

* <a href="https://gitbox.apache.org" target="_blank">GitBox</a>
* <a href="https://github.com/apache" target="_blank">GitHub</a>

Some projects began using [read-only-mirrors](git.html) of SVN repositories when Apache's support for Git was limited. This is no longer necessary. [Writable Git](project-repo-policy.html) repositories are available to all projects.

<h3 id="create">Creating repositories<a class="headerlink" href="#create" title="Permanent link">&para;</a></h3>

Apache projects can have as many **public** Git repositories as their product development work requires. Use the <a href="http://selfserve.apache.org/" target="_blank">Self Serve tool</a> to create an additional repository.

Some projects require a **private** Git repository, for reasons like:

  - Developing security patches.
  - Preparing the quarterly Bzoard reports when it is necessary to include information in a  `<private>` section of the report.
  - Maintaining the details of legal contracts, Memorandums of Understanding (MOUs) and similar arrangements with third parties. PMCs can enter into such arrangements if they are directly required for the development of the project's product or products.
  - Keeping information that should not be public.

Each PMC can have **one** private Git repository. Open a Jira ticket for Infra to request one, explaining the reasons the project needs it.

<h3 id="asfyaml">.asf.yaml for Git repositories<a class="headerlink" href="#asfyaml" title="Permanent link">&para;</a></h3>

`.asf.yaml` is a branch-specific file. Projects hosting their websites in a Git repository must use `.asf.yaml` to build and update their sites. Review [this documentation](asf-yaml.html) before working with your `.asf.yaml` files.

Projects can also place `.asf.yaml` in the root of a repository to control:

-  notification settings
-  github settings
-  pelican builds

Read [the .asf.yaml primer](asf-yaml.html) to learn more.

<h2 id="svn">SVN repositories<a class="headerlink" href="#svn" title="Permanent link">&para;</a></h2>

Information about SVN is at <a href="https://subversion.apache.org/" target="_blank">the Apache SVN site</a> and <a href="http://svnbook.red-bean.com/" target="_blank">Version Control with Subversion</a>. The website provides links for _SVN clients_ you can download and install to make it easier to work with SVN.

To browse the repositories or download a few individual files, you can

- use <a href="https://svn.apache.org/viewvc/" target="_blank">viewvc</a>
- find a project repository at <a href="https://svn.apache.org/repos/asf/" target="_blank">the list of SVN repos</a>

<h3 id="commandline">Command-line SVN access<a class="headerlink" href="#commandline" title="Permanent link">&para;</a></h3>

You can check out a project repository anonymously once you have installed a SVN client. For example, to get the Spamassassin module, use:

     $ svn checkout http://svn.apache.org/repos/asf/spamassassin/trunk spamassassin

<h3 id="commandlinecommit">Committing code through the command line<a class="headerlink" href="#commandlinecommit" title="Permanent link">&para;</a></h3>

If you are a project committer and don't want to use a SVN client like Tortoise, you can commit your new and updated files using the command line. We use HTTPS basic authentication, so you need to specify your user name and password as part of the check-in command.

For example, if you wanted to add the file 'test.txt', you might follow these steps:

``` $ svn co https://svn.apache.org/repos/asf/excalibur/trunk/ excalibur-trunk
$ cd excalibur-trunk
$ echo "test" > test.txt
$ svn add test.txt
$ svn commit --username your-name --password your-password \
  --message "Trying out svn"
```

Apache does not support `svnserve` or `svn+ssh`.

<h3 id="configuring">Configuring the SVN client<a class="headerlink" href="#configuring" title="Permanent link">&para;</a></h3>

Committers need to properly configure their svn client. One particular issue is OS-specific line-endings for text files. When you add a new text file, especially when applying patches from Bugzilla, make sure that the line-endings are appropriate for your system, then do (for test.txt)

`svn add test.txt svn propset svn:eol-style native test.txt` 

You can configure your svn client to do that automatically for some common file types. Add the contents of <a href="https://www.apache.org/dev/svn-eol-style.txt" target="_blank">this file</a> to the bottom of your ~/.subversion/config file, normally found at:

- Windows: C:\Documents and Settings\{username}\Application Data\Subversion\config
- Windows 7: C:\Users\{username}\AppData\Roaming\Subversion\config]
- Linux & Mac OSX: ~/.subversion/config or /etc/subversion/config

You may need to set additional properties for some files. For example, apply `svn:executable=*` to script files (e.g. .bat, .cgi, .cmd, .sh) that are intended to be executed. Since not all such files are intended to be executed, do not make the executable property an automatic default.

Pay attention to the messages from your svn client when you do 'svn commit'.

**Tip**: If you use TortoiseSVN, a popular Windows GUI client that integrates with Windows Explorer, you can right click in Explorer and select TortoiseSVN - Settings, and then press the "Edit" button to update your "Subversion configuration file:". If you do not see 

     *.c = svn:eol-style=native

copy the above svn-eol-style.txt file's contents into the end of the config editor that appears, and save the file.

<h3 id="svnssl">SVN SSL server certificate<a class="headerlink" href="#svnssl" title="Permanent link">&para;</a></h3>

You can check the validity of the server certificate on the <a href="/machines.html" target="_blank">Apache host keys listing</a>.

<h3 id="errormessages">Typical SVN error messages<a class="headerlink" href="#errormessages" title="Permanent link">&para;</a></h3>

**Error validating server certificate**

```Error validating server certificate for 'https://svn.apache.org:443':
 - The certificate is not issued by a trusted authority. Use the
   fingerprint to validate the certificate manually!
Certificate information:
 - Hostname: *.apache.org
 - Valid: from Apr 20 00:00:00 2017 GMT until July 20 23:59:59 2019 GMT
 - Issuer: SSL.com
 - SHA-1 Fingerprint 2D:97:67:D9:2E:20:EE:07:3D:26:DA:97:A6:43:36:5F:71:8E:94:19
(R)eject, accept (t)emporarily or accept (p)ermanently?
```

Check the fingerprint against the list at the link above for server certificates.

**No such revision**

If you get an error like

`svn: No such revision 765287`

This may be because of a short lag in the synchronization between Subversion mirrors, and can occur if multiple commits run in quick succession. This error usually happens if you are located in Europe, or are explicitly using the European mirror.

Wait for 10 seconds and repeat the command, and you should have success.

_Note_ that this error can also occur when running `mvn release:prepare`. The mvn release plugin has a special property to handle this situation: <a href="http://maven.apache.org/maven-release/maven-release-plugin/prepare-mojo.html#waitBeforeTagging" target="_blank">waitBeforeTagging</a>.

**Not the latest baseline**

If you get an error like this:

```svn: Commit failed (details follow):
svn: The specified baseline is not the latest baseline, so it may not be
checked out.
```

This may be because of a short lag in the synchronization between Subversion mirrors, and can occur if multiple commits run in quick succession. This error usually happens if you are located in Europe, or are explicitly using the European mirror.

Wait for 10 seconds and repeat the command, and you should have success.

**Problems using date revisions**

If you are using a date revision such as `-r{2004-09-12}:{2004-08-12}` and not getting any or all of the revisions you expected, this is a known problem specific to the ASF repository.

Unfortunately, there is nothing that can be done to improve this situation, so you must use a workaround. You can use `svn log` or ViewVC to locate the actual revision number that is first after the date you desire, and substitute that into your `-r` argument to the svn command.

For example, consider the desired command:

`$ svn diff -rHEAD:{2005-01-01}`

While this produces no results, running `svn log` alone produces a result like this:

```
------------------------------------------------------------------------
r124032 | aheritier | 2005-01-04 09:58:16 +1100 (Tue, 04 Jan 2005) | 1 line

Switch to subversion
------------------------------------------------------------------------
r123911 | brett | 2005-01-03 09:48:57 +1100 (Mon, 03 Jan 2005) | 1 line

remove nagoya references
------------------------------------------------------------------------
r116173 | brett | 2004-10-23 22:11:51 +1000 (Sat, 23 Oct 2004) | 2 lines

remove old requires descriptions
```

So try the command:

`$ svn diff -rHEAD:123911`

This problem crops up because the order of the revisions is not identical to the order of dates in the repository. This is a side effect of loading CVS repositories with history including dates prior to the earliest date in the Subversion repository.

<h3 id="svnfaqs">SVN FAQs<a class="headerlink" href="#svnfaqs" title="Permanent link">&para;</a></h3>

- **When should I use svn lock?** Very rarely. Commits in subversion are transactional. This means that locks are almost always unnecessary. An oft-quoted use case is to prevent concurrent editing of a large, unmergeable binary document. However, for open development, good communication is preferable to locking even in this use case. A good, timely post to the list to let your fellow developers know that you're going to start editing that huge PDF is better than locking the file. 
- **How often can I run a cron job that connects to the repository?** Hourly is fine. Please do not use programs that poll the repository more frequently than hourly. People who run automated scripts that continuously poll the repository wind up getting their access denied, and that may impact other folks connecting through the same host. If you need to stay more in-sync than an hourly cron allows, subscribe your script to the relevant commit mailing list.
- **How do I mirror the whole SVN repository for an experiment?**  First, ask yourself whether you really want the entire ASF repository Most people really want only a single project. In that case, just check out that source directory from the repo. If you really do want the entire ASF repository, don't use svnsync. Instead, start by looking <a href="httpa://svn-master.apache.org/dump/" target="_blank">here</a>. Use that to bootstrap your repo.
- **Why do I get a 403 error when I try to commit code?** Run `svn info` and check that the URL starts with `https://`. If it starts with `http://`, run:

`$ svn switch --relocate http://svn.apache.org https://svn.apache.org`

If you still get 403 Forbidden errors, ask your PMC to double-check the authz file and LDAP/Unix group membership.

<h2 id="migrating">Migrating an SVN code repository to Git<a class="headerlink" href="#migrating" title="Permanent link">&para;</a></h2>

Instructions are [here](svn-to-git-migration.html).
