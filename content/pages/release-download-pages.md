Title: Release Downoload Pages for Projects

Your project's release download page links the project's content to the mirrors where people can download your latest release(s). This page describes how a release manager can put such a page together.

Material about Apache's policies on releases, mirrors, and download pages is <a href="https://www.apache.org/dev/mirrors" target="_blank">here</a>.

## Contents ##

<ul>
<li><a href="#links">Download links</a></li>
<li><a href="#download-page">Your Apache project's download page</a></li>
<li><a href="#download-scripts">Download scripts</a></li>
<li><a href="#best_practice">Best practices</a></li>
<li><a href="#less-than-24hr">Support for bypassing the 24 hour rule</a></li>
<li><a href="#resources">Resources</a></li>
<li><a href="#questions">Questions?</a></li>
<li><a href="#help">Help improve this document</a></li>
</ul>

<h2 id="links">Download links</h2>

  - Your project's download page can only link to release artifacts that your PMC has approved.
  - Do not link to `dist.apache.org`.
  - The download page must include a link to the source distribution. It may include links to binary distributions.
  - Links to the mirrored distribution artifacts must not reference the main Apache download server. They should use the standard mechanisms to distribute the load between the mirrors. See below for details.
  - All links to checksums, detached signatures and public keys must reference the main Apache web site and should use `https://` (SSL). For example: `https://downloads.apache.org/httpd/KEYS`.
  - Old releases should be <a href="https://www.apache.org/legal/release-policy.html#how-to-archive" target="_blank">archived</a> and may be linked from the download page.
  - Remove all official pre-releases (e.g. milestones, alphas, betas) in a timely fashion once the project releases the final or GA version.
  
<h2 id="download-page">Your Apache project's download page</h2>

Your Apache project's download page:

  - must have at least one link to the current release. This link must use the "closer" utility. For example: `https://www.apache.org/dyn/closer.lua/PROJECT/VERSION/SOURCE-RELEASE`.
  - must have a link to the checksum and hash for the current release. These links must use direct links to the Apache distribution server. For example: `https://downloads.apache.org/PROJECT/VERSION/HASH-OR-CHECKSUM`.
  - must have a link to the keys file for your project. This link must use direct links to the Apache distribution server. For example: `https://downloads.apache.org/PROJECT/KEYS`.
  - should have instructions on how to verify downloads. For this you can include a link to the <a href="https://www.apache.org/info/verification.html" target="_blank">Apache documentation on verification</a>.
  - must not include a link to the top level "closer" utility (e.g. `http://www.apache.org/dyn/closer.cgi/PROJECT`) as the KEYS, sigs and hashes are missing, as are any verification instructions.
  
<h2 id="download-scripts">Download scripts</h2>

Balancing the downloads between mirrors requires the use of a script. You'll find below a standard mechanism to let you easily create scripts that comply with the ASF mirroring distribution policy and take advantage of more advanced features such as intelligent selection of a preferred mirror.

There are two basic options:

  - The <a href="#closer">generic download script</a> is quick to set up but is linked from (rather than integrated with) the project documentation.
  - A <a href="#custom">project-specific script</a> is integrated with a page created in the normal way for the project and uses the project's standard document look and feel. This option takes more time to set up.
  
<h3 id="closer">Generic download script</h3>

The starting point for a generic script is a download page in the standard documentation which describes the releases. To use the generic script, you need to alter the page so the actual download links to the generic script in the appropriate fashion.

The generic script is `closer.cgi`. Paaa in the relative path from the distribution root to the artifact as a parameter. So if the artifact is `foo-5.5.1.zip` and is located in `bar/foo` relative to `downloads.apache.org`, then `http://www.apache.org/dyn/closer.cgi/bar/foo/foo-5.5.1.zip` will display the mirrored distribution for downloading.

As an alternative, you can generate a direct download link using the following syntax:

`http://www.apache.org/dyn/closer.cgi?filename=bar/foo/foo-5.5.1.zip&action=download`

See below for how to generate a customised page of direct links using a mirror.

Note there is some information which every project should include on the download page (e.g. KEYS, sigs, hashes). Please read <a href="#best_practice">best practices</a>.

