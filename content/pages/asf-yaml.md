Title: Working with .asf.yaml

`.asf.yaml` is a branch-specific <a href="https://en.wikipedia.org/wiki/YAML" target="_blank">YAML</a> configuration file that a project may create (using a text editor of your choice) and put in the root of a Git repository to control features such as

  - notification schemes
  - website staging
  - GitHub settings
  - Pelican builds

It operates on a per-branch basis, meaning you can have different settings for different branches, and only those with an active `.asf.yaml` file will kick off a feature. Metadata settings (repo settings, features, labels) are not branch-dependent and should exist in the main (default) branch.

<h2 id="top">Before you start using .asf.yaml</h2>

  - `.asf.yaml` only works with Git repositories. There is no equivalent at the moment for Subversion repositories.
  - Do <b>not</b> use the document separator `--` in your `.asf.yaml` file. It will cause parsing to fail.
  - The configuration file is specific to the branch in which it resides and only code blocks with a `whoami` matching the branch name will run.
  - The configuration file holds a great deal of power, as it controls a host of automated systems.
  - Before using a feature in `.asf.yaml`, make sure that you have discussed what you propose with the entire project team, and understand what the configuration changes will do to the team's workflow and project resources.
  - You can add configuration blocks to an `.asf.yaml` file in any order; they do not depend on each other or flow from one to the next. 

## Contents
<ul>
  <li><a href="#notif">Notification settings for repositories</a>
    <ul>
      <li><a href="#review">Reviewing your old (pre-.asf.yaml) configuration</a></li>
      <li><a href="#split">Splitting email notifications based on context</a></li>
      <li><a href="#bypath">by-path commit emails</a></li>
      <li><a href="#botschemes">Special schemes for bots</a></li>
      <li><a href="#jiraoptions">Jira notification options</a></li>
    </ul></li>
  <li><a href="#deploy">Web site deployment service for Git repositories</a>
    <ul>
      <li><a href="#primer">Primer</a></li>
      <li><a href="#staging">Staging a web site preview domain</a></li>
      <li><a href="#autostage">Automatically staging new branches with a dynamic profile</a></li>
      <li><a href="#publish">Publishing a branch to your project web site</a></li>
      <li><a href="#nondefault">Specifying a non-default hostname</a></li>
      <li><a href="#subdir">Specifying a sub-directory to publish to</a></li>
      <li><a href="#pelican">Pelican sub-directories for static output</a></li>
    </ul></li>
  <li><a href="#blog">Blog deployment service for Git repositories</a></li>
  <li>GitHub settings
    <ul>
      <li><a href="#triage">Assigning the GitHub 'triage' role to external collaborators</a></li>
      <li><a href="#autolink">Autolinks for Jira</a></li>
      <li><a href="#branchpro">Branch protection</a></li>
      <li><a href="#customsubject">Custom subject lines for GitHub events</a></li>
      <li><a href="#default_branch">Default branch</a></li>
      <li><a href="#delete_branch">Delete branch on merge</a></li>
      <li><a href="#depend_alerts">Dependabot alerts and updates</a></li>
      <li><a href="#GHA_build_status">GitHub Actions build status emails</a></li>
      <li><a href="#discussions">GitHub Discussions</a></li>
      <li><a href="#pages">GitHub Pages</a></li>
      <li><a href="#merge">Merge buttons</a></li>
      <li><a href="#repo_features">Repository features</a></li>
      <li><a href="#repo_meta">Repository metadata</a></li>
      <li><a href="#tag_protect">Tag protection</a></li>      
    </ul>
  </li>
  <li><a href="#static">Generating static website content</a>
    <ul>
      <li><a href="#autobuild">Automatically building new branches</a></li>
      <li><a href="#buildpub">Building and publishing at the same time</a></li>
      <li><a href="#config_notif">Configuring notifications</a></li>
      <li><a href="#jekyll_cms">Jekyll CMS</a></li>
      <li><a href="#pelican_cms">Pelican CMS</a></li>
      <li><a href="pg_count">Pelican - Requiring minimum page count</a></li>
    </ul>
  </li>
  <li>Deprecated features
    <ul>
      <li><a href="#whitelisting">Jenkins PR whitelisting</a></li>  
    </ul>
  </li>
  <li><a href="#development">Further development</a></li>
