Title: Apache Maven repositories

Here is an overview of Maven repositories in use at the Apache Software Foundation.

<h2 id="basic">Basic information</h2>

The main snapshot and release Maven repositories for Apache are at <a href="https://repository.apache.org" target="_blank">https://repository.apache.org</a>. The repository also proxies Apache's legacy repositories.

If your Apache project would like to use `repository.apache.org`, see [Publishing Maven Releases](publishing-maven-artifacts.html).

  - Use the `New` repo and staging process to help prevent accidental releases and ensure that releases meet Apache standards.
  - Subscribe to the repository mailing list via `repository-subscribe@apache.org` for questions, complaints and ideas.

If you're a user looking for Apache artifacts from a Maven repository, all releases are synced to <a href="https://repo1.maven.org/maven2" target="_blank">Central</a> and snapshots are available here:
<a href="https://repository.apache.org/snapshots/" target="_blank">http://repository.apache.org/snapshots/</a>.

<h2 id="faq">FAQs about the ASF Jar repositories</h2>
  
<h4 id="m1m2">m1/m2?</h4>

There are two types of Maven repository. Loosely, Maven-1 and Maven-2 use 'm1' and 'm2' repositories, though Maven-2 can point to legacy Maven-1 repositories. Apache supports both, but is phasing out the m1 repositories.

<h4 id="deploytoboth">Do I need to deploy to both m1/m2 repositories?</h4>

No, because the Maven2 repository layout is the standard used by most tools, including Maven, Ivy and Buildr.

<h4 id="thirdparty">Can we put third party files in the repositories?</h4>

You can with the <em>snapshot</em> repositories, but you cannot with the <em>release</em> repositories. When putting third party files in the <em>snapshot</em> repositories, please email the repository mailing list to explain what you are doing. Ideally, you should upload third party files to the 'central' Maven repository via the <a href="https://maven.apache.org/guides/mini/guide-central-repository-upload.html" target="_blank">Maven upload process</a>.

<h4 id="revolutioncode">Can I release a research branch to the repositories?</h4>

As long as your project's PMC is happy with the release, you can release a research branch to the snapshot repository; otherwise you should just release in your `people.apache.org` personal space.

<h4 id="repodotapache">What is `repository.apache.org`?</h4>

Apache operates a repository manager at <a href="https://repository.apache.org/" target="_blank">https://repository.apache.org/</a>. Apache projects can use it to deploying snapshots, releases, or both. See the [Publishing Maven Releases](publishing-maven-artifacts.html) guide for more details.

<h4 id="resources">What resources are available?</h4>

  - Mailing List: <a href="mailto:repository@apache.org" target="_blank">repository@apache.org</a>
  - [Publishing Maven Releases](publishing-maven-artifacts.html)

<h4 id="rsyncs">How do rsyncs happen?</h4>

All the official repositories rsync automatically.
