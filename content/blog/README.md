## The Infra Blog

 -  [index.md](index.md) is the wheelhouse for the blog. There you define the general title and which template the blog is using.
 -  The <a href="https://github.com/apache/infrastructure-website/blob/master/content/theme/templates/blog.html">blog's template</a> defines the look and feel of the blog page, and also calls the blog articles for display.

### Creating a blog entry

To create an entry, create an .md file in this folder. It probably should be like the permalink for the entry.
  - give the file a meaningful title that does not duplicate one we have used already.
  - The first line of the file should look like `layout: post title: THE ENTRY'S TITLE date: '2010-01-01' permalink: KEY WORDS FROM THE TITLE`. Note that the title does not need a period at its end.
  - Write your entry using Markdown.
  - When you save and commit the file, the system automatically posts it, displaying it at the top of the list of blog entries.
  - **Note**: we cannot currently create entries to be posted later. As soon as you commit an entry, it is live.
  - You can edit the entry at any time. Updating an older entry does not move it to the top of the blog's display.
