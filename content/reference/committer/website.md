Title: How To Manage any Apache Project's Website
slug: reference/committer/website

[TOC]

Every Apache project or podling has a website hosted at apache.org that 
is maintained by one of these tools.  It is up to each project to decide 
the details of how their own website is maintained and what software
is used - as long as it results in static files that can be served by the
our public web servers (limited support for .htaccess files and CGI
scripts is also available). 

The basic requirements for site management
are that only committers should be able to modify the site and that
notifications of all site changes should be sent to the relevant
project mailing lists.  The Apache CMS allows non-committers to send 
patches via a simple web interface by "Mail Diff"ing to the project 
mailing list that can be easily published by a committer.

The infrastructure team currently supports two primary tools for
publishing and maintaining Apache project websites:

  - **Apache CMS**, which provides a simple browser-based user interface
    for editing, staging and publishing site content in Markdown, HTML
    or any other source format for which support has been added. See
    the [CMS reference](cmsref) and [adoption](cmsadoption) for more details. The Apache CMS
    uses svnpubsub as the underlying mechanism for publishing a site.
  - **svnpubsub**, which allows the static contents of a designated svn
    folder ([example](http://svn.apache.org/repos/asf/ant/site/ant/production/)) to automatically published
    as the project web site at `http://project.apache.org/`. The project
    team can use any site build mechanism it wants as long as the above
    requirements are met.

Some projects still use a deprecated site deployment system based
on periodic synchronization of static files from people.apache.org to
the live web servers. This mechanism will be **discontinued** at the end of
2012, by which time all projects should have migrated to one of the above
site publishing mechanisms.

# How do I preview my project website? # {#preview}

For svnpubsub sites, review the local files in your svn checkout before
committing them. The changes will be published immediately after you
commit them.

For CMS sites, just commit the changes (without "publish"-ing them) and browse
to `http://TLP.staging.apache.org/`. The CMS 
web interface includes a [Staged] link that will take you there directly.

# Can I control the configuration of my project website? # {#configure}

Yes, the central config file allows you to use `.htaccess` files in your
website directories to control configuration. Of course, reading and
parsing an `.htaccess` file on each request can slow down the server, so
you should consider requesting an adjustment in the central config file for
permanent configuration changes.

# How does logging work? # {#logging}

Each day's error and access logs are kept in
`www.apache.org:/x1/logs/www/`. They are shuffled off each night to a
directory under `people.apache.org:/x1/logarchive/` and are then
periodically archived to other media.

No formal log analysis is performed, but you are free to grab the logs and
do whatever analysis you would like.

# Do project sites have to use [the CMS](cms)? # {#use-cms}

No.  It's recommended but not required.  ([More information](http://www.apache.org/dev/cms) and
[reference](http://www.apache.org/dev/cmsref) about the Apache CMS.)

# Do project sites have to use [svnpubsub](http://svn.apache.org/viewvc/subversion/trunk/tools/server-side/svnpubsub/)? # {#svnpubsub}

Yes.  Infrastructure will mandate transition to svnpubsub over this year.
(svnpubsub [requires](#intro) the generated site files to be in a Subversion
tree somewhere.  For CMS users this tree will be the CMS build output tree.)

## What revision of the site is currently being served? ## {#svnpubsub-revision}

Look at the `.revision` file at the root of your site (for example,
<https://www.apache.org/dist/subversion/.revision> or 
<http://subversion.apache.org/.revision>).  That file is updated after every
successful `svn update`.  (If the update is underway or exited abnormally,
`.revision` won't have been changed.)

# How to provide public access to our project mail archive mbox files? # {#mail}

Some projects have a "mail" directory at the top of their project website.
Enable this by creating a symbolic link in svnpubsub or CMS output
(to `/home/apmail/public-arch/$tlp.apache.org`).
Also see other [notes](http://apache.org/dev/#mail).

# Can my project site use its own favicon instead of just the Apache Feather? # {#feather}

Yes, just add a `favicon.ico` file to your site's root.  The feather is only
used for project sites that don't have a `favicon.ico` file.

# How can I minimize the number of changes committed in my Maven/JavaDoc/generated site? # {#generated}

If you are using svnpubsub, the commit will perform very slowly if the number of changes is large - particularly if the number of files is large.
This is often the case with JavaDoc, and to a lesser extent Maven generated sites.

You may wish to use the CMS instead of svnpubsub directly. This moves the work to the server-side, but it will still be valuable to minimize the changes committed.

These are some steps that can be taken:

 - Ask infrastructure to store your generated content in the CMS repository, rather than the main ASF repository. While this won't necessarily speed up the commit, it will prevent it from impacting other users.
 - When running JavaDoc, pass the `-notimestamp` option. This will avoid most files from being modified between runs if there haven't been code changes.
 - Use a Maven skin that doesn't generate a timestamp into the output. This may require customizing the current skins.
 - If you use the Maven dependencies report in the Project Info Reports plugin, use version 2.7+ of the plugin (*not yet released*) which avoids random strings being generated.
 - If you maintain historical versions of documentation, always check-in to a single "trunk", then use an `svn copy` operation to tag or branch the content, rather than checking in a complete copy
 - Minimize uses of "publish date" and "version" in templates to those that are truly necessary or helpful. Consider using a "last modified date" and version in the URL instead (unless "latest" is implied).
 - Minimize Subversion keywords in the output that may change frequently without significant meaning. This includes in source code that may be rendered to JavaDoc or a Maven JXR source cross-reference).
 - Avoid publishing Maven reports that change constantly to the project site. Code coverage, style reports, static analysis, etc. can be generated into a working copy on the CI server instead for easy developer viewing, and project's can consider utilizing https://analysis.apache.org/ for such reports as well.

