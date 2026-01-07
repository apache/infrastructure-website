Title: CSP builder
slug: tools/csp

In order to update your project website's Content-Security-Policy (CSP) header, 
you will need to create a `.htaccess` file at the root of the website output.

The .htaccess file needs only a single directive with a comment:

~~~apache
# CSP permissions for foo.apache.org - approved by VP Data Privacy.
SetEnv CSP_PROJECT_DOMAINS "host1 host2 host3"
~~~

Where `host1`, `host2`, and so on, are the additional domains or URLs your 
project needs to unblock for the website to work. Each additional host you 
add **MUST** have been pre-approved by VP Data Privacy (privacy@apache.org),
and **SHOULD** have an accompanying comment in the .htaccess file explaining 
why the CSP is changed and where permission was obtained.

The hosts can be URLs with or without globs, as in this example with Algolia:

~~~apache
# CSP permissions for foo.apache.org - Adding 3rd party service Algolia. Approved by VP Data Privacy.
SetEnv CSP_PROJECT_DOMAINS "https://*.algolia.net/ https://*.algolianet.com/ https://*.algolia.io/"
~~~

Any hosts listed in the `CSP_PROJECT_DOMAINS` variable will be added to the default- and base source 
elements in the existing CSP header, and should suffice for the vast majority of projects.

The following domains are already allowed by default and do not need to be added:
* `https://www.apachecon.com/`
* `https://www.communityovercode.org/`
* `https://*.apache.org/`
* `https://apache.org/`
* `https://*.scarf.sh/`

If you need more specifically tailored headers, please reach out to users@infra.apache.org 
and we can assist you.

**DO NOT EDIT CSP HEADERS WITHOUT ASKING FIRST**.
