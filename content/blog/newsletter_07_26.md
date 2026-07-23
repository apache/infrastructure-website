title: Inside Infra July 2026 
date: '2026-07-23' 
permalink: newsletter0726
layout: post 

Welcome to _Inside Infra_ for July, 2026

## Roundtable

The July Roundtable featured a presentation by Clay Johnson of Gradle Technologies on **Predictive Test Selection**, which can propose a subset of a project's test to cover only those modules and functions that the most recent commit may affect. This can dramatically reduce build time and the amount of build resources deployed. 

More details, including a PDF of the presentation slide deck, are on this page: <a href="https://cwiki.apache.org/confluence/spaces/INFRA/pages/430408857/Infra+Roundtable+2026-07-01" target="_blank">s.apache.org/wjtlv</a>.

The next roundtable will be **August 5, 1700 UTC**. The Tooling team will present the current state of the **Apache Trusted Releases (ATR)** platform, and Daniel Gruno will report on the current state of the **Contingent Approval Platform (CAP)**. (See the call for CAP testers, below.)

Note: the October Roundtable will be an in-person event at Community Over Code Glasgow.

Details about joining a roundtable, and what goes on at one, are here: <a href="https://infra.apache.org/roundtable.html">infra.apache.org/roundtable.html</a>.

## Atlassian migration

Work continues on the migration of our in-house Jira and Confluence Wiki services to their cloud equivalents. When the change-over will happen is not yet available.

## MFA

The new ASF multi-factor authentication (MFA) system is live and protecting access to some ASF services and systems, such as webmod, but Infra and early adopters are still working on resolving some usability issues and completing the documentation before expanding its use across the ASF.

From the in-development documentation, MFA "adds a second step to your login. After entering your ASF username and password, you confirm your identity with a device you control -- an authenticator app on your phone, a hardware security key, or a passkey built into your laptop." Further information is available at <a href="https://infra.apache.org/mfa.html">mfa.html</a>.

## CAP - active beta seeks testers

Work is in progress to streamline and automate procedural/technical decision votes that relate to infrastructure, security, and tooling, using a service called the Contingent Approval Platform (CAP). CAP provides a single, uniform workflow for establishing proof of consensus in a project for a given action, whether this is a social/manual thing or an automated task that requires approval.

A demo version is up and running at <a href="https://cap-test.apache.org" target="_blank">cap-test.apache.org</a>, and the 'about' page on that site provides documentation and the tool's rationale in great detail.

## Infra at C/C Glasgow

The conference website is now live: <a href="https://communityovercode.org/" target="_blank">communityovercode.org</a>. It does not yet have a detailed schedule of when each talk and presentation takes place, but that will be coming soon.

## Infra 101: Failed update to .asf.yaml

If you made a change to your project's .asf.yaml file and it doesn't seem to have updated, make a semantic change, not a white-space change, to the file, commit it, and try again. A semantic change is something like adding a labels entry under github. See: <a href="https://github.com/apache/infrastructure-asfyaml" targert="_blank">github.com/apache/infrastructure-asfyaml</a>.

**More next month!**