<h3 id="custom">Project-specific download script</h3>

To create a project-specific download page, you need:

  - a wrapper cgi script (for the standard python mirroring script)
  - a project page (containing information for the user together with variables the script populates with the correct values)

The script takes the path to the project page as an input and passes it to the standard mirroring script. The standard script reads the page and uses information about the mirrors to substitute values for the variables. When you link to the project page (for example, from the rest of the project documentation), it is important to target these links at the script address (and not the page address).

Conventionally, the wrapper script is called `download.cgi`. Create this in the same directory as the project page. This wrapper script sets up the correct directory and calls the mirroring script:

```
#!/bin/sh
# Wrapper around the standard mirrors.cgi script
exec /www/www.apache.org/dyn/mirrors/mirrors.cgi $*
```

The release download page should be generated in the same way as the rest of the project documentation. By convention, the name of the resulting page is `download.html`.

**Note**: the mirroring script guesses the download release page to be processed by matching file names. There is no requirement to call the script `download.cgi` and the download release page `download.html` but the name of the script must correspond to the name of the download page. For example, `release.cgi` and `release.html` will work but `download.cgi` and `release.html` will not.

There are a number of elements that a good project download page should contain. See the content to generate that page <a href="https://svn.apache.org/repos/asf/httpd/site/trunk/content/download.mdtext" target="_blank">here</a>.

Downloads of artifacts are linked to a mirror by a variable url. The correct mirroring base url will be substituted for the `[preferred]` variable. The rest of the url should be the path to the artifact relative to the base of the Apache distribution directory.

For example, for artifact `foo-1.0.0.tar.gz` contained in `bar/foo` should use `[preferred]/bar/foo/foo-1.0.0.tar.gz`

Provide links to the checksum and signature for the artifact next to the download link. It is important that users check the sum and verify the signature so these links should be close and clear. **Note**: these documents must _not_ be mirrored.

For example, for artifact foo-1.0.0.tar.gz contained in bar/foo :

```
`<a href="[preferred]/bar/foo/foo-1.0.0.tar.gz">zip</a>`
`<a href='https://downloads.apache.org/bar/foo/foo-1.0.0.tar.gz.md5'>MD5</a>`
`<a href='https://downloads.apache.org/bar/foo/foo-1.0.0.tar.gz.asc'>PGP</a>`
```

Give users information about the mirrors and the chance to choose a different mirror if they prefer. This is a little complex to describe, so here is a typical script:

```
<p>[if-any logo]
<a href="[link]"><img align="right" src="[logo]" border="0"
/></a>[end]
The currently selected mirror is <b>[preferred]</b>.  If you
encounter a problem with this mirror, please select another mirror.  If all
mirrors are failing, there are <i>backup</i> mirrors (at the
end of the mirrors list) that should be available.</p>

<form action="[location]" method="get" id="SelectMirror">
Other mirrors: <select name="Preferred">
[if-any http]
  [for http]<option value="[http]">[http]</option>[end]
[end]

[if-any ftp]
  [for ftp]<option value="[ftp]">[ftp]</option>[end]
[end]
[if-any backup]
  [for backup]<option value="[backup]">[backup]
  (backup)</option>[end]
[end]
</select>
<input type="submit" value="Change" />
</form>


<p>You may also consult the <a href="http://www.apache.org/mirrors/">complete list of mirrors</a>.</p>
```
More advice on creating a good project page is [below](#best_practice).

Before you commit the download script, make it executable. The CMS will not honor propset changes post-initial-commit, so if you forget this step please make the needed property changes on both the staging and production svn trees. See <a href="https://cwiki.apache.org/confluence/display/INFRA/Apache+CMS+reference" target="_blank">Apache CMS Reference</a> for details. Of course this caveat only applies to CMS sites; sites that use [pypubsub](pypubsub.html) or svnpubsub exclusively will apply propset changes automatically as soon as they are committed. For example:

```
% svn propset svn:executable '*' download.cgi
% svn commit
```

All that remains is to wait for the main website to sync.

<h2 id="best_practice">Best practices</h2>



_information moving here from https://www.apache.org/dev/release-download-pages.html_
