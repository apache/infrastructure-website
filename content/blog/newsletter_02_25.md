title: Inside Infra February 2025 
date: '2025-02-25' 
permalink: newsletter0225 layout: post

<h2>Roundtable</h2>
<b>The February roundtable</b> took place Wednesday, February 5, 2025. The main topic was creation, review and management of <b>custom GitHub Actions</b> that projects can use in their compile and build processes, and the self-serve way to add custom GitHub Actions to the GHA Allowlist.

There is now a management committee of subject matter experts who will review custom GitHub Actions as ASF community members submit them, and will add them to the ASF allowList if they are approved. Further details are available at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2025-02-05+1700+UTC" target="_blank">Infra Roundtable 2025-02-05 1700 UTC</a>

We hope this process will fix the current bottleneck that is slowing down review of new GitHubActions, and will provide guidance to help submitters create stronger and more resilient code.


There will be <b>no roundtable</b> in March, 2025. The next roundtable will be Wednesday, April 2, 2025, 1700 UTC. The main topic will be announced soon. 

See <a href="https://infra.apache.org/roundtable.html" target="_blank">infra.apache.org/roundtable.html</a> for details about how to join a roundtable, and what happens at it. 

<h2>ASFMM</h2>

Infra has developed a custom chat service that ASF Members can use during the annual Members' Meeting, which this year is on <b>March 6</b>.

The tool, <b>ASFMM</b>, is available at <a href="https://asfmm.apache.org/oauth.html" target="_blank">asfmm.apache.org/oauth.html</a>. Members must log in using their ASF credentials to use it.

ASFMM has two channels: the main channel, where members can follow the business of the meeting, and the 'back channel' for informal comments and conversations. ASFMM ends our reliance on third-party chat tools or sites.

<h2>.asf.yaml update</h2>

Infra is releasing a significant update to .asf.yaml, the versatile controller for compiles and builds. The documentation is not complete on the biggest new option, adding custom features to you .asf.yaml file, so for the moment the new version is available as an 'opt-in' (see below).

Other significant enhancements include:

<ul>
  <li>You can <b>enable or disable GitHub discussions</b>. Learn more at <a href="https://github.com/apache/infrastructure-asfyaml/tree/ng-parser?tab=readme-ov-file#repository-features" target="_blank">github.com/apache/infrastructure-asfyaml/tree/ng-parser?tab=readme-ov-file#repository-features</a></li>
  <li>Projects can enable/disable the <b>merge PR</b> button in the GitHub UI and configure which actions to allow (squash, merge, or rebase). Learn more at <a href="https://github.com/apache/infrastructure-asfyaml/tree/ng-parser?tab=readme-ov-file#merge" target="_blank">github.com/apache/infrastructure-asfyaml/tree/ng-parser?tab=readme-ov-file#merge</a>.</li>
  <li>Better error validation and reporting when the build process encounters a badly-configured .asf.yaml file.</li>
  <li>Better tracking of which commits caused which updates to the code.</li>
</ul>

To opt in to the updated .asf.yaml, add this code to your existing .asf.yaml file:

```
meta:
  nextgen: true
```

If you run into issues or decide you do not want to use the new features yet, opt out by removing the code snippet from your .asf.yaml file.

Please report any problems or errors you encounter by email to <code>users@infra.apache.org</code>.

More next month!
