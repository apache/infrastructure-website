Title: Assembling LICENSE and NOTICE files
license: https://www.apache.org/licenses/LICENSE-2.0

This is a "how to" guide for Apache Committers assembling `LICENSE` and `NOTICE` files for their project's product.

### Overview

The `LICENSE` file communicates the licensing of all content in an Apache product distribution. It always contains the text of the Apache License, and
sometimes more information.

The `NOTICE` file is described in <a href="https://www.apache.org/licenses/LICENSE-2.0.html#redistribution" target="_blank"> section 4.4</a> of the Apache License version
2.0. It is required by <a href="https://www.apache.org/legal/src-headers.html#notice" target="_blank">ASF policy</a>.

The <a href="https://www.apache.org/legal" target="_blank">complete requirements</a> for `LICENSE` and `NOTICE` files are available.

  - <a href="#guiding">Guiding principle</a>
  - <a href="#source-tree-location">Location</a>
  - <a href="#step-by-step">Step-by-step instructions</a>
  - Bundling
    - <a href="#permissive-deps">Bundling permissively-licensed dependencies</a>
    - <a href="#alv2-dep">Bundling an Apache 2-0 licensed dependency</a>
    - <a href="#bundle-asf-product">Bundling other ASF products</a>
    - <a href="#bundled-vs-non-bundled">Bundled vs. non-bundled dependencies</a>
    - <a href="#deps-of-deps">Dependencies of dependencies</a>
  - <a href="#mod-notice">Modifications to NOTICE</a>
  - <a href="#binary">Binary distributions</a>
  - <a href="#example-notice">Example NOTICE file</a>

<h3 id="guiding">Guiding principle<a class="headerlink" href="#guiding" title="Permanent link">&para;</a></h3>

The `LICENSE` and `NOTICE` files must **exactly represent** the contents of the distribution they reside in. Only components and resources that are actually included in a distribution have any bearing on the content of that distribution's `NOTICE` and `LICENSE`.

<h3 id="source-tree-location">Location<a class="headerlink" href="#source-tree-location" title="Permanent link">&para;</a></h3>

`LICENSE` and `NOTICE` files belong at the top level of the source tree. ASF prefers that the files have their bare names, but a PMC can opt to call them `LICENSE.txt` and `NOTICE.txt`.

<h3 id="step-by-step">Step-by-step instructions<a class="headerlink" href="#step-by-step" title="Permanent link">&para;</a></h3>

To assemble `LICENSE` and `NOTICE` files from scratch for products with complex requirements, follow these steps:

  - Copy the full <a href="https://www.apache.org/licenses/LICENSE-2.0.txt" target="_blank">Apache 2.0 license</a> text into a `LICENSE` file.
  - Create a 'NOTICE' file specific to your product's details, and complying with the instructions below. An <a href="#example-notice">example `NOTICE` file</a> is at the bottom of this page.
    - Add any <a href="#mod-notice">mandatory</a> legal notifications specific to the IP of your product.
    - For any <a href="#bundled-vs-non-bundled">bundled</a> dependency, consider whether `LICENSE` and/or `NOTICE` need to be modified. **Do not** modify `LICENSE` or `NOTICE` for non-bundled dependencies.

<h3 id="permissive-deps">Bundling permissively-licensed dependencies<a class="headerlink" href="#permissive-deps" title="Permanent link">&para;</a></h3>

Bundling a dependency which is issued under one of the following licenses is straightforward, assuming that license applies uniformly to all files within the dependency:

  - BSD (without advertising clause)
  - MIT/X11

In `LICENSE`, add a <a href="http://s.apache.org/Hqj" target="_blank">pointer</a> to the dependency's license within the distribution and a short note summarizing its licensing:

```
This product bundles SuperWidget 1.2.3, which is available under a
"3-clause BSD" license. For details, see deps/superwidget/.
```
Under normal circumstances, there is no need to modify `NOTICE` to mention a bundled dependency.

**NOTE**: It's also possible to include the text of the 3rd party license within your product's `LICENSE` file. This is best reserved for short licenses. It's important to specify the version of the dependency as licenses sometimes change as product versions change.

There are a number of other "permissive" licenses which the ASF Legal Affairs Committee has <a href="https://www.apache.org/legal/resolved.html#category-a" target="_blank"> approved</a> for use. Some of these may require additions to `NOTICE` -- if in doubt, <a href="https://www.apache.org/legal/resolved.html#asking-questions" target="_blank">ask for assistance</a>.

<h3 id="alv2-dep">Bundling an Apache 2-0-licensed dependency<a class="headerlink" href="#alv2-dep" title="Permanent link">&para;</a></h3>

