Title: Policy for nightlies.apache.org

license: https://www.apache.org/licenses/LICENSE-2.0

**Note**: this policy may evolve in the course of a larger review of release and download strategies for The ASF.

This document explains `nightlies.apache.org`: how to use the service and how much data data you can store there for how long, and what Infra expects of users of the service.

## History
The service was created to replace previous storage services at `ci.apache.org/projects` (Buildbot) and is also a replacement for artifacts and logs that
were otherwise kept on `ci-builds.apache.org` (was `builds.apache.org`) along with the other Controllers (ci-hbase, ci-hadoop etc.).

## Usage
nightlies, as implied by its name, is designed as a 'short term' storage solution. Examples of how projects use the service are:

  - Nightly Snapshots of trunk/main builds for developer-only testing.
  - Different website versions - e.g : trunk/main/bleeding edge docs , RC1, $latest release version, $previous release version.
  - Javadocs / Api Docs.
  - Logs of jobs.
  - Artifacts, packages as created by a build or builds.
  - Historical data for analysis, graphing etc.
  - A generated index.html to your sub-directories of data.

**Note**: nightlies is **not an official release channel**. Do not place product release artifacts here. Please review Apache's release distribution policy, especially the section on release channels.

There are various ways to get your data to nightlies.apache.org and this is covered on `https://nightlies.apache.org` itself.

## Data Retention
Data of previous jobs, including artifacts and logs, should only be kept for around 30 days as a general guide.
Keeping multiple website versions is fine; and we expect you would want to have a trunk/main version and perhaps
a version of the current release / previous release. Rotate as your releases occur. Release artifacts would obviously be kept
around for more than 30 days, which is fine. The same would apply for apidocs / javadocs.

Generally, Infra is okay with statistical gathering and display for review and further analysis, We do understand
the need for seeing how builds perform over time, but please note that, again, this is considered data that
could be lost. If it is important to your project, you should back it up off-site.

## Expectations
All data placed on nightlies should be considered 'ephemeral'. Infra does NOT back up nightlies.apache.org.
Ideally, build data/results are reproducible from any previous commit and should be replayed if needed. The
same applies here to your website versions and apidocs / javadocs.

The project should not create permalinks to specific data or specific urls. Consider using symlinks to $trunk, $current,
$previous etc. so that if the data underneath needs to be regenerated, incoming links would continue to work.
Infra will ensure the longevity of project level URIs such as `nightlies.apache.org/$project`.

## Summary
nightlies.apache.org is a service provided by Infra for all projects to use. Infra will maintain this service for as long as it sees
it is of benefit to projects. It will guarantee project level urls. Anything underneath `nightlies.apache.org/$project/*` is not
guaranteed. Data is ephemeral, should be considered volatile and is not backed up. Projects should utilize off site
backups for any data it deems too important to lose. Projects should be able to reproduce the data at any time should
they wish for any restoration of data following data loss (hardware issue etc.).
