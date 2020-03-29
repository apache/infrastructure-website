Title: Applying the Apache license, version 2.0

This document is to help Apache developers understand what they need to do to apply the <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank">Apache License, Version 2.0</a> or _ALv2_ to Apache software, including source code, documentation, and binary distributions. It is descriptive guidance, and does not supplant or otherwise modify any of the terms within the license itself. In case of uncertainty, consult <a href="https://www.apache.org/legal" target="_blank">general Apache policy</a>.

Information on other Apache-related licenses and updates regarding compatibility with other <a href="https://www.opensource.org" taarget="_blank">open source</a> licenses appears in the <a href="https://www.apache.org/licenses/" target="_blank">Licenses</a> section.

<h2>Contents</h2>

<ul>
<li><a href="#license">Understanding the 2.0 license</a></li>
<li><a href="#new">Applying the license to new software</a></li>
<li><a href="#existing">Updating Existing Software</a></li>
<li><a href="#faq-existing">Frequently Asked Questions (Updates)</a><ul>
<li><a href="#convert_to_2_0">Do I have to convert Apache 1.1 licenses to 2.0 licenses in source code?</a></li>
<li><a href="#convert-all">When do I have to convert ASF code to the new license?</a></li>
<li><a href="#conversion">Do I have to convert old versions and branches of code to the new license?</a></li>
<li><a href="#deadline">Does that mean live branches of code all have to be updated by 1 March 2004?</a></li>
</ul>
</li>
<li><a href="#faq">Frequently Asked Questions (General)</a><ul>
<li><a href="#info-whereis">Where Can I Find More Information?</a></li>
<li><a href="#policy-whereis">Where Can I Find Policy?</a></li>
<li><a href="#license-whereis">Where do I find a copy of the new license?</a></li>
<li><a href="#copy-per-file">Do I have to have a copy of the license in each source file?</a></li>
<li><a href="#attribution">In my current source files I have attribution notices for other works. Do I put this in each source file now?</a></li>
<li><a href="#contributor-copyright">Can/Should individual committers added copyright statements to the NOTICE or source code files?</a></li>
<li><a href="#license-file-name">Can the LICENSE and NOTICE files be called LICENSE.txt and NOTICE.txt?</a></li>
<li><a href="#license-include">Should the license be included in source files for documentation (e.g. XML that is transformed to HTML)?</a></li>
</ul>
</li>
</ul>



<h2 id="license">Understanding the 2.0 license</h2>
<p>The ALv2 is <a href="https://www.apache.org/licenses/LICENSE-2.0.txt" target="_blank">this set</a> of self-documented copyright and patent licensing terms. Anyone can use the license, not just the <abbr title="Apache Software Foundation">ASF</abbr> and its projects, and can be <a href="https://www.apache.org/licenses/LICENSE-2.0.html#apply" target="_blank">applied</a> by reference to the versioned license terms. An appendix to the license describes how to do this.

**Note** that the ASF does not use copyright assignment and that the original authors retain the copyrights for individual parts of the collective work . The method described in the appendix is only suitable for copyright owners, so the ASF uses a variation of
this method.

