Title: Managing your project web site

license: https://www.apache.org/licenses/LICENSE-2.0

Every Apache project or podling has a website hosted at `apache.org`. Apache provides tools to support it. Each project decides how their website looks, its contents, how they maintain it, and what software they use to support it, as long as the result is static files that our public web servers can make available to browsers. We also have limited support for .htaccess files and CGI scripts.


## Contents

<ul>
<li><a href="#planning">Planning the project website</a></li>
<li><a href="#default">Creating the website</a></li>
<li><a href="#sitemanagement">Site management</a></li>
<li><a href="#preview">Previewing the website</a></li>
</ul>

<h2 id="planning">Planning the project website<a class="headerlink" href="#planning" title="Permanent link">&para;</a></h2>

Your project team wants to build an excellent application that solves a problem, simplifies a process, or breaks new ground. You also want people to find it, try it, and adopt it. Your project website is key to attracting and engaging both contributors to project development and people and organizations that will become part of your user community.

Your website **must**

  - satisfy the <a href="https://www.apache.org/foundation/marks/pmcs" target="_blank">Apache branding requirements</a>, in particular that <a href="https://www.apache.org/foundation/marks/pmcs#navigation" target="_blank">certain links</a> appear on the site's landing page, in whatever navigation structure the site uses. Whimsy's <a href="https://whimsy.apache.org/site/" target="_blank">Apache Project Website Checks</a> tool periodically reviews all top-level project (TLP) websites to provide a report on how well they comply with that policy, and to identify issues that a project may need to address.
  - comply with the Infrastructure team's [project site policy](project-site-policy.html).

The site also **should**

  - explain what your project's product does.
  - pitch how your product solves a problem or creates a new opportunity.
  - invite people to get involved in the development team.
  - offer a link to the Apache downloads platform so people can download the latest builds of the product that you want the public to use.
  - provide documentation that will help people not part of the project understand how to get started with the product and how to keep going.
  - describe how the project team works, and its connection to the Apache Software Foundation.
  - explain how people can get in touch with the project to provide feedback or ask questions.

Once you have outlined the content that will be on the website, and decided how and where to display it, you need to decide how to build the site.

<h2 id="default">Creating the website<a class="headerlink" href="#default" title="Permanent link">&para;</a></h2>

Projects are free to choose their own styles and layout for websites, and have a range of options for actually creating the pages. The goal is to create an informative and useful **static** HTML website that can engage visitors, explain your project to them, and provide download links and documentation so they can use your project's applications.

### JavaScript issues

Many TLP sites use JavaScript (JS) to provide functions ranging from menu navigation to animations and image galleries. While JS can enhance the site experience for most visitors, it can pose problems:

  1. **Visitors who have scripting languages disabled**. General-interest sites can have as much as 10% of their site visitors with JS disabled in their browsers; that percentage is probably lower for sites aimed at a more technical audience. Make sure your site provides access to the essential information it must deliver even if the visitor's browser has disabled scripting languages.
  2. **Visitors who use assistive devices to read and work with web pages**. A web search on "JavaScript and assistive readers" will provide helpful information on writing and deploying JS in ways that cause the fewest issues for people using assistive devices to access your project website. The <a href="http://www.cynthiasays.com/" target="_blank">Cynthia Says</a> site can help you check your website for compliance with accessibility guidelines, including JavaScript issues.

### 1. Website-building options

#### GitHub Action using Pelican

This replaces the ASF Pelican template, which Infra is retiring by the end of 2024. Details on using the Pelican GitHub Action will be available shortly.

#### Jekyll

<a href="https://jekyllrb.com/" target="_blank">Jekyll</a> is a straightforward tool for developing blogs or static websites using Markdown, and it is easy to deploy the resulting website as GitHub Pages. There are many tutorials online about doing this.

#### Hugo

At least <a href="https://github.com/search?q=topic%3Ahugo+org%3Aapache&type=Repositories" target="_blank">six ASF projects</a> use <a href="https://gohugo.io/" target="_blank">Hugo</a>, an open-source framework for building static web sites.
  
#### JBake

At least <a href="https://github.com/search?q=topic%3Ajbake+org%3Aapache&type=Repositories" target="_blank">two ASF projects</a> use <a href="https://jbake.org/" target="_blank">JBake</a>, a Java-based tool for building static web sites.

#### MKDocs

<a href="https://www.mkdocs.org/" target="_blank">MKDocs</a> is a static site generator designed for creating project documentation. However, at least one ASF project uses it to build their entire project website. See [this note](asfyaml-mkdocs.html) on the build sequence to use to preserve your project site's [.asf.yaml](asf-yaml.html) file.

#### Basic website template in Markdown ####

