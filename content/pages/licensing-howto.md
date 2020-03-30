Title: Assembling LICENSE and NOTICE files

This document is a "how to" guide aimed at Apache Committers assembling `LICENSE` and `NOTICE` files for an Apache product.

<li><a href="#overview-of-files">Overview of the LICENSE and NOTICE files</a></li>





<li><a href="#guiding-principle">Guiding principle</a></li>
<li><a href="#source-tree-location">Location Within the Source Tree</a></li>
<li><a href="#simple">The Simple Case -- No Bundled Dependencies</a></li>
<li><a href="#step-by-step">Step-by-Step Instructions</a></li>
</ul>
</li>
<li><a href="#permissive-deps">Bundling Permissively-Licensed Dependencies</a><ul>
<li><a href="#alv2-dep">Bundling an Apache-2.0-licensed Dependency</a></li>
<li><a href="#bundle-asf-product">Bundling Other ASF Products</a></li>
</ul>
</li>
<li><a href="#mod-notice">Modifications to NOTICE</a></li>
<li><a href="#bundled-vs-non-bundled">Bundled vs. Non-bundled Dependencies</a></li>
<li><a href="#deps-of-deps">Dependencies of Dependencies</a></li>
<li><a href="#binary">Binary Distributions</a></li>
</ul>

<h1 id="assembling-license-and-notice">Assembling LICENSE and NOTICE<a class="headerlink" href="#assembling-license-and-notice" title="Permanent link">&para;</a></h1>
<h2 id="audience">Intended Audience<a class="headerlink" href="#audience" title="Permanent link">&para;</a></h2>
<p>This document is a "how to" guide aimed at Apache Committers assembling
<code>LICENSE</code> and <code>NOTICE</code> files for an Apache product.</p>
<h2 id="overview-of-files">Overview of the <code>LICENSE</code> and <code>NOTICE</code> files<a class="headerlink" href="#overview-of-files" title="Permanent link">&para;</a></h2>
<p>The <code>LICENSE</code> file communicates the licensing of all content in an Apache
product distribution.  It always contains the text of the Apache License, and
sometimes more.</p>
<p>The <code>NOTICE</code> file is described in <a href="http://www.apache.org/licenses/LICENSE-2.0.html#redistribution">section 4.4 of the Apache License version
2.0</a>.  It
presence is not mandated by the license itself, but by <a href="http://www.apache.org/legal/src-headers.html#notice">ASF
policy</a>.</p>
<p>The complete requirements for <code>LICENSE</code> and <code>NOTICE</code> are described
<a href="http://www.apache.org/legal">elsewhere</a>.</p>
<h2 id="guiding-principle">Guiding principle<a class="headerlink" href="#guiding-principle" title="Permanent link">&para;</a></h2>
<p>The <code>LICENSE</code> and <code>NOTICE</code> files must
<strong>exactly</strong> represent the contents of the distribution they reside in.</p>
<p>Only bits that are actually included in a distribution have any bearing on the content of NOTICE and LICENSE.</p>
<h2 id="source-tree-location">Location Within the Source Tree<a class="headerlink" href="#source-tree-location" title="Permanent link">&para;</a></h2>
<p><code>LICENSE</code> and <code>NOTICE</code> belong at the <a href="http://www.apache.org/legal/src-headers.html#notice">top level of the source
tree</a>.  They may
be named <code>LICENSE.txt</code> and <code>NOTICE.txt</code>, but the <a href="http://apache.org/dev/apply-license.html#license-file-name">bare names are
preferred</a>.</p>
<h2 id="simple">The Simple Case -- No Bundled Dependencies<a class="headerlink" href="#simple" title="Permanent link">&para;</a></h2>
<p>For a source tree which consists entirely of code licensed to the ASF by the
copyright holders and which has no bundled dependencies, <code>LICENSE</code> should
contain the text of the <a href="http://apache.org/licenses/LICENSE-2.0.txt">ALv2</a> --
no more, no less.</p>
<p><code>NOTICE</code> should contain only the <a href="http://www.apache.org/legal/src-headers.html#notice">following
text</a>, adapted with the
product's name and copyright dates:</p>
<div class="codehilite"><pre><span class="n">Apache</span> <span class="p">[</span><span class="n">PRODUCT_NAME</span><span class="p">]</span>
<span class="n">Copyright</span> <span class="p">[</span><span class="n">XXXX</span><span class="o">-</span><span class="n">XXXX</span><span class="p">]</span> <span class="n">The</span> <span class="n">Apache</span> <span class="n">Software</span> <span class="n">Foundation</span>

