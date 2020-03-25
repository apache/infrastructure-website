Title: Guidelines for project websites

These guidelines relate to Infra policies on resource consumption, linking, legal use, and site ownership. For policies and guidelines that fall under other committees or directors, please see their respective sites/pages.

- Projects cannot use tools that require write access to the project repository.
- Never link directly to downloads hosted at `apache.org`. Always use the mirror scripts.
- Never redirect from the front page of your project's site, `$TLP.apache.org` to another domain. `$TLP.apache.org` **must** be your main project site. Links from your project site to other locations are of course okay.
- Never redirect from a `$TLP.apache.org` site to a non-ASF site unless this is explicitly recognized as an external web site.
- Don't cause unnecessary resource use (CPU, RAM, disk space). Use common sense, but Infra will ultimately decide on a case-by-case basis whether there is unnecessary use.
- All official project web sites (including their domain names) must be owned by the ASF and hosted on ASF hardware under Infra control.
- If you use cookies or other means of tracking users of an ASF website, state what you are doing explicitly and get the visitor's permission to track and store their data.
- Web sites must be licensed under Apache License v.2.
- You must not host or distribute any material that may constitute a felony under US or German law.
- All web sites must be available on ASF's git or svn servers, and published using git- or pypubsub (this includes the ASF CMS system).
- Do not host source releases or convenience binaries directly on the web site. Use the mirror system through `dist.apache.org` (but do NOT link to `dist.apache.org`; use `closer.lua`).

Should you have any questions, feel free to contact us at <a href="mailto:infrastructure@apache.org" target="_blank">infrastructure@apache.org</a> or on our <a href="https://the-asf.slack.com" target="_blank">Slack channel</a>.
