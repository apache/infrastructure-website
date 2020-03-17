Title: Release Distribution Policy

This policy governs how Apache software releases are distributed through the technical channels that Infra maintains. It complements the formal <a href="https://www.apache.org/legal/release-policy.html" target="_blank">Apache Release Policy</a>, which defines what must be in a software release, and the [Release Creation Process](release-creation.html) page, which describes the steps for a PMC to create a release.

## Release distribution channels ##

  - The Apache Software Foundation's official channel for distribution of current Apache software releases to the general public is `downloads.apache.org/`. This directory is automatically sync'd out to the ASF mirror network, and most users download releases from one of the ASF mirrors.
  - The public may also obtain Apache software from any number of downstream channels (rpm, deb, homebrew, etc.) which redistribute our releases in either original or derived form. The vast majority of such downstream channels operate independently of Apache.
  - Infra maintains a number of developer-only channels which facilitate distribution of unreleased software to consenting members of a development community.
  - All historic Apache releases are available from `archive.apache.org`.
  
## Release distribution directories ##

Every top-level project at Apache has its own public distribution directory, which is a subdirectory of `downloads.apache.org/`. Each PMC is responsible for all artifacts within their project's distribution directory.

Apache Incubator podlings cannot create official ASF releases; see the <a href="http://incubator.apache.org/guides/releasemanagement.html" target="_blank">Incubator documentation</a> for details and discussion.

## Public distribution ##

Projects **must** upload all official releases to the official distribution channel, `downloads.apache.org/`. Content suitable for the official distribution channel includes:

  - Official releases
  - "Convenience binaries", compiled code anyone can download and install
  - Cryptographic signatures and checksums
  - The KEYS file
  - README, CHANGES and similar documents describing distributed content

If an Apache PMC wishes to publish additional materials through the official distribution channel and there is any question about the suitability of said materials, the PMC **must** consult with the ASF Board before publishing.

## Distribution of unreleased materials ##

Unreleased materials, in original or derived form,

  -  **may** be distributed to consenting members of a project's development community
  -  **must not** be advertised to anyone outside of the project development community
  -  **must not** be distributed through `www.apache.org/dist` or `downloads.apache.org`
  -  **must not** be distributed through channels which encourage use by anyone outside the project development community

## Notify Infra before uploading large artifacts ##

Projects must coordinate with Infra in advance about releases of larger than 1GB of artifacts to mitigate strain on mirroring and download resources.

## Requirements for cryptographic signatures and checksums ##

For more information, see the [release signing](release-signing.html) page.

**Note**: <a href="https://www.ietf.org/rfc/rfc2119.txt" target="_blank">RFC 2119</a> describes how **must**, **should**, **should not** and similar terms are to be interpreted.

For every artifact distributed to the public through Apache channels, the PMC

  - **must** supply a valid OpenPGP-compatible ASCII-armored detached signature file.
  - **must** supply at least one checksum file.
  - **should** supply a SHA-256 and/or SHA-512 checksum file.
  - **SHOULD NOT** supply a MD5 or SHA-1 checksum file because these are deprecated.

For new releases, PMCs **must** supply SHA-256 and/or SHA-512 and **should not** supply MD5 or SHA-1. Existing releases do not need to be changed.

The names of signature and checksum files **must** be formed by adding to the name of the artifact the following suffixes:

  - .asc for a (ASCII-armored) PGP signature
  - .md5 for a MD5 checksum
  - .sha1 for a SHA-1 checksum
  - .sha256 for a SHA-256 checksum
  - .sha512 for a SHA-512 checksum

Regarding signature and checksum files:

  - Legacy suffix .sha s**should not be** be used and .sha files **should not** be provided.
  - Binary PGP signature .sig files **must not** be provided.
  - .mds files (containing checksums) **may** be provided.
  - Signature and checksum files for verifying distributed artifacts **should not** be provided, unless named as indicated above.
  
Regarding KEYS files:

  - Projects **must** publish a KEYS file in their distribution directory which contains all public keys used to sign artifacts.
  - Signing keys used at Apache **must** be published in the KEYS file and **should** be made available through the global public keyserver network. Signing keys **should** be linked into a strong web of trust.
  - Signing keys for new artifacts **must** be RSA and at least 2048 bit. New keys **should** be 4096 bit RSA. Signatures **should** be cryptographically strong.
  - Private keys **must not** be stored on any ASF machine. Likewise, signatures for releases **must not** be created on ASF machines.
  - Compromised signing keys **must** be revoked and replaced immediately.
  
## Download links ##

  - The website documentation for any Apache product **must** provide public download links where interested parties may obtain current official source releases and accompanying cryptographic files.
  - Links to mirrored distribution artifacts **must not** reference the main Apache web site. They **should** use the [standard mechanisms](mirror-howto.html) to distribute the load between the mirrors.
  - All links to checksums, detached signatures and public keys **must** reference `downloads.apache.org/` using `https://` (TLS).
  - Old releases **should** be archived and **MAY** be linked to from public download pages.
  
## Archiving releases ##

  - All releases **must** be archived on `archive.apache.org`. This generally happens via an automated process which adds releases to the archive about a day after they first appear on `downloads.apache.org/`.
  - Each project's distribution directory **should** contain the latest release in each branch that is currently under development. When development ceases on a version branch, releases of that branch **should** be removed.
  
## Using Maven for releases ##

Infra operates an Apache Maven repository manager at `repository.apache.org`. Projects **may** use the repository system as a downstream channel to redistribute released materials via Maven Central, and **may** use it to distribute snapshots containing unreleased materials directly to consenting members of a project development community.

Projects **must not** point or refer to `repository.apache.org` directly in download pages, release announcements or emails. Instead, any public download links for those releases **should** point to Maven Central.

Read more about [Maven releases for Apache projects](maven-releases.html).

## Policy administration ##

This policy is **required** for all Apache projects. The <a href="https://whimsy.apache.org/foundation/orgchart/vp-infra" target="_blank">V.P. of Apache Infrastructure</a> **must** approve changes to this policy.