</ul>

<hr/>

<h2 id="notif">Notification settings for repositories</h2>

Projects can set their notification targets for commits and GitHub issues/PRs/actions and discussions via .asf.yaml. Note that Jira issue email notification schemes are separate and require an Infra Jira ticket to change.

| Notifications | |
| ----------------- | -------------------- |
| commits | `commits@foo.apache.org` |
| issues | `issues@foo.apache.org` |
| pullrequests | `dev@foo.apache.org` |
| jira_options | `link label worklog` |
| jobs | `dev@foo.apache.org` |
| discussions | `issues@foo.apache.org` |


**NOTE**: Setting up notification schemes via `.asf.yaml` can only happen in the default (i.e. main/master/trunk etc.) branch of a repository, and each configuration change will cause your project's `private@` list to receive a notification of the change, for review purposes.

Settings made in .asf.yaml takes precedence over the original legacy mail targets (entered when you set up the repository). If a specific target scheme is not found in `.asf.yaml`, the legacy defaults will be used instead.

<h3 id="review">Reviewing your old (pre-.asf.yaml) configuration</h3>
If you wish to take a look at the default (old style) configuration for a repository, visit `gitbox.apache.org/schemes.cgi?$repository-name-here`, for instance `gitbox.apache.org/schemes.cgi?lucene-solr`.

<h3 id="split">Splitting email notifications based on context</h3>

You can divide pull requests and issues into sub-categories to split up the open/close emails and the comments/code review parts.

For instance, if a project wants new PRs to send an email to `dev@foo`, but wants any comments on that PR to go to `issues@foo`, employ the following configuration:

| notifications      | email           | notes          |
| -------------------- | -------------------- | -------------------- |
| commits | `commits@foo.apache.org` | |
| issues | `issues@foo.apache.org` | Send all issue emails (new, closed, comments) to `issues@` |
| pullrequests_status | `dev@foo.apache.org` | Send new/closed PR notifications to `dev@` |
| pullrequests_comment | `issues@foo.apache.org` | Send individual PR comments/reviews to `issues@` |
            

You can split `issues` into `issues_status` and `issues_comment` for sending issue emails to the appropriate targets.

The hierarchy for determining the email target for an action is:

  1. If a specific status or comment target is specified, use that.
  2. Otherwise, if a global issue/pull request target exists, use that.
  3. Otherwise, fall back to the targets that were configured when the repository was set up.
  4. Finally, fall back to dev@project for issues/PRs and commits@ for commits.

<h3 id="bypath">by-path commit emails</h3>

Projects may specify that commits to a repository that touches on specific paths will have a copy of the commit email sent to one or more specific addresses.

These paths are glob-enabled.

```
notifications:
  commits:  commits@foo.apache.org
  commits_by_path:
    "sub-folder/*": foo@bar.apache.org
    "docs/README.md":
      - foo@bar.apache.org
      - janedoe@apache.org
```

<h3 id="botschemes">Special schemes for bots</h3>
Projects may create special rules for bots such as dependabot on GitHub to have PR and issue activity from these directed to a distinct mailing list. The general syntax for this is to append `_bot_$botname` to the scheme, for instance:

| notifications       | email       | notes    |
| ---------------------------- | -------------------- | -------------------- |
| commits | `commits@foo.apache.org` | |
| pullrequests | `issues@foo.apache.org` | Send all PR emails (new, closed, comments) to `issues@` |
| pullrequests_bot_dependabot | `private@foo.apache.org` | Send depandabot PRs to `private@` instead |


