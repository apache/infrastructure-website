Title: Project sites using MKDocs
license: https://www.apache.org/licenses/LICENSE-2.0

<a href="https://www.mkdocs.org/" target="_blank">MKDocs</a> is a static site generator designed for creating project documentation. However, at least one ASF project uses it to build their entire project website.

As of August 2021, you need to use a special MKDocs build command sequence so it can handle the project site's `.asf.yaml` file, which must be in the root of the site.

The command `mkdocs gh-deploy` removes the site, rebuilds it, and then deploys the updated contents to the given remote branch. This removes, but does not replace, the `.asf.yaml` file.

To prevent the new build from removing the `.asf.yaml` file, use this build command sequence: 

```
rm -r site
mkdir site
cp ../.asf.yaml site/
mkdocs gh-deploy --dirty
```
