Title: Guidelines for project websites
license: https://www.apache.org/licenses/LICENSE-2.0

These guidelines relate to Infra policies on resource consumption, linking, legal use, and site ownership. For policies and guidelines that fall under other committees or directors, please see their respective sites/pages.

**NOTE:**  In December, 2021 all TLP web sites and the main `apache.org` site started redirecting any pages using `http` to `https` and set up HTTP Strict Transport Security, or <a href="https://www.globalsign.com/en/blog/what-is-hsts-and-how-do-i-use-it" target="_blank">HSTS</a>. This was at the request of projects and end users, to enhance site security.


- Projects cannot use tools that require write access to the project repository.
- Never link directly to downloads hosted at `apache.org`. Always use the mirror scripts like closer.lua.
- Never redirect from the front page of your project's site, `$TLP.apache.org` to another domain. `$TLP.apache.org` **must** be your main project site. Links from your project site to other locations are of course okay.
- Never redirect from a `$TLP.apache.org` site to a non-ASF site unless the ASF has explicitly approved this, as for projects that have an existing web presence before joining the ASF.
- Don't cause unnecessary resource use (CPU, RAM, disk space). Use common sense, but Infra will ultimately decide on a case-by-case basis whether there is unnecessary use.
- The ASF must own all official project web sites (including their domain names), and you must host them on ASF hardware under Infra control.
- If you use cookies or other means of tracking users of an ASF website, state what you are doing explicitly and get the visitor's permission to track and store their data.
- Web sites must be licensed under Apache License v.2.
- You must not host or distribute any material that may constitute a felony under US or German law.
- All web sites must be available on ASF's git or svn servers, and published using git- or pypubsub.
- Do not host source releases or convenience binaries directly on the web site. See [Release download pages for projects](release-download-pages.html).

**Note**: Any ASF project can use the ASF **Infrastructure Pelican Action** GitHub Action to compile and deploy its website. The repository for this GHA is <a href="https://github.com/apache/infrastructure-actions/tree/main/pelican" target="_blank">github.com/apache/infrastructure-actions/tree/main/pelican</a>. 

Should you have any questions, feel free to contact us at <a href="mailto:infrastructure@apache.org" target="_blank">infrastructure@apache.org</a> or on our <a href="https://the-asf.slack.com" target="_blank">Slack channel</a>.