These special schemes are currently only available for pull requests and issues.

<h3 id="jiraoptions">Jira notification options</h3>

You can enable Jira notifications that will fire when a GitHub issue or pull request has a ticket in its title, such as `[TICKET-1234] Improve foo bar`.

You can set one or more of these options:

  - `comment`: Add the PR/issue event as a comment in the referenced Jira ticket.
  - `worklog`: Add the event as a worklog entry instead of a comment in the Jira ticket you reference.
  - `label`: Add a 'pull-request-available' label to referenced tickets. **NOTE**: Some Jira projects have set limitations on who can add labels to tickets. If labels are not being added, you can address this by granting the Jira user `githubbot` access to your Jira space as a committer.
  - `link`: When you create a GitHub PR/issue, embed a link to the PR or issue in the Jira ticket you reference. 

You can concatenate the options you want to use as a string list, like this:

```
notifications:
  ...
  jira_options: link label comment
```
<p align="right"><a href="#top">Return to top</a></p>

<h2 id="deploy">Web site deployment service for Git repositories</h2>

The staging and publish features of the .asf.yaml file in a Git repository manage web site deployment.

**NOTE**: Web site staging and publishing features are applied for the repository in which you have specified staging and publishing. Thus, only specify them within the repository that contains your web site material, or you could end up seeing a list of source code files from your source repository on your site.

**NOTE**: Web site staging and publishing features are specific to the branch in which the .asf.yaml file resides and will not run without an accompanying `whoami`.

<h3 id="primer">Primer</h3>

A basic staging and publishing profile could be:

```
# Staging and publishing profile for yourproject-website.git:
staging:
  profile: ~
  whoami:  asf-staging
 
publish:
  whoami:  asf-site
```

This configuration enables a staging (live preview) web site at `yourproject.staged.apache.org` using the `asf-staging` branch of your repository, and deploys the `asf-site` branch of the repository to your main web site at `yourproject.apache.org`. Details below:

<h3 id="staging">Staging a web site preview domain</h3>

To enable staging a live preview of your project's web site, add a `staging` entry to the site repository's .asf.yaml file.
This example uses the imaginary `yourproject-website.git` with an `.asf.yaml` file containing the following entry:

```
staging:
  profile: beta
```

This would stage the current branch at `yourproject-beta.staged.apache.org`. 

You can add multiple staging profiles and thus stage multiple branches for preview. This can be helpful when doing A/B evaluations of website contents and features.

You can also omit the profile value, and stage directly at `yourproject.staged.apache.org`: 

```
staging:
  profile: ~
```
`~` (tilde) means "no value" in YAML.

**Preventing branch-override on cloning a branch**

Set a protection on multi-tenancy by specifying a `whoami` setting. If the setting's value does not match the name of the current branch, no checkout/update happens. You can have this in the `.asf.yaml` file on the `asf-staging` branch:

```
staging:
  profile: ~
  whoami:  asf-staging
```

When you clone that branch to a new branch like `asf-staging-copy`, the staging website server will notice that the value of `whoami` does not match `asf-staging-copy`, and will ignore that branch until you update the `whoami` to match it.

<h3 id="autostage">Automatically staging new branches with a dynamic profile</h3>

If you use features such as `autobuild`, you can automatically stage branches on `staged.apache.org` with the `autostage` keyword.

As with `autobuild`, it must match the branches you wish to autostage:

```
staging:
  profile: ~
  whoami:  asf-staging
  autostage: site/*
```

The autostaging feature derives a profile from the branch name, thus `site/*` would stage all branches matching `site/*`-staging as `<project>-*.staged.apache.org`. For instance:

  - Branch `site/foo` is autobuilt and the output goes to `site/foo-staging`.
  - `site/foo-staging` matches `site/*` in the `autostage` command.
  - The site is staged as `$project-foo.staged.apache.org`, for instance `tomcat-foo.staged.apache.org`.

