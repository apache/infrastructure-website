Title: Apache Maven repositories

license: https://www.apache.org/licenses/LICENSE-2.0

<h2 id="basic">Basic information<a class="headerlink" href="#basic" title="Permanent link">&para;</a></h2>

**Reminder**: Apache projects **must** release all software packages through the ASF distribution system. See [Release distribution policy](release-distribution.html) for more details.

The ASF maintains internal snapshot and release Maven repositories at <a href="https://repository.apache.org" target="_blank">https://repository.apache.org</a>. The repository also proxies Apache's legacy repositories. 

**Note**: these repos are intended for internal ASF project use, not for public distribution of artifacts. Except in the rare situation when a project needs external testing of preproduction artifacts, **do not** provide download links to 'repository.apache.org' assets to users external to The ASF.

If your Apache project would like to use `repository.apache.org`, see [Publishing Maven Releases](publishing-maven-artifacts.html).

  - Use the `New` repo and staging process to help prevent accidental releases and ensure that releases meet Apache standards.
  - Subscribe to the repository mailing list via `repository-subscribe@apache.org` for questions, complaints and ideas.

If you're a user looking for Apache artifacts from a Maven repository, all releases are synced to <a href="https://repo1.maven.org/maven2" target="_blank">Maven Central</a> and snapshots are available here:
<a href="https://repository.apache.org/snapshots/" target="_blank">http://repository.apache.org/snapshots/</a>.

<h2 id="faq">FAQs about the ASF Jar repositories<a class="headerlink" href="#faq" title="Permanent link">&para;</a></h2>

<h4 id="thirdparty">Can we put third party files in the repositories?<a class="headerlink" href="#thirdparty" title="Permanent link">&para;</a></h4>

You can with the <em>snapshot</em> repositories, but you cannot with the <em>release</em> repositories. When putting third party files in the snapshot repositories, please email the repository mailing list to explain what you are doing. Ideally, you should upload third party files to the 'central' Maven repository via the <a href="https://maven.apache.org/guides/mini/guide-central-repository-upload.html" target="_blank">Maven upload process</a>.

<h4 id="revolutioncode">Can I release a research branch to the repositories?<a class="headerlink" href="#revolutioncode" title="Permanent link">&para;</a></h4>

As long as your project's PMC is happy with the release, you can release a research branch to the snapshot repository; otherwise you should just release in your `home.apache.org` personal space.

<h4 id="rsyncs">How do rsyncs happen?<a class="headerlink" href="#rsyncs" title="Permanent link">&para;</a></h4>

All official repositories rsync automatically.
