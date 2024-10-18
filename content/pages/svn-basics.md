Title: Subversion basics
license: https://www.apache.org/licenses/LICENSE-2.0

Our developers are located all around the world. To enable them to work together on our software, we keep the source code in Internet-accessible revision control systems, [Git](git.html) and Subversion (SVN).

Apache committers have write access to the Apache Subversion repository so they can make changes to their project's source code. Everyone has read access to the repositories, so you may download the most up-to-date development version of software that interests you.

If you are looking for a stable release of a project's source code, you should download it from the <a href="http://www.apache.org/dyn/closer.lua/" target="_blank">distribution directory</a>. Only download directly from the SVN repository if you want to be on the *bleeding-edge* of the development effort. The code contained there may fail to work, and may even eat your hard drive.

  - <a href="#accessing">Accessing the Subversion repository</a>
  - <a href="#configuring">Configuring the Subversion client</a>
  - <a href="#ssl">SSL server certificate</a>
  - <a href="#faq">Frequently asked questions</a>

<h3 id="accessing">Accessing the Subversion repository<a class="headerlink" href="#accessing" title="Permanent link">&para;</a></h3>

There are several ways to access the Subversion repository:

**Web Access**

If you just wish to browse around or download a few individual files, the best tool is the web-based <a href="http://svn.apache.org/viewvc/" target="_blank">ViewVC interface for Subversion</a>. You can also go straight to the <a href="http://svn.apache.org/repos/asf/" target="_blank">public repository</a>.

**Anonymous Subversion**

To access the Subversion repository anonymously, you need a Subversion client. 

**Finding the project you want**

You can <a href="http://svn.apache.org/repos/asf/" target="_blank">browse</a> for the project that interests you and check it out. For example, to get the Spamassassin module, use:

`$ svn checkout http://svn.apache.org/repos/asf/spamassassin/trunk spamassassin`

For more help on using Subversion, consult the <a href="http://subversion.tigris.org/" target="_blank">Subversion website</a> or this free <a href="http://subversion.tigris.org/" target="_blank">Subversion book</a>. The website provides a list of clients and useful links.

**Committer Subversion access**

We currently use HTTPS basic authentication for logging in to Subversion (certificate info below). To change your password, visit <a href="https://svn.apache.org/change-password" target="_blank">svn.apache.org/change-password</a>.

This will prompt you to enter a svn password of your choice. If you cannot log in, or have lost your password, visit the <a href="https://id.apache.org" target="_blank">Apache Account Utility</a> to reset it.

When you make changes to the repository, you can commit them with your username/password combination, i.e.

```
$ svn co https://svn.apache.org/repos/asf/excalibur/trunk/ excalibur-trunk
$ cd excalibur-trunk
$ echo "test" > test.txt
$ svn add test.txt
$ svn commit --username your-name --password your-password \
  --message "Trying out svn"
```

`svnserve` is not supported, nor is `svn+ssh`.

<h3 id="configuring">Configuring the Subversion client<a class="headerlink" href="#configuring" title="Permanent link">&para;</a></h3>

Committers need to configure their svn client properly. One particular issue is OS-specific line endings for text files. When you add a new text file, especially when applying patches from Bugzilla, first ensure that the line-endings are appropriate for your system, then do:

```
svn add test.txt svn propset svn:eol-style native test.txt
```

Your svn client can be configured to do that automatically for some common file types.

Add the contents of the file `http://www.apache.org/dev/svn-eol-style.txt` to the bottom of your `~/.subversion/config` file. For Windows this is normally found at `C:\\Documents and Settings\\{username}\\Application Data\\Subversion\\config`.

You may need to set additional properties for some files. For example, apply `svn:executable=*` to script files (.bat, .cgi, .cmd, .sh) that are intended to be executed. Since not all such files are necessarily intended to be executed, do not make the executable property an automatic default.

Pay attention to the messages from your svn client when you do `svn commit`.

**Tip**: If you use TortoiseSVN, a popular Windows GUI client that integrates with Windows Explorer, you can right-click in Explorer, select `TortoiseSVN - Settings`, and select "Edit" to update your Subversion configuration file. Copy the above `svn-eol-style.txt` file's contents into the end of the configuration file that appears, and save the file.

<h3 id="ssl">SSL server certificate<a class="headerlink" href="#ssl" title="Permanent link">&para;</a></h3>

The server certificate for `https://svn.apache.org/` is a real SSL certificate. However, Subversion, by default, does not currently ship with a list of trusted CAs. So, here's some information to help you verify the validity of our certificate:

```
 - Hostname: *.apache.org
 - Valid: from Jul  1 00:00:00 2019 GMT until Jun 30 23:59:59 2021 GMT
 - Issuer: Sectigo RSA Domain Validation Secure Server CA, Sectigo Limited, Salford, Greater Manchester, GB
 - Fingerprint: 88:A1:77:AC:CE:5E:6C:0D:22:BC:1F:E4:4E:AA:D4:2A:A4:C0:71:4F
```

Note that the SSL certificate for our Subversion repository is different from certificates used when logging into Apache infrastructure. See the [New Committer's guide](new-committers-guide.html) for more information.

<h3 id="faq">Frequently asked questions<a class="headerlink" href="#faq" title="Permanent link">&para;</a></h3>

**When should I use 'svn lock'?**

Very rarely. Commits in subversion are transactional. This means that locks are almost always unnecessary.

An oft-quoted use case is to prevent concurrent editing of a large unmergeable binary document. However, for open development, good communication is preferable to locking even in this use case. A clear, timely post to the list to let your fellow developers know that you're going to start editing that huge PDF is better than locking the file.

**How frequently can I run a cron that connects to the repository?**

Hourly is fine. Please do not use programs that poll the repository more frequently than hourly. People who run automated scripts that continuously poll the repository wind up getting their access denied, which may impact other folks connecting through the same host. If you need to stay more in-sync than an hourly cron allows, subscribe your script to the relevant commit mailing list.

**How do I mirror the entire SVN repository for my experimental $foo?^^

First, ask yourself: do I really want the *entire* ASF repository? Generally most people really want only a single project. In that case, just check out that source directory from the repo.

If you really do want the entire ASF repository, *don't* use `svnsync`. Instead, start by looking here: `http://svn-master.apache.org/dump/`. Use that to bootstrap your repo.

**Why do I get a 403 error when I try to commit?**

Run `svn info` and check that the URL starts with `https://`. If it starts with `http://`, run:

```
$ svn switch --relocate http://svn.apache.org https://svn.apache.org
```

If you still get 403 Forbidden errors, ask your PMC to double-check the authz file and LDAP/Unix group membership.
