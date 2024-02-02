Title: Working with .asf.yaml

## Introduction
.asf.yaml is a branch-specific <a href="https://en.wikipedia.org/wiki/YAML" target="_blank">YAML</a> configuration file that a project may create (using a text editor of your choice) and put in the root of a Git repository to control features such as

  - notification schemes
  - website staging
  - GitHub settings
  - Pelican builds

It operates on a per-branch basis, meaning you can have different settings for different branches, and only those with an active .asf.yaml file will kick off a feature. Metadata settings (repo settings, features, labels) are not branch-dependent and should exist in the main (default) branch.

## Before you start using .asf.yaml
  - .asf.yaml only works with Git repositories. There is no equivalent at the moment for Subversion repositories.
  - Do not use the document separator `--` in your .asf.yaml file. It will cause parsing to fail.
  - The configuration file is specific to the branch in which it resides and only code blocks with a `whoami` matching the branch name will run.
  - The configuration file holds a great deal of power, as it controls a host of automated systems.
  - Before using a feature in .asf.yaml, make sure that you have discussed what you propose with the entire project team, and have understood what the configuration changes will do to the team's workflow and project resources.
  - You can add configuration blocks to an .asf.yaml file in any order; they do not depend on each other or flow from one to the next.


Development
Implemented Features
Notification settings for repositories
Taking a look at your old (pre-.asf.yaml) configuration
Splitting email notifications based on context
by-path commit emails
Special schemes for bots
Jira notification options
Web site deployment service for Git repositories
Primer
Staging a web site preview domain
Automatically staging new branches with a dynamic profile
Publishing a branch to your project web site
Specifying a non-default hostname
Specifying a sub-directory to publish to
Pelican sub-directories for static output
Blog deployment service for Git repositories
GitHub settings
Repository metadata
Repository features
Merge buttons
Dependabot Alerts and Updates
GitHub Pages
GitHub Actions build status emails
Default branch
Branch protection
Delete branch on merge
Tag protection
Jenkins PR whitelisting
Assigning external collaborators with the triage role on GitHub
Autolinks for Jira
GitHub Discussions
Custom subject lines for GitHub events
Static web site content generation
Jekyll CMS
Pelican CMS
Automatically building new branches
Requiring minimum page count
Configuring Notifications
Building and publishing at the same time
Upcoming features
Introduction


Development
If you would like to add some features you are free to open a Pull Request and propose your changes, the whole logic is defined in the asfyaml.py file.

Implemented Features
Notification settings for repositories
Projects can set their notification targets for commits and GitHub issues/PRs/actions and discussions via .asf.yaml. Note that Jira issue email notification schemes are separate and require an Infra Jira ticket to change.

notifications:
  commits:      commits@foo.apache.org
  issues:       issues@foo.apache.org
  pullrequests: dev@foo.apache.org
  jira_options: link label worklog
  jobs:         dev@foo.apache.org
  discussions:  issues@foo.apache.org
NOTE: Setting up notification schemes via .asf.yaml can only happen in the default (i.e. main/master/trunk etc.) branch of a repository, and each configuration change will cause your project's private@ list to receive a notification of the change, for review purposes.

Settings made in .asf.yaml takes precedence over the original legacy mail targets (entered when setting up the repository). If a specific target scheme is not found in .asf.yaml, the legacy defaults will be used instead.

Taking a look at your old (pre-.asf.yaml) configuration
If you wish to take a look at the default (old style) configuration for a repository, visit https://gitbox.apache.org/schemes.cgi?$repository-name-here , for instance https://gitbox.apache.org/schemes.cgi?lucene-solr

Splitting email notifications based on context
You can divide pull requests and issues into sub-categories to split up the open/close emails and the comments/code review parts.
For instance, if a project wants new PRs to send an email to dev@foo, but wants any comments on that PR to go to issues@foo, employ the following configuration:

notifications:
  commits:              commits@foo.apache.org
  # Send all issue emails (new, closed, comments) to issues@
  issues:               issues@foo.apache.org
  # Send new/closed PR notifications to dev@
  pullrequests_status:  dev@foo.apache.org
  # Send individual PR comments/reviews to issues@
  pullrequests_comment: issues@foo.apache.org
Likewise, you can split issues into issues_status and issues_comment for sending issue emails to the appropriate targets.

The hierarchy for determining the email target for an action is:

If a specific status or comment target is specified, use that
otherwise, if a global issue/pull request target exists, use that
otherwise, fall back to the targets that were configured when the repository was set up
finally, fall back to dev@project for issues/PRs and commits@ for commits
by-path commit emails
Projects may specify that commits to a repository that touches on specific paths will have a copy of the commit email sent to one or more specific addresses.
These paths are glob-enabled.

notifications:
  commits:              commits@foo.apache.org
  commits_by_path:
    "sub-folder/*": foo@bar.apache.org
    "docs/README.md":
      - foo@bar.apache.org
      - janedoe@apache.org
Special schemes for bots
Projects may create special rules for bots on GitHub, such as dependabot, to have PR and issue activity from these directed to a distinct mailing list. The general syntax for this is done by appending "_bot_$botname" to the scheme, for instance:

notifications:
  commits:                     commits@foo.apache.org
  # Send all PR emails (new, closed, comments) to issues@
  pullrequests:                issues@foo.apache.org
  # Send depandabot PRs to private@ instead
  pullrequests_bot_dependabot: private@foo.apache.org
These special schemes are currently only available for pull requests and issues.

Jira notification options
You can use the file to enable Jira notifications that will fire when a GitHub issue or pull request has a ticket in its title, such as "[TICKET-1234] Improve foo bar".
You can set one or more of these options:

comment: Add the PR/issue event as a comment in the referenced Jira ticket.
worklog: Add the event as a worklog entry instead of a comment in the Jira ticket you reference.
label: Add a 'pull-request-available' label to referenced tickets. NOTE: Some Jira projects have set limitations on who can add labels to tickets. If labels are not being added, you can address this by granting the Jira user githubbot access to your Jira space as a committer.
link: When you create a GitHub PR/issue, embed a link to the PR or issue in the Jira ticket you reference. 
Concatenate the options you want to use as a string list, like this:

notifications:
  ...
  jira_options: link label comment


Web site deployment service for Git repositories
The staging and publish features of the .asf.yaml file in a git repository manage web site deployment.

NOTE : Web site staging and publishing features are applied for the repository in which you have specified staging and publishing . Thus, only specify them within the repository that contains your web site material, or you could end up just seeing a list of source code files from your source repository.

NOTE : Web site staging and publishing features are specific to the branch in which the .asf.yaml resides and will not run without an accompanying whoami.

Primer
A basic staging and publishing profile could be:

# Staging and publishing profile for yourproject-website.git:
staging:
  profile: ~
  whoami:  asf-staging
 
publish:
  whoami:  asf-site
This configuration enables a staging (live preview) web site at yourproject.staged.apache.org using the asf-staging branch of your repository, and deploys the asf-site branch of the repository to your main web site at yourproject.apache.org. Details below:

Staging a web site preview domain
To enable staging (live preview) of your project's web site,  add a staging entry to the site repository's .asf.yaml file.
As an example, take the imaginary yourproject-website.git with an .asf.yaml file containing the following entry:

staging:
  profile: beta
This would stage the current branch at https://yourproject-beta.staged.apache.org/ . You can add multiple staging profiles and thus multiple branches staged for preview. This can be helpful when doing A/B evaluations of website contents and features.

You can also omit the profile value, and stage directly at https://yourproject.staged.apache.org/ ( "~" (tilde) means "no value" in YAML):

staging:
  profile: ~



Preventing branch-override on cloning a branch
Set a protection on multi-tenancy by specifying a whoami setting. If the setting's value does not match the current branch, no checkout/update happens. You can have this in the .asf.yaml file on the asf-staging branch:

staging:
  profile: ~
  whoami:  asf-staging
