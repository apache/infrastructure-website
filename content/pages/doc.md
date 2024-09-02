Title: Documentation
license: https://www.apache.org/licenses/LICENSE-2.0

Infra provides a library of resources that is constantly evolving to reflect the current state of Apache's infrastructure and policies.

### Overview ###

- Please read this <a href="https://www.apache.org/foundation/how-it-works.html#roles" target="_blank">introduction</a> to the different roles within an Apache project community.
- Through the documentation, unless it is specifically defined, the term `developer` mean: <a href="https://www.apache.org/foundation/how-it-works.html#developers" target="_blank">developer/contributor</a> or <a href="https://www.apache.org/foundation/how-it-works.html#committers" target="_blank">committer</a>.
- <a href="https://www.apache.org/dev/" target="_blank">Here</a> you can find an extensive infrastructure overview for <a href="https://www.apache.org/foundation/how-it-works.html#developers" target="_blank">developers</a>.

### General guides ###

- [Understanding Opensource](understanding-opensource.html)
- [Writing a good bug report](bug-writing-guide.html)
- [Creating a Jira ticket](jira-guidelines.html)
- [Creating a patch for project code](patch.html)

### PMC resources ###

#### Source code ####
- [Project source code repositories](version-control.html)
- [Repositories for Maven releases and snapshots](repository-faq.html)
- <a href="https://cwiki.apache.org/confluence/display/INFRA/Git+-+.asf.yaml+features" target="_blank">.asf.yaml features for Git repositories</a>
- [GitHub Actions and Secrets](github-actions-secrets.html)
  - [GitHub Actions policy](github-actions-policy.html)

#### Build and release ####
- [Release creation process](release-publishing.html)
- Creating optional [Maven releases](publishing-maven-artifacts.html) 
- [Signing releases](release-signing.html)
- [Cryptography with OpenPGP](openpgp.html)
- [Release distribution policy](release-distribution.html)
- [Release download pages](release-download-pages.html)
- [Assembling LICENSE and NOTICE files](licensing-howto.html)
- General information about [content distribution](mirrors.html)
- [Handling cryptography within an ASF release](crypto.html)
- [Deploying a self-hosted runner](self-hosted-runners.html)

#### Website, blog and wiki ####
- [Project website guidelines](website-guidelines.html). **Note**: No new projects can use the Apache CMS, which has reached end-of-life. Any projects still using the CMS must migrate to another resource to maintain their websites. Projects that have not migrated their site may find that they are no longer able to update it.
- Here is how one project <a href="https://cwiki.apache.org/confluence/display/INFRA/How+Apache+Jena+migrated+from+the+CMS" target="_blank">did the migration</a>.
- A [project site template](asf-pelican.html) written in Pelican is available to smooth migration away from the CMS, and to support creation of new project sites.
- [Managing your project website](project-site.html)
- [Project blog](project-blog.html)
- <a href="https://cwiki.apache.org/confluence/display/INFRA/Managing+permissions+on+your+project%27s+Confluence+Space" target="_blank">Managing permissions on your project's Confluence space</a>.

#### Other ####
- [Managing project committers](managing-committers.html)
- [Virtual machine for your project](vm-policy.html)
- [Mailing list moderation](mailing-list-moderation.html)


### Committer resources ###

- [New committer's guide](new-committers-guide.html)
- [Managing your Apache email address](committer-email.html)
- <a href="https://people.apache.org" target="_blank">Apache People</a> provides a simple phone book-like 
lookup for Apache Committers.
- <a href="https://whimsy.apache.org/" target="_blank">The Whimsy Project</a> provides a number of committer-specific tools for finding information about Apache people.
- [Transitioning to a new PGP key](key-transition.html)
- [Getting started with Git](git-primer.html)
- Information on setting up and using <a href="https://cwiki.apache.org/confluence/display/INFRA/OPIE" target="_blank">OPIE (One Password In Everything)</a>.
- The ASF has a fee-waiver arrangement so that committers participating in ASF projects can make free use of the [Apple Developer Program](apple-dev-program.html) to prepare and distribute project applications for Apple operating systems.
- [Apache mailing list etiquette](contrib-email-tips.html)
- [How to submit a patch for project code](patch.html)

### Contributor resources ###

[New contributor's guide](contributors.html)

### Infra Wiki

The <a href="https://cwiki.apache.org/confluence/display/INFRA/" target="_blank">Infra Wiki</a> provides scripts, how-to articles, and code samples. Most pages support the functions of the Infra team, but a great deal of material has guidance for project committers and PMCs.

You can also browse the complete <a href="https://cwiki.apache.org/" target="_blank" >ASF Wiki</a>.
