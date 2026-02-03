title: Parallel PUT problem in repository.apache.org with Apache Maven 3.9.12  
date: '2026-02-03' 
permalink: parallelputproblem layout: post


Apache Maven 3.9.12 has a change that causes a problem in repository.apache.org (the Sonatype Nexus 2 Pro staging suite): if your build uses **parallel PUT** deployment, the build creates a separate staging repository for each of the requests instead of assembling everything in one repository.

The Maven team is working on a resolution to this issue. Until the fix is available, they suggest **disabling parallel PUTs**. 

You can do this in several ways:

1. Upgrade to ASF Parent POM 37 (https://maven.apache.org/pom/asf/) which contains the workaround (https://github.com/apache/maven-apache-parent/pull/566).

2. Using the command line, add the user property `-Daether.connector.basic.parallelPut=false`

3. In the project root directory `.mvn/maven.config`, add a file with these contents:

`-Daether.connector.basic.parallelPut=false`

Read more about this here: https://maven.apache.org/configure.html#mvn-maven-config-file

4. In ~/.m2/settings.xml, add this property to a profile that is always enabled:

`-Daether.connector.basic.parallelPut=false`

**Note**: you only have to use one of these options, not all four.

This is a resolver property, so you cannot deal with it as a POM project property. You must pass it as a user property to the Maven instance you are using for the build.

See <a href="https://maven.apache.org/resolver-archives/resolver-1.9.25/configuration.html" target="_blank">maven.apache.org/resolver-archives/resolver-1.9.25/configuration.html</a> for information about the configuration key `aether.connector.basic.parallelPut`.

## How to fix having multiple staging repositories

If your project's build has run into this issue already, and you have multiple staging repositories, here is how to fix this issue:

  1. Delete the multiple parallel staging repositories that the build created
  2. Apply one of the four suggested fixes to disable parallel PUTs
  3. Build the release again.

The Apache Maven project will advise users and Infra when this workaround is no longer needed. The issue is tracked in <a href="https://github.com/apache/maven/issues/11634" target="_blank">github.com/apache/maven/issues/11634</a>>.
