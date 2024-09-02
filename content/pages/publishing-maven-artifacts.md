Title: Publishing Maven Releases to Maven Central Repository

license: https://www.apache.org/licenses/LICENSE-2.0

[Apache Maven](https://maven.apache.org/) is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information.

This document describes how to release Maven artifacts for Apache Software Foundation projects to the [Maven Central Repository](https://maven.apache.org/repository/index.html). This is optional. Apache projects **must** release all software packages through the ASF distribution system. See [Release distribution policy](release-distribution.html) for more details.

**Note** make sure you are using version 3.0.5 or newer of Maven. You can <a href="https://maven.apache.org/download.cgi" target="_blank">download</a> and install the latest version of Maven before continuing.

## Setting up your project in the ASF Nexus Repository ##

The [ASF Nexus repository](https://repository.apache.org/) enforces security by constraining who can deploy or release a project's artifacts. Nexus maps which artifacts (usually by GroupId) your project produces. This is particularly helpful in preventing accidental releases of a project.

Before a project can use the repository to release Maven artifacts, it must be configured in Nexus. This is generally a quick and easy process. To get set up, <a href="https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?issuetype=3&priority=3&pid=10410&components=12312660&summary=Enable+Nexus+Access+For+[insert+project]&description=Project+URL:%0D%0DSVN+URL:%0D%0DMaven+Group+Ids:%0D%0DManaged+By+This+TLP+Project:" target="_blank">use this link</a> to create a Jira ticket with the following information:

  - **Project URL**: a link to your project page (usually `https://<project>.apache.org/`).
  - **SVN URL**: where you store your source code, in case Infra needs to look up more information.
  - **Maven Group IDs**: a list of the groupIDs for this project. They should all be subgroups of `org.apache`.
  - **Managed By This TLP Project**: if this is a subproject, list the TLP that is responsible. Subprojects usually don't have their own LDAP group, so we need the TLP LDAP group for permissions. 

If you have specific questions or concerns, please call them out in the ticket.
  
Once you file the Jira ticket, Infra will do the following:

  - **Set up the project in Nexus**: We configure your groupIds in Nexus and link them to the appropriate LDAP group for authorization.
  - **Move Existing Artifacts**: To maintain the proper `maven-metadata.xml` files and prevent rsync conflicts in Central, we must move all your artifacts to the new repository. We will mark the folder in the old repository as read-only to prevent accidental deployments.
  - **Check POMs**: If your project is Maven-based, we will check your POM for any obvious problems.
  
Further information about the POM and other Maven matters is <a href="https://maven.apache.org/pom/asf/" target="_blank">here</a>.

## Adjusting your build to deploy to the ASF Nexus repository ##
To use the ASF Nexus repository, follow these steps.

### Inherit the Apache POM ###
Inherit the Apache Parent POM like this:

```
<parent>
  <groupId>org.apache</groupId>
  <artifactId>apache</artifactId>
  <version>23</version>
</parent>
```

This parent POM sets up the defaults so your `<distributionManagement>` section uses the correct release and snapshot repositories. Be sure to remove those from your POM so they inherit correctly. Keep the entry for deploying your site (if you use Maven to deploy your site). If you do, we suggest you use `apache.website` as the ID to better match the settings below and to save the sanity of committers working on multiple projects.

The POM also provides a default configuration to make sure that a correct source archive is created for your project. This is separate and in addition to the typical `-sources.jar` that is created.

### Set up your development environment ###

You must sign all artifacts with a key that is publicly verifiable. Follow the instructions here to get your keys created and environment set up.

**Note**: We recommend that you use <a href="https://maven.apache.org/guides/mini/guide-encryption.html" target="_blank">Maven's password encryption capabilities</a> for your passwords. **Do not** store your signing key in `settings.xml`.

The <a href="https://maven.apache.org/plugins/maven-gpg-plugin/" target="_blank">gpg plugin</a> can prompt for the key (input is masked) or you can configure it to use an agent.

```
<settings>
...
  <servers>
    <!-- To publish a snapshot of your project -->
    <server>
      <id>apache.snapshots.https</id>
      <username> <!-- YOUR APACHE LDAP USERNAME --> </username>
      <password> <!-- YOUR APACHE LDAP PASSWORD (encrypted) --> </password>
    </server>
    <!-- To stage a release of your project -->
    <server>
      <id>apache.releases.https</id>
      <username> <!-- YOUR APACHE LDAP USERNAME --> </username>
      <password> <!-- YOUR APACHE LDAP PASSWORD (encrypted) --> </password>
    </server>
   ...
  </servers>
</settings>
```

### Test your settings ###

Try installing locally artifacts with activation of the `apache-release` profile:

`mvn clean install -Papache-release`

This will build artifacts and sources and sign them.

## Staging your release ##

### 1. Prepare your POMs ###

1. Make sure there are no dependencies on snapshots in the POMs to be released. However, the project you want to stage must be a SNAPSHOT version.
2. Check that your POMs will not lose content when they are rewritten during the release process:
3. Verify that all pom.xml files have an SCM definition.
4. Do a dryRun release: `mvn release:prepare -DdryRun=true` You may also wish to pass `-DautoVersionSubmodules=true` as this will save you time if your project is multi-moduled.
5. Diff the original file `pom.xml` with the one called `pom.xml.tag` to see if the license or any other info has been removed. This has been known to happen if the starting `<project>` tag is not on a single line. The only things that should be different between these files are the `<version>` and `<scm>` elements. Backport any other changes you find to the original `pom.xml` file and commit it before proceeding with the release.

### 2. Publish a snapshot ###

```
mvn deploy
...
[INFO] [deploy:deploy]
[INFO] Retrieving previous build number from apache.snapshots.https
...
```

**Notes**

  - If you experience an error like a _HTTP 401_ during deployment, check your settings for the required server entries as outlined above.
  - Be sure that the generated artifacts respect the <a href="https://www.apache.org/legal/release-policy.html#distribute-raw-artifact" target="_blank">Apache release rules</a>: NOTICE and LICENSE files should be present in the META-INF directory within the jar.
  - Verify the deployment under the ASF <a href="https://repository.apache.org/content/repositories/snapshots/" target="_blank">Maven Snapshot repository</a>.
  
### 3. Prepare the release ###
```
mvn release:clean
mvn release:prepare
```

**Notes**

  - Don't try to publish `.sha256` or `.sha512` files; Nexus doesn't handle them.
  - Remove `.md5`s in `dist.apache.org/repos/dist/release/` manually.
  - Preparing the release will create a new tag in SVN, and automatically check the version in on your behalf.
  - If you're located in Europe, `release:prepare` may fail with `Unable to tag SCM` and `svn: No such revision X`. Wait 10 seconds and run `mvn release:prepare` again.
  
### 4. Stage the release for a vote ###

`mvn release:perform`

Maven automatically inserts the release into a temporary staging repository for you. See <a href="https://help.sonatype.com/repomanager2/staging-releases" target="_blank">the Nexus staging documentation</a> for full details.

Now you must close the staging repository to indicate to Nexus that the build is done and to make the artifacts available. Follow the steps in **Closing the Staged Repository**, later in this document. This will allow your community to **vote** on the staged artifacts.

## Troubleshooting ##

1. If you get an **error message** like this:

```
[INFO] Unable to tag SCM
Provider message:
The svn tag command failed.
Command output:
svn: Commit failed (details follow):
svn: File
'/repos/asf/maven/plugins/tags/maven-eclipse-plugin-2.7/.../EclipsePlugin.java'
already exists
```
Then use a Subversion client 1.6 or newer and run `svn update`.

2. If you get an **error message** similar to:

```
[ERROR] BUILD FAILURE
[INFO]
[INFO] Unable to tag SCM
Provider message:
The svn tag command failed.
Command output:
svn: Path
'https://svn.apache.org/repos/asf/maven/plugins/tags/maven-eclipse-plugin-2.7'
already exists
```

Delete the tag using 

`svn del -m "re-releasing build" {svn path}`

This likely occurred because you're trying to restage the release and you didn't roll back the changes that created the previous tag, or you're trying to release a version that already exists. If that is the case, you need to adjust the versions in your POM and start over.

## Procedures for Ant + Ivy ##

<a href="https://ant.apache.org/" target="_blank">Apache Ant</a> is a popular command-line build tool. <a href="https://ant.apache.org/ivy/" target="_blank">Ivy</a> is a dependency manager designed to work with Ant. 

### 1 Prepare your build ###

Usually your normal build process will create the artifacts you want to publish (typically jars), but you may need to PGP-sign them the same way you sign your normal distribution artifacts. The jars are expected to follow the naming scheme `artifactId-version.jar`.

You will need a minimal POM for your jar. If you are already using Ivy, you can use the `makepom` task to create one from your `ivy.xml` file. Otherwise see the Apache Maven project's <a href="https://maven.apache.org/pom.html" target="_blank">documentation</a> for "minimal" and the Apache Compress Antlib's <a href="https://svn.apache.org/repos/asf/ant/antlibs/compress/trunk/project-template.pom" target="_blank">POM</a> for an example. 

If you are publishing multiple jars you may consider adding a parent POM to encapsulate the common information; see the Maven documentation for details. An example might be <a href="https://svn.apache.org/repos/asf/ant/core/trunk/src/etc/poms/pom.xml" target="_blank">Ant's parent POM</a>, used for the several jars that make up an Ant release.

Users who use your project's jars from the Maven repository rather than using your "normal" distributions will likely want additional artifacts containing the source files or javadocs matching your jars in files named `artifactId-version-sources.jar` and `artifactId-version-javadoc.jar` respectively. Don't forget to sign those jars as well if you provide them.

### 2. Create minimal Ivy files for your project ###

If you are not already using Ivy in your project you'll need to create a minimal `ivy.xml` file for it. The syntax is described in <a href="https://ant.apache.org/ivy/history/latest-milestone/ivyfile.html" target="_blank">Ivy's documentation</a>. Since you will only use the file to publish your artifacts, all you need to provide are the organization, module and revision definitions and an entry for each artifact you want to publish; see <a href="http://svn.apache.org/repos/asf/ant/core/trunk/release/ivy.xml" target="_blank">Ant's ivy.xml file</a> for a minimal version.

`organization` and `module` combined must match your Maven `groupId`.

You need `artifact` elements for your jar as well as the POM and any PGP signature file. You don't need artifacts for your checksum files (if you create any) since Nexus creates MD5 and SHA1 checksums for you.

If you are publishing source or javadoc jars as well, you'll need to provide something similar to Maven's classifier. You do so by adding an extra attribute to each artifact element that lives outside of Ivy's XML namespace and referencing this element in your `ivysettings.xml` file (see below). An example which uses this approach is <a href="http://svn.apache.org/repos/asf/ant/antlibs/compress/trunk/project-template.ivy.xml" target="_blank">the Compress Antlib's ivy.xml</a>. It contains additional information and `-sources` as well as `-javadoc` artifacts.

Alternatively you can specify the `-sources` and `-javadoc` artifacts inside your `publish` task rather than your `ivy.xml` file. If you use Ivy 2.2.0 or later, you can also configure it to PGP-sign your artifacts so you no longer need to specify your signatures as artifacts. Ivy's own <a href="http://svn.apache.org/repos/asf/ant/ivy/core/trunk/ivysettings-release.xml" target="_blank">ivy-settings.xml</a> configures Ivy to sign artifacts and the <a href="http://svn.apache.org/repos/asf/ant/ivy/core/trunk/build-release.xml" target="_blank">publish task inside the upload-nexus target</a> declares the POM as well as `-sources` and `-javadoc` jars as additional artifacts.

### 3. Configure Ivy to use Nexus ###

If you are already using Ivy you may need to adapt your `resolvers` configuration by adding an url resolver for Nexus and referencing that in a module matching your `ivy.xml`.

You usually need to adapt the `ivysettings.xml` file used by Ant by using the same values for `organization` and `name` on the module element that you used in your `ivy.xml` file (where `name` on the module element in `ivysettings.xml` corresponds to `module` in `ivy.xml`).

Ant's `ivysettings.xml` uses Ant properties for the authentication information and Nexus' URL which will be expanded by the `ivy:configure` task. It also shows how to use the `classifier` extra attribute.

### 4. Upload the artifacts ###

Uploading involves three Ivy tasks.

1. `ivy:configure` uses your `ivysettings.xml` file to configure Ivy (what else?).
2. `ivy:resolve` reads your `ivy.xml` and doesn't do much beyond that if you are only using Ivy to upload your artifacts.
3. `ivy:publish` publishes the artifacts to Nexus.

Here is a link to an <a href="http://svn.apache.org/repos/asf/ant/antlibs/common/trunk/upload.xml" target="_blank">example build file combining those steps</a> that expects you to provide the authentication information via the command line (i.e. `ant -Dupload.user=YOUR-ASF_ID -Dupload.password=YOUR-PASSWORD`).

## Common procedures ##

How to manage your staged release, no matter which build tool you used.

### Close the staged repository ###

Your artifacts should now exist in a new staging repository. See <a href="http://central.sonatype.org/pages/releasing-the-deployment.html#locate-and-examine-your-staging-repository" target="_blank">Locate and Examine</a> for instructions on how to "close" this repository to trigger the quality checks and prepare it for a vote.

Now you go call your vote. Based on the results you will either promote (yay!) or drop and restage the release. If you are an **incubating project**, don't forget the IPMC vote before promoting. The actual Vote process is project=specific, but if you're looking for some examples, the Maven project has thorough <a href="http://maven.apache.org/developers/release/maven-project-release-procedure.html" target="_blank">documentation on their voting process</a>.

### Drop a repository ###

If you bungled the release or your vote failed, follow <a href="http://central.sonatype.org/pages/releasing-the-deployment.html#close-and-drop-or-release-your-staging-repository" target="_blank">these instructions</a> to drop your repo. _Don't forget to roll back any SCM changes_.

### Promote a repository ###

Congratulations, your vote was successful. The last step is to <a href="http://central.sonatype.org/pages/releasing-the-deployment.html#close-and-drop-or-release-your-staging-repository" target="_blank">promote the artifacts</a> to the release repository where they will get picked up by Central.


