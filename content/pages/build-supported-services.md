Title: ASF Build and Supported Services
license: https://www.apache.org/licenses/LICENSE-2.0

## Introduction
Here is a summary of The ASF's 'build' (CI/CD) and related services, those hosted at The ASF and those supported externally, directly or via integration.

Note that 'supported' means that Infra provides the service or provides access to the service. It does not mean that a particular service is considered
an official 'release channel'.

-  <a href="#jenkins">Jenkins</a>
-  <a href="#buildbot">Buildbot</a>
-  <a href="#gump">Apache Gump</a>
-  <a href="#gha">GitHub Actions</a>
-  <a href="#artifactory">Artifactory</a>
-  <a href="#nexus">Nexus</a>
-  <a href="#nightlies">Nightlies</a>
-  <a href="#dockerhub">DockerHub</a>
-  <a href="#gradle">Gradle Enterprise</a>
-  <a href="#sonarcloud">Sonarcloud</a>

<h2 id="jenkins">Jenkins<a class="headerlink" href="#jenkins" title="Permanent link">&para;</a></h2>

Infra operates a Cloudbees Core cluster comprising a single <a href="https://jenkins-ccos.apache.org/" target="_blank">Operations Center</a> and several Controllers. These comprise a shared Controller <a href="https://ci-builds.apache.org/" target="_blank">ci-builds instance</a> which many projects share, and some individual project Controllers (listed on the main Operations Center <a href="https://jenkins-ccos.apache.org/job/controllers" target="_blank">Controllers</a> page).

#### Access control
Jenkins is LDAP enabled and so all ASF Committers have login access. Project level access is then applied at a Controller level for the project Controllers and at a
Folder level for the shared ci-builds shared instance. If your project has a Folder here, you already have access there to edit/create builds. If you are
a project without a Folder then an Infra Jira ticket will get you the Folder you need.

#### Integrations
Jenkins has integrations with GitHub Actions (GHA), nightlies.apache.org, and Nexus for snapshot deployments. More information on this will appear here soon.

#### More information
The Infra Confluence wiki space has <a href="https://cwiki.apache.org/confluence/display/INFRA/Jenkins" target="_blank">more information about Jenkins</a>.

<h2 id="buildbot">Buildbot<a class="headerlink" href="#buildbot" title="Permanent link">&para;</a></h2>

ASF Infra runs an instance of the open source Buildbot software. Buildbot runs on a single controller and hosts many Ubuntu and Windows nodes, or 'workers' in current Buildbot terminology.

#### Adding/configuring Buildbot jobs
Projects can add/edit/remove their configuration files via Subversion or Git.

  - <a href="https://svn.apache.org/repos/infra/infrastructure/buildbot2/projects" target="_blank">Subversion</a> 
  - <a href="https://github.com/apache/infrastructure-bb2" target="_blank">Git/GitHub</a> 

Use the standard naming `$projectname.py` for your config file. You may place multiple build jobs in this file.

Once committed, changes should be picked up automatically.
If this does not happen, please contact Infrastructure.

#### Access control
Log in to <a href="https://ci2.apache.org/" target="_blank">ci2.apache.org</a> with your LDAP creds. Use `$username@apache.org` for the user and your LDAP password.

#### Integrations
Buildbot integrates with `nightlies.apache.org` and Nexus for snapshot deployments.

IRC: Currently irc integration is disabled. We have an open Jira ticket tracking this.

#### More Information
The Infra Confluence wiki has <a href="https://cwiki.apache.org/confluence/display/INFRA/Buildbot" target="_blank">more about Buildbot</a>.

<h2 id="gump">Apache Gump<a class="headerlink" href="#gump" title="Permanent link">&para;</a></h2>

The <a href="https://gump.apache.org/" target="_blank">Apache Gump project</a> runs <a href="http://vmgump.apache.org/" target="_blank">this instance</a>. Projects are welcome to ask them directly for access.

Gump is a cross-project continuous integration server. It is different from the "usual" CI servers in that it expects the individual project builds to succeed;
its purpose is to check the integration of a project with the latest code rather than with a fixed version of the project's dependencies. If you want a more
traditional nightly build server, Gump is not for you.

Use Gump if you want to know when a change in your dependencies breaks your project or when your changes have broken other projects.

Gump is written in Python and supports several build tools (including shell scripts, GNU make, Ant, Maven and NAnt) and version control systems
(svn, CVS, git, bzr, hg, darcs and Perforce). The Apache installation of Gump builds many ASF projects and their dependencies.

Gump started in the Java part of the Foundation but also builds projects like APR, HTTPd and log4net. 

<h2 id="gha">GitHub Actions<a class="headerlink" href="#gha" title="Permanent link">&para;</a></h2>

The ASF supports and recommends the use of GitHub Actions (GHA).

#### Integrations
Infra makes use of an 'allow' list to allow Marketplace actions for your workflows. File an Infra Jira ticket if you need to have one added
to the list.

