Title: GitHub Flavored Markdown

license: https://www.apache.org/licenses/LICENSE-2.0

Content for this site, and for all sites using the [ASF-Pelican template](asf-pelican.html), is structured using [GitHub Flavored Markdown][3] (GFM).

File extensions are **md**, **markdown**, **mkd**, and **mdown**. If you have an **mdtext** file, it is from the Apache CMS, which is deprecated as of summer, 2021. Change the file extension to **md**.

Sites built with the ASF-Pelican template use a version of [cmark-gfm][1] by [GitHub][2] through the `pelican-gfm` plugin that Infra created.

- [Mastering Markdown][3].

- [Detailed Specification][4] with many examples.

- If your project previously built its site using the Apache CMS, here are some differences from `markdown.pl` that the CMS used:

  - [HTML Blocks][5]
    - Make sure the first line of any html block starts in column one.
    - A blank line terminates an html block
      - [Exception][6] to this rule for `style`, `pre`, and `script`.
    - Review [Markdown content within an HTML block][7]

  - [Autolinks][8]
    - [www][9]
    - [url][10]
    - [email][11]

  - [Disallowed html][12] the tagfilter extension disables certain html tags. The asfgenid plugin reenables `script`, `style`, and `iframe` html tags.
    
- [Examples][13]

- ID and Class annotations

```md
## What is the Apache Software Foundation?  {#what}

The Apache Software Foundation (ASF) is a non-profit 501(c)(3) corporation,
incorporated in Delaware, USA, in June of 1999. The ASF is a natural
outgrowth of The Apache Group, which formed in 1995 to develop the Apache HTTP Server.
```

Set the class to display an image to `float-right`:

```md
![Logo](images/logo.svg) {.float-right}
```

You can also float an HTML fragment at the right of the page display:

```html
<div class=".pull-right" style="float:right; border-style:dotted; width:200px; padding:5px; margin:5px">

SEE INSTEAD: [Trademark Resources Site Map][resources].

</div>
```

- Migrating a site from the Apache CMS

If you are moving a project site of the Apache CMS and will be using the ASF-Pelican template:

  - Change any **mdtext** file extension to **md**.
  - Replace the multiple line `notice:` at the top of the file with a one-line reference to the Apache License.
  - Any {#id} and {.class} annotations have any # tags between the annotation and the heading text removed.
  - Only one {#id} or {.class} annotation is allowed on a tag.
  - {.class} annotations are seldom used.


[1]: https://github.com/github/cmark-gfm
[2]: https://github.blog/2017-03-14-a-formal-spec-for-github-markdown/
[3]: https://guides.github.com/features/mastering-markdown/
[4]: https://github.github.com/gfm/
[5]: https://github.github.com/gfm/#html-block
[6]: https://github.github.com/gfm/#example-139
[7]: https://github.github.com/gfm/#example-122
[8]: https://github.github.com/gfm/#autolink
[9]: https://github.github.com/gfm/#extended-www-autolink
[10]: https://github.github.com/gfm/#extended-url-autolink
[11]: https://github.github.com/gfm/#extended-email-autolink
[12]: https://github.github.com/gfm/#disallowed-raw-html-extension-
[13]: https://sindresorhus.com/github-markdown-css/

