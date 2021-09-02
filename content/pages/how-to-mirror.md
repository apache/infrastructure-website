Title: How to be an Apache Software Foundation download mirror

## NOTE - as of August, 2021, the ASF is not accepting further mirror site applications


<hr>

**The following information is of historical interest only**

The Apache Software Foundation has mirror sites all around the world, but we are always looking for additional reliable and well-connected sites that can help us distribute our software by mirroring our main software distribution directory.

  - <a href="#requirements">Requirements</a>
  - <a href="#techniques">Mirroring techniques</a>
  - <a href="#sponsorinfo">Sponsor information</a>
  - <a href="#testing">Testing your mirror</a>
  - <a href="#ready">Let us know you when are ready</a>
  - <a href="#questions">Questions?</a>

<h2 id="requirements">Requirements<a class="headerlink" href="#requirements" title="Permanent link">&para;</a></h2>

We have a few requirements for those wishing to run a mirror:

  - We select https mirrors as "preferred" mirrors. We do add ftp mirrors to our list, but we no longer accept http mirrors.
  - At least 150 GB of available disk space. The current distribution directory is around 110 GB, but we wish to leave room for considerable expansion.
  - You may mirror either the full distributions tree, or a reduced tree that excludes a few very resource-intensive (disk-wise and bandwidth-wise) projects.
  - You must not trim or abridge the mirrored tree in any way.
  - You must not modify the mirrored tree in any way. In particular, HEADER.html and README.html files must not be altered or removed. See below for adding sponsor information.
  - Your mirror must not be shown "inside" another site using, for instance, frames. 
  - You must do an **update-check** at least once and preferably twice a day. You may sync a maximum of four times per day, but only if you have a slow or poor connection that causes timeouts.
  - You must subscribe to the mailing list for mirror maintainers (see below).

In addition, we require that you run the <a href="https://httpd.apache.org/" target="_blank">Apache HTTP Server</a> version 2.2 or later and use the following configuration for your web mirror to allow all the features of our download site to function optimally:

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

Please ensure that the server does not send a `Content-Encoding` header for any of the compressed archives. The hashes and signatures used to check downloads are created for the compressed archives so it is vital that the browser is not told to decompress them. For example, `.tar.gz` and `.tgz` files are compressed TAR files. They should have a suitable Content-Type - e.g. `application/x-gzip` - but no `Content-Encoding` should be sent. If the server incorrectly sends `Content-Encoding: x-gzip` (for example), many browsers will automatically decompress the response. This produces a TAR file which will not verify when checked against the hashes or sigs.

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
  - Run the job twice a day; no more than four times a day in any case.
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

We have noticed that certain sites redirect 404 pages as a form of extra advertising or as a traffic booster. We remove mirrors that do this from our list and then send an email to the maintainer's address to ask them to correct the issue. The top level `/README.html` file, as mentioned, is the **only** local alteration of any part of the mirror we accept for you to provide sponsor information.

<h2 id="testing">Testing your mirror<a class="headerlink" href="#testing" title="Permanent link">&para;</a></h2>

We sometimes get requests to add mirrors that are not working correctly. Please check at least the following:

  - Page headers and footers display correctly
  - All top-level directories and files on the ASF mirror are present on your mirror
  - Download a couple of files to check that the process works. 
  - Trying to download a missing file should generate a `404 Not Found` error. You can verify this by modifying one of the valid URLs that you tested above.
  
<h2 id="ready">Let us know when you are ready<a class="headerlink" href="#ready" title="Permanent link">&para;</a></h2>

Once your site is configured, tested, and updating consistently, subscribe to the mirror-maintainers mailing list by sending an mail to `mirrors-subscribe@apache.org`.

If possible, please use an alias like `admin@hostname.example` for the contact address rather than a personal e-mail address. To subscribe the alias address, send the email to `mirrors-subscribe-admin=example.org@apache.org`.

Submit the details of your mirror by submitting them to the <a href="https://issues.apache.org/jira/projects/INFRA" target="_blank">Infra Issue Tracker</a>. 

Create an account if you do not already have one, then create a new issue in the project "Infrastructure (INFRA)" with the component "Mirrors". Include the following information in the _Description_ field:

  - URL of mirror:
  - (optional) rsync mirror: `rsync://rsync.your.org/apache/`
  - Country where the mirror is located:
  - Contact email address:
  - Update frequency (2-4 times per day):
  - Rsync repository used:
  - I use these rsync options:
  - I have configured my Apache HTTP server as requested (yes/no):
  - I have subscribed the contact address to mirrors@apache.org (yes/no):
  - At the moment, I rsync from this IP address: (your IP address here)
  - I am checking the output from the rsynch job on a regular basis

We only use the IP address to check the logs before we add the mirror to the list. Once your mirror is on the list, you can change the IP of the mirror without notifying us.

<h2 id="questions">Questions?<a class="headerlink" href="#questions" title="Permanent link">&para;</a></h2>

If you have any questions, feel free to raise them in your Jira ticket (component "Mirrors") or on the mirror maintainers' public mailing list `mirrors@apache.org`. You don't need to subscribe to the list in order to post (but a short note in your signature that you request replies to be CC'd to you would help).

_information will move here from https://www.apache.org/info/how-to-mirror.html_