If you'd like to get started with an easy-to-use, <a href="https://github.github.com/gfm/" target="_blank">Markdown</a>-based site that many projects have used, see the <a href="https://github.com/apache/apache-website-template" target="_blank">sample Apache project website</a> repository, which has many useful features and instructions for using `svnpubsub`.

#### HTML files ####

You can use any other tool that generates static HTML pages, or hand-code those pages. You then check them into your project's website repository. The check-in will trigger a site update.

#### Custom website directives using .htaccess files ####
Project websites can make use of .htaccess files for setting up custom redirects and other tweaks to the handling of requests. The default [AllowOverride](https://httpd.apache.org/docs/2.4/mod/core.html#allowoverride) setting is `All`, 
which generally enables any sort of redirects or rewrites (using `RewriteRule`, `Redirect`, etc.). Some project websites have custom settings in their dedicated virtual host configuration, which may require asking the Infrastructure Team for assistance. If you are in doubt, ask.

### Tools not supported

#### ASF Pelican template

**Note** Infra is discontinuing the Pelican template by the end of 2024, in favour of a GitHub Action using Pelican.
Infra is migrating the websites of projects using the Pelican option to GitHub Actions.

<a href="https://docs.getpelican.com/en/stable/" target="_blank">Pelican</a> is a static site generator written in Python. Highlights include:

  - Write your content directly with your editor of choice in reStructuredText or Markdown formats.
  - Includes a simple CLI tool to (re)generate your site.
  - Easy to interface with distributed version control systems and web hooks.
  - Completely static output is easy to host anywhere.
  
Pelican has paths to <a href="https://docs.getpelican.com/en/stable/importer.html#import" target="_blank">migrate existing websites from many technologies</a>, including Blogger, Dotclear, Posterous, Tumblr, WordPress, and RSS/Atom.

Any ASF project can use the [**ASF-Pelican template**](asf-pelican.html) as the basis for their project website. 
  
See a how-to on using [Pelican and Buildbot](pelican-buildbot.html) to develop and deploy a project website.

Pelican supports both flat websites and those that have subdirectories. For the latter, Pelican provides a <a href="https://github.com/akhayyat/pelican-page-hierarchy" target="_blank">plugin</a>.

Browse a <a href="https://github.com/getpelican/pelican-plugins/" target="_blank">collection of Pelican plugins</a> to find others that support functionality you want to add to your site. 

This <a href="https://github.com/search?q=topic%3Apelican+org%3Aapache&type=Repositories" target="_blank">GitHub query</a> returns ASF repositories
which have the `pelican` Topic. You can review them as examples of Pelican in action.
#### GitHub Pages
Infra does not have a structure in place to support using [GitHub Pages](github-pages.html) for project websites.

#### Apache CMS
The Apache CMS, which projects used to build and deploy their websites since 2010, is no longer available as of July 31, 2021. All projects that used it, including the main Apache website, have moved or must move to other technologies. Those that linger will find at some point that they can no longer update their website. See the notes in the section on site management tools, below.

### 2. Website repository

If you don't have a web site repository for your project yet, you can create one using <a href="https://selfserve.apache.org/" target="_blank">Self-serve</a>.

The convention is to name the repository `$project-site.git`, for instance `httpd-site.git`.

Copy whatever you need to start a build into the master branch of the new repository. This will act as the base of the build process.

### 3. The build process

Configure Pelican or Jekyll to build the site automatically when its contents change, using [.asf.yaml](asf-yaml.html) and Buildbot. 

### 4. A staging website

Using [.asf.yaml](asf-yaml.html) with a Git repository, once you have your generated web site committed and pushed to a branch, you can set up a staging web site to test your changes before publishing them to your main web site.

To do so, add or edit `.asf.yaml` in the staging branch (where the build output is generated) and add the following (assuming your staging branch is asf-staging):

```
staging:
  profile: ~
  whoami:  asf-staging
```

Upon commits to this branch, your staging web site will appear with the latest output at: `https://$project.staged.apache.org/`
For more details, see [.asf.yaml](asf-yaml.html).

### 5. Publishing

When you are ready to publish a branch of your Git web site repository to your project web site, you can use `.asf.yaml`:

```
publish:
  whoami:  asf-site
```

For more detailed procedures, see see [.asf.yaml](asf-yaml.html).



<h2 id="sitemanagement">Site management</h2>
  
  The basic requirements for site management are that 

  - only committers should be able to modify the site.
  - notifications of all site changes are sent to the relevant project mailing lists.


<h3 id="tools">Management tools<a class="headerlink" href="#tools" title="Permanent link">&para;</a></h3>

Infra supports these tools for publishing and maintaining Apache project websites:

  -  **[Site template](asf-pelican.html)** streamlines migration of an existing project site on the deprecated CMS, and creation of new project sites.
  -  **[Pelican and BuildBot](pelican-buildbot.html)** streamline creating and publishing your project website.
  - **svnpubsub** automatically publishes the static contents of a designated svn folder (<a href="https://svn.apache.org/repos/asf/ant/site/ant/production/" target="_blank">example</a>) as the project web site at `http://project.apache.org`. The project team can use any site build mechanism it wants as long as the above requirements are met.
  - [**pypubsub**](pypubsub.html) automatically serves the static contents of a designated Git repository as the website for a project. Git-based websites are typically maintained in a repository branch to be published as `https://project.apache.org`. A project can host the site from its primary project repository. Typically these will be built as a Jenkins or a Buildbot job (see below). We recommend that you only have a single writer to the asf-site branch to avoid potential conflicts.
  - For **websites using a Git repository**, you can add an [.asf.yaml](asf-yaml.html) configuration file. The file lets you set instructions that simplify updating and maintaining the site.

  
### Build tools

Infra provides these build tools:

  - **Jenkins** is an open-source automation server that supports building, deploying and automating a project. Infra resources on Jenkins start <a href="https://cwiki.apache.org/confluence/display/INFRA/Jenkins" target="_blank">here</a>. 
  - **Buildbot** is a job scheduling system: it queues jobs, executes the jobs when the required resources are available, and reports the results. 
  
<h3 id="logging">Logging<a class="headerlink" href="#logging" title="Permanent link">&para;</a></h3>

The build output from your job when you compile your site is available from either Buildbot or Jenkins, depending on which you use.

<h3 id="svnpubsub-revision">Finding the site revision number<a class="headerlink" href="#svnpubsub-revision" title="Permanent link">&para;</a></h3>

This only applies to _SVN based websites_.

Look at the `.revision` file at the root of your site (for example, <a href="http://subversion.apache.org/.revision" target="_blank">http://subversion.apache.org/.revision</a>). That file updates after every successful svn update. (If the update is underway or exited abnormally, `.revision` won't have changed.)

### Topics in GitHub

If you're managing an ASF website repository in GitHub, please add `website` and `<TOOL>` Topics  to it, where `<TOOL>` is the name of the tool you are using to generate the website, like `pelican` or `hugo`. This helps others who are looking for an example of use of that tool find your repository, with queries like
 <a href="https://github.com/search?q=org%3Aapache+topic%3Ahugo" target="_blank">this one</a>.

You can use the [.asf.yaml](asf-yaml.html) mechanism to add those Topics.

<h3 id="mail">Providing public access to the project's mail archive mbox files<a class="headerlink" href="#mail" title="Permanent link">&para;</a></h3>

Some projects have a "mail" directory at the top of their project website. Enable this by creating a symbolic link  to `/home/apmail/public-arch/$tlp.apache.org` in `svnpubsub`.

See more <a href="https://apache.org/dev/#mail" target="_blank">notes about project mail</a>.

<h3 id="feather">Using the project's favicon<a class="headerlink" href="#feather" title="Permanent link">&para;</a></h3>

To use a custom favicon for your project's website, add the `favicon.ico` file to your site's root directory. The ASF feather appears for project sites that don't have a `favicon.ico` file.

<h3 id="generated">Minimizing the number of changes committed in the project's Maven- or JavaDoc- generated site<a class="headerlink" href="#generated" title="Permanent link">&para;</a></h3>

If you are using `svnpubsub`, the commit performs very slowly if the number of changes is large, particularly if the number of files is also large. This is often the case with JavaDoc, and to a lesser extent with Maven-generated sites. 

To speed up the commit:

  - When running JavaDoc, pass the `-notimestamp` option. This will avoid most files from being modified between runs if there haven't been code changes.
  - Use a Maven skin that doesn't add a timestamp to the output. This may require customizing the current skins.
  - If you use the Maven dependencies report in the Project Info Reports plugin, use version 2.7+ of the plugin to avoid random strings being generated.
  - If you maintain historical versions of documentation, always check changes in to a single "trunk", then use an `svn copy` operation to tag or branch the content, rather than checking in a complete copy.
  - Minimize use of "publish date" and "version" in templates to those that are truly necessary or helpful. Consider using a "last modified date" and version in the URL instead (unless "latest" is implied).
  - Minimize Subversion keywords in the output that may change frequently without significant meaning. This includes keywords in source code that may be rendered to JavaDoc or a Maven JXR source cross-reference.
  - Avoid publishing Maven reports that change constantly to the project site. Code coverage, style reports, static analysis, etc. can be generated into working copies on the CI server instead for easy developer viewing.

<h2 id="preview">Previewing the website<a class="headerlink" href="#preview" title="Permanent link">&para;</a></h2>

  - For svnpubsub sites, review the local files in your svn checkout before committing them. The changes will be published immediately after you commit them.
  - There is no preview mode for `pypubsub`. You should ideally have a way to build and test the website locally.
