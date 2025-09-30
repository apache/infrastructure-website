title: Inside Infra September 2025 
date: '2025-09-30' 
permalink: newsletter0925
layout: post 

Welcome to *Inside Infra* for September, 2025

## Infra at Community over Code

The Infrastructure team was busy at Community over Code in Minneapolis this month. The team gave a track of presentations, had a host of valuable hallway conversations, and even hosted the first-ever Games Night at an ASF convention. 

Games Night looks to be a feature of ASF conventions in the future. And by way of hallway conversations and response and questions during Infra presentations, we have identified many in the ASF community who are willing to help support Infra's work

## Roundtable

The September Roundtable was part of Community Over Code The full summary, including many helpful comments and suggestions, is at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2025-08-06+1700+UTC" target="_blank">Infra Roundtable 2025-08-06 1700 UTC</a>

The October Roundtable will be a <b>Wednesday, October 1, 1700 UTC, on the #roundtabled channel in the ASF space on Slack</b>. The main topic will be 'Infra 101', and we are hoping folks associated with podlings or otherwise new to The ASF will join us to learn about what Infra can offer to projects, and how to access those resources.

Information about how to take part in the online roundtables is at <a href="https://infra.apache.org/roundtable.html" target="_blank">https://infra.apache.org/roundtable.html</a>.

## .asf.yaml for your project's product

.asf.yaml is a branch-specific configuration file that a project may create (using a text editor of your choice) and put in the root of a Git repository to control features such as

  - notification schemes
  - website staging
  - GitHub settings
  - Pelican builds

It operates on a per-branch basis, meaning you can have different settings for different branches, and only those branches with an active .asf.yaml file will kick off a feature. 

Much more information is available at <a href="https://github.com/apache/infrastructure-asfyaml" target="_blank">github.com/apache/infrastructure-asfyaml</a>

## Blocking cyber threats with MFA

There has been a dramatic increase recently in cyber threats, notably by agents of national governments who can deploy resources far beyond those available to the cliche hacker working from his mom's basement. These agents will take any opportunity to obtain one piece of personally identifying information (PII) about you, and then another and another, until they have enough 'markers' to be able to log into something while pretending to be you. That could be an online network where you work or play, your bank account, or where you put your software code for safekeeping. Once the agent has logged in to a network, they may be able to cause damage to areas well beyond your credit balance or your personal code repository.

You as an individual can reduce your vulnerability to such attacks by adopting <b>Multi-Factor Identification</b> (MFA) to log in to networks or services. You establish two or more 'factors', or types of evidence about who you are, with an authentication mechanism, and then have to provide those factors to that mechanism when logging in to the network you are trying to protect. The factors could include:

something you know (a password, your favorite band or sports team, your nickname when you were young)
something you are (biometric information, a retinal scan, a fingerprint...)

In the case of The ASF, you can help us protect project code repositories, private information (such as details about ASF members), and confidential documents that projects or The ASF have created in areas that should be available only to those with 'need to know'.

Many people still rely on SMS (Short Message Service) as the second factor to confirm their identity, using text messages to and from their phone or other device when logging in to sites and code repos. SMS is highly vulnerable, and Infra strongly recommends <b>against</b> using it as a factor in MFA. SMS vulnerabilities include:

redirect attack: An agent hacks in to the phone system you use and can get copies of messages, including one-time passwords (OTPs) or verification codes
SIM swap attack: Someone within your phone company could be bribed or induced to transfer your phone service to an agent, who can then intercept texts (including OTPs and codes) and calls intended for you.

There are many authentication services available, some based on open-source code, but Infra does not make recommendations of particular services at this time. We encourage you, though, to do your research, compare the usability of two or three good candidates, and settle soon on an MFA option that will help keep you, and us, more safe.


**More next month!**
