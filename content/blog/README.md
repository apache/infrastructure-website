## The Infra Blog

 -  [index.md](index.md) is the wheelhouse for the blog. There you define the general title and which template the blog is using.
 -  The <a href="https://github.com/apache/infrastructure-website/blob/master/content/theme/templates/blog.html">blog's template</a> defines the look and feel of the blog page, and also calls the blog articles for display.

### Blog entry metadata

Metadata includes the title of the entry and the date it was published. Pelican supports a large number of metadata fields, some of which support searching and filtering when you are looking for specific information.

Required metadata: For each blog entry, make sure you provide the following metadata at the top of the file:

  - layout: post
  - title: the article's title
  - date: the date the post first appeared (yyyy-mm-dd)
  - permalink: a short phrase identifying the post
  - category: content category. Only provide ONE for each blog post. Current options are `event`, `general`, `infra`, `policy`, `projects`, `security`, `service`, `tools`. _note: filtering is not enabled yet._

These metadata fields are available, but are currently optional for the Infra blog:

  - author: content author, when there is just one
  - authors: separate the names of multiple content authors with commas
  - keywords: content keywords, separated by commas (HTML content only)
  - modified: the most recent date of changes to the post (yyyy-mm-dd)
  - slug: identifier used in URLs and translations
  - status: options are `draft`, `hidden`, or `published`
  - summary: brief description for use on index pages
  - tags: content tags, separated by commas
  - url: URL to use for this article

Pelican supports these tags, which the Infra blog does not use:

  - lang: content language ID
  - save_as: save content to this relative file path
  - template: template to use to generate content
  - translation (true or false)

The first line of the file should have this metadata, at a minimum: 
```
  layout: post title: THE ENTRY'S TITLE date: 2010-01-01 permalink: KEY WORDS FROM THE TITLE category CATEGORY
```

Note that the title does not need a period at its end.

For better readability as you are editing, you can lay out the metadata using multiple lines:

```
layout: post
title: THE ENTRY'S TITLE
date: 2010-01-01
permalink: KEY WORDS FROM THE TITLE
category CATEGORY
```

### Creating a blog entry

To create an entry, create an .md file in this folder. The file's name should probably be like the permalink for the entry.
  - give the file a meaningful title that does not duplicate one we have used already.
  - Starting at the first line of the file, add metadata for the entry, as described above.

  - Write your entry using Markdown.
  - If you do not want to publish the blog post as soon as you commit it to the repository, set the metadata `status: draft`. When you are ready to publish the post, change the status to `published` or remove the `status` metadata altogether. Then commit the file.
  - You can edit the entry at any time. Updating an older entry does not move it to the top of the blog's display.

### Making use of the search feature

The search feature is not currently enabled for the ASF blog. As soon as it available, information on preparing your blog post to be searchable will appear here.
