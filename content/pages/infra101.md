Title: Infra 101

## What Infra is ##

The Infrastructure team (Infra) manages the systems and hardware that run the services that the ASF and its projects depend on. Infra also reviews requests to install new systems or software on ASF machines. It's a small team, distributed across many time zones. Someone is on duty at all hours to respond to emergency issues.

## Infra and incubating projects ##

Your mentor is your first stop in figuring out technical issues for your incubating project. They can explain, based on long experience, how to get the best out of the ASF systems, machines, and services. However, if the mentor is not available, members of the new project can move forward the process of setting up project resources.

### Phase 1: The first steps to establish a new podling ###

**Podling bootstrap file**

The very first task is for a mentor or champion to bootstrap the project via the _podlings.xml_ file, that tracks all current and previous podlings.

This file is located at <a href="https://svn.apache.org/repos/asf/incubator/public/trunk/content/podlings.xml" target="_blank">here</a>. You may use existing entries as a primer.

**DNS**

DNS entry ($projectname.apache.org) is required for the podling website and mailing lists to work. Request this once podlings.xml has been updated, by filing a JIRA ticket with Infra. See the next point before completing the ticket.

The Domain Name System (DNS) is a hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities.

**LDAP**

Activate LDAP for the project by filing a JIRA ticket with Infra. Typically you can request both LDAP and DNS in the same ticket.

The Lightweight Directory Access Protocol (LDAP) is an open, vendor-neutral, industry standard application protocol for accessing and maintaining distributed directory information services over an Internet Protocol network.

### Phase 2: Mailing lists ###

Mailing lists are an integral part of the Apache Way. Projects must have them set up before requesting other development resources
Typically, a project will need three lists; private@ for podling PMC communications and/or security issues, dev@ for development discussions, and commits@ for code commit notifications.

Projects may also request separate lists for issues, pull requests, and users (this is very important once you do your first software release and begin to develop a user community) if they like, and can do so at any time.

The project's mentor(s) can can request mailing lists once DNS and LDAP are set up, through <a href="https://selfserve.apache.org/" target="_blank">SelfServe</a>.

It takes about twelve hours after the mentor makes the request before the mailing lists become active. This gives Infra time to catch and deal with any errors in the requests.

### Phase 3: Requesting new project resources or moving existing ones ###

**Code repositories**

Version control 99% of time requires a github.com transition of existing repositories to the `github.com/apache/` organization

For NEW repositories or if you wish to copy existing code without transferring github stars, etc,, your mentor can request new repositories via <a href="https://selfserve.apache.org/" target="_blank">SelfServe</a>.

For existing repositories on GitHub that needs migration, file a JIRA ticket with Infra.

**Bug tracking**

You can enable GitHub issues (and wikis) via our .asf.yaml service. This is a per-repo feature. The project can request a JIRA instance via <a href="https://selfserve.apache.org/" target="_blank">SelfServe</a>.

**Confluence Wiki**

Every project can have a dedicated space on the Apache Confluence wiki. Project participants can use the space to develop documentation, share planning and process documents, and work collaboratively. They can opt to make some pages in their space available to the public. Request a Confluence wiki space for the project via <a href="https://selfserve.apache.org/" target="_blank">SelfServe</a>.

**Website**

Standard practice is to create a web site repository via <a href="https://selfserve.apache.org/" target="_blank_">SelfServe</a>, and then use .asf.yaml for publishing on $project.apache.org.
