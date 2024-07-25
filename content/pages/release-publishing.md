Title: Release Creation Process

These best practices help guide a PMC through the steps to create and publish an Apache software product release. It complements the formal <a href="https://www.apache.org/legal/release-policy.html" target="_blank">Apache Release Policy</a>, defining what must be in a software release, and [Release Distribution Policy](release-distribution.html).

Every Apache Software Foundation project software release must meet requirements for content, process, and publication. These requirements ensure that Apache contributors and users benefit from appropriate legal protection the ASF provides, and reflect the Foundation's goals of open, collaborative software development.

## Contents ##

  - <a href="#definition">An Apache release</a>
  - <a href="#releasemanager">The release manager</a>
  - <a href="#valid">A valid release package</a>
  - <a href="#signing">Signing release artifacts</a>
  - <a href="#voting">Voting whether to approve the release</a>
  - <a href="#distribution">Distribution</a>
    - <a href="#uploading">Uploading packages</a>
    - <a href="#normal">Normal distribution on the Apache downloads site</a>
    - <a href="#tomaven">Maven distribution</a>
  - <a href="#timeline">Release distribution availability schedule</a>
  - <a href="#faqs">FAQs</a>

<h2 id="definition">An Apache release<a class="headerlink" href="#definition" title="Permanent link">&para;</a></h2>

An Apache release is a set of **valid**, **signed**, artifacts, **voted on** by the appropriate PMC and **distributed** on the official ASF release infrastructure. See below for discussion of the words in bold, all of which are essential.

To make a release, an Apache project:

1. Has code that complies with the software licensing requirements
2. Decides as a community to make a release, and designates a release manager
3. The release manager prepares and signs the proposed release materials
4. The PMC votes whether to approve the release
5. If the vote passes, the release manager copies the artifacts to the distribution infrastructure.

A release starts when the project community agrees to make a release. However, no release manager can make a valid release unless the community has taken the necessary steps. The source code and build process must comply with the ASF legal and intellectual property requirements for a valid release, and the project must have the infrastructure in place to correctly **sign** the release artifacts (see below).

<h2 id="releasemanager">The release manager<a class="headerlink" href="#releasemanager" title="Permanent link">&para;</a></h2>

Most projects designate a committer to be the _release manager_ who takes responsibility for the mechanics of a release. It is a good idea to let several committers take this role on different releases so that more than one person is comfortable doing a release. Release managers shepherd a release from an initial community consensus to getting the compiled code package to final distribution, and may be involved in publicizing the release to the project's community and the ASF in general.

By default, only PMC members can publish release artifacts to https://dist.apache.org/repos/dist/release/. If your project wishes to allow non-PMC member committers to publish release artifacts, please [contact infrastructure](contact.html) with your request. Note that there are only two options: PMC members can publish release artifacts, or Committers can publish release artifacts. Allowing Commmitters to publish release artifacts will require project consensus, so include a link to an email thread with that consensus.

***Release managers do the mechanical work; but the PMC in general, and the PMC chair in particular (as an officer of the Foundation), remains responsible for compliance with ASF requirements.***

<h2 id="valid">A valid release package<a class="headerlink" href="#valid" title="Permanent link">&para;</a></h2>

The Apache Software Foundation exists to create open source software, so the fundamental requirement for a release is that it has the necessary source code to build the project. A project may provide compiled binaries of each release for the convenience of users.

All project source code must be covered by the <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank">Apache License, version 2.0</a>. The license or appropriate boilerplate text must be included in each source file. For the license to be valid, the code must have been contributed by an individual covered by an appropriate <a href="https://www.apache.org/licenses/contributor-agreements.html" target="_blank">contributor license agreement</a>, or have otherwise been licensed to the Foundation and passed through IP clearance. See <a href="https://www.apache.org/legal/release-policy.html" target="_blank">this page</a> for details on release requirements. When in doubt, contact the Foundation's Legal resources by filing a Jira ticket under the 'LEGAL' project. The Apache <a href="https://creadur.apache.org/rat/" target="_blank">Release Audit Tool (RAT)</a> can help you verify that your proposed release complies with the requirements.

Many projects have dependencies on non-Apache components. For an Apache release to be valid, it can only depend on non-Apache components that have compatible licenses. For more information on third party licenses allowed, see the <a href="https://www.apache.org/legal/resolved.html" target="_blank">ASF Third Party License Policy</a>.

<h2 id="signing">Signing release artifacts<a class="headerlink" href="#signing" title="Permanent link">&para;</a></h2>

The files that make up an Apache release always are accompanied by cryptographic signatures. This allows users to ensure that the files have not been tampered with since they were created. The mechanics of signing depend on the project's build technology. Infra strongly recommends that projects set up automated infrastructure to sign the files to simplify the work. Generally, projects set up their build system so that the same process that creates the files for a release also signs them.

The process of setting up to sign the code is somewhat complicated, and is described on the [release signing](release-signing.html) page. If you plan to serve as a release manager, you should generate a key and publish it well in advance of creating a release.

**Note** while your project can create and review as many release candidates as it wishes, and can use any automated build process that makes it easier and more reliable to create them, the project cannot publish any release candidate as an official release until it is approved by the voting process described below, and signed by a legal person. The ASF has **not** authorized a completely-automated process for both building and releasing artifacts that does not involve review and approval by the project's PMC and the signature of a human in the release artifact bundle.

