title: Inside Infra June 2025 
date: '2025-06-23' 
permalink: newsletter0625 layout: post

**Welcome to Inside Infra for June, 2025**

## Roundtable

Discussions at the June Roundtable covered, among other things:

  - Misuse of GitHub Actions. Projects are using, and sometimes force-pushing, tags, rather than SHAs. While there are GHA linters that can help identify problems, we should move actively to encourage projects to stop using tags in GHAs, and only use SHAs. There was discussion of the possibility of applying some sort of seal of approval on custom GHAs that comply with this requirement.
  - Creating a checklist or scorecard to encourage creators to bring their custom GHAs into compliance with our requirements.
  - Review of progress on repository.a.o, and Tooling's progress on the Apache Trusted Release platform.
  - What PMCs can use as a password manager (at the moment, only a private repo on SVN or Git).
  - Complete notes from the meeting are at Infra Roundtable 2025-06-04 1700 UTC

The next roundtable will be **Wednesday, July 2, 1700 UTC**. Infra will pull a number of coming-soon improvements out of its hat for discussion.

Information about how to take part in a roundtable is at <a href="https://infra.apache.org/roundtable.html" target="_blank">infra.apache.org/roundtable.html</a>.

## Uptick in IP bans due to 404 errors on repository.apache.org

Infra is seeing a significant increase in the number of IP bans placed by our automated block system, Blocky. These are largely due to incorrectly configured Maven builds or Artifactory systems using `repository.apache.org` as a primary repository.

`repository.apache.org` is not a general-purpose Maven repository, and should only be used by ASF Committers to test pre-production ASF code artifacts. <a href="https://mvnrepository.com/repos/central" target="_blank">Maven Central</a> is the correct public Java artifact service.  

In addition, the Maven project identified an issue where repository.apache.org was incorrectly included in the Apache Parent POM. Downstream users should upgrade their parent POM to avoid this issue.

For further information, see: <a href="https://issues.apache.org/jira/browse/MPOM-451" target="_blank">issues.apache.org/jira/browse/MPOM-451</a>.

If you believe your IP has been blocked, you can check your connectivity status via <a href="https://infra.apache.org/abc/" target="_blank">infra.apache.org/abc</a>.

## Bugzilla

Due to a significant increase in abuse, largely driven by AI scraping, the ASF Bugzilla instance is now only available to **authenticated users**. To use it, log in with your ASF credentials.

## GitHub Actions compliance deadline

Infra received this message from GitHiub:
```
The Windows Server 2019 runner image will be fully unsupported by June 30, 2025.
To raise awareness of the upcoming removal, we will temporarily fail jobs using Windows Server 2019.
Builds that are scheduled to run during the brownout periods will fail.
The brownouts are scheduled for the following dates and times:
 
June 17 13:00-21:00 UTC
June 24 13:00-21:00 UTC
 
What you need to do
 
Jobs using the windows-2019 YAML workflow label should be updated to windows-2022, windows-2025 or windows-latest.
You can always get up-to-date information on our tools by reading about the software in the runner images repository.
Please contact GitHub Support if you run into any problems or need help. 
```

## The whitespace kick trick

If a build fails, sometimes it does not restart even after you have fixed the issue that caused it to fail. A trick that often works is to add a whitespace at the end of any line of code and commit that updated file to get the build to start again. If this fails, contact Infra

Infra is working on a new flow of events for builds that will improve stability and observability; we will let the world know when it is in place.



**More next month!**
