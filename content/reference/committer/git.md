Title: Getting started with Git
slug: reference/committer/git

[TOC]

This document aims to be a primer in getting started using Git within the ASF.
There are two forms of git repositories:

- Read-only mirrors, hosted at <https://git.apache.org>
- Read/write repositories hosted at <https://git-wip-us.apache.org/repos/asf>

This document is chiefly about the read/write repositories at git-wip.

# Repository Checkout

For now the repository URLs are all of the form:

    https://git-wip-us.apache.org/repos/asf/reponame.git

## To clone a repository:

### Non Committers

    $ git clone http://git-wip-us.apache.org/repos/asf/reponame.git

### Committers

    $ git clone https://git-wip-us.apache.org/repos/asf/reponame.git


# Committers: Getting Started

First things first, you'll want to set up your name and email that will be used by git when you make commits:

    $ git config --global user.name "My Name Here"
    $ git config --global user.email myusername@apache.org

If you're a long time GitHub user you can instead set these configuration variables on a per repository basis like such:

    $ git config user.name "My Name Here"
    $ git config user.email myusername@apache.org

You can also add your apache.org email address to your GitHub account so that your Gravatar and user account are linked to from the Apache mirrors on GitHub.

To push to a repository you need to authenticate. More recent versions of Git will prompt for a username and password, and in some cases will cache the credentials in your operating system's default credential store.

On Mac OS X, you need to have installed git-credential-osxkeychain and set the following configuration:

    $ git config --global credential.helper osxkeychain

If you are not prompted, then you will need to setup a ~/.netrc file that contains your user credentials:

    $ (umask 0277; cat >> ~/.netrc <<EOF)
    machine git-wip-us.apache.org
    login username
    password mypassword
    EOF
    chmod 0600 ~/.netrc

Alternatively you can list your username in the Git repository URL but this will require that you type your password for every fetch and push. You can do this by cloning a URL like:

    $ git clone https://username@git-wip-us.apache.org/repos/asf/reponame.git

While its possible to list your password in the URL this is highly discouraged as it obviously leaves your password in plain text in the shell history.

## Windows Users

You can use git-gui as part of the msysgit package.

Instead of setting up a ~/.netrc file you need to:

- Set up a %HOME% environment pointing to C:\Users\yourloginname\
- Create a _netrc file in %HOME%\_netrc with this text all on one line: machine git-wip-us.apache.org login username password mypassword

### Line Endings

In general, you will want line endings to be normalized in the Git repository and set to be platform specific on checkout.

The msysgit installer on Windows will prompt to set the core.autocrlf setting to true by default. On Mac OS X or Linux, the following setting should be used:

    $ git config --global core.autocrlf input

Further details and attributes for handling them differently per file type can be found in the GitHub article Dealing with line endings.

# Troubleshooting

## no DAV locking

If you get an error like this:

    :::text
    error: no DAV locking support on http://git-wip-us.apache.org/repos/asf/reponame.git/
    fatal: git-http-push failed

It means that you're trying to push over *HTTP* which is disabled. To fix this error change the remote repository URL to use *HTTPS*. You can either edit the .git/config file to update the URL variable or alternatively:

    $ git config remote.origin.url https://git-wip-us.apache.org/repos/asf/reponame.git


# Further Git Reading

- [http://learn.github.com/p/setup.html](http://learn.github.com/p/setup.html)
- [http://gitref.org/](http://gitref.org/)
