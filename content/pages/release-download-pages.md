Title: Release Download Pages for Projects
license: https://www.apache.org/licenses/LICENSE-2.0

Your project's release download page is where people can download your product's latest release(s). This page describes how a release manager can put such a page together.

Review

  - the policy on [release distribution](release-distribution.html) if you are unsure of the best way to use the project download page
  - guidelines on [signing releases](release-signing.html)

## Contents ##

<ul>
<li><a href="#links">Download links</a></li>
<li><a href="#download-page">Your Apache project's download page</a></li>
<li><a href="#download-scripts">Using the closer.lua download script</a></li>
<li><a href="#best_practice">Best practices</a></li>
<li><a href="#stats">Download statistics</a></li>
<li><a href="#questions">Questions?</a></li>
</ul>

<h2 id="links">Download links<a class="headerlink" href="#links" title="Permanent link">&para;</a></h2>

  - Your project's download page can only link to release artifacts that your PMC has approved.
  - Do not link directly to `dist.apache.org`.
  - The download page **must** include a link to the source distribution. It **may** include links to binary distributions.
  - Use **closer.lua**, the standard mechanism to distribute Apache downloads. See below for details.
  - All links to checksums, detached signatures and public keys **must** reference the Apache Distribution Directory (<a href="https://downloads.apache.org/" target="_blank">downloads.apache.org</a>) and use `https://` (SSL). For example: `https://downloads.apache.org/httpd/KEYS`.
  - All releases are automatically <a href="https://www.apache.org/legal/release-policy.html#how-to-archive" target="_blank">archived</a>. You may continue to link to recent releases, as well as the latest one, from the download page, as a convenience for the user community. You **should** remove links to older releases that you no longer support.
  - Remove all official pre-releases (e.g. milestones, alphas, betas) in a timely fashion once the project releases the final or GA version.
  
<h2 id="download-page">Your Apache project's download page<a class="headerlink" href="#download-page" title="Permanent link">&para;</a></h2>

Your Apache project's download page:

  - **must** have at least one link to the current release. This link **must** use the `closer.lua` utility. For example: `https://www.apache.org/dyn/closer.lua/PROJECT/VERSION/SOURCE-RELEASE`. (Note: the `mirrors.cgi` and `closer.cgi` scripts have been deprecated. Calls to them redirect to `closer.lua`.)
  - **must** have a link to the checksum for the current release. These links **must** use direct links to the Apache distribution server. For example: `https://downloads.apache.org/PROJECT/VERSION/CHECKSUM`.
  - **must** have a link to the KEYS file for your project on the Apache distribution server. For example: `https://downloads.apache.org/PROJECT/KEYS`.
  - **must** have a link to the signature file for each release. See the [release signing](release-signing.html) page for more information. 
  - **should** have instructions on how to verify downloads. For this you can include a link to the <a href="https://www.apache.org/info/verification.html" target="_blank">Apache documentation on verification</a>.
  - **must not** include a download link to the top-level `closer.lua` utility (e.g. `http://www.apache.org/dyn/closer.lua/PROJECT`).

<h3 id="current-and-older-releases">Current and older releases<a class="headerlink" href="#current-and-older-releases" title="Permanent link">&para;</a></h3>

  - Do **not** keep software distributions on your project's website. Move them to one of the two software distribution sites:

  - **Current public releases** appear on `downloads.apache.org/`. Place current, official releases that the PMC has approved for end-users on the main public release site. Make all changes at <a href="https://dist.apache.org/repos/dist/release/" target="_blank">`https://dist.apache.org/repos/dist/release/`</a>.

  - **Older releases** that you no longer recommend to the general public still appear on `archive.apache.org/dist/`. This site automatically contains all the content that has ever appeared on `downloads.apache.org/`. It is rarely necessary to touch this site, except during a reorganization. Once your project no longer recommends public use of a particular release, delete it from `downloads.apache.org/dist/` by removing it from <a href="https://dist.apache.org/repos/dist/release/" target="_blank">https://dist.apache.org/repos/dist/release/</a>, and removing the link to it from your download page. It remain on the archive site.

To remove an old release from the release area, use a command of the form:

```svn del -m"Archiving release m.n" https://dist.apache.org/repos/dist/release/<project>/etc/m.n```

You can use this for release directories or individual files (if multiple releases are present in a single directory).

<h2 id="download-scripts">Using the closer.lua download script<a class="headerlink" href="#download-scripts" title="Permanent link">&para;</a></h2>

Apache project download pages **must** use a closer.lua script. You'll find below a standard mechanism to let you easily create scripts that comply with the ASF distribution policy.

There are two options:

  - The <a href="#closer">closer.lua download script</a> is quick to set up. The project documentation links to it (rather than integrating it).
  - A <a href="#custom">project-specific script</a>, which in the end calls `closer.lua` integrated with a page created in the normal way for the project and uses the project's standard document look and feel. This option takes more time to set up.
  
<h3 id="closer">Generic closer.lua download script<a class="headerlink" href="#closer" title="Permanent link">&para;</a></h3>

The starting point for using the generic `closer.lua` script is a download page in your project's standard documentation which describes the releases. To use the generic script: 

  - Alter the page so the download link points to `closer.lua`.
  - Pass in the relative path from the distribution root to the artifact as a parameter.