When you clone that branch to a new branch like asf-staging-copy, the staging web site server will notice that the value of whoami does not match asf-staging-copy, and will ignore that branch until you update the whoami to match it.

Automatically staging new branches with a dynamic profile
If you use features such as autobuild, you can also automatically stage branches on staged.apache.org with the autostage keyword.

As with autobuild, it must match the branches you wish to autostage:

staging:
  profile: ~
  whoami:  asf-staging
  autostage: site/*
The autostaging feature derives a profile from the branch name, thus site/* would stage all branches matching site/*-staging as <project>-*.staged.apache.org. For instance:

Branch site/foo is autobuilt and the output goes to site/foo-staging
site/foo-staging matches site/* in the autostage command
the site is staged as $project-foo.staged.apache.org, for instance tomcat-foo.staged.apache.org
Publishing a branch to your project web site
Note: if you have previously used gitwcsub for web site publishing, your first publish action using .asf.yaml will cause any existing gitwcsub or svnwcsub subscription to stop working. This ensures that there are no race conditions or "repository fights" going on when you publish.

Note: although publishing the asf-site branch used to work without .asf.yaml being present, since May 2021 that file MUST be present at the root of the branch you wish to publish. for everything (including soft purging the CDN cache on updates) to work correctly.

To publish a branch to your project web site sub-domain (yourproject.apache.org), set up a configuration block called publish in your .asf.yaml file. Enable branch-protection through the whoami parameter, like so:

publish:
  whoami: asf-site
If, for whatever reason, a project wishes to revert to gitwcsub for publishing, remove the publish feature in your .asf.yaml file.

Specifying a non-default hostname
By default, web sites are published at $project.apache.org, where $project is the sub-domain name of your project as determined by the repository name.

Some projects, like openoffice.org, have special domains and may publish to these by specifying a hostname attribute in the publish configuration block, as shown below.

This is also useful when a PMC manages several websites, like comdev-site and comdev-events-site.

publish:
  whoami:   asf-site
  hostname: www.openoffice.org
NOTE: You cannot specify your $project.apache.org hostname with this setting. It has to be inferred to prevent abuse. Also, please do not abuse this feature in any other way, thanks!



Specifying a sub-directory to publish to
To publish to a sub-directory of the web site URL, specify a subdir value. Such checkouts can be useful for sub-projects.
For instance, if httpd wished to check out a repository into httpd.apache.org/subproject, they could use the following configuration:

publish:
  whoami:    asf-site
  subdir:    subproject
Known Issue
Issue: In some cases (such as recent migration to this mechanism) the initial website check in will clobber the sub-directory sites with a '404' error.

Remediation: Committing to the sub sites will trigger the mechanism to re-pull the content from sub-sites.

Pelican sub-directories for static output
The staging and deployment servers support the pelican build output/ sub-dir as the root directory for the web site. Thus, the website root can be either:

The root of the git branch
The output/ directory at the root of the branch
Blog deployment service for Git repositories
Blogs can be deployed in the same manner as websites, and will be deployed as both $project.blog.apache.org AND $project.apache.org/blog (will redirect internally if a blog is deployed this way).

Deploying a blog is done by utilizing the type parameter in your publish setting:

publish:
  whoami:    asf-blog
  type:      blog
NB: there is an internal rewrite, so $project.apache.org/blog will only rewrite to /www/blogs/$project internally if that directory exists e.g. a separate blog is deployed



GitHub settings
Repository metadata
NOTE: Repository defaults via .asf.yaml may only be set in the main/master/trunk or default branch of a repository,

Projects can update their GitHub metadata (repository description, homepage and labels) via .asf.yaml like this:

github:
  description: "JSONP module for Apache Foobar"
  homepage: https://foobar.apache.org/
  labels:
    - json
    - jsonp
    - foobar
    - apache
To remove labels from the repository, remove them from the list. You may only have 20 active labels at any given time per repository.

NOTE : Metadata changes will only apply if you specify them in the .asf.yaml file in the master (or otherwise default) branch of a repository

Repository features
Projects can enable/disable GitHub repository features to support their documentation and development model.

github:
  features:
    # Enable wiki for documentation
    wiki: true
    # Enable issue management
    issues: true
    # Enable projects for project management boards
    projects: true
Merge buttons
Projects can enable/disable the "merge PR" button in the GitHub UI and configure which actions to allow by adding the following configuration (or derivatives thereof):

github:
  enabled_merge_buttons:
    # enable squash button:
    squash:  true
    # enable merge button:
    merge:   true
    # disable rebase button:
    rebase:  false
At least one of squash, merge, or rebase must be true.

Dependabot Alerts and Updates
Projects can enable and disable Dependabot alerts and automatic security update Pull Requests: 

github:
  dependabot_alerts:  true
  dependabot_updates: false
GitHub Pages
Projects can enable/update GitHub Pages settings, using GitHub for website publishing, by specifying which branch (and optional path) to publish:

github:
  ghp_branch:  master
  ghp_path:    /docs
The ghp_branch setting can ONLY be either your default branch (e.g. master, main, ...) or gh-pages. (Note: This is subject to change as GitHub is relaxing the rules).

The ghp_path setting should ALWAYS be specified. It can be either /docs or /. If not specified, it will default to /docs.

GitHub Actions build status emails
You can add a jobs directive in the standard notifications section to have GitHub actions send you notifications when a build fails, or when it transitions from failure to success:

notifications:
  jobs:   jobs@foo.apache.org
This triggers emails when a workflow run fails or if it succeeds after a series of failures. We do not send notifications on normal successful runs, so as to not spam too much.

Default branch
To change the default GitHub repository branch (which is used as the landing branch when users browse to https://github.com/apache/<repository>  address or the default branch pull requests are initially based on, etc.) you need to create an INFRA ticket. If you are renaming the default branch and the new default branch does not yet exist, you can ask Infra to rename the branch at the same time. [Remember to include a link to the mailing list thread where the change of the default was agreed.]

Branch protection
Projects can enable branch protection in their repos, including most of the sub-level protection features such as 'require status checks to pass before merging' , 'approval by at least $n people' , and 'require pull request reviews'.

Branch Protection examples
github:
  protected_branches:
    main:
      required_status_checks:
        # strict means "Require branches to be up to date before merging".
        strict: true
        # contexts are the names of checks that must pass
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
NB (1): Enabling any of the above checks overrides what you may have set previously, so you'll need to add all the existing checks to your .asf.yaml to reproduce any that Infra set manually for you.

NB (2): If you need to remove a required check in order to push a change to .asf.yaml, you will need to create an Infra Jira ticket with a request to have the check manually removed.



All protected branches in the YAML must be dictionary entries. Thus, if you only want to disable force push from a branch, you can construct a minimal dictionary like so:

Prevent force pushes
github:
  protected_branches:
    master: {}
Branches that are not in the YAML or are not dictionary entries are not protected.



To completely remove all branch protection rules, set the protected_branches section to null, as such:

Prevent force pushes
github:
  protected_branches: ~
Delete branch on merge
Add this snippet below so branches get auto-deleted upon PR merge to your default branch:

Delete Branch on Merge
github:
  del_branch_on_merge: true
You can revert this by setting it back to false. (Merely removing the entry would not do that).

Tag protection
As with branch protection rules, you can enable tag protection rules. These rules allows anyone with write-access to create a tag that matches the rule, but does not allow the tag to be deleted or overwritten.

Tag protection rules follow a simple GLOB format, and supports an arbitrary number of tag patterns:

Tag protection rules
github:
  protected_tags:
    - "rel/*"
    - "v*.*.*"
Jenkins PR whitelisting
NOTE: This no longer works. This feature was based on a Jenkins Plugin that is no longer maintained and has been removed from use. The code still exists in asfyaml.py for the time being whilst a similar plugin is investigated for possible
compatibility, or it will be removed in the near future. Ignore this feature for now then.
For projects using Jenkins for CI testing, PRs are generally only built when a committer submits one. Projects MAY choose to designate a GitHub 'safe/reliable' person using the jenkins/github_whitelist feature:

jenkins:
  github_whitelist:
    - janedoe
    - githubmonkey
    - papasmurf1234
    - dependabot[bot]
The GitHub IDs listed here would have access to start builds based on PRs, in addition to the committers on the project. For automated accounts, such as Dependabot, you will need to add the [bot] suffix to its name.

Assigning external collaborators with the triage role on GitHub
Projects may assign external (non-committer) collaborators the triage role for their repository.
The triage role allows people to assign, edit, and close issues and pull requests, without giving them write access to the code.
Add such people to the 'collaborators' stanza inside the github section, as a list of GitHub IDs:

Add collaborators with Triage role
github:
  collaborators:
    - Humbedooh
    - gstein
To remove people as collaborators, remove them from the list. You may only have 10 active collaborators at any given time per repository. For more you need to ask vp-infra@apache.org for an exception.

Note: If you wish to completely empty a previously non-empty list of collaborators, you should explicitly specify an empty list:

Removing all collaborators
github:
  collaborators: []
Autolinks for Jira
Projects may specify one or more Jira projects to set up autolinking for in their repository, wherein any Jira ticket that is referred to automatically creates a link to the external Jira instance at ASF.

The following snippet would set up autolinking for the INFRA and AMBARI projects in a repository:

Autolinks for Jira
github:
  autolink_jira:
    - INFRA
    - AMBARI
The autolink_jira property can be either a single string, or a list of strings, each corresponding to a Jira project on issues.apache.org. It MUST adhere to the Jira project name syntax (uppercase alphabetical characters only).
We will evaluate the need for other autolink features in the near future.

GitHub Discussions
GitHub Discussions is currently a beta feature and does not have an API endpoint. Until this is addressed, please open an Infra Jira ticket with a link to a consensus discussion thread for your project.

Custom subject lines for GitHub events
It is possible for a project to customize the subject lines for GitHub events (issues and pull requests being opened, closed, and commented on) on a per-repository basis.

Customizing the subject line can be done either for individual events, or for all events (by using the catchall directive), and follows the Python f-string format:

Custom GitHub Subjects
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
The format follows a dictionary/hash with an event type and a subject line template.

Supported event types
The following event types are currently supported:

close_issue: Someone closes an issue
close_pr: Someone closes a pull request
comment_issue: Someone comments on an issue
comment_pr: Someone comments on a pull request
diffcomment: Someone comments on a segment of code in a pull request
merge_pr: Someone merges a pull request
new_issue: Someone has created a new issue
new_pr: Someone has created a new pull request
catchall: If custom subjects are enabled for this repository, but no specific subject line template is defined for that event type, this will be used if present. If there is no catchall, and the event type does not have a template, the ASF default subject line will be used instead.
catchall_discussions: Custom catch-all for discussions, as these use slightly different variables.
Supported template variables
The subject line templates support the use of the following variables only. Custom variables or calls are not supported.

repository: The repository the event is for (but see the note below)
user: The GitHub user that triggered this event by creating, commenting on, merging or closing the issue/pr
category: The category of this issue/pr. Will be either "issue" or "pr", respectively
issue_id: The ID of this issue (same as pr_id, as GitHub uses the same internal number pool for both issues and pull requests)
pr_id: The ID of this pull request (same as issue_id)
link: The URL to this specific issue/pr or the specific comment on it
title: The title of the pull request, issue or discussion
{action}: The generic action that happened (created/deleted/edited)
{url}: The URL for the discussion or comment that was affected (Discussions)
{body}: The body of text, either the discussion itself or a comment
{action_human}: If a comment happened, this is a human readable representation of the action
{recipient}: The mailing list this was sent to
{unsub}: The unsubscribe address of the mailing list this was sent to
Note: 

If your project uses multiple GitHub repositories, we recommend using the repository variable to let people know which repo the email relates to. If your project has a single repo or does not use GitHub integration much (or at all), you can omit that variable..

Static web site content generation
See also https://infra.apache.org/project-site.html which lists more options and examples of website generation.

NOTE : Web site staging and publishing features are specific to the branch in which the .asf.yaml resides and will not run without an accompanying whoami.

Jekyll CMS
Projects can build their websites automatically using Jekyll. This solution allows the use of custom plugins. Content generated this way can be staged or pushed directly to production when it is used in conjunction with the staging or publish configuration options.

You can optionally specify a named output directory as outputdir. If a value is not specified for this property, it defaults to 'output'.

_config.yml

Please do not change destination in Jekyll's _config.yaml file. It must stay as is and output the generated files into a _site folder.


To set up an automatic build, add a jekyll section to .asf.yaml

jekyll:
  whoami: jekyll-source-branch
  target: asf-staging-jekyll       # output branches need to be asf-site OR asf-staging*
#  outputdir: outputdir            # MAY be needed, but generally can be left out


Pelican CMS
Projects can automatically build web sites using the Pelican Static Site Generator and have the result either staged or pushed directly to production (with the addition of a staging or publish configuration, as seen above).

To set up an automatic build, add a pelican section to .asf.yaml:



pelican:
  whoami: master
  target: asf-site


The above configuration generates the site using Pelican and pushes only the created output to the asf-site branch. An example web site repository that uses the pelican auto-build feature is: https://github.com/apache/infrastructure-website.

Our Pelican builds support GFM (GitHub-Flavored Markdown), meaning you can edit web sites using the GitHub UI and instantly get a preview of your page before pushing it to the build/publish process.

GFM is enabled by default, but will change to standard markdown if you have PLUGINS defined in your pelicanconf.py file. To explicitly enable GFM along with other manually defined plugins, you may specify gfm as a plugin, and it will be woven into the build.

Furthermore, you can build off one branch and publish to another using the target parameter, as seen above. If you leave this parameter out, the build process pushes the generated site to the same branch it built from (in the output/ base directory).

Pelican auto-builds support using different themes via the theme argument to specify the directory that contains your theme. This is equivalent to the -t switch in Pelican.

Automatically building new branches
The Pelican builder supports a feature called autobuild. When enabled and assigned a pattern, it builds any branch that matches the pattern, and puts the output in a branch with the same root name but ending in -staging.

As an example, setting autobuild to site/* would automatically build the branch site/foo, and put the resulting web site in site/foo-staging. This can be mixed in with the standard parameters:

pelican:
  whoami: master
  target: asf-site
  autobuild: site/*


Requiring minimum page count
The Pelican builder has an optional keyword, minimum_page_count, which sets a lower limit to the number of pages that must be built for the builder to succeed and stage/publish the result.

This can be used to prevent misconfigured builds from publishing partial or blank web sites. The command expects a positive integer in order to check:

pelican:
  whoami: master
  target: asf-site
  minimum_page_count: 200  # If fewer than 200 html pages were built, cancel the build!


Configuring Notifications
The Pelican builder has an optional keyword: notify which defines a list to which a status report will be sent upon job completion. If no option is specified, a notification will be sent to notifications@infra.apache.org instead.

pelican:
  whoami: master
  target: asf-site
  notify: list@apache.org
Building and publishing at the same time
You can build and publish your website at the same time by employing both the pelican and publish configurations in your .asf.yaml file:

pelican:
  whoami: master
  target: asf-site
 
publish:
  whoami: asf-site
The configuration snippet above would, when present in both master and asf-site branches, build the web site from the master branch, then push the result to the asf-site branch and publish that branch as your project web site.

Likewise, you can employ auto-build-and-stage:

pelican:
  whoami: master
  target: asf-site
 
staging:
  whoami: asf-site
  profile: ~
This would build your site from the master branch, push the result to the asf-site branch and then stage that result on your staging domain.



Upcoming features
These features have not been implemented in production yet, but are documented here for future use.

Autolinks - https://docs.github.com/en/github/administering-a-repository/managing-repository-settings/configuring-autolinks-to-reference-external-resources 