<p>Section 4d of the <a href="http://www.apache.org/licenses/LICENSE-2.0.txt">license</a>
provides for attribution notices to be included with a work in a 
<a href="http://www.apache.org/licenses/example-NOTICE.txt">NOTICE</a> file, such that 
the attribution notices will remain, in some form, within any derivative works.
Apache projects <a href="http://www.apache.org/legal/src-headers.html#notice">MUST</a>
include correct NOTICE documents in every distribution.  </p>
<h1 id="new">Applying the license to new software<a class="headerlink" href="#new" title="Permanent link">&para;</a></h1>
<p>To apply the <abbr title="Apache License, Version 2.0">ALv2</abbr> to a new software distribution, include one copy of the
license text by copying the file:</p>
<p><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">http://www.apache.org/licenses/LICENSE-2.0.txt</a></p>
<p>into a file called LICENSE in the top directory of your distribution.
If the distribution is a jar or tar file, try to add the LICENSE file
first in order to place it at the top of the archive. This covers
the collective licensing for the distribution.</p>
<p>In addition, a correct NOTICE file
<a href="http://www.apache.org/legal/src-headers.html#notice">MUST</a>
be included in the same directory as the LICENSE file.</p>
<p>Each original source document (code and documentation, but excluding the 
LICENSE and NOTICE files) <a href="http://www.apache.org/legal/src-headers.html#headers">SHOULD</a>
include a short license header at the top. If the distribution contains 
documents not covered by <a href="http://www.apache.org/licenses/icla.txt"><abbr title="Individual Contributor License Agreement">CLA</abbr></a>,
<a href="http://www.apache.org/licenses/cla-corporate.txt"><abbr title="Corporate Contributor License Agreement">CCLA</abbr></a> or
<a href='http://www.apache.org/licenses/software-grant.txt'>Software Grant</a>
(such as third-party libraries) then see the
<a href='http://www.apache.org/legal/resolved.html'>policy guide</a>.</p>
<h1 id="existing">Updating Existing Software<a class="headerlink" href="#existing" title="Permanent link">&para;</a></h1>
<p>In brief, the aim is to achieve a final distribution as described above in
<a href="#new">applying the license to new software</a>. Some conversion tools are 
listed <a href="http://www.apache.org/legal/src-headers.html#faq-update-scripts">here</a>.</p>
<h1 id="faq-existing">Frequently Asked Questions (Updates)<a class="headerlink" href="#faq-existing" title="Permanent link">&para;</a></h1>
<h2 id="convert_to_2_0">Do I have to convert Apache 1.1 licenses to 2.0 licenses in source code?<a class="headerlink" href="#convert_to_2_0" title="Permanent link">&para;</a></h2>
<p>If the code is owned or distributed by the Apache Software Foundation, then
the answer is <strong>Yes</strong>.  The 2.0 license was approved by the <abbr title="Apache Software Foundation">ASF</abbr> board
in their January 2004 meeting.  As part of that meeting, the board mandated
that all <abbr title="Apache Software Foundation">ASF</abbr> software distributions must be converted to the new license
by March 1, 2004.</p>
<p>If the code is not owned by the <abbr title="Apache Software Foundation">ASF</abbr>, then the decision is up to the copyright
owner.  Naturally, we strongly recommend that you upgrade to the new license.</p>
<h2 id="convert-all">When do I have to convert <abbr title="Apache Software Foundation">ASF</abbr> code to the new license?<a class="headerlink" href="#convert-all" title="Permanent link">&para;</a></h2>
<p>All code released after 1 March 2004 must have been converted.</p>
<h2 id="conversion">Do I have to convert old versions and branches of code to the new license?<a class="headerlink" href="#conversion" title="Permanent link">&para;</a></h2>
<p>Only if you want the <abbr title="Apache Software Foundation">ASF</abbr> to make a new release of that code after 1 March 2004.
"Dead" branches of code do not have to be updated.</p>
<h2 id="deadline">Does that mean live branches of code all have to be updated by 1 March 2004?<a class="headerlink" href="#deadline" title="Permanent link">&para;</a></h2>
<p>Code has to be updated prior to any release after 1 March 2004.  However code
in the source repository can remain under the old 1.1 license until such time
as you are ready to perform a release.  Note that this applies to <strong>any</strong>
kind of release after 1 March 2004 - including bug fixes.</p>
<h1 id="faq">Frequently Asked Questions (General)<a class="headerlink" href="#faq" title="Permanent link">&para;</a></h1>
<h2 id="info-whereis">Where Can I Find More Information?<a class="headerlink" href="#info-whereis" title="Permanent link">&para;</a></h2>
<p>The legal affairs <a href="http://www.apache.org/legal">home page</a>.</p>
<h2 id="policy-whereis">Where Can I Find Policy?<a class="headerlink" href="#policy-whereis" title="Permanent link">&para;</a></h2>
<p>Follow links from the legal affairs <a href="http://www.apache.org/legal">home page</a>.</p>
<h2 id="license-whereis">Where do I find a copy of the new license?<a class="headerlink" href="#license-whereis" title="Permanent link">&para;</a></h2>
<p><a href="http://www.apache.org/licenses/">http://www.apache.org/licenses/</a></p>
<h2 id="copy-per-file">Do I have to have a copy of the license in each source file?<a class="headerlink" href="#copy-per-file" title="Permanent link">&para;</a></h2>
<p>Only one full copy of the license is needed per distribution.
See the <a href="http://www.apache.org/legal/src-headers.html">policy</a>.</p>
<h2 id="attribution">In my current source files I have attribution notices for other works. Do I put this in each source file now?<a class="headerlink" href="#attribution" title="Permanent link">&para;</a></h2>
<p>See the <a href="http://www.apache.org/legal/src-headers.html">policy</a>.</p>
<h2 id="contributor-copyright">Can/Should individual committers added copyright statements to the NOTICE or source code files?<a class="headerlink" href="#contributor-copyright" title="Permanent link">&para;</a></h2>
<p>No.</p>
<p>Though committers retain copyright, Apache asks that they do not add copyright
statements.  See the <a href="http://www.apache.org/legal/src-headers.html">policy</a>
for more details.</p>
<h2 id="license-file-name">Can the LICENSE and NOTICE files be called LICENSE.txt and NOTICE.txt?<a class="headerlink" href="#license-file-name" title="Permanent link">&para;</a></h2>
<p>This is permitted.  However the preference is that the files be called LICENSE
and NOTICE.</p>
<h2 id="license-include">Should the license be included in source files for documentation (e.g. XML that is transformed to HTML)?<a class="headerlink" href="#license-include" title="Permanent link">&para;</a></h2>
<p>Yes. See the <a href="http://www.apache.org/legal/src-headers.html">policy</a> for more
details.</p></div>

_moving information from https://www.apache.org/dev/apply-license.html_