<h3 id="publish">Publishing a branch to your project web site</h3>

**Notes**

  - if you have previously used `gitwcsub` for website publishing, your first publish action using `.asf.yaml` will cause any existing `gitwcsub` or `svnwcsub` subscription to stop working. This ensures that there are no race conditions or "repository fights" going on when you publish.
  - lthough publishing the `asf-site` branch used to work without `.asf.yaml` being present, since May 2021 that file **must** be present at the root of the branch you wish to publish for everything (including soft purging the CDN cache on updates) to work correctly.

To publish a branch to your project website sub-domain (`yourproject.apache.org`), set up a configuration block called `publish` in your `.asf.yaml` file. Enable branch-protection through the `whoami` parameter, like so:

```
publish:
  whoami: asf-site
```

If, for whatever reason, a project wishes to revert to `gitwcsub` for publishing, remove the publish feature in your `.asf.yaml` file.

<h3 id="nondefault">Specifying a non-default hostname</h3>

By default, web sites are published at `$project.apache.org`, where `$project` is the sub-domain name of your project as determined by the repository name.

Some projects, like `openoffice.org`, have special domains and may publish to these by specifying a `hostname` attribute in the publish configuration block, as shown below.

This is also useful when a PMC manages several websites, like `comdev-site` and `comdev-events-site`.

```
publish:
  whoami:   asf-site
  hostname: www.openoffice.org
```

**NOTE**: You cannot specify your `$project.apache.org` hostname with this setting. It has to be inferred to prevent abuse. Also, please do not abuse this feature in any other way. (Thanks!)

<h3 id="subdir">Specifying a sub-directory to publish to</h3>

To publish to a sub-directory of the web site URL, specify a `subdir` value. Such checkouts can be useful for sub-projects.
For instance, if httpd wished to check out a repository into `httpd.apache.org/subproject`, they could use the following configuration:

```
publish:
  whoami:    asf-site
  subdir:    subproject
```

**Known Issue**: In some cases (such as recent migration to this mechanism) the initial website check-in will clobber the sub-directory sites with a '404' error.

_Remediation_: Committing to the sub sites will trigger the mechanism to re-pull the content from sub-sites.

<h3 id="pelican">Pelican sub-directories for static output</h3>

The staging and deployment servers support the Pelican build `output/` sub-dir as the root directory for the web site. Thus, the website root can be either:

  - The root of the git branch
  - The `output/` directory at the root of the branch

<p align="right"><a href="#top">Return to top</a></p>

<h2 id="blog">Blog deployment service for Git repositories</h2>

You can deploy a project blog in the same manner as the project's website. It will be deployed as both `$project.blog.apache.org` AND `$project.apache.org/blog` (will redirect internally if a blog is deployed this way).

Deploy a blog by using the `type` parameter in your `publish` setting:

```
publish:
  whoami:    asf-blog
  type:      blog
```

**NB**: there is an internal rewrite, so `$project.apache.org/blog` will only rewrite to `/www/blogs/$project` internally if that directory exists e.g. a separate blog is deployed.

<p align="right"><a href="#top">Return to top</a></p>

<h2>GitHub settings</h2>

<h3 id="triage">Assigning the GitHub 'triage' role to external collaborators</h3>

Projects may assign external (non-committer) collaborators the `triage` role for their repository. This allows them to assign, edit, and close issues and pull requests, without giving them write-access to the code.

Add such people to the `collaborators` stanza in the `github` section, as a list of GitHub IDs:

```
github:
  collaborators:
    - Humbedooh
    - gstein
```

To remove people as collaborators, remove them from the list. You may only have ten active collaborators at any given time per repository. If you need more, ask `vp-infra@apache.org` for an exception.

**Note**: If you wish to completely empty a previously non-empty list of collaborators, explicitly specify an empty list:

```
github:
  collaborators: []
```

