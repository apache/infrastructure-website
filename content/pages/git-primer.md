Title: Getting started with Git
license: https://www.apache.org/licenses/LICENSE-2.0

This document is a primer on using Git for an Apache Software Foundation project.

## Contents ##

  - <a href="#repotypes">Repository types</a>
    -  <a href="#publicprivate">Public and private repositories</a>
  - <a href="repocheckout">Repository checkout</a>
  - <a href="#committers">Committers: getting started</a>
  - <a href="#windowsusers">Windows users</a>
  - <a href="#lineendings">Line endings</a>
  - <a href="#trouble">Troubleshooting</a>
  - <a href="#further">Further reading</a>

<h2 id="repotypes">Repository types<a class="headerlink" href="#repotypes" title="Permanent link">&para;</a></h2>

There are two forms of Git repositories:

1. Read-only mirrors hosted at `https://git.apache.org`
2. Read/write repositories hosted at `https://gitbox.apache.org/repos/asf`

This document is chiefly about the read/write repositories.

<h3 id="publicprivate">Public and private repositories<a class="headerlink" href="#publicprivate" title="Permanent link">&para;</a></h3>

Projects can set up as many **public repositories** as their development work requires, using <a href="https://selfserve.apache.org/" target="_blank">SelfServe</a>. 

Each project can also have a **private repository** space for working on sensitive issues such as:

  - security patches
  - writing a draft of the project Board report when there is a section that will appear in a `<private>` tag
  - sharing credentials

The private repository is **not** for uses such as project code development not related to a security issue.

See the [Project Code Repository Policy](project-repo-policy.html) for further details.

Open a Jira ticket for Infra to request a private repository. 

<h2 id="repocheckout">Repository checkout<a class="headerlink" href="#repocheckout" title="Permanent link">&para;</a></h2>

The repository URLs are all of the form:

```
https://gitbox.apache.org/repos/asf/reponame.git
```

### Cloning a repository ###

  - **Committers**: `$ git clone https://gitbox.apache.org/repos/asf/reponame.git`
  - **Non-Committers**: `$ git clone http://gitbox.apache.org/repos/asf/reponame.git`

<h2 id="committers">Committers: getting started<a class="headerlink" href="#committers" title="Permanent link">&para;</a></h2>

Set up your name and email that Git will use when you make commits:

```
$ git config --global user.name "My Name Here"
$ git config --global user.email myusername@apache.org
```

If you're a long-time GitHub user you can set these configuration variables on a per-repository basis:

```
$ git config user.name "My Name Here"
$ git config user.email myusername@apache.org
```

You can also add your `apache.org` email address to your GitHub account so that the Apache mirrors on GitHub link to your Gravatar and user account.

To push to a repository you need to authenticate. More recent versions of Git prompt for a user name and password, and in some cases will cache the credentials in your operating system's default credential store.

On Mac OS X, you need to have `git-credential-osxkeychain` installed, and to set the following configuration:

```
$ git config --global credential.helper osxkeychain
```

If you do not see an authentication prompt, you need to set up a `~/.netrc` file that contains your user credentials:

```
$ (umask 0277; cat >> ~/.netrc <<EOF)
machine gitbox.apache.org
login username
password mypassword
EOF
chmod 0600 ~/.netrc
```

You can list your user name in the Git repository URL, but this requires that you provide your password for every fetch and push. You can simplify this step by cloning a URL like:

```
$ git clone https://username@gitbox.apache.org/repos/asf/reponame.git
```

While it's _possible_ to list your password in the URL, we discourage this practice as it leaves your password in plain text in the shell history.

<h2 id="windowsusers">Windows users<a class="headerlink" href="#windowsusers" title="Permanent link">&para;</a></h2>

You can use `git-gui` as part of the `msysgit` package.

Instead of setting up a `~/.netrc` file you need to:

1. Set up a `%HOME%` environment pointing to `C:\Users\yourloginname\`
1. Create a `_netrc` file in `%HOME%_netrc` with this text all on one line: `machine gitbox.apache.org login username password mypassword`

<h2 id="lineendings">Line endings<a class="headerlink" href="#lineendings" title="Permanent link">&para;</a></h2>

In general, you should normalize line endings in the Git repository and set them to be platform specific on checkout.

  - The `msysgit` installer on **Windows** will prompt you to set the `core.autocrlf` setting to `true` by default. 
  - On **Mac OS X or Linux**, use this setting: `$ git config --global core.autocrlf input`

Further details and attributes for handling line endings differently per file type are available at <a href="https://help.github.com/en/github/using-git/configuring-git-to-handle-line-endings" target="_blank">Configuring Git to handle line endings</a>.

<h2 id="trouble">Troubleshooting<a class="headerlink" href="#trouble" title="Permanent link">&para;</a></h2>

#### no DAV locking ####

If you get an error like this:

```
error: no DAV locking support on http://gitbox.apache.org/repos/asf/reponame.git/
fatal: git-http-push failed
```

It means that you're trying to push over **HTTP**, which is disabled. To fix this error change the remote repository URL to use **HTTPS**. You can edit the `.git/config` file to update the URL variable, or use:

```
$ git config remote.origin.url https://gitbox.apache.org/repos/asf/reponame.git
```

<h2 id="further">Further reading<a class="headerlink" href="#further" title="Permanent link">&para;</a></h2>

  - <a href="https://lab.github.com/" target="_blank">GitHub Learning Lab</a>
  - <a href="https://github.github.com/training-kit/" target="_blank">Git Cheat Sheets</a>
  - [GitHub roles](github-roles.html)
