Title: Guide for new project contributors

This guide provides tips and suggestions for new <strong>contributors</strong> to Apache projects. A contributor is anyone who wants to contribute code, documentation, tests, ideas, anything to any project hosted here at the Apache Software Foundation (ASF).

**Note**: if you are interested in contributing _financially_ to support the ASF and the open-source movement, please see <a href="https://www.apache.org/foundation/contributing.html" target="_blank">Sponsorship and Donations</a>.

More information is available in the [guide](new-committers-guide.html) and [FAQs](committers.html) for project committers.

<h2 id="links">Contents<a class="headerlink" href="#links" title="Permanent link">&para;</a></h2>

  - <a href="#comdev">Community Development is here to help!</a>
  - <a href="#mail">Everything happens on mailing lists</a>
  - <a href="#howitworks">How open-source works at Apache</a>
  - <a href="#svnbasics">Source code repositories</a>
  - <a href="#providingfeedback">Providing feedback to Apache projects</a></i></p>


<h3 id="comdev">Community Development is here to help!<a class="headerlink" href="#comdev" title="Permanent link">&para;</a></h3>

Apache values "Community over code", and is full of volunteers who want to help you. Guideposts and helpful information and mentors for newcomers to Apache can be found at <a href="http://community.apache.org/" target="_blank">Community Development</a>.

<h3 id="mail">Everything happens on mailing lists<a class="headerlink" href="#mail" title="Permanent link">&para;</a></h3>

Virtually everything at Apache happens on one of our publicly archived mailing lists. Find the <a href="https://www.apache.org/dev/#mail" target="_blank">right Apache mailing list</a> and read some <a href="https://www.apache.org/dev/contrib-email-tips" target="_blank">tips</a> on asking questions and making comments.

<h3 id="howitworks">How open-source works at Apache<a class="headerlink" href="#howitworks" title="Permanent link">&para;</a></h3>

There are many books, presentations, and academic papers about the way open-source software development works and how you can become a valuable member of the open source/free software community. For an overview of how it works at Apache, see

  - the <a href="https://www.apache.org/" target="_blank">ASF home page</a>
  - the <a href="https://www.apache.org/foundation/how-it-works.html">ASF How it works</a> document
  - Cameron Riley's [Understanding Opensource](understanding-opensource.html) document
  - the <a href="https://www.fsf.org/" target="_blank">Free Software Foundation (FSF) website</a>
  - the <a href="https://www.opensource.org/" target="_blank">Open Source Initiative website</a>
  - <a href="http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/" target="_blank">The Cathedral and the Bazaar</a>

<h3 id="svnbasics">Source code repositories<a class="headerlink" href="#svnbasics" title="Permanent link">&para;</a></h3>

Apache projects use either of these repository systems:

  - [Subversion](svn-basics.html)
  - [Git](git-primer.html).

<h3 id="bleeding-edge">Nightly code / Development code<a class="headerlink" href="#bleeding-edge" title="Permanent link">&para;</a></h3>

Getting the source directly from the source repository usually gives you the latest, or "bleeding edge" version of that particular project.

<h3 id="providingfeedback">Providing feedback to Apache projects<a class="headerlink" href="#providingfeedback" title="Permanent link">&para;</a></h3>

A valuable way to contribute to ASF projects is to use the project's software and then provide feedback about it to its developers. Different Apache software
projects have different preferences about how you should submit feedback. Check out the project website for more information. In the absence of project-specific information on how to provide feedback, follow these guidelines.

A vital part of the ASF projects are the project mailing lists. Most projects have a users' list named `users@${project}.apache.org` or `user@${project}.apache.org`. Subscribe to it by sending an e-mail to `users-subscribe@${project}.apache.org`, then follow the instructions. We have many <a href="https://www.apache.org/dev/contrib-email-tips" target="_blank">tips on asking questions</a> in a way that gets answers.