<h3 id="autolink">Autolinks for Jira</h3>

Projects may specify one or more Jira projects to set up autolinking for in their repository, wherein any Jira ticket that is referred to automatically creates a link to the external Jira instance at ASF.

The following snippet would set up autolinking for the INFRA and AMBARI projects in a repository:

```
github:
  autolink_jira:
    - INFRA
    - AMBARI
```

The `autolink_jira` property can be a single string or a list of strings, each corresponding to a Jira project on `issues.apache.org`. It **must** adhere to the Jira project name syntax (uppercase alphabetical characters only).
We will evaluate the need for other autolink features.

<h3 id="branchpro">Branch protection</h3>

Projects can enable branch protection in their repos, including most of the sub-level protection features such as 'require status checks to pass before merging' , 'approval by at least $n people' , and 'require pull request reviews'.

Here are some examples:

```
github:
  protected_branches:
    main:
      required_status_checks:
        # strict means "Require branches to be up to date before merging".
        strict: true
        # contexts are the names of checks that must pass.
        contexts:
          - gh-infra/jenkins
          - another/build-that-must-pass
      required_pull_request_reviews:
        dismiss_stale_reviews: true
        require_code_owner_reviews: true
        required_approving_review_count: 3

      # squash or rebase must be allowed in the repo for this setting to be set to true.
      required_linear_history: false
  
      required_signatures: true
 
      # requires all conversations to be resolved before merging is possible
      required_conversation_resolution: true
 
    branch_b:
      required_signatures: true
```

**Notes**
  1. Enabling any of the above checks overrides what you may have set previously, so you'll need to add all the existing checks to your `.asf.yaml` file to reproduce any that Infra set manually for you.
  2. If you need to remove a required check in order to push a change to `.asf.yaml`, create an Infra Jira ticket with a request to have the check manually removed.

All protected branches in the YAML must be dictionary entries. Thus, if you only want to disable force push from a branch, you can construct a **minimal dictionary**:

```
github:
  protected_branches:
    master: {}
```

Branches that are not in your `.asf.yaml` file or are not dictionary entries are not protected.

To completely remove all branch protection rules, set the protected_branches section to null:

```
github:
  protected_branches: ~
```

<h3 id="customsubject">Custom subject lines for GitHub events</h3>

You can customize the subject lines for GitHub events (issues and pull requests being opened, closed, and commented on) on a per-repository basis.

You can customise the subject line either for individual events, or for all events (by using the `catchall` directive), following the Python f-string format:

```
github:
  custom_subjects:
    new_pr: "[PR] {title} ({repository})"
    close_pr: "Re: [PR] {title} ({repository})"
    comment_pr: "Re: [PR] {title} ({repository})"
    merge_pr: "Re: [PR] {title} ({repository})"
    new_issue: "[I] {title} ({repository})"
    comment_issue: "Re: [I] {title} ({repository})"
    close_issue: "Re: [I] {title} ({repository})"
    catchall: "[GH] {title} ({repository})"
    new_discussion: "[D] {title} ({repository})"
    edit_discussion: "Re: [D] {title} ({repository})"
    close_discussion: "Re: [D] {title} ({repository})"
    close_discussion_with_comment: "Re: [D] {title} ({repository})"
    reopen_discussion: "Re: [D] {title} ({repository})"
    new_comment_discussion: "Re: [D] {title} ({repository})"
    edit_comment_discussion: "Re: [D] {title} ({repository})"
    delete_comment_discussion: "Re: [D] {title} ({repository})"
```

The format follows a dictionary/hash with an event type and a subject line template.

The following **event types** are currently supported:

