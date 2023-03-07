

layout: post
title: Project Blogs Migration
date: '2023-03-01'
permalink: Project_Blogs_Migration

#### Project Blogs and You!

Hey, everyone! Happy March! Today we're announcing to all projects that Infra is migrating `blogs.apache.org` away from Roller.

#### Where are my existing posts going?

You have a few options to migrate your existing posts. Infra can export your posts in either Jekyll Markdown, which can be used directly by GitHub Pages (and Pelican/Hugo), or CSV if you'd like to move your blog to a different platform. Infra will be supporting Pelican builds for the migration in the same way TLP sites work for some projects. [Here is a cwiki page with more info about asf.yaml and site builds](https://cwiki.apache.org/confluence/display/INFRA/Git+-+.asf.yaml+features#Git.asf.yamlfeatures-WebsitedeploymentserviceforGitrepositories).

#### What steps do I need to take to make sure our project blog stays intact?

First things first: put in an Infra Jira ticket to track the migration. Then we can communicate back and forth there to answer questions specific to your site. 

After May 31st, all blogs will be migrated to an archive, so the content will be preserved. However, permalinks aren't guaranteed to work for the archived posts. An existing permalink will redirect to the top level of the archive. If you migrate your blog to a new site, then we can set up redirects to better serve existing permalinks.

Based on your current www site configuration we can take various paths to migrate your posts. For instance, `infra.apache.org` is already set to use our BuildBot Pelican builder, so it was just a matter of creating a 'blog' directory and filling it with posts in Markdown. The build did the rest and Pelican/Jeykll/Hugo are all blog aware. If your site isn't using our builder and uses something like GitHub Actions to build GitHub Pages (which is Jekyll) the process is about the same. Being that each project runs their own site, there will likely be lots of variation in how each migration will be preformed. 

#### What is happening to blogs.apache.org?

`blogs.a.o` will live on as an aggrigator for all the project blogs. The domain will stay in place to process any permalink redirects to your new blog. 
