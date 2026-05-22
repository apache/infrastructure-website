title: Inside Infra May 2026 
date: '2026-05-22' 
permalink: newsletter0526 layout: post

## Welcome to _Inside Infra_ for May, 2026

### Roundtable

The May 6 Roundtable focused on **AI coding and its implications for ASF infrastructure**. 

To start, Andrew Musselman of the Tooling team described a tool he has developed to do a security scan of software in development. The tool inspects a potential release in more than 350 ways at three levels (from most to least critical) and provides recommendations for humans to review. 

Andrew demonstrated samples of the reports the tool produces, using Apache STeVe as the target. The tool found over 300 issues and reported them ranked by severity, plus providing other information. The tool originally focused on submissions to the Apache Trusted Releases platform, but it has now been made more generic so it can focus on any project's product.

Once the tool has a suitable name, it will be made generally available to ASF projects, and potentially further in the software development world. This will help address the flood of AI-generated pull requests that projects have trouble evaluating in a timely manner.

Discussion then addressed the challenges and opportunities AI coding presents to the ASF. Some comments:

  - Jarek Potiuk: Programming with AI seems to be a huge change in the way we do programming, and this makes a lot of people uneasy. There is an emotional journey toward embracing AI. A huge amount of code now is ai-generated or ai-supported.
  - Henri Yandell : AI and Jacquard looms are chapters of the same story, along with moving beyond punch cards and printing presses requiring manual placing of physical letters
  - Bob Thomson: none of this is currently profitable, so costs necessarily will increase massively - also no sign of the usual thing with technology where it gets cheaper; so far, rather the opposite.
  - Danny Angus: I do think we are behind the curve in ai-adoption for ops. We aren't building up repositories of prompts and steering. We certainly don't have agentic feedback loops

A summary of the discussion is at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2026-05-06" target="_blank">Infra Roundtable 2026-05-06</a>.

The next two roundtables will be

  - June 3, 1700 UTC. Piotr P. Karwasz will present on **release automation**.
  - July 1, 1700 UTC. Clay Johnson of Gradle will present on **predictive test analysis**.

Details about joining a roundtable, and what goes on at one, are here: <a href="https://infra.apache.org/roundtable.html">infra.apache.org/roundtable.html</a>.

### MFA

The soft launch of the new multi-factor authorization system for the ASF started in early April and is continuing with no major issues reported.

### Infra at C/C Glasgow

The Infrastructure team will present a full track at Community over Code Glasgow, October 11-14:

  - Apache Trusted Releases: Securing the Open Source Supply Chain
  - CI Workshop
  - Defending the Foundation: Implementing Automated Integrity Validation (AIV) Gates for Apache Projects
  - Distributed Denial of Service: Traffic characterization and mitigation
  - How To Infra
  - Infra Deployment Workshop
  - IRL Roundtable
  - Where are we going with ASF Infra?

Additionally, Infra will be hosting Games Night, which was very popular at the 2025 convention.

More details are at <a href="https://communityovercode.org/" target="_blank">communityovercode.org</a>. We hope to see you there! 

### Infra 101

**A guest with a membership to a single ASF Slack channel wants access to other channels.**

An ASF Member or Committer should make this request in a Jira ticket for Infra. Provide the guest's user name and the additional channels they should have access to.

_More next month!_
