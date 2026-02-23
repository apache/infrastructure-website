title: Inside Infra February 2026 
date: '2026-02-23' 
permalink: newsletter0226
layout: post 

**Welcome to _Inside Infra_ for February, 2026**

## Roundtable

At the February Roundtable, Jarek Potiuk talked about the **dependency tracker** he developed for Apache Airflow, and how he used **AI** to help with developing the tool.

Airflow builds multiple versions of its product from one common repository. Each version has a slightly different set of dependencies. When a dependency needs to be updated. it is necessary to check whether each flavor that uses it is ready to work with the updated version. As they deal with about 100 variants of their product drawing on 700 dependencies, the challenge of getting everything so it will compile and run properly is challenging.

Jarek demonstrated how the dependency tracker monitors incoming updates and the release to which they relate, which makes it easier for the team to focus on any adjustments they need to make to one or more releases before updating the dependency they share. The tool has helped them identify and keep current a 'golden' set of dependencies to work with.

He also described the process of prompting AI to help with the creation of the tool, and how the machine-produced code goes through careful testing and human review before the team puts too much trust in it.

The full conversation, plus a link to a YouTube video of Jarek speaking at FOSDEM about the dependency tracker, is at <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2026-02-11" target="_blank">Infra Roundtable 2026-02-11</a>.

The next Roundtable will be **Wednesday, March 4, 2026, 1800 UTC**. The featured topic: new tools for **coping with the increase in distributed abuse and attacks on ASF infrastructure**.

## Atlassian migration - projects needed for beta testing

Atlassian is discontinuing support for the on-premises versions of Jira Issue Tracker and the Confluence Wiki, so The ASF will be migrating to cloud instances of these services in the coming months.

We need projects that are willing to let Infra copy their ticket and wiki data to a cloud test location, and test how working with the cloud versions of these tools goes. Infra will perform the test migration, so project members only need to engage in testing: 

1. Log in to the Cloud test instance 
2. Browse around your test Jira project / Confluence wiki and ensure all looks as it does in the live, locally-hosted instance 
3. Create some Jira tickets, delete some, go through your usual workflow, etc. Create, edit, move, and delete some wiki pages (go crazy: remember, this is a test environment so you cannot hurt the real pages). 
4. After a few days playing, or in case of problems, report to the Infra team via a (real) Jira ticket (see below). 

The information you provide will be a huge help to the migration effort.

If your project is willing to participate, please create an INFRA Jira ticket, which we will use to track your project's testing progress. For a component, select `migration`, and give it a title in this form: `Atlassian testing - PROJECT NAME`.

If you are not sure about something in this testing effort, ask us via `users@infra.apache.org` or in the #asfinfra Slack channel.

Testing begins **NOW** - and we need to complete testing by the end of April so we can move to the next phase of the migration


## When you need to talk with Infra

Years ago, when the Infra team was largely made up of volunteers, the best way to give or get information was by email to `users@infra.a.o`. That is no longer the case. The best way by far to get help from Infra is by opening a Jira ticket. The best ways to share information or engage with Infra are by the #asfinfra Slack channel, or by taking part in a Roundtable (each roundtable has time after the main presentation when anyone can bring forward an issue that needs attention). Information on joining and taking part in roundtables is at <a href="https://infra.apache.org/roundtable.html" target="_blank">infra.apache.org/roundtable.html</a>.


## The end of Reviewboard

Apache Reviewboard is very rarely used these days, and our Reviewboard instance is many years out of date. So Reviewboard at `reviews.apache.org`, which opened for business in October, 2010, will be turned off on March 31, 2026. There will be no direct replacement.


**More next month!**
