Title: Build and manage a project website with Pelican and Buildbot

license: https://www.apache.org/licenses/LICENSE-2.0

ASF projects can use <a href="https://docs.getpelican.com/en/stable/" target="_blank">Pelican</a> to create and manage the project website. Pelican provides a framework and the option of using themes to display your site pages, which you write in <a href="https://github.github.com/gfm/" target="_blank">GitHub-flavored-markdown</a> (GFM). You can set <a href="https://buildbot.net/" target="_blank">Buildbot</a> to build and publish the site every time someone saves updates to a page.


Pelican provides support for importing an existing site that runs on WordPress or some other service.

### Sites with sub-directories

Pelican supports both "flat" sites and sites that have sub-directories. For the latter, add the <a href="https://github.com/akhayyat/pelican-page-hierarchy" target="_blank">pelican-page-hierarchy</a> plugin. The plugin creates a website hierarchy that matches the file hierarchy of the material in the repository.

### Key files and directories ###

The repository structure for your Pelican project website has three key directories and a configuration file.

The directories are:

  - **content/pages**: holds the static pages for your website. You write and edit them using GFM.
      - Each page is a `.md` file.
      - The first line is `Title:` and the name of the page.
      - the second line is `Date:` and the date of the current version of the page.
   - **content/articles**: if your website has a blog or a series of featured articles, they go in this directory and will appear on the front page of the site. They have the same three requirements as the static pages, above.
   - **theme/plugins**: holds the plugins Pelican and Buildbot use to build and deploy the site.

The configuration file is `pelicanconf.py`.

### Setting up a Pelican website on Git ###

Create the repository for the website content using the <a href="https://gitbox.apache.org/setup/newrepo.html" target="_blank">GitBox's Boxer self service tool</a> (https://gitbox.apache.org/setup/newrepo.html).

1. Clone the repository to a local workspace
2. Run `pelican-quickstart` in the root of the repository on the master branch. 
    - The script asks where you want to create the website. Accept " . ", the default, unless you have a specific location in mind for it.
    - Use $PROJECTNAME for the site title.
    - Set the website author as $PROJECTNAME also. This lets all members of the project edit the website.
    - Accept the default language as English. You can, if you want, provide alternative versions of the website, or of certain pages, in other languages.
    - Specify a default prefix: `https://$PROJECTNAME.apache.org` (or similar friendly name)
    - Set article pagination to `No`.
    - Set time zone to `UTC`.
    - Set generation of tasks.py / makefile to 'No'.
    
3. Site configuration:

In your site repository, run the following commands:

```
for x in "content/pages content/articles theme/plugins"; do mkdir -p $x; done
rm -rf output publishconf.py
echo -e "\nPLUGIN_PATHS=['./theme/plugins']\nPLUGINS=[]\n"  >> pelicanconf.py
echo -e "pelican\nbeautifulsoup4" >> requirements.txt

```

4. Commit and push your changes.
5. Set up continuous integration (CI): use the <a href="https://cwiki.apache.org/confluence/display/INFRA/git+-+.asf.yaml+features" target="_blank">asf.yaml</a> mechanism to have Pelican build and, optionally, publish your website.

### Setting up a Pelican website on Subversion ###

Setting up Pelican to work with a Subversion repository requires a bit more hands-on work. If you would like to do this, open a Jira ticket for INFRA to make a request for help.

### Updating your website ###

Create and update markdown files (.md) in the content/pages and content/articles directories. If you have set up continuous integration (step 5, above), when you add pages or commit edits the site automatically updates.

### Using a Pelican theme ###

Pelican provides a range of <a href="http://www.pelicanthemes.com/" target="_blank">themes</a> that can help you develop a pleasing site without too much effort. Be sure to specify the directory containing the 'static' and 'templates' directories as `theme:` in the .asf.yaml file.

### Pelican plugins ###

There is a directory of <a href="https://github.com/getpelican/pelican-plugins/" target="_blank">Pelican plugins</a> that deliver extra functionality for a website.


