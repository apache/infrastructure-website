Title: How to be an Apache Software Foundation download mirror

The Apache Software Foundation has mirror sites all around the world, but we are always looking for additional reliable and well-connected sites that can help us distribute our software by mirroring our main software distribution directory.

## Requirements ##

We have a few requirements for those wishing to run a mirror:

  - At least 90 GB of available disk space. The current distribution directory is around 45 GB, but we wish to leave room for considerable expansion.
  - You may mirror either the full distributions tree, or a reduced tree that excludes a few very resource-intensive (disk-wise and bandwidth-wise) projects.
  - You must not trim or abridge the mirrored tree in any way.
  - You must not modify the mirrored tree in any way. In particular, HEADER.html and README.html files must not be altered or removed. See below for adding sponsor information.
  - Your mirror must not be shown "inside" another site using, for instance, frames. 
  - You must do an **update-check** at least onc and preferably twice a day. You may sync a maximum of four times per day, but only if you have a slow or poor connection that causes timeouts.
  - You must subscribe to the mailing list for mirror maintainers (see below).

In addition, we require that you run the Apache HTTP Server version 2.2 or later and use the following configuration for your web mirror to allow all the features of our download site to function optimally:

_information will move here from https://www.apache.org/info/how-to-mirror.html_
