Title: Apache mirroring information

<h2 id="introduction">Introduction<a class="headerlink" href="#introduction" title="Permanent link">&para;</a></h2>
This page describes the requirements and practices for mirroring Apache Software Foundation releases. If you need clarification on any of the statements here, ask your question on the `users@infra.apache.org` mailing list.

All ASF project must use the ASF infrastructure to distribute source, binary and documentation builds so that their releases appear in `dist.apache.org`. This is how ASF keeps track of what releases it has made. Projects may distribute their code through other channels in addition to the ASF infrastructure.

As of March, 2020, all mirror sites are required to use the secure "https" protocol instead of "http". Sites using "https" encrypt data and move it through a secure socket layer (SSL) protocol between the website's server and the vistor's browser.

Projects must adhere to the following guidelines to ensure a consistent way to mirror our distributions, therefore lowering the impact of the enormous amount of bandwidth downloads consume.

<h2 id="goals">Goals<a class="headerlink" href="#goals" title="Permanent link">&para;</a></h2>

  - Current ASF releases must be accessible from participating mirrors.
  - The mirrors should be used by default.
  - Only use `downloads.apache.org` as fallback/backup mirror.
  - The download page should perform a best-guess determination of which mirror to use.
  - The user should be able to override the mirror selection.
  - All releases must be signed by the release manager.
  - PGP/MD5 signature links from project sites may not point to mirrors.
  - Only mirror current, recommended releases. Old releases are automatically archived to `archive.apache.org/dist/` and can be deleted from the main distribution directory.
  
<h2 id="location">Location of files on main server<a class="headerlink" href="#location" title="Permanent link">&para;</a></h2>

Do **not** keep software distributions on the project's website. Move them to one of the two software distribution sites:

  - **Current public releases** appear on `downloads.apache.org/`. Place current, official releases that the PMC has approved for end-users here, on the main public release site that is mirrored world-wide. Make all changes at <a href="https://dist.apache.org/repos/dist/release/" target="_blank">`https://dist.apache.org/repos/dist/release/`</a>.

  - **Older releases** that you no longer recommend to the general public should appear on `archive.apache.org/dist/`. This site automatically contains all the content of `downloads.apache.org/`, but nothing is ever deleted. Therefore it should rarely be necessary to touch this site, except during a reorganization. Once your project no longer recommends public use of a particualr release, simply delete it from `downloads.apache.org/dist/` by removing it from <a href="https://dist.apache.org/repos/dist/release/" target="_blank">`https://dist.apache.org/repos/dist/release/`</a>. It will remain  on the archive site.
  
<h2 id="use">How a project uses mirrors<a class="headerlink" href="#use" title="Permanent link">&para;</a></h2>

Complete instructions are on [How to be an Apache Software Foundation download mirror](how-to-mirror.html).
