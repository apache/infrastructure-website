Title: Release Distribution Policy

<h1 id="policy"> </h1>

This policy governs how Apache software releases are distributed through the technical channels that Infra maintains and other distribution platforms. It complements the formal <a href="https://www.apache.org/legal/release-policy.html" target="_blank">Apache Release Policy</a>, which defines what must be in a software release, and the [Release Creation Process](release-publishing.html) page, which describes the steps for a PMC to create a release.

<h2 id="links">Contents</h2>

<ul>
<li><a href="#policy">Release Distribution Policy</a></li>
<li><a href="#channels">Release Distribution Channels</a></li>
<li><a href="#dist-dir">Release Distribution Directory</a></li>
<li><a href="#release-content">Release Content</a></li>
<li><a href="#public-distribution">Public Distribution</a></li>
<li><a href="#unreleased">Distribution of Unreleased Materials</a></li>
<li><a href="#heads-up">Notify Infra Before Uploading Large (&gt;1GB) artifacts</a></li>
<li><a href="#sigs-and-sums">Cryptographic Signatures and Checksums Requirements</a></li>
<li><a href="#download-links">Download Links Requirements</a></li>
<li><a href="#archival">Releases Must Be Archived</a></li>
<li><a href="#maven">Using Maven For Releases</a></li>
<li><a href="#administration">Policy Administration</a></li>
</ul>


<h2 id="channels">Release distribution channels<a class="headerlink" href="#channels" title="Permanent link">&para;</a></h2>

  - The Apache Software Foundation's official channel for distribution of current Apache software releases to the general public is `downloads.apache.org/`. This directory is automatically sync'd out to the ASF mirror network, and most users download releases from one of the ASF mirrors.
  - The public may also obtain Apache software from any number of downstream channels (rpm, deb, homebrew, etc.) which redistribute our releases in either original or derived form. The vast majority of such downstream channels operate independently of Apache.
  - Infra maintains a number of developer-only channels which facilitate distribution of unreleased software to consenting members of a development community.
  - All historic Apache releases are available from `archive.apache.org`.
  
<h2 id="dist-dir">Release distribution directory<a class="headerlink" href="#dist-dir" title="Permanent link">&para;</a></h2>

Every top-level project at Apache has its own public distribution directory, which is a subdirectory of `downloads.apache.org/`. Each PMC is responsible for all artifacts within their project's distribution directory.

Apache Incubator podlings cannot create official ASF releases; see the <a href="http://incubator.apache.org/guides/releasemanagement.html" target="_blank">Incubator documentation</a> for details and discussion.

<h2 id="release-content">Release content<a class="headerlink" href="#release-content" title="Permanent link">&para;</a></h2>

The <a href="http://www.apache.org/dev/release#what" target="_blank">Apache Release Policy</a> governs the content of official Apache releases and the process by which projects create valid releases.

The Policy specifies that binary packages provided by the project or third parties which meet certain criteria may be distributed alongside official source packages. Such packages are sometimes referred to as "convenience binaries" or PMC-approved artifacts to distinguish them from other binary packages.

<h2 id="public-distribution">Public distribution channels<a class="headerlink" href="#public-distribution" title="Permanent link">&para;</a></h2>

Projects **must** upload all official releases to the official distribution channel, `downloads.apache.org/`. Content suitable for the official distribution channel includes:

  - Official releases
  - PMC-approved artifacts, compiled code anyone can download and install
  - Cryptographic signatures and checksums
  - The <a href="#sigs-and-sums">KEYS</a> file
  - README, CHANGES and similar documents describing distributed content

If an Apache PMC wishes to publish additional materials through the official distribution channel and there is any question about the suitability of said materials, the PMC **must** consult with the ASF Board before publishing.

<h2 id="unreleased">Distribution of unreleased materials<a class="headerlink" href="#unreleased" title="Permanent link">&para;</a></h2>

Unreleased materials, in original or derived form,

  -  **may** be distributed to consenting members of a project's development community
  -  **must not** be advertised to anyone outside of the project development community
  -  **must not** be distributed through `www.apache.org/dist` or `downloads.apache.org`
  -  **must not** be distributed through channels which encourage use by anyone outside the project development community

<h2 id="heads-up">Notify Infra before uploading large artifacts<a class="headerlink" href="#heads-up" title="Permanent link">&para;</a></h2>

Projects must coordinate with Infra in advance about releases of larger than 1GB of artifacts to mitigate strain on mirroring and download resources.

<h2 id="sigs-and-sums">Requirements for cryptographic signatures and checksums<a class="headerlink" href="#sigs-and-sums" title="Permanent link">&para;</a></h2>