| event type | notes |
| -------------------- | ---------------------------------------- |
| close_issue | Someone closes an issue |
| close_pr | Someone closes a pull request |
| comment_issue | Someone comments on an issue |
| comment_pr | Someone comments on a pull request |
| diffcomment | Someone comments on a segment of code in a pull request |
| merge_pr | Someone merges a pull request |
| new_issue | Someone createds an issue |
| new_pr | Someone createsd a pull request |
| catchall | If custom subjects are enabled for this repository, but no specific subject line template is defined for that event type, this will be used if present. If there is no `catchall`, and the event type does not have a template, the ASF default subject line will be used instead. |
| catchall_discussions | Custom catch-all for discussions, as these use slightly different variables. |


The **subject line templates** support the use of the following variables only. Custom variables or calls are **not** supported.

| variable | notes |
| --------------- | ----------------------------------- |
| repository | The repository the event is for (but see the note below) |
| user | The GitHub user who triggered this event by creating, commenting on, merging or closing the issue/pr. |
| category | This will be either "issue" or "pr". |
| issue_id | The ID of this issue (same as `pr_id`, as GitHub uses the same internal number pool for both issues and pull requests). |
| pr_id | The ID of this pull request (same as issue_id). |
| link | The URL to this specific issue/pr or to the specific comment on it. |
| title | The title of the pull request, issue or discussion. |
| {action} | The generic action that happened (created/deleted/edited). |
| {url} | The URL for the discussion or comment that was affected (Discussions). |
| {body} | The body of text, either the discussion itself or a comment. |
| {action_human} | If a comment happened, this is a human-readable representation of the action. |
| {recipient} | The mailing list this was sent to. |
| {unsub} | The unsubscribe address of the mailing list this was sent to. |


**Note**: If your project uses multiple GitHub repositories, we recommend using the `repository` variable to let people know which repo the email relates to. If your project has a single repo or does not use GitHub integration much (or at all), you can omit that variable.

<h3 id="default_branch">Default branch</h3>

To change the default GitHub repository branch (which is the landing branch when users browse to `github.com/apache/<repository>` and the default branch pull requests are initially based on, etc.) create an INFRA Jira ticket. If you are renaming the default branch and the new default branch does not yet exist, you can ask Infra to rename the branch at the same time. Include a **link** to the mailing list thread where the change of the default was agreed.

<h3 id="delete_branch">Delete branch on merge</h3>

Add this snippet below so branches get auto-deleted upon PR merges to your default branch:

```
github:
  del_branch_on_merge: true
```

You can revert this by setting the variable back to false. (Merely removing the entry will not do that).

<h3 id="dependabot">Dependabot alerts and updates</h3>

Projects can enable and disable Dependabot alerts and automatic security update pull requests: 

```
github:
  dependabot_alerts:  true
  dependabot_updates: false
```

<h3 id="depend_alerts">Dependabot alerts and updates</h3>

Projects can enable and disable Dependabot alerts and automatic security update pull requests: 

```
github:
  dependabot_alerts:  true
  dependabot_updates: false
```

<h3 id="GHA_build_status">GitHub Actions build status emails</h3>

You can add a jobs directive in the standard notifications section to have GitHub actions send you notifications when a build fails, or when it transitions from failure to success:

```
notifications:
  jobs:   jobs@foo.apache.org
```

This triggers emails when a workflow run fails or if it succeeds after a series of failures. We do not send notifications on normal, successful runs, so as to not spam too much.

<h3 id="discussions">GitHub Discussions</h3>

GitHub Discussions is currently a beta feature and does not have an API endpoint. Until this is addressed, and if your project wants to use this feature, open an Infra Jira ticket with a link to a consensus discussion thread.

<h3 id="pages">GitHub Pages</h3>

Projects that use GitHub for website publishing can enable/update GitHub Pages settings, by specifying which branch (and optional path) to publish:

```
github:
  ghp_branch:  master
  ghp_path:    /docs
```

The `ghp_branch` setting can **only** be your default branch (e.g. master, main, ...) or `gh-pages`. 

**Note**: This is subject to change as GitHub is relaxing the rules.

The `ghp_path` setting should **always** be specified. It can be either `/docs` or `/`. If not specified, it will default to `/docs`.

