Title: How to mirror ASF software releases locally

Organizations may wish to create a download mirror that includes the releases of most or all of the Apache Software Foundation's projects. Here is how to set up such a mirror.

**NOTE - as of August, 2021, the ASF itself is not accepting further mirror site applications.**

  - <a href="#requirements">Requirements</a>
  - <a href="#techniques">Mirroring techniques</a>
  - <a href="#sponsorinfo">Sponsor information</a>
  - <a href="#testing">Testing your mirror</a>
  - <a href="#questions">Questions?</a>

<h2 id="requirements">Requirements<a class="headerlink" href="#requirements" title="Permanent link">&para;</a></h2>

Hosting a mirror has a few requirements:

  - You should have at least 150 GB of available disk space. The current distribution directory is around 110 GB, but it is constantly expanding.
  - You may mirror either the full distributions tree, or a reduced tree that excludes a few very resource-intensive (disk-wise and bandwidth-wise) projects.
  - You must not trim or abridge the mirrored tree in any way.
  - You must not modify the mirrored tree in any way. In particular, you must not alter or remove HEADER.html or README.html files. See below for adding sponsor information.
  - Your mirror must not appear "inside" another site using, for instance, frames. 

We encourage you to 

  - do an **update-check** at least four times a day a day. You may sync a maximum of six times per day, but only if you have a slow or poor connection that causes timeouts.
  - run the <a href="https://httpd.apache.org/" target="_blank">Apache HTTP Server</a> version 2.2 or later and use the following configuration for your web mirror to allow all the features of our download site to function optimally:

```
<Directory /path/to/mirror>
  IndexOptions FancyIndexing NameWidth=* FoldersFirst ScanHTMLTitles DescriptionWidth=*
  HeaderName HEADER.html
  ReadmeName README.html
  AllowOverride FileInfo Indexes
  Options Indexes SymLinksIfOwnerMatch FollowSymLinks
  ErrorDocument 404 default
</Directory>
```

**Note** that our HEADER.html files do not contain the HTML preamble, so it is important **not** to enable the `SuppressHTMLPreamble` option.

Make sure that the server does not send a `Content-Encoding` header for any of the compressed archives. The hashes and signatures used to check downloads are created for the compressed archives so it is vital that the browser is not told to decompress them. For example, `.tar.gz` and `.tgz` files are compressed TAR files. They should have a suitable Content-Type - e.g. `application/x-gzip` - but no `Content-Encoding` should be sent. If the server incorrectly sends `Content-Encoding: x-gzip` (for example), many browsers will automatically decompress the response. This produces a TAR file which will not verify when checked against the hashes or sigs.

<h2 id="techniques">Mirroring techniques<a class="headerlink" href="#techniques" title="Permanent link">&para;</a></h2>

We only support <a href="https://rsync.samba.org/" target="_blank">rsync</a> for updating mirrors.

Update your mirror with:

```
rsync -avz --delete --safe-links rsync.apache.org::apache-dist /path/to/mirror
```

To exclude resource-intensive projects, replace `::apache-dist` with `::apache-dist-most`. Do not use `--exclude`.

If there is a problem with file/directory permissions, make sure you use a proper umask in your cronjob:

```
umask 022 ; rsync ...
```

  - Don't rsync "on the hour" (`cronjob minute 0`). Pick a random minute between 5 and 55. Never run cronjobs at minute 0 unless the nature of the job requires it.
  - Run the job four times a day; no more than six times a day in any case.
  - Check the output from the rsynch job regularly so you can detect problems like lack of disk space or permission issues.
  
<h2 id="sponsorinfo">Sponsor information<a class="headerlink" href="#sponsorinfo" title="Permanent link">&para;</a></h2>

Here is how to add sponsor information:

  1. Edit the file `/local/path/to/mirror/README.html`
  2. Add to your rsync options `--exclude "/README.html"`

The contents of README.html appear near the bottom of your mirror's home page.

  - Only customize the home-page (top-level) README.html. Do not change any other README.html files. 
  - Don't omit the '/' in `"/README.html"`.

Please limit the contents of the README.html to something like:

```
This mirror is donated by www.domain.com [url] to support the Apache open source community.
```

Search engines interpret referring to specific services or products as _PageRank manipulation_. This could hurt your site's ranking.

<h2 id="testing">Testing your mirror<a class="headerlink" href="#testing" title="Permanent link">&para;</a></h2>

If your mirror is not working properly, check the following:

  - Page headers and footers display correctly.
  - All top-level directories and files on the ASF mirror are present on your mirror.
  - Download a couple of files to check that the process works. 
  - Trying to download a missing file should generate a `404 Not Found` error. You can verify this by modifying one of the valid URLs that you tested above.

<h2 id="questions">Questions?<a class="headerlink" href="#questions" title="Permanent link">&para;</a></h2>

If you have any questions, contact us at `users@infra.apache.org`.
