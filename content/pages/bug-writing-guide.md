Title: Writing a good bug report
license: https://www.apache.org/licenses/LICENSE-2.0

  - <a href="#overview">Bug reporting</a>
  - <a href="#systems">Bug-tracking systems</a>
  - <a href="#newbug">Is this a new bug?</a>
  - <a href="#useful">A useful bug report</a>
  - <a href="#blocked">If your report or comment gets blocked</a>
  - <a href="#followup">Following up</a>


<h2 id="overview">Bug reporting<a class="headerlink" href="#overview" title="Permanent link">&para;</a></h2>

When you run into an issue with ASF instrastructure, with the software one of the ASF projects produces, or with an ASF-related website, you may be the first person to have noticed the issue. If so, you should report it. The people responsible for the thing that has a bug or other issue will be happy to know about the problem so they can fix it before more people run into it.

For the purposes of this discussion, we'll call any issue, from a calculation error in a function to a punctuation error on a web page, a "bug". Something that you would like to see added to an application or a website to make it better would be an "enhancement request". Both are useful; we are looking at bugs here.

**Note**: do not include sensitive information in a bug report. See the [Infra policy on sharing sensitive information](sensitive_info.html) and send such information by email to `root@infra.apache.org`. Provide a reference to any related bug reports.

<h2 id="systems">Bug-tracking systems<a class="headerlink" href="#systems" title="Permanent link">&para;</a></h2>

ASF has two bug-tracking systems:

  - <a href="https://issues.apache.org/jira/" target="_blank">Jira</a>
  - <a href="https://bz.apache.org/" target="_blank">Bugzilla</a>
  
Infra itself uses <a href="https://issues.apache.org/jira/projects/INFRA/issues" target="_blank">Jira</a> (requires login).

Projects can use either system, or some other method of tracking bugs. If the bug you found is in a project's application or website, you need to find out where that project wants to hear about it. If you cannot find the project in either Jira or Bugzilla, ask for advice on the project's `dev@` or `users@` mailing list.

<h2 id="newbug">Is this a new bug?<a class="headerlink" href="#newbug" title="Permanent link">&para;</a></h2>

Before spending the time filing a bug report, it's useful to check whether a report about the bug you found already exists. If so, you can add comments or additional information to the existing report.

Infra maintains several real-time [status pages](stats.html). If the infrastructure issue you ran into is reported on one of these pages, Infra already knows about it.

If what you found seems to be a new bug, you get to report it!

<h2 id="useful">A useful bug report<a class="headerlink" href="#useful" title="Permanent link">&para;</a></h2>

Useful bug reports get bugs fixed. A useful bug report is usually:

  - Reproducible. If a developer or sysadmin can't see it or conclusively prove that it exists, they may stamp it "WORKSFORME" or "INVALID", and move on to the next bug. Every detail you can provide helps.
  - Specific. The quicker the person looking at your report can connect your issue to a specific problem, the quicker they can fix it.

Let's say the application you're testing is a web browser. You crash at foo.com, and want to write up a bug report:

**A bad report**: "My browser crashed. I think I was on foo.com. My computer uses Windows. I think that this is a really bad problem and you should fix it now. By the way, your icons really suck. Nobody will use your software if you keep those ugly icons. Oh, and my grandmother's home page doesn't look right, either, it's all messed up. Good luck.

**A good report**: "I crashed each time when I went to foo.com, using the 10.28.99 build on a Win NT 4.0 (Service Pack 5) system. I also rebooted into Linux, and reproduced this problem using the 10.28.99 Linux build. The browser crashed each time while drawing the Foo banner at the top of the page. I broke apart the page, and discovered that the following image link will crash the application reproducibly, unless you remove the "border=0" attribute: `<IMG SRC="http://foo.com/images/topics/topicfoos.gif" width=34 height=44 border=0 alt="News">`"

When you enter a bug report, both Bugzilla and Jira provide some helpful fields where you can select things like your operating system. If you are reporting a bug via email to a project, you need to remember to provide all the relevant information that could help identify the source of the problem.

Once you have established the conditions (operating system, web browser, and so on), include the steps to reproduce the problem:

  1. What you wanted to do.
  2. The steps you took to do it.
  3. What you expected to happen.
  4. What actually happened.
  
If you can capture onscreen error messages, extracts from logs, or relevant screen shots, include them in the report.

The bug-tracking systems allow you to suggest a **severity** for the bug. If you are reporting by email, explain the urgency of getting the bug fixed.

Make sure you provide a useful **title** for the report:

   - Useful: "PCMCIA install fails on Tosh Tecra 780DVD w/ 3c589"
   - Not useful: "Browser crashes" or "Install problem"
   
Review [Creating a Jira ticket](jira-guidelines.html) for specifics about Jira bug reports.

### What not to include ###

Adding editorial comments ("what sort of idiot would release a product with such a bug?") is worse than useless. It sets you up as a critic rather than a partner to the people whose help you need.

<h2 id="blocked">If your report or comment gets blocked<a class="headerlink" href="#blocked" title="Permanent link">&para;</a></h2>

Infra uses various tools and techniques to prevent spammers from posting material on Jira. If your new bug report, or comment on an existing report, gets blocked, [contact Infra](contact.html) so we can resolve the issue and fine-tune our spam filters.

<h2 id="followup">Following up<a class="headerlink" href="#followup" title="Permanent link">&para;</a></h2>

In either bug tracking system you can arrange to get updates whenever the status of the bug report changes. If you are reporting by email and want to get updates sent to one or more email addresses, specify them.

_Based on contributions from Eli Goldberg, Claudius Gayle, Peter Mock, Chris Pratt, Tom Schutter, and Chris Yeh._