If the artifact is `foo-5.5.1.zip` and it is located in `bar/foo` relative to `downloads.apache.org`, then the link `http://www.apache.org/dyn/closer.lua/bar/foo/foo-5.5.1.zip` provides the link for downloading.

As an alternative, you can generate a direct download link using the following syntax:

`http://www.apache.org/dyn/closer.lua/bar/foo/foo-5.5.1.zip?action=download`

**Note**: there is some information which every project should include on the download page (e.g. KEYS and signatures). Please read about <a href="#best_practice">best practices</a> for download pages.

<h3 id="custom">Project-specific download script<a class="headerlink" href="#custom" title="Permanent link">&para;</a></h3>

To use a project-specific download script, create a project page containing information for the user about the release to download, together with variables the script populates with the appropriate values.

Assuming you have called your download page `download.html`, you can invoke our global download script by using the URI `download.cgi`.

This URI takes the path to the page as an input and passes it to `closer.lua`. When you link to the project page (for example, from the rest of the project documentation), it is important to target these links at the script address (and not the HTML page address).

There is no requirement to name the script `download.cgi` and the download release page `download.html`, but the name of the script **must** correspond to the name of the download page. For example:

  - `release.cgi` and `release.html` will work
  - `download.cgi` and `release.html` will **not** work


There are a number of elements that a good project download page should contain. See the content to generate that page <a href="https://svn.apache.org/repos/asf/httpd/site/trunk/content/download.mdtext" target="_blank">here</a>.
Alternately, you can get inspiration from the [default download template](https://github.com/apache/infrastructure-p6/blob/production/modules/closer_cgi/files/closer.html) that will be used when no custom HTML template exists for a project.

A variable URL links to downloadable artifacts. The download script substitutes the correct base URL for the `[preferred]` variable. The rest of the URL should be the path to the artifact relative to the base of the Apache distribution directory.

For example, for artifact `foo-1.0.0.tar.gz` contained in `bar/foo`, use `[preferred]/bar/foo/foo-1.0.0.tar.gz`

Provide links to the checksum and signature for the artifact next to the download link. It is important that users check the sum and verify the signature, so these links should be close and clear.

For example, for artifact foo-1.0.0.tar.gz contained in bar/foo :

```
`<a href="[preferred]/bar/foo/foo-1.0.0.tar.gz">zip</a>`
`<a href='https://downloads.apache.org/bar/foo/foo-1.0.0.tar.gz.asc'>PGP</a>`
```

More advice on creating a good project page is [below](#best_practice).

All that remains is to wait for the main website to sync with the new page.

<h2 id="best_practice">Best practices<a class="headerlink" href="#best_practice" title="Permanent link">&para;</a></h2>

<h3 id="remind-users">Remind users to check sums and signatures</h3>

It is important that users understand that they should always verify the check sums and (if possible) the OpenPGP compatible signature of each file they download. The content of the release download page plays a critical role in this education process.

Provide clear and easy links to the KEYS, sums and signatures from the download release page or include the information directly in the page itself. The <a href="https://httpd.apache.org/download.cgi" target="_blank">HTTPD page</a> is a good example.

Include a reminder text with links to more information for users. For example:

```
Note: when downloading, please check the
<a href="https://infra.apache.org/release-signing.html#sha-checksum" target="_blank">sha checksum</a>
and verify the 
<a href="https://www.infra.apache.org/release-signing#openpgp" target="_blank">OpenPGP compatible signature</a> 
from the <a href="https://www.apache.org" target="_blank">main Apache site</a>. 
Links are provided above (next to the release download link).
This <a href="https://downloads.apache.org/ws/axis2/KEYS" target="_blank">KEYS file</a> 
contains the public keys used for signing release. We recommend that you use a web of trust, if possible, to confirm the identity of these keys.
For more information, please see the <a href="https://www.apache.org/dev/release.html" target="_blank">Apache Release FAQ</a>.
```

<h3 id="linked-urls">Make sure the browser displays linked URLs<a class="headerlink" href="#linked-urls" title="Permanent link">&para;</a></h3>

Users need to be able to verify the origin of the artifacts, signatures and sums they download. Check that the stylesheets your download site uses do not obscure the linked URLs. It is best to use a simple, plain style for download links. Note that some of the Maven-style sheets may obscure some external links in some browsers.

<h3 id="less-than-24hr">Timing your release announcement<a class="headerlink" href="#less-than-24hr" title="Permanent link">&para;</a></h3>

Your release will be available almost immediately after you upload it to `https://downloads.apache.org/`, please refer to this [release distribution timeline](release-publishing.html#timeline) document for details.

<h2 id="stats">Download statistics<a class="headerlink" href="#stats" title="Permanent link">&para;</a></h2>

You can review downloads of your project's releases by day, week, month or quarter at our <a href="https://logs.apache.org/stats/">download statistics site</a>. Only project committers can access the page, but they can view download statistics for any Apache project.

<h2 id="questions">Questions?<a class="headerlink" href="#questions" title="Permanent link">&para;</a></h2>

If you need assistance in implementing this policy, contact the `users@infra.apache.org` mailing list.
