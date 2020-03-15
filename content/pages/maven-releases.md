Title: Publishing Maven Releases

Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information.

this document describes how to release Maven artifacts. These are optional. Apache project **must** release all software packages through the ASF mirror system. See [Release distribution policy](release-distribution-policy.html) for more details.

**Note** make sure you are using version 3.0.5 or newer of Maven. You can <a href="https://maven.apache.org/download.cgi" target="_blank">download</a> and install the latest version of Maven before continuing.

## Setting up your project in the Nexus repository ##

The Nexus repository enforces security by constraining who can deploy or release a project's artifacts. Nexus maps which artifacts (usually by GroupId) your project produces. This is particularly helpful in preventing accidental releases of a project.

Before a project can use the repository to release Maven artifacts, it must be configured in Nexus. This is generally a quick and easy process. To get set up, <a href="https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?issuetype=3&priority=3&pid=10410&components=12312660&summary=Enable+Nexus+Access+For+[insert+project]&description=Project+URL:%0D%0DSVN+URL:%0D%0DMaven+Group+Ids:%0D%0DManaged+By+This+TLP+Project:" target="_blank">use this link</a> to create a Jira ticket with the following information:

  - **Project URL**: a link to your project page.
  - **SVN URL**: where you store your source code, in case Infra needs to look up more information.
  - **Maven Group IDs**: a list of the groupIDs for this project. They should all be subgroups of `org.apache`.
  - **Managed By This TLP Project**: if this is a subproject, list the TLP that is responsible. Subprojects usually don't have their own LDAP group, so we need the TLP LDAP group for permissions. 

If you have specific questions or concerns, please call them out in the ticket.
  
Once you file the Jira ticket, Infra will do the following:

  - **Set up the project in Nexus**: We configure your groupIds in Nexus and link them to the appropriate LDAP group for authorization.
  - **Move Existing Artifacts**: To maintain the proper `maven-metadata.xml` files and prevent rsync conflicts in Central, we must move all your artifacts to the new repository. We will mark the folder in the old repository as read-only to prevent accidental deployments.
  - **Check POMs**: If your project is Maven-based, we will check your POM for any obvious problems.
  
Further information about the POM and other Maven matters is <a href="https://maven.apache.org/pom/asf/" target="_blank">here</a>.

## Adjusting your build to use the Maven repository ##
To use the Maven repository, follow these steps.

### Inherit the Apache POM ###
Inherit the Apache Parent POM like this:

```
<parent>
  <groupId>org.apache</groupId>
  <artifactId>apache</artifactId>
  <version>10</version>
</parent>
```

This parent POM sets up the defaults so your `<distributionManagement>` section uses the correct release and snapshot repositories. Be sure to remove those from your POM so they inherit correctly. Keep the entry for deploying your site (if you use Maven to deploy your site). If you do, we suggest you use `apache.website` as the id to better match the settings below and to save the sanity of committers working on multiple projects.

The POM also provides a default configuration to make sure that a correct source archive is created for your project. This is separate and in addition to the typical `-sources.jar` that is created.

### Set up your development environment ###




_moving information here from `https://www.apache.org/dev/publishing-maven-artifacts.html`_

possibly include these fragments:

  - Don't try to publish `.sha256`, `.sha512` files yet; Nexus doesn't handle them (as of March 2018)
  = `.md5`s in `dist.apache.org/repos/dist/release/` must be removed manually.