<h2 id="voting">Voting whether to approve the release<a class="headerlink" href="#voting" title="Permanent link">&para;</a></h2>

A binding release vote of the PMC is the critical gating step in the release process. Without such a vote, the release is just a set of files prepared by an individual. After such a vote, it is a formal offering of the ASF, backed by the "full faith and credit" of the Foundation.

<h2 id="distribution">Distribution<a class="headerlink" href="#distribution" title="Permanent link">&para;</a></h2>

The Apache infrastructure _must_ be the primary source for all artifacts officially released by the ASF.

Infra maintains the Apache release distribution infrastructure, which has three parts:

- the directories of current releases on `downloads.apache.org`
- previous releases on `archive.apache.org`
- Maven repository on `repository.apache.org`

<h3 id="uploading">Uploading packages<a class="headerlink" href="#uploading" title="Permanent link">&para;</a></h3>

  - Upload development packages and snapshots to `https://dist.apache.org/repos/dist/dev/$project/`
  - Upload release packages to `https://dist.apache.org/repos/dist/release/$project/`. If your project uses a Subersion repository, you can use `svn mv` from the `dev` folder.
  - Incubator projects can find their dev/release folder inside their incubator directory.

<h3 id="normal">Normal distribution on the Apache downloads site<a class="headerlink" href="#normal" title="Permanent link">&para;</a></h3>

See the [Release Distribution Policy](release-distribution.html) for specific technical requirements.

Each Apache TLP has a `release/TLP-name` directory in the distribution Subversion repository at `https://dist.apache.org/repos/dist/`. Once a release vote passes, the release manager adds the release artifacts (plus signature and hash files) to this location. Each project is responsible for the structure of its directory. [PyPubSub](pypubsub.html) pushes the contents of these directories to `http://downloads.apache.org/`. **Note** only store the most recent version of each supported release here.

  - **Do not** use the SVN directories under `https://dist.apache.org/repos/dist/` to link to product releases. Projects must use the ASF release system. See [Release Download Pages](release-download-pages.html) for further details.

  - A signature (`.asc`) can become invalid because the signing key is revoked or has expired. Make sure all current signatures for your project in `downloads.apache.org/` are valid.

  - Hash, signature and KEYS files are excluded from the public release:

`*.md5 *.sha *.sha1 *.sha256 *.sha512 *.asc *.sig KEYS *.mds MD5SUM SHA*SUM`

  - **Do not** publish `.md5` files because MD5 is broken.
  - **Do not** publish `.sig` files. Make sure your `.asc`s are plain-text files.
  - The download page should use `HTTPS:` rather than plain `HTTP:` for linking to KEYS, sigs and hashes (for example: `https://downloads.apache.org/httpd/KEYS`).

  - In addition to the checksum files required in the [Release Distribution Policy](release-distribution.html), the project can provide an `MD5SUM` or `SHA*SUM`. `MD5SUM` and `SHA*SUM` must look like the output of `md5sum(1)`: lines containing a checksum, followed by a filename ; use only plain file names (no slashes). Do not use any other file names for such files.

If the release directory does not yet exist, please create a Jira ticket for INFRA with the required information (see the [contact](contact.html) page).

**Note**: By default, only PMC/PPMC members have write access to the `dist/release` directories. The `dist/dev` directories by default allow write access by committers.

<h3 id="tomaven">Maven distribution<a class="headerlink" href="#tomaven" title="Permanent link">&para;</a></h3>

See [Publishing Maven releases](publishing-maven-artifacts.html).

<h2 id="timeline">Release distribution availability schedule<a class="headerlink" href="#timeline" title="Permanent link">&para;</a></h2>

Releases pushed to the `dist/release` subversion directory will be available for download almost immediately after the push/move operation has completed, 
though the exact speed depends on the size of the artifact(s) that have been uploaded. Generally speaking, releases should be available on 
[downloads.apache.org](https://downloads.apache.org/) within 15 minutes of publishing them to `dist/release`.


Our global content delivery network (CDN) at [dlcdn.apache.org](https://dlcdn.apache.org/) will have files available for download within 
seconds of them appearing on downloads.apache.org. However, due to our current caching algorithms, they may not appear in the raw directory listings 
for up to two hours even though the files are present on the service. We are currently working on ways to improve this experience, and will 
update this page when/if the process has changed.


Our [download helper script](release-download-pages.html#download-scripts) also employ caching to help speed up processing, and its findings 
(whether or not a release is present on the CDN) may be delayed by up to an hour in some circumstances. We therefore advise projects to wait 
for one hour after publishing a release before announcing it to the wider public.

As a rule of thumb, projects should currently:

1. upload or move the release to the `dist/release` space in subversion
2. after a few minutes, check [downloads.apache.org](https://downloads.apache.org/) for whether their release has been published on our download server
3. when the download is present, wait one hour for any caching to reset, then announce the general availability of the release


<h2 id="faqs">FAQs<a class="headerlink" href="#faqs" title="Permanent link">&para;</a></h2>

  - **How do I archive an old release?** `downloads.apache.org` is automatically archived every four hours. Therefore, a copy of every official release exists in the archives. Just delete the copy of the release that is in your project's dist directory. Remember to update any links from the download page related to that release.
