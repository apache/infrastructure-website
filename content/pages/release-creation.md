Title: Release Creation Process

These best practices help guide a PMC through the steps to create and publish an Apache software product release. It complements the formal <a href="https://www.apache.org/legal/release-policy.html" target="_blank">Apache Release Policy</a>, defining what must be in a software release, and [Release Distribution Policy](release-distribution-policy.html), which describes the technical details of where releases are placed/mirrored.

Every Apache Software Foundation project software release must meet requirements for content , process , and publication. These requirements ensure that Apache contributors and users benefit from appropriate legal protection the ASF provides, and reflect the Foundation's goals of open, collaborative software development.

## What makes an Apache release ##

An Apache release is a set of **valid**, **signed**, artifacts, **voted on** by the appropriate PMC and **distributed** on the official ASF release infrastructure. See below for discussion of the words in bold, all of which are essential.

To make a release, an Apache project:

1. Has code that complies with the software licensing requirements
2. Decides as a community to make a release, and designates a release manager
3. The release manager prepares and signs the proposed release materials
4. The PMC votes whether to approve the release
5. If the vote passes, the release manager copies the artifacts to the distribution infrastructure.

A release starts when the project community agrees to make a release. However, no release manager can make a valid release unless the community has taken the necessary steps. The source code and build process must comply with the ASF legal and intellectual property requirements for a valid release, and the project must have the infrastructure in place to correctly **sign** the release artifacts (see below).

## The release manager ##

Most projects designate a committer to be the _release manager_ who takes responsibility for the mechanics of a release. It is a good idea to let several committers take this role on different releases so that more than one person is comfoortable doing a release. Release managers shepherd a release from an initial community consensus to getting the compiled code package to final distribution, and may be involved in publicizing the release to the project's community and the ASF in general.

Release managers do the mechanical work; but the PMC in general, and the PMC chair in particular (as an officer of the Foundation), are responsible for compliance with ASF requirements.

Any committer may serve as release manager.

## A valid release package ##

The Apache Software Foundation exists to create open source software, so the fundamental requirement for a release is that it has the necessary source code to build the project. A project may provide compiled binaries of each release for the convenience of users.

All project source code must be covered by the <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank">Apache License, version 2.0</a>. The license or appropriate boilerplate text must be included in each source file. For the license to be valid, the code must have been contributed by an individual covered by an appropriate <a href="https://www.apache.org/licenses/contributor-agreements.html" target="_blank">contributor license agreement</a>, or have otherwise been licensed to the Foundation and passed through IP clearance. See <a href="https://www.apache.org/legal/release-policy.html" target="_blank">this page</a> for details on release requirements. When in doubt, contact the Foundation's Legal resources by filing a Jira ticket under the 'LEGAL' project. The Apache <a href="https://creadur.apache.org/rat/" target="_blank">Release Audit Tool (RAT)</a> can help you verify that your proposed release complies with the requirements.

Many projects have dependencies on non-Apache components. For an Apache release to be valid, it can only depend on non-Apache components that have compatible licenses. For more information on third party licenses allowed, see the <a href="https://www.apache.org/legal/resolved.html" target="_blank">ASF Third Party License Policy</a>.

## Signing release artifacts ##

