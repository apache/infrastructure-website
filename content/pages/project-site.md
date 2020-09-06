Title: Managing your project web site

Every Apache project or podling has a website hosted at `apache.org`. Apache provides tools to maintain it. Each project decides how their website looks, its contents, how they maintain it, and what software they use to support it, as long as the result is static files that our public web servers can make available to browsers. We also have limited support for .htaccess files and CGI scripts.


## Contents ##

<ul>
<li><a href="#default">Creating the website</a></li>
<li><a href="#sitemanagement">Site management</a></li>
<li><a href="#preview">Previewing the website</a></li>
</ul>

<h2 id="default">Creating the website<a class="headerlink" href="#default" title="Permanent link">&para;</a></h2>

Projects are free to choose their own styles and layout for websites, and have a range of options for actually creating the pages. The goal is to create and informative and useful **static** HTML website that can engage visitors, explain your project to them, and provide download links and documentation so they can use your project's applications.

### Website-building options ###

If you're managing an ASF website repository in GitHub, please add `website` and `<TOOL>` Topics  to it, where `<TOOL>` is the name of the tool
used to generate the website, like `pelican`, `hugo` etc. This helps others use your repository as an example using queries like
 <a href="https://github.com/search?q=org%3Aapache+topic%3Ahugo" target="_blank">this one</a>.
You can use the `.asf.yaml` mechanism to add those Topics.

#### Website template in Markdown ####

If you'd like to get started with an easy-to-use, <a href="https://github.github.com/gfm/" target="_blank">Markdown</a>-based site that many projects have used, see the <a href="https://github.com/apache/apache-website-template" target="_blank">sample Apache project website</a> repository which has many useful features and instructions for using svnpubsub.

#### Pelican ####

<a href="https://docs.getpelican.com/en/stable/" target="_blank">Pelican</a> is a static site generator written in Python. Highlights include:

  - Write your content directly with your editor of choice in reStructuredText or Markdown formats
  - Includes a simple CLI tool to (re)generate your site
  - Easy to interface with distributed version control systems and web hooks
  - Completely static output is easy to host anywhere
  
Pelican has paths to <a href="https://docs.getpelican.com/en/stable/importer.html#import" target="_blank">migrate existing websites from many technologies</a>, including Blogger, Dotclear, Posterous, Tumblr, WordPress, and RSS/Atom.
  
See a how-to on using [Pelican and Buildbot](pelican-buildbot.html) to develop and deploy a project website.

<a href="https://github.com/search?q=topic%3Apelican+org%3Aapache&type=Repositories" target="_blank">This GitHub query</a> returns ASF repositories
which have the `pelican` Topic, that should provide a few examples.

#### Github Pages ####

*In theory*, projects with a Git code repository can use [GitHub Pages](github-pages.html) to create a staging site for reviewing their website, and to publish the site when it is ready. One project has done this as a proof-of-concept; however Infra does not have a structure in place to fully support using GitHub Pages for project websites.

#### Jekyll ####

<a href="https://jekyllrb.com/" target="_blank">Jekyll</a> is a straightforward tool for developing blogs or static websites using Markdown, and it is easy to deploy the resulting website as Github Pages. There are many tutorials for doing this avaiilable online.

#### Hugo ####

At least <a href="https://github.com/search?q=topic%3Ahugo+org%3Aapache&type=Repositories" target="_blank">six ASF projects</a> use <a href="https://gohugo.io/" target="_blank">Hugo</a>, an open-source framework for building static web sites.
  
#### JBake ####

At least <a href="https://github.com/search?q=topic%3Ajbake+org%3Aapache&type=Repositories" target="_blank">two ASF projects</a> use <a href="https://jbake.org/" target="_blank">JBake</a>, a Java-based tool for building static web sites.

<h2 id="sitemanagement">Site management</a></h2>
  
  The basic requirements for site management are that 

  - only committers should be able to modify the site.
  - notifications of all site changes are sent to the relevant project mailing lists. The Apache CMS allows non-committers to send patches via a simple web interface by "Mail Diff"ing to the project mailing list that can be easily published by a committer.

<h3 id="tools">Management tools<a class="headerlink" href="#tools" title="Permanent link">&para;</a></h3>

