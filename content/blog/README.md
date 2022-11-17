## The Infra Blog

 -  [index.md](index.md) is the wheelhouse for the blog. There you define the general title and which template the blog is using.
 -  The <a href="https://github.com/apache/infrastructure-website/blob/master/content/theme/templates/blog.html">blog's template</a> defines the look and feel of the blog page, and also calls the blog articles for display.

### Blog entry metadata

_this sections will cover the metadata fields available, per https://docs.getpelican.com/en/latest/content.html#publishing-drafts and indicate the minimum metadata each entry should have._

### Creating a blog entry

To create an entry, create an .md file in this folder. The file's name should probably be like the permalink for the entry.
  - give the file a meaningful title that does not duplicate one we have used already.
  - The first line of the file should have this metadata, at a minimum: `layout: post title: THE ENTRY'S TITLE date: '2010-01-01' permalink: KEY WORDS FROM THE TITLE`. Note that the title does not need a period at its end.
  - Write your entry using Markdown.
  - If you do not want to publish the blog post as soon as you commit it to the repository, set the metadata `status: draft`. When you are ready to publish the post, change the status to `published` or remove the `status` metadata altogether. Then commit the file.
  - You can edit the entry at any time. Updating an older entry does not move it to the top of the blog's display.

### Making use of the search feature

The search feature is not currently enabled for the ASF blog. As soon as it available, information on preparing your blog post to be searchable will appear here.