<h3 id="merge">Merge buttons</h3>

Projects can enable/disable the `merge PR` button in the GitHub UI and configure which actions to allow by adding the following configuration (or derivatives thereof):

```
github:
  enabled_merge_buttons:
    # enable squash button:
    squash:  true
    # enable merge button:
    merge:   true
    # disable rebase button:
    rebase:  false
```

At least one of `squash`, `merge`, or `rebase` must be true.

<h3 id="repo_features">Repository features</h3>

Projects can enable/disable GitHub repository features to support their documentation and development model.

```
github:
  features:
    # Enable wiki for documentation
    wiki: true
    # Enable issue management
    issues: true
    # Enable projects for project management boards
    projects: true
```

<h3 id="repo_meta">Repository metadata</h3>

**NOTE**: Repository defaults via `.asf.yaml` may only be set in the main/master/trunk or default branch of a repository,

Projects can update their GitHub metadata (repository description, homepage and labels) via `.asf.yaml` like this:

```
github:
  description: "JSONP module for Apache Foobar"
  homepage: https://foobar.apache.org/
  labels:
    - json
    - jsonp
    - foobar
    - apache
```

To remove labels from the repository, remove them from the list. You may only have 20 active labels at any given time per repository.

**NOTE**: Metadata changes will only apply if you specify them in the `.asf.yaml` file in the master (or otherwise default) branch of a repository.

<h3 id="tag_protect">Tag protection</h3>

As with branch protection rules, you can enable tag protection rules. These rules allow anyone with write-access to create a tag that matches the rule, but does not allow the tag to be deleted or overwritten.

Tag protection rules follow a simple GLOB format, and support an arbitrary number of tag patterns:

```
github:
  protected_tags:
    - "rel/*"
    - "v*.*.*"
```

<p align="right"><a href="#top">Return to top</a>

<h2 id="static">Generating static website content</h2>

See also <a href="https://infra.apache.org/project-site.html">Managing your project web site</a>, which lists more options and examples of website generation.

**NOTE**: Website staging and publishing features are specific to the branch in which the `.asf.yaml` resides and will not run without an accompanying `whoami`.

<h3 id="autobuild">Automatically building new branches</h3>

The Pelican builder supports a feature called `autobuild`. When enabled and assigned a pattern, it builds any branch that matches the pattern, and puts the output in a branch with the same root name but ending in `-staging`.

As an example, setting autobuild to `site/*` would automatically build the branch `site/foo`, and put the resulting web site in `site/foo-staging`. This can be mixed in with the standard parameters:

```
pelican:
  whoami: master
  target: asf-site
  autobuild: site/*
```

<h3 id="buildpub">Building and publishing at the same time</h3>

You can build and publish your website at the same time by employing both the `pelican` and `publish` configurations in your `.asf.yaml` file:

```
pelican:
  whoami: master
  target: asf-site
 
publish:
  whoami: asf-site
```

The configuration snippet above would, when present in both master and asf-site branches, build the web site from the master branch, then push the result to the asf-site branch and publish that branch as your project web site.

Likewise, you can employ auto-build-and-stage:

```
pelican:
  whoami: master
  target: asf-site
 
staging:
  whoami: asf-site
  profile: ~
```

This would build your site from the master branch, push the result to the asf-site branch and then stage that result on your staging domain.

<h3 id="config_notif">Configuring Notifications</h3>

The Pelican builder has an optional keyword, `notify` which defines a list to which a status report will be sent upon job completion. If no option is specified, a notification will be sent to `notifications@infra.apache.org` instead.

```
pelican:
  whoami: master
  target: asf-site
  notify: list@apache.org
```

<h3 id="jekyll_cms">Jekyll CMS</h3>

Projects can build their websites automatically using <a href="https://jekyllrb.com/" target="_blank">Jekyll</a>. This solution allows the use of custom plugins. Content generated this way can be staged or pushed directly to production when it is used in conjunction with the staging or publishing configuration options.