Assuming that the bundled dependency itself contains no bundled sub-components under other licenses, so the ALv2 applies uniformly to all files, there is no need to modify <code>LICENSE</code>. However, for completeness it is useful to list the products and their versions, as is done for products under other licenses.

If the dependency supplies a <code>NOTICE</code> file, its contents must be analyzed and the relevant portions bubbled up into the top-level <code>NOTICE</code> file.

<h3 id="bundle-asf-product">Bundling other ASF products<a class="headerlink" href="#bundle-asf-product" title="Permanent link">&para;</a></h3>

It is not necessary to duplicate the line "This product includes software developed at the Apache Software Foundation...", though the ASF copyright line and any other portions of <code>NOTICE</code> must be considered for propagation.

<h3 id="bundled-vs-non-bundled">Bundled vs. non-bundled dependencies<a class="headerlink" href="#bundled-vs-non-bundled" title="Permanent link">&para;</a></h3>

You must customize `LICENSE` and `NOTICE` files according to the content of the specific distribution they reside within. Do not add to `LICENSE` and `NOTICE` dependencies which are not in the distribution. **Only bundled bits matter.**

Example: If the only difference between `apache-foo-1.0.tgz` and `apache-foo-1.1.tgz` is that one bundles SuperWidget while the other forces users to download SuperWidget separately, `LICENSE` and `NOTICE` may need to be modified to account for the different bundled bits.

<h3 id="deps-of-deps">Dependencies of dependencies<a class="headerlink" href="#deps-of-deps" title="Permanent link">&para;</a></h3>

Dependencies of dependencies (including so-called "transitive dependencies") are no different from first-order dependencies for the purposes of assembling `LICENSE` and `NOTICE`: `LICENSE` and `NOTICE` need only be modified to accommodate them **only if their bits are bundled**.

<h3 id="mod-notice">Modifications to NOTICE<a class="headerlink" href="#mod-notice" title="Permanent link">&para;</a></h3>

The `NOTICE` file is reserved for a certain subset of legally required notifications which are not satisfied by either the text of `LICENSE` or the presence of licensing information embedded within the bundled dependency. Aside from Apache-licensed dependencies which supply `NOTICE` files of their own, it is uncommon for a dependency to require additions to `NOTICE`.

Copyright notifications which have been <a href="https://www.apache.org/legal/src-headers.html#headers" target="_blank">relocated</a>, rather than removed, from source files must be preserved in `NOTICE`. However, elements such as the copyright notifications embedded within BSD and MIT licenses <a href="https://issues.apache.org/jira/browse/LEGAL-59" target="_blank">do not need to be duplicated</a> in `NOTICE`. You can leave those notices in their original locations.

It is important to keep `NOTICE` as brief and simple as possible, as each addition places a burden on downstream consumers.

**Do not** add anything to `NOTICE` which is not legally required.

<h3 id="binary">Binary distributions<a class="headerlink" href="#binary" title="Permanent link">&para;</a></h3>

What applies to canonical source distributions also applies to all redistributions, including binary redistributions:

**All redistributions must obey the licensing requirements of the contents.**

When assembling binary distributions, it is common to pull in and bundle additional dependencies which are not bundled with the source distribution. You must account for these additional dependencies in `LICENSE` and `NOTICE`. As a result, the `LICENSE` and `NOTICE` files for a binary distribution may differ from those in the source distribution it was built from.

In any case, the principle remains the same: `LICENSE` and `NOTICE` must **exactly** represent the contents of the distribution they reside in.

<h3 id="example-notice">Example NOTICE file<a class="headerlink" href="#example-notice" title="Permanent link">&para;</a></h3>

The following is the text of the `NOTICE` file for <a href="https://royale.apache.org/" target="_blank">Apache Royale</a>:

```
Apache Royale
Copyright 2020 The Apache Software Foundation

This product includes software developed at
The Apache Software Foundation (http://www.apache.org/).

The Initial Developer of some parts of the framework, which are copied from, derived from, or
inspired by Adobe Flex (via Apache Flex), is Adobe Systems Incorporated (http://www.adobe.com/).
Copyright 2003 - 2012 Adobe Systems Incorporated. All Rights Reserved.

The Initial Developer of the examples/mxroyale/tourdeflexmodules, 
is Adobe Systems Incorporated (http://www.adobe.com/).
Copyright 2009 - 2013 Adobe Systems Incorporated. All Rights Reserved.

The ping sound effect (ping.mp3) in 
examples/mxroyale/tourdeflexmodules/src/mx/effects/assets
was created by CameronMusic. (http://www.freesound.org/people/cameronmusic/sounds/138420/)
```