<span class="n">This</span> <span class="n">product</span> <span class="n">includes</span> <span class="n">software</span> <span class="n">developed</span> <span class="n">at</span>
<span class="n">The</span> <span class="n">Apache</span> <span class="n">Software</span> <span class="n">Foundation</span> <span class="p">(</span><span class="n">http</span><span class="p">:</span><span class="o">//</span><span class="n">www</span><span class="p">.</span><span class="n">apache</span><span class="p">.</span><span class="n">org</span><span class="o">/</span><span class="p">).</span>
</pre></div>


<h2 id="step-by-step">Step-by-Step Instructions<a class="headerlink" href="#step-by-step" title="Permanent link">&para;</a></h2>
<p>To assemble <code>LICENSE</code> and <code>NOTICE</code> files from scratch for products with more
complex requirements, follow these steps:</p>
<ol>
<li>
<p>Start with <a href="#simple">boilerplate</a> <code>LICENSE</code> and <code>NOTICE</code> files, as above.</p>
</li>
<li>
<p>Add any <a href="#mod-notice">mandatory</a> legal notifications specific to the IP of
    your product to <code>NOTICE</code>.</p>
</li>
<li>
<p>For any dependency whose bits are <a href="#bundled-vs-non-bundled">bundled</a>,
    consider whether <code>LICENSE</code> and <code>NOTICE</code> need to be modified.  (DO NOT
    modify <code>LICENSE</code> or <code>NOTICE</code> for dependencies whose bits are not bundled.)</p>
</li>
</ol>
<h1 id="permissive-deps">Bundling Permissively-Licensed Dependencies<a class="headerlink" href="#permissive-deps" title="Permanent link">&para;</a></h1>
<p>Bundling a dependency which is issued under one of the following licenses is
straightforward, assuming that said license applies uniformly to all files
within the dependency:</p>
<ul>
<li>BSD (without advertising clause)</li>
<li>MIT/X11</li>
</ul>
<p>In <code>LICENSE</code>, add a <a href="http://s.apache.org/Hqj">pointer</a> to the dependency's
license within the distribution and a short note summarizing its licensing:</p>
<div class="codehilite"><pre><span class="n">This</span> <span class="n">product</span> <span class="n">bundles</span> <span class="n">SuperWidget</span> 1<span class="p">.</span>2<span class="p">.</span>3<span class="p">,</span> <span class="n">which</span> <span class="n">is</span> <span class="n">available</span> <span class="n">under</span> <span class="n">a</span>
&quot;3<span class="o">-</span><span class="n">clause</span> <span class="n">BSD</span>&quot; <span class="n">license</span><span class="p">.</span>  <span class="n">For</span> <span class="n">details</span><span class="p">,</span> <span class="n">see</span> <span class="n">deps</span><span class="o">/</span><span class="n">superwidget</span><span class="o">/</span><span class="p">.</span>
</pre></div>


<p>Under normal circumstances, there is no need to modify <code>NOTICE</code>.</p>
<p>NOTE: It's also possible to include the text of the 3rd party license within the LICENSE file.
This is best reserved for short licenses. It's important to specify the version of the dependency
as licenses are sometimes changed.</p>
<p>There are a number of other "permissive" licenses which are
<a href="http://www.apache.org/legal/resolved.html#category-a">approved</a> for use
by the ASF Legal Affairs Committee.  Some of these may require additions to
<code>NOTICE</code> -- if in doubt,
<a href="http://www.apache.org/legal/resolved.html#asking-questions">ask</a>.</p>
<h2 id="alv2-dep">Bundling an Apache-2.0-licensed Dependency<a class="headerlink" href="#alv2-dep" title="Permanent link">&para;</a></h2>
<p>Assuming once again that that the bundled dependency itself contains no bundled
subcomponents under other licenses and thus the ALv2 applies uniformly to all
files, there is no need to modify <code>LICENSE</code>.  However, for completeness it is useful
to list the products and their versions, as is done for products under other licenses.</p>
<p>If the dependency supplies a <code>NOTICE</code> file, its contents must be analyzed and
the relevant portions bubbled up into the top-level <code>NOTICE</code> file.</p>
<h2 id="bundle-asf-product">Bundling Other ASF Products<a class="headerlink" href="#bundle-asf-product" title="Permanent link">&para;</a></h2>
<p>It is not necessary to duplicate the line "This product includes software
developed at the Apache Software Foundation...", though the ASF copyright line
and any other portions of <code>NOTICE</code> must be considered for propagation.</p>
<h1 id="mod-notice">Modifications to NOTICE<a class="headerlink" href="#mod-notice" title="Permanent link">&para;</a></h1>
<p><code>NOTICE</code> is reserved for a certain subset of legally required notifications
which are not satisfied by either the text of <code>LICENSE</code> or the presence of
licensing information embedded within the bundled dependency.  Aside from
Apache-licensed dependencies which supply <code>NOTICE</code> files of their own, it is
uncommon for a dependency to require additions to <code>NOTICE</code>.</p>
<p>Copyright notifications which have been
<a href="http://www.apache.org/legal/src-headers.html#headers">relocated</a> from source
files (rather than removed) must be preserved in <code>NOTICE</code>.  However, elements
such as the copyright notifications embedded within BSD and MIT licenses
<a href="https://issues.apache.org/jira/browse/LEGAL-59">need</a>
<a href="https://issues.apache.org/jira/browse/LEGAL-62">not</a> be duplicated in
<code>NOTICE</code> -- it suffices to leave those notices in their original locations.</p>
<p>It is important to keep <code>NOTICE</code> as brief and simple as possible, as each
addition places a burden on downstream consumers.</p>
<p><strong>Do not add anything to <code>NOTICE</code> which is not legally required.</strong></p>
<h1 id="bundled-vs-non-bundled">Bundled vs. Non-bundled Dependencies<a class="headerlink" href="#bundled-vs-non-bundled" title="Permanent link">&para;</a></h1>
<p><code>LICENSE</code> and <code>NOTICE</code> must always be tailored to the content of the specific
distribution they reside within.  Dependencies which are not included in the
distribution MUST NOT be added to <code>LICENSE</code> and <code>NOTICE</code>.  As far as <code>LICENSE</code>
and <code>NOTICE</code> are concerned, <em>only bundled bits matter.</em></p>
<p>Example: If the only difference between <code>apache-foo-1.0.tgz</code> and
<code>apache-foo-1.1.tgz</code> is that one bundles SuperWidget while the other forces
users to download SuperWidget separately, then <code>LICENSE</code> and <code>NOTICE</code> may very
well need to be modified to account for the different bundled bits.</p>
<h1 id="deps-of-deps">Dependencies of Dependencies<a class="headerlink" href="#deps-of-deps" title="Permanent link">&para;</a></h1>
<p>Dependencies of dependencies (including so-called "transitive dependencies")
are no different from first-order dependencies for the purposes of assembling
<code>LICENSE</code> and <code>NOTICE</code>: <code>LICENSE</code> and <code>NOTICE</code> need only be modified to
accommodate them <em>if and only if their bits are bundled</em>.</p>
<h1 id="binary">Binary Distributions<a class="headerlink" href="#binary" title="Permanent link">&para;</a></h1>
<p>What applies to canonical source distributions also applies to all
redistributions, including binary redistributions:</p>
<p><em>Any redistribution must obey the licensing requirements of the contents.</em></p>
<p>The best way to do that will likely depend on the binary packaging form. </p>
<p>When assembling binary distributions, it is common to pull in and bundle
additional dependencies which are not bundled with the source distribution.
These additional dependencies must be accounted for in <code>LICENSE</code> and <code>NOTICE</code>.</p>
<p>As a result, the <code>LICENSE</code> and <code>NOTICE</code> files for a binary distribution may
well differ from those in the source distribution it was built from.</p>
<p>In any case, the principle remains the same: <code>LICENSE</code> and <code>NOTICE</code> must
<strong>exactly</strong> represent the contents of the distribution they reside in.</p></div>



_migrating information from https://www.apache.org/dev/licensing-howto.html_