GHA integrates with nightlies.apache.org, Dockerhub, Artifactory, Jenkins and more via credentials supplied as GitHub Secrets.

#### Access control
All Committers have access to GHA and their workflows via `commit` using their LDAP credentials.

#### More information
In addition to the official GitHub documentation, Infra has placed some <a href="https://infra.apache.org/github-actions-secrets.html" target="_blank">notes</a> on a  Confluence wiki page.

<h2 id="artifactory">Artifactory<a class="headerlink" href="#artifactory" title="Permanent link">&para;</a></h2>

The folks at Jfrog provide us an <a href="https://apache.jfrog.io/" target="_blank">instance of Artifactory</a> for all ASF projects to use. Projects are free to publish debs, rpms, Helm Charts and more. Use a Jira ticket to ask Infra to set up the project's initial repository type.

#### Access Control
Access is via LDAP credentials. Infra needs to set up the project's initial repository/group access.

#### Integrations
Many possibilities here for upload/download via the use of a PAT token.

#### More information
A <a href="https://cwiki.apache.org/confluence/display/INFRA/Artifactory" target="_blank">Confluence wiki page</a> will soon contain some more Artifactory information.

<h2 id="nexus">Nexus<a class="headerlink" href="#nexus" title="Permanent link">&para;</a></h2>

The ASF has a Nexus instance at <a href="https://repository.apache.org/" target="_blank">repository.apache.org</a> , maintained by the Maven community in conjunction with people from Sonatype.

#### Access control
The instance has committer-only access to push to staging and to snapshots via their LDAP credentials, and promotion from staging to release. Once released, the artifacts get synced over to <a href="https://repo.maven.apache.org/maven2/" target="_blank">Maven Central</a>.

Snapshots and staged artifacts do not get synced.

#### Integrations
Pushing snapshots can be done via GHA, Buildbot and Jenkins.

Experimental signing and push to Staging (in readiness for a manual promotion to release) is being tested.

#### More information
See <a href="https://infra.apache.org/publishing-maven-artifacts.html">Publishing Maven artifacts</a>.

<h2 id="nightlies">Nightlies<a class="headerlink" href="#nightlies" title="Permanent link">&para;</a></h2>
Infra runs a server at <a href="https://nightlies.apache.org/" target="_blank">nightlies.apache.org</a> where projects can store various build output such as snapshot builds, versioned website documentation, artifacts (jars, etc.), and apidocs. Jenkins, Buildbot and GitHub Actions all integrate with nightlies. Committers also have PUT access via their LDAP credentials.

<h2 id="dockerhub">DockerHub<a class="headerlink" href="#dockerhub" title="Permanent link">&para;</a></h2>

The ASF has an 'apache' account at <a href="https://hub.docker.com/orgs/apache" target="_blank">DockerHub</a> for all projects to use.

#### Access control
Committers need to sign up for a personal account, then create a Jira ticket asking Infra to set up their access. The ticket should state

  - dockerhub_id : asf_id
  - project name
  - repository name(s)
  - team name

Infra adds DockerHub user IDs to a project 'team', which has read/write access to the project repositories.

#### Integrations
The ASF has tokens/credentials in GHA, Jenkins and Buildbot for projects to use when pushing to Dockerhub using a role account. If you want to make use of this option, open a Jira ticket for Infra, to request they enable it for your project's repository.

#### More information

  - <a href="https://cwiki.apache.org/confluence/display/INFRA/Github+Actions+to+DockerHub" target="_blank">GitHub Actions to DockerHub</a>

<h2 id="gradle">Gradle Enterprise<a class="headerlink" href="#gradle" title="Permanent link">&para;</a></h2>
Gradle is a suite of acceleration and analytics technologies for CI/CD systems to help projects identify and analyze trends while optimizing build resources. The result is faster builds, with fewer failures, The ASF instance of Gradle enterprise is at <a href="https://ge.apache.org/" target="_blank">ge.apache.org</a>.

More information is available at the [Gradle page](gradle.html).

<h2 id="sonarcloud">Sonarcloud<a class="headerlink" href="#sonarcloud" title="Permanent link">&para;</a></h2>

The ASF has an 'apache' account at <a href="https://sonarcloud.io/organizations/apache" target="_blank">sonarcloud.io</a> where projects can have their code analyzed.

#### Access control
Committers must log in to Sonarcloud with their GitHub ID. In addition you must have your ASF account and your GitHub accounts linked so that you then
appear as a member of the ASF organization on GitHub. That is how Sonarcloud identifies you as belonging to the 'apache' organization on their system.

#### Integrations
The ASF has auth tokens available under a role account for use via GHA and Jenkins.

#### More information
<a href="https://cwiki.apache.org/confluence/display/INFRA/SonarCloud+for+ASF+projects" target="_blank">SonarCloud for ASF projects</a>
