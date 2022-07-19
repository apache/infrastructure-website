Title: Local builds of your Pelican-template website

Once your infrastructure-pelican site is deployed to GitHub, you can easily edit it locally in a clone of the GitHub repo, and test your changes locally (on OSX or Linux) before uploading them to GitHub. Once you upload the changes, the CI/CD system will automatically use them to update the project website (depending on your configuration, the update will go either to a staging area or to the live site).

**Note**: the tool mentioned below _may_ work on <a href="https://docs.microsoft.com/en-us/windows/wsl/about" target="_blank">WSL</a> or <a href="https://www.cygwin.com/" target="_blank">cygwin</a>, but will **not** work under native Windows.

## Preparation

Make sure you have installed:
  - cmake
  - python3 or greater
  - pip3

Download the [automatic build tool](https://raw.githubusercontent.com/apache/infrastructure-pelican/master/bin/local-pelican-site.sh), and run it, providing the name of your GitHub website repo. 

Example:

`./local-pelican-website.sh infrastructure-website`

Once the process has completed, you should be able to see the rendered site by opening a web browser to http://localhost:8000/.

## Use

After you have done local edits on the source files for the website, you can test them locally by running the script again as above.