For more information, see the <a href="https://www.apache.org/dev/release-signing.html" target="_blank">release signing</a> page.

**Note**: <a href="https://www.ietf.org/rfc/rfc2119.txt" target="_blank">RFC 2119</a> describes how **must**, **should**, **should not** and similar terms are to be interpreted.

For every artifact distributed to the public through Apache channels, the PMC

  - **must** supply a valid OpenPGP-compatible ASCII-armored detached signature file.
  - **must** supply at least one checksum file.
  - **should** supply a SHA-256 and/or SHA-512 checksum file.
  - **SHOULD NOT** supply a MD5 or SHA-1 checksum file because these are deprecated.

For new releases, PMCs **must** supply SHA-256 and/or SHA-512 and **should not** supply MD5 or SHA-1. Existing releases do not need to be changed.

The names of signature and checksum files **must** be formed by adding to the name of the artifact the appropriate suffix:

  - `.asc` for a (ASCII-armored) PGP signature
  - `.sha256` for an SHA-256 checksum
  - `.sha512` for an SHA-512 checksum
  
Noted for completeness that this specification also applies to **deprecated** file types:

  - `.md5` for an MD5 checksum
  - `.sha1` for an SHA-1 checksum

Regarding signature and checksum files:

  - Legacy suffix `.sha` **should not be** be used and `.sha` files **should not** be provided.
  - Binary PGP signature `.sig` files **must not** be provided.
  - `.mds` files (containing checksums) **may** be provided for individual files.
  - Signature and checksum files for verifying distributed artifacts **should not** be provided, unless named as indicated above.
  
Regarding KEYS files:

  - Projects **must** publish a KEYS file in their distribution directory which contains all public keys used to sign artifacts.
  - Signing keys used at Apache **must** be published in the KEYS file and **should** be made available through the global public keyserver network. Signing keys **should** be linked into a strong web of trust.
  - Signing keys for new artifacts **must** be RSA and at least 2048 bit. New keys **should** be 4096 bit RSA. Signatures **should** be cryptographically strong.
  - Private keys **must not** be stored on any ASF machine. Likewise, signatures for releases **must not** be created on ASF machines.
  - Compromised signing keys **must** be revoked and replaced immediately.
  
<h2 id="download-links">Download links<a class="headerlink" href="#download-links" title="Permanent link">&para;</a></h2>

  - The website documentation for any Apache product **must** provide public download links where interested parties may obtain current official source releases and accompanying cryptographic files.
  - Links to mirrored distribution artifacts **must not** reference the main Apache web site. They **should** use the [standard mechanisms](how-to-mirror.html) to distribute the load between the mirrors.
  - All links to checksums, detached signatures and public keys **must** reference `downloads.apache.org/` using `https://` (TLS).
  - Old releases **should** be archived and **MAY** be linked to from public download pages.
  
<h2 id="archival">Archiving releases<a class="headerlink" href="#archival" title="Permanent link">&para;</a></h2>

  - All releases **must** be archived on `archive.apache.org`. This generally happens via an automated process which adds releases to the archive about a day after they first appear on `downloads.apache.org/`.
  - Each project's distribution directory **should** contain the latest release in each branch that is currently under development. When development ceases on a version branch, releases of that branch **should** be removed.
  
<h2 id="maven">Using Maven for releases<a class="headerlink" href="#maven" title="Permanent link">&para;</a></h2>

Infra operates an Apache Maven repository manager at `repository.apache.org`. Projects **may** use the repository system as a downstream channel to redistribute released materials via Maven Central, and **may** use it to distribute snapshots containing unreleased materials directly to consenting members of a project development community.

Projects **must not** point or refer to `repository.apache.org` directly in download pages, release announcements or emails. Instead, any public download links for those releases **should** point to Maven Central.

Read more about [Maven releases for Apache projects](publishing-maven-artifacts.html).

<h2 id="other-platforms">Other Release Platforms<a class="headerlink" href="#other-platforms" title="Permanent link">&para;</a></h2>

The ASF manages a number of distribution platforms that projects are welcome to use. Projects can distribute PMC-approved artifacts on ASF managed distribution platforms and other distribution platforms as long as those binaries comply with ASF release, licensing, branding and trademark policies. Currently ASF managed platforms include <a href="https://github.com/apache" target="_blank">github</a> and <a href="https://hub.docker.com/u/apache" target="_blank">docker</a>.

<h2 id="administration">Policy administration<a class="headerlink" href="#administration" title="Permanent link">&para;</a></h2>

This policy is **required** for all Apache projects. The <a href="https://whimsy.apache.org/foundation/orgchart/vp-infra" target="_blank">V.P. of Apache Infrastructure</a> **must** approve changes to this policy.
