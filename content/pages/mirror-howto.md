Title: How to be an Apache Software Foundation download mirror

The Apache Software Foundation has mirror sites all around the world, but we are always looking for additional reliable and well-connected sites that can help us distribute our software by mirroring our main software distribution directory.

## Requirements ##

We have a few requirements for those wishing to run a mirror:

  - We select https mirrors as "preferred" mirrors. We do add ftp mirrors to our list, but we no longer accept http mirrors.
  - At least 100 GB of available disk space. The current distribution directory is around 50 GB, but we wish to leave room for considerable expansion.
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





_information will move here from https://www.apache.org/info/how-to-mirror.html_
