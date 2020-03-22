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



<h3 id="custom">Project-specific download script</h3>


_information moving here from https://www.apache.org/dev/release-download-pages.html_