You can optionally specify a named output directory as `outputdir`. If a value is not specified for this property, it defaults to 'output'.

**Warning** Do not change `destination` in Jekyll's `_config.yaml` file. It must stay as is and output the generated files into a `_site` folder.

To set up an automatic build, add a jekyll section to `.asf.yaml`:

```
jekyll:
  whoami: jekyll-source-branch
  target: asf-staging-jekyll       # output branches need to be asf-site OR asf-staging*
#  outputdir: outputdir            # MAY be needed, but generally can be left out
```

<h3 id="pelican_cms">Pelican CMS</h3>

Projects can automatically build web sites using the <a href="https://blog.getpelican.com/" target="_blank">Pelican Static Site Generator</a> and have the result either staged or pushed directly to production (with the addition of a staging or publish configuration, as seen above).

To set up an automatic build, add a Pelican section to `.asf.yaml`:

```
pelican:
  whoami: master
  target: asf-site
```

The above configuration generates the site using Pelican and pushes only the created output to the `asf-site` branch. An example website repository that uses the Pelican auto-build feature is the <a href="https://github.com/apache/infrastructure-website" target="_blank">Infrastructure website</a>.

Our Pelican builds support GFM (GitHub-Flavored Markdown), meaning you can edit websites using the GitHub UI and instantly get a preview of your page before pushing it to the build/publish process.

GFM is enabled by default, but will change to standard markdown if you have PLUGINS defined in your `pelicanconf.py` file. To explicitly enable GFM along with other manually defined plugins, you may specify gfm as a plugin, and it will be woven into the build.

Furthermore, you can build off one branch and publish to another using the `target` parameter, as seen above. If you leave this parameter out, the build process pushes the generated site to the same branch it built from (in the `output/ base` directory).

Pelican auto-builds support using different themes via the `theme` argument to specify the directory that contains your theme. This is equivalent to the `-t` switch in Pelican.

<h3 id="pg_count">Pelican - Requiring minimum page count</h3>

The Pelican builder has an optional keyword, `minimum_page_count`, which sets a lower limit to the number of pages that must be built for the builder to succeed and stage/publish the result.

This can be used to prevent misconfigured builds from publishing partial or blank web sites. The command expects a positive integer in order to check:

```
pelican:
  whoami: master
  target: asf-site
  minimum_page_count: 200  # If fewer than 200 html pages were built, cancel the build!
```

<p align="right"><a href="#top">Return to top</p>

<h2>Deprecated features</h2>

<h3 id="whitelisting">Jenkins PR whitelisting</h3>

**NOTE**: This no longer works. This feature was based on a Jenkins plugin that is no longer maintained and has been removed from use. The code still exists in `asfyaml.py` for the time being while we research a similar plugin for possible
use. Ignore this feature for now.

For projects using Jenkins for CI testing, PRs are generally only built when a committer submits one. Projects **may** choose to designate a GitHub 'safe/reliable' person using the jenkins/github_whitelist feature:

```
jenkins:
  github_whitelist:
    - janedoe
    - githubmonkey
    - papasmurf1234
    - dependabot[bot]
```

The GitHub IDs listed here would have access to start builds based on PRs, in addition to the committers on the project. For automated accounts, such as Dependabot, you need to add the `[bot]` suffix to its name.

<p align="right"><a href="#top">Return to top</a>

<h2 id="development">Further Development</h2>

These features have not been implemented in production yet, but are documented here for future use.

  - <a href="https://docs.github.com/en/github/administering-a-repository/managing-repository-settings/configuring-autolinks-to-reference-external-resources" target="_blank">Autolinks</a>

If you would like to add features you are free to open a pull request and propose your changes. The whole logic is defined in the `asfyaml.py` file.

<p align="right"><a href="#top">Return to top</a>