Tell the developer and user community about your use of the software product, your experiences in setting it up, issues you encountered, and any general feedback you may have. Don't forget to include any positive observations that will show you appreciate the effort the team is making. Your story will likely be very welcome if you write it clearly, in a friendly tone, and Read The Manual before asking for answers that you could find there. You'll probably receive enthusiastic responses from some of the developers and other users (although responses may not appear right away: everybody is busy). 

If you found specific issues or have an idea about how things should work, the project may ask you to submit a detailed bug report or patch to improve things.

Many projects also have a developer-focused mailing list named `dev@${project}.apache.org` for discussion of technical project details.

<h4 id="bugreports">How to send in a bug report<a class="headerlink" href="#bugreports" title="Permanent link">&para;</a></h4>

Projects take bug reports very seriously. To help a team fix the bug quickly, include as much information with your report as possible, such as your
platform, version numbers of the application you were using, error logs, configuration, etc. If you are not
sure whether a piece of information is relevant, include it.

See [Writing a good bug report](bug-writing-guide.html).

#### How to submit a patch ####

A patch is a computer-generated file that describes differences between different versions of one or more source files, with the intention of improving the current application code. Different software projects have different preferences about how to submit a patch. Check out the project website for more information.

For an example of project patch guidelines,see the Apache Subversion project's <a href="https://subversion.apache.org/docs/community-guide/general.html#patches" target="_blank">patch guide</a>.

To contribute a change or addition to existing source code:

1. Check out the latest copy of the source code from the project's code repository.
2. Change the source files to incorporate your change or addition. Make sure you provide appropriate source code documentation (like javadoc for
Java sources), and follow the project's coding conventions.
3. Check the software still compiles and runs correctly on your local machine.
4. Run any unit or regression tests the software may have.

If all this works, you can create your patch. Remove all build products and remnants (like any 'build', 'dist' or 'bin' directories) from the module tree, then build the actual patch. Here's how to do it using the command line SVN client under unix:

Apache projects prefer the unified diff format. The subversion tool creates that automatically. If you use other tools, please refer to their documentation for details on setting the diff format.

```
    # location where the modules are stored
    cd checkout</p>
<div class="codehilite"><pre><span class="c"># directory of the module</span>
<span class="n">cd</span> <span class="n">site</span>

<span class="c"># creation of the diff</span>
<span class="n">svn</span> <span class="nb">diff</span> <span class="o">&gt;</span> <span class="n">site</span><span class="p">.</span><span class="nb">patch</span>
</pre></div>
```

The Subversion client now examines all subdirectories for changed files, then compares the changed file to the one on the server. It generates the
patch.

The '&gt;' redirection results in the resulting patch being put in a text file named (in this case) `site.patch`.

With your patch generated, you need to send it to the developers. Different projects have different preferences for this. Usually you add it as an attachment to the relevant bug report in the bug tracking database. If a relevant bug report doesn't exist yet, create one.

A very few projects don't use an issue tracker. In that case, send the patch as an attachment to an e-mail with a subject prefixed with "<code>[PATCH]</code>", to the appropriate development mailing list. If the patch is large, please ask before e-mailing it in case there is a better way to provide it.

Supply a different patch per issue. A patch can span multiple files but you should normally try not to fix multiple bugs in a single patch, unless those bugs are intimately related.

Be patient if your patch is not applied as fast as you'd like ( Open source developers are all volunteers, often doing the development in their spare time) or a developer asks you to make changes to the patch. If you do not receive any feedback in a reasonable amount of time (say, a week or two), feel free to send a follow-up e-mail to the developer list.

<h4 id="websites">How to suggest changes to project websites<a class="headerlink" href="#websites" title="Permanent link">&para;</a></h4>
<p>One of the simplest ways to contribute to Apache projects is by suggesting improvements to the project's website or product documentation. If something doesn't make 
sense to you, or if you have a better way to explain something, send the project a patch!

Projects use many different content management systems for their websites. Some systems have a web-based editor that makes it relatively simple to provide improvements, once you have access rights. Ask the PMC for such rights, explaining how you would like to help, or simply provide your suggestions in an email.
