Title: Project Blog
license: https://www.apache.org/licenses/LICENSE-2.0

Until June, 2023, the ASF supported using Apache Roller for project blogs. That support has ended. Now we encourage projects to develop their blog using the technology of their choice.

If you're building your site via Pelican, Hugo, or another static site generator, it's as easy as following their steps to create posts. For instance, infra.apache.org is using Pelican builds hosted by the ASF. Posts just need to be written using markdown and created under a directory named "blog". 

All project blogs should be accessible via $projectName.apache.org/blog. A blog can be a great way of announcing new milestones and features, sharing tips and tricks, and putting a "face" on your project for your developer and user communities. The project's PMC is responsible for the blog's content, and for granting write access to PPMC members.

There are some resources available if you're using <a href="https://cwiki.apache.org/confluence/display/INFRA/Git+-+.asf.yaml+features#Git.asf.yamlfeatures-BlogdeploymentserviceforGitrepositories" target="_blank">.asf.yaml</a> for blog deployment.

It is good practice to discuss the content of blog posts on the project's dev list before publishing.

### Requesting a project blog ###

You no longer have to request a blog from Infra. If your project doesn't currently have a blog, you should discuss this on the project mailing lists and come to a decision about the blogging software to use before moving forward.

### Getting editor access ###

Your blog code should be in your project's website repo or another separate GitHub/GitBox repo. Access is controlled via the same process as committing code to any other ASF repo. Contributors can use PRs to create new content that can be reviewed by the project and then approved to be published. 

### Working with your blog ###

This is not a personal blog; it is part of the way your project presents itself to the world. The PMC should approve a plan that covers

- Who is responsible for the blog. It will not write itself!
- Frequency of posts (such as "at least one blog entry a month, with more entries as events require")
- Topics ("Let's have a series of tips for new users, a post describing each new release, and...")
- Whether a PMC needs to review a draft of the new blog post before the writer publishes it.

### What's next for blogs.apache.org? ###

Moving forward, Infra will set up an aggregator which will work the way Roller did, gathering the latest posts from each project blog into one page. We have no timeline for making this available yet.
