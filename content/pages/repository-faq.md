Title: Apache Maven repositories

Here is an overview of Maven repositories in use at the Apache Software Foundation.

<h2>Contents</h2>
<ul>
<li><a href="#basic">Basic information</a></li>
<li><a href="#rules">A few good rules</a></li>
<li><a href="#faq">FAQs about the ASF Jar Repositories</a><ul>
<li><a href="#m1m2">m1/m2?</a></li>
<li><a href="#deploytoboth">Do I need to deploy to both m1/m2 repositories?</a></li>
<li><a href="#thirdparty">Can we put third party files in the repositories?</a></li>
<li><a href="#revolutioncode">I'm working on a research branch, can I release to the repositories?</a></li>
<li><a href="#repodotapache">What is repository.apache.org?</a></li>
<li><a href="#resources">What resources are available?</a></li>
<li><a href="#rsyncs">How do rsyncs happen?</a></li>
</ul>
</li>
</ul>


<h2 id="basic">Basic information</h2>

The main snapshot and release Maven repositories for Apache are at <a href="https://repository.apache.org" target="_blank">https://repository.apache.org</a>. The repository also proxies Apache's legacy repositories.

If your Apache project would like to use `repository.apache.org`, see [Publishing Maven Releases](publishing-maven-artifacts.html).
<p id="rules">&nbsp;</p>

  - Use the `New` repo and staging process to help prevent accidental releases and ensure that releases meet Apache standards.
  - Subscribe to the repository mailing list via `repository-subscribe@apache.org` for questions, complaints and ideas.

If you're a user looking for Apache artifacts from a Maven repository, all releases are synced to <a href="https://repo1.maven.org/maven2" target="_blank">Central</a> and snapshots are available here:
<a href="https://repository.apache.org/snapshots/" target="_blank">http://repository.apache.org/snapshots/</a>.

<h2 id="faq">FAQs about the ASF Jar repositories<</h2>
  
<h2 id="m1m2">m1/m2?<a class="headerlink" href="#m1m2" title="Permanent link">&para;</a></h2>
<p>There are two types of Maven repository. Loosely 'm1' repositories and 'm2'
repositories - matching the repositories used by Maven-1 and Maven-2,
though Maven-2 can point to legacy Maven-1 repositories. We support both,
but are phasing out the m1 repositories.</p>
<h2 id="deploytoboth">Do I need to deploy to both m1/m2 repositories?<a class="headerlink" href="#deploytoboth" title="Permanent link">&para;</a></h2>
<p>No, because the Maven2 repository layout is the standard used by most tools,
including Maven, Ivy and Buildr</p>
<h2 id="thirdparty">Can we put third party files in the repositories?<a class="headerlink" href="#thirdparty" title="Permanent link">&para;</a></h2>
<p>You can with the <em>snapshot</em> repositories, but you cannot with the <em>release</em>
repositories. When putting third party files in the <em>snapshot</em>
repositories, please email the repository mailing list to explain what you
are doing. Ideally third party files should be uploaded to he 'central'
Maven repository via the <a href="http://maven.apache.org/guides/mini/guide-central-repository-upload.html">Maven upload
process.</a> </p>
<h2 id="revolutioncode">I'm working on a research branch, can I release to the repositories?<a class="headerlink" href="#revolutioncode" title="Permanent link">&para;</a></h2>
<p>As long as your project (ie PMC) is happy with the release, then they can
go in the snapshot repository, otherwise you should just release in your
people.apache.org/~login space.</p>
<h2 id="repodotapache">What is repository.apache.org?<a class="headerlink" href="#repodotapache" title="Permanent link">&para;</a></h2>
<p>Apache operates a repository manager at
<a href="https://repository.apache.org/">https://repository.apache.org/</a>. It can be
used by Apache projects for deploying snapshots, releases, or both. See the
<a href="http://www.apache.org/dev/publishing-maven-artifacts.html">Publishing Maven
Releases</a> guide
for more details.</p>
<h2 id="resources">What resources are available?<a class="headerlink" href="#resources" title="Permanent link">&para;</a></h2>
<ul>
<li>
<p>Mailing List: <a href="mailto:repository@apache.org">repository@apache.org</a> [
<a href="mailto:repository-subscribe@apache.org">Subscribe</a> ]</p>
</li>
<li>
<p>Guides: <a href="http://www.apache.org/dev/publishing-maven-artifacts.html">Publishing Maven
Releases</a> </p>
</li>
</ul>
<h2 id="rsyncs">How do rsyncs happen?<a class="headerlink" href="#rsyncs" title="Permanent link">&para;</a></h2>
<p>All the official repositories rsync automatically.</p></div>


_moving information from https://www.apache.org/dev/repository-faq.html_
