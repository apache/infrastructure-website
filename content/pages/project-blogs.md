Title: Project Blog

**Change to blogs under way**: _As of June, 2023, the ASF is no longer using Apache Roller for project blogs. This page is being updated with more relevant information._


Apache projects and podlings can create a blog on their own. If you're building your site via Pelican, Hugo, or other static site generator it's as easy as following their steps to create posts. For instance, infra.apache.org is using Pelican builds hosted by the ASF. Posts just need to be markdown and created under a directory named "blog". All project blogs should be accessible via $projectName.apache.org/blog. A blog can be a great way of announcing new milestones and features, sharing tips and tricks, and putting a "face" on your project for your developer and user communities. The project's PMC is responsible for the blog's content, and for granting write access to PPMC members.

There are some resources avaiable if you're using <a href="https://cwiki.apache.org/confluence/display/INFRA/Git+-+.asf.yaml+features#Git.asf.yamlfeatures-BlogdeploymentserviceforGitrepositories" target="_blank"> .asf.yaml</a>

It is good practice to discuss the content of blog posts on the project's dev list before publishing.

### Requesting a project blog ###

You no longer have to request a blog from Infra. If your project doesn't currently have a blog, you should discuss this on the project mailing lists before moving forward.

### Getting editor access ###

Your blog code should be in your project's website repo or another separate GitHub/GitBox repo. Access is controlled via the same process as committing code to any other ASF repo. Contributors can use PRs to create new content that can be approved by the project. 

### Working with your blog ###

This is not a personal blog; it is part of the way your project presents itself to the world. The PMC should approve a plan that covers

- Who is responsible for the blog. It will not write itself!
- Frequency (such as "at least one blog entry a month, with more entries as events require")
- Topics ("Let's have a series of tips for new users, a post describing each new release, and...")
- Whether a PMC needs to review a draft of the new blog post before the writer publishes it.

### What's next for blogs.apache.org? ###

Moving forward Infra will setup an aggregator which will resemble a planet-like view. Similar to how Roller would gather latest posts from each blog into one page.