Infra supports these tools for publishing and maintaining Apache project websites:

  - **[Pelican and BuildBot](pelican-buildbot.html)** streamline creating and publishing your project website.
  - **svnpubsub** automatically publishes the static contents of a designated svn folder (<a href="https://svn.apache.org/repos/asf/ant/site/ant/production/" target="_blank">example</a>) as the project web site at `http://project.apache.org`. The project team can use any site build mechanism it wants as long as the above requirements are met.
  - [**pypubsub**](pypubsub.html) automatically serves the static contents of a designated git repository as the website for a project. Git-based websites are typically maintained in a repository branch to be published as `https://project.apache.org`. A project can host the site from its primary project repository. Typically these will be built as a Jenkins or a Buildbot job (see below). We recommend that you only have a single writer to the asf-site branch to avoid potential conflicts.
  - For **websites using a git repository**, you can add a <a href="https://cwiki.apache.org/confluence/display/INFRA/.asf.yaml+features+for+git+repositories" target="_blank">.asf.yaml</a> configuration file. The file lets you set instructions that simplify updating and maintaining the site.
  - **Apache CMS** _(being deprecated; don't use for new sites)_ provides a simple browser-based user interface for editing, staging and publishing site content in Markdown, HTML or any other source format for which support has been added. See the <a href="cmsref">CMS reference</a> and <a href="cmsadoption">adoption</a> for more details. The Apache CMS uses pypubsub as the underlying mechanism for publishing a site. **Note**: No new projects can use the Apache CMS, and we enccourage projects using it to migrate to another resource for maintaining their websites. Here are <a href="https://cwiki.apache.org/confluence/display/INFRA/Migrate+your+project+website+from+the+Apache+CMS" target="_blank">migration instructions</a>.
  
#### Build tools ####

Infra provides these build tools:

  - **Jenkins** is an open source automation server that supports building, deploying and automating a project. Infra resources on Jenkins start <a href="https://cwiki.apache.org/confluence/display/INFRA/Jenkins" target="_blank">here</a>. 
  - **Buildbot** is a job scheduling system: it queues jobs, executes the jobs when the required resources are available, and reports the results. 
  
<h3 id="logging">Logging<a class="headerlink" href="#logging" title="Permanent link">&para;</a></h3>

The build output from your job when you compile your site is available from either Buildbot or Jenkins, depending on which you use.

<h3 id="svnpubsub-revision">Finding the site revision number<a class="headerlink" href="#svnpubsub-revision" title="Permanent link">&para;</a></h3>

This only applies to _SVN based websites_.

Look at the `.revision` file at the root of your site (for example, <a href="http://subversion.apache.org/.revision" target="_blank">http://subversion.apache.org/.revision</a>). That file updates after every successful svn update. (If the update is underway or exited abnormally, `.revision` won't have changed.)

<h3 id="mail">Providing public access to the project's mail archive mbox files<a class="headerlink" href="#mail" title="Permanent link">&para;</a></h3>

Some projects have a "mail" directory at the top of their project website. Enable this by creating a symbolic link  to `/home/apmail/public-arch/$tlp.apache.org` in svnpubsub or CMS output.

See more <a href="https://apache.org/dev/#mail" target="_blank">notes aboout project mail</a>.

<h3 id="feather">Using the project's favicon<a class="headerlink" href="#feather" title="Permanent link">&para;</a></h2>

To use a custom favicon for your project's website, add the `favicon.ico` file to your site's root directory. The ASF feather appears for project sites that don't have a `favicon.ico` file.

<h3 id="generated">Minimizing the number of changes committed in the project's Maven- or JavaDoc- generated site<a class="headerlink" href="#generated" title="Permanent link">&para;</a></h3>

If you are using svnpubsub, the commit performs very slowly if the number of changes is large, particularly if the number of files is large. This is often the case with JavaDoc, and to a lesser extent with Maven-generated sites. 

Here is what you can do to speed up the commit:

  - Ask Infra to store your generated content in the CMS repository, rather than the main ASF repository. While this won't necessarily speed up your own commit, it will prevent it from impacting other users.
  - When running JavaDoc, pass the `-notimestamp` option. This will avoid most files from being modified between runs if there haven't been code changes.
  - Use a Maven skin that doesn't generate a timestamp into the output. This may require customizing the current skins.
  - If you use the Maven dependencies report in the Project Info Reports plugin, use version 2.7+ of the plugin to avoid random strings being generated.
  - If you maintain historical versions of documentation, always check-in to a single "trunk", then use an `svn copy` operation to tag or branch the content, rather than checking in a complete copy.
  - Minimize use of "publish date" and "version" in templates to those that are truly necessary or helpful. Consider using a "last modified date" and version in the URL instead (unless "latest" is implied).
  - Minimize Subversion keywords in the output that may change frequently without significant meaning. This includes keywords in source code that may be rendered to JavaDoc or a Maven JXR source cross-reference.
  - Avoid publishing Maven reports that change constantly to the project site. Code coverage, style reports, static analysis, etc. can be generated into a working copy on the CI server instead for easy developer viewing.

<h2 id="preview">Previewing the website<a class="headerlink" href="#preview" title="Permanent link">&para;</a></h2>

  - For svnpubsub sites, review the local files in your svn checkout before committing them. The changes will be published immediately after you commit them.
  - For CMS sites, just commit the changes (without "publish"-ing them). Then click the `Staged` link that will take you to the staged site.
  - There is no preview mode for pypubsub. You should ideally have a way to build and test the website locally.
