Title: Guide for new project committers
license: https://www.apache.org/licenses/LICENSE-2.0

Here's how to set up the technical and social environment that will support your work as a committer to an Apache project. Some projects have more specific guidelines which the project website or the PMC provide for you. We also have a thorough [Committers' FAQs](committers.html) for both new and experienced committers.

  - <a href="#what-is-a-committer">What is a committer?</a>
  - <a href="#becoming-a-committer">Becoming a committer</a>
      - <a href="#the-committers-way">The Committer's Way</a>
      - <a href="#submitting-your-individual-contributor-license-agreement-icla">Submitting your Individual Contributor License Agreement (ICLA)</a>
      - <a href="#acceptance-of-your-icla">Acceptance of your ICLA</a>
      - <a href="#apache-committer-account-creation">Apache Committer account creation</a>
      - <a href="#set-up-your-apacheorg-email-address">Set up your @apache.org email address</a>
      - <a href="#set-up-subversion-or-git-access">Set up Subversion or Git access</a>
      - <a href="#config-access">Configure your access to project Git repositories</a>
      - <a href="#set-up-security-and-pgp-keys">Set up Security and PGP Keys</a>
  - <a href="#committer-resources">Committer resources</a>
      - <a href="#check-out-the-committers-only-subversion-module">the Committers-only Subversion module</a>
  - <a href="#get-to-know-the-apache-community">The Apache Community</a>
      - <a href="#mailing-lists">Join mailing lists</a>
  - <a href="#committer-responsibilities">Committer responsibilities</a>
  - <a href="#attending-apachecon">Attending Community Over Code</a>
  - <a href="#identity-theft">Identity theft</a>
  - <a href="#share-your-wisdom">Share your wisdom</a>
  - <a href="#last">The last word</a>

<h3 id="what-is-a-committer">What is a committer?<a class="headerlink" href="#what-is-a-committer" title="Permanent link">&para;</a></h3>

The plain sense of the word "committer" is that you have access rights to your project's repository so you can read and write the source code. Rather than creating a patch and submitting it to be actively reviewed and then committed, you can now create a local patch and commit it yourself - or even review and commit patches created by others. Your fellow committers will review your patches, usually after you commit them.

<h3 id="becoming-a-committer">Becoming a committer<a class="headerlink" href="#becoming-a-committer" title="Permanent link">&para;</a></h3>

If you are not yet a committer, but would like to become one, review:

  - <a href="https://www.apache.org/foundation/getinvolved.html#become-a-committer" target="_blank">Become a committer</a>
  - <a href="https://www.apache.org/foundation/how-it-works.html#committers" target="_blank">ASF committers</a>
  - <a href="https://www.apache.org/foundation/how-it-works.html#meritocracy" target="_blank">Meritocracy</a>

<h3 id="the-committers-way">The Committer's Way<a class="headerlink" href="#the-committers-way" title="Permanent link">&para;</a></h3>

As a committer, you have access to a specific Apache project's repository so you can create and edit source code files, not just read them. Instead of having to create and submit a patch which other committers would have to review and approve, you can now create a local patch and commit it yourself; you can also review and commit patches that other project contributors and committers create. Your patches can still be reviewed by your fellow committers.

Some projects use **RTC** (Review then Commit) rather than **CTR** (Commit then Review). Check which pattern your project uses, and then follow it.

Take more care than you may have done before when working on the code, since you  can now change things directly, without review. Make sure you understand how your project's committers work and coordinate with each other. Ask your project PMC, or any active committer on the project, for guidance if there are things you are not sure about. In general, the more visible and engaged you are in the project, the more fun you will have and the more access you will have to advice and feedback.

<h3 id="submitting-your-individual-contributor-license-agreement-icla">Submitting your Individual Contributor License Agreement (ICLA)</h3>

If you are a brand-new committer, you must complete and submit an <a href="https://www.apache.org/licenses/#contributor-license-agreements" target="_blank">Individual Contributor License Agreement</a> (ICLA) before the ASF can activate your committer account. Note that an account can only be created if a PMC (or Incubator podling) has invited you. The ICLA is a formal contract that declares the terms under which you will contribute intellectual property to the ASF. Note that the ICLA does <strong>not</strong> assign copyright to the ASF; you retain copyright to your own work. However it does grant the ASF sufficient rights to release any work you submit under the Apache license.</p>

  - Choose an Apache ID before submitting your ICLA. Also select an alternative, in case the ID you want is unsuitable or already taken. Your ID must consist of at least three lower-case alphanumeric characters, starting with a letter. (<a href="https://people.apache.org/committer-index.html" target="_blank">This list</a> shows the IDs that are already taken.)
  - Identify your project (PMC or incubator podling).
  - **IMPORTANT**: you may need to hold discussions with your employer before signing the ICLA, since your employer may have rights to the coding work you do, even outside of your employment. Your employer might even need to provide a <a href="https://www.apache.org/licenses/#contributor-license-agreements" target="_blank">Corporate CLA</a> - determining that is your responsibility. Make sure that you keep up-to-date with this requirement.
  - Read and understand the agreements ICLA specifies and strive to meet the standards expected. Correct title to code sources is of great importance to ASF and it must be to you, too.
  - Make sure that any code you contribute is original work, and that you publicly contribute it to the ASF. In the case of any doubt (or when a contribution has a complex history) please consult your project PMC before committing it.

Some procedures may appear a little bureaucratic, but they are there to protect you as well as ASF. For a clearer understanding read the <a href="https://www.apache.org/licenses/" target="_blank">ASF license guide</a>.

For details on how to submit your ICLA, please see <a href="https://www.apache.org/licenses/#submitting" target="_blank">Submitting License Agreements</a>. Make sure you fill out the ICLA clearly. To minimize the chance of typographical errors, submit the ICLA as an attachment to an email you send from the email address you provide in the ICLA.</p>

<h3 id="acceptance-of-your-icla">Acceptance of your ICLA<a class="headerlink" href="#acceptance-of-your-icla" title="Permanent link">&para;</a></h3>

After the ASF Secretary records your ICLA, your PMC can submit your requested ID for activation. The acceptance process may take some time. The ASF will inform you and your PMC chair when the process is complete. This quiet lull is a good time to familiarize yourself with the Apache Software Foundation in general. Browse the <a href="https://www.apache.org/dev/" target="_blank">developer guides and information</a>, material about the ASF <a href="https://infra.apache.org/" target="_blank">infrastructure</a>, and the <a href="https://www.apache.org/foundation/" target="_blank">Foundation website</a>. We update the websites regularly.

You will also need to familiarize yourself with some Apache policies and procedures. You have probably picked up a lot of this by osmosis already, and your fellow committers and PMC members on your project's `dev@` mailing list are the first place to ask questions.

Key Committer resources:

  - <a href="https://www.apache.org/dev/index.html" target="_blank">ASF Developer Guides &amp; Resources</a> contains pointers to the most important information
  - the <a href="https://www.apache.org/foundation/how-it-works.html" target="_blank">ASF How it works</a> document
  - the <a href="https://training.apache.org/" target="_blank">Apache Training (Incubating)</a> pages
  - the <a href="https://www.apache.org/foundation/bylaws.html" target="_blank">ASF Bylaws</a>

<h3 id="apache-committer-account-creation">Apache Committer account creation<a class="headerlink" href="#apache-committer-account-creation" title="Permanent link">&para;</a></h3>

You will receive an email when your account has been created. (This may take a week or two.) It is now time to do several general tasks, and possibly take some other steps specific to your project that your PMC will share with you.

<h4 id="set-up-your-apacheorg-email-address">Set up your `@apache.org` email address<a class="headerlink" href="#set-up-your-apacheorg-email-address" title="Permanent link">&para;</a></h4>

Read the <a href="https://infra.apache.org/committer-email.html" target="_blank">guide</a> to connecting to and working with your Apache email inbox.

Record any email aliases you use in the `asf-altEmail` field in your LDAP record. You can do this through the the <a href="https://id.apache.org/" target="_blank">self-serve application</a>. The system uses the address in the LDAP `mail` field to forward email sent to your `@apache.org` address. This field must have at least one entry, which must not be your `@apache.org` address.

The `asf-altEmail` field is used to validate subscription requests and correlate subscriptions. (There is no need to duplicate `mail` entries in `asf-altEmail`.)

**Note**: Please read [Dealing with spam in your ASF email account](spam-reporting.html) and **do not** flag valid ASF-related email as spam.

<h3 id="set-up-subversion-or-git-access">Set up Subversion or Git access<a class="headerlink" href="#set-up-subversion-or-git-access" title="Permanent link">&para;</a></h3>

Read about [source control repositories at Apache](version-control.html).

<h3 id="config-access">Configure your access to project Git repositories<a class="headerlink" href="#config-access" title="Permanent link">&para;</a></h3>

If your project uses Git to store, develop, and deploy its product code, you can use either GitHub or Apache's Gitbox for actions such as merging pull requests.

#### Using GitHub

To use GitHub, you need to integrate your GitHub ID with your Apache account, so that you can merge pull requests and perform other Git tasks.

1. Verify you have a GitHub ID enabled with <a href="https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/" target="_blank">two factor authentication (2FA)</a>.
2. Merge your Apache and GitHub accounts using <a href="https://gitbox.apache.org/boxer/" target="_blank">Boxer</a>, the Apache account linking utility for GitHub. Follow the steps outlined in the linking process. You should see three green checks in Boxer when your account has been fully linked.
3. After about two to five minutes, you should have access to your project's repositories on GitHub.

#### Using Gitbox
To connect to Git repositories through Gitbox, visit <a href="https://gitbox.apache.org" target="_blank">Gitbox</a> and follow the onscreen instructions.

### Your first commit to a Git repository
If your project has a page for its developers and committers on its website, add your name and information to it. This is a great way to make your first commit, and helps your team get to know you.

It also serves another purpose: you will learn how to add documentation to your project's website and the technology used to build it. Documentation is vital, and being able to improve the project's web site is a skill that you will need. If your project has not documented how to rebuild the website, then ask on your `dev@` mailing list and use the answer to create a document describing how to do that. It will be gratefully received!

Every team has a lot of "tribal knowledge" that team members hold in their heads or in private notes, but that the whole team needs to know in order to function well and survive a disaster like a key team member suddenly becoming unavailable. You can help migrate tribal knowledge into the documentation, by noting where you have to ask a team member for guidance that you cannot find in the docs.

<h3 id="set-up-security-and-pgp-keys">Set Up Security And PGP Keys<a class="headerlink" href="#set-up-security-and-pgp-keys" title="Permanent link">&para;</a></h3>

Security is vital and Apache pays great attention to it. Remember that at all times, and ensure that all your Apache passwords are sufficiently secure, and that any code you check in is safe.

<a href="https://www.openpgp.org/" target="_blank">OpenPGP</a> is a <a href="https://www.ietf.org/rfc/rfc2440.txt" target="_blank">standard</a> that provides (among other things) methods to create digital signatures for documents ranging from emails to ASF releases. Many applications provide OpenPGP compatible signatures, including the well-known <a href="https://gnupg.org/" target="_blank">GPG</a>. We recommend that you create a PGP key for your `apache.org` address (or add that address to an existing key). **DO NOT** create this key on any machine to which many users have access and **DO NOT** ever copy your private key to any other shared machine. Release managers need to take particular <a href="https://infra.apache.org/release-signing.html#private-key-protection" target="_blank">care of keys used to sign releases</a>.

Upload the public key to a public key server, for example the <a href="https://pgp.mit.edu/" target="_blank">MIT PGP Public Key Server</a>. Then add your keys' primary fingerprints to <a href="https://id.apache.org/" target="_blank">your LDAP profile</a>. The system adds your key to the <a href="https://people.apache.org/keys/" target="_blank">individual and per-project pre-fetched KEYS files</a>, and lets automated tools encrypt communications to you.

Start to build up a good web of trust now before you need to use it in earnest. Be prepared to exchange key information at face-to-face events where ASF folks may be present. The best practice is to insist on identification before signing another person's key. See the <a href="release-signing.html#link-into-wot" target="_blank">Apache release signing guide</a>.

<h3 id="committer-resources">Committer Resources<a class="headerlink" href="#committer-resources" title="Permanent link">&para;</a></h3>

The [Infra documentation page](doc.html) provides a list of resources for committers and other Apache folks.

<h4 id="check-out-the-committers-only-subversion-module">Check out the Committers-only Subversion module<a class="headerlink" href="#check-out-the-committers-only-subversion-module" title="Permanent link">&para;</a></h4>

Do a checkout of the private `committers` module. This is stored in the subversion repository at `https://svn.apache.org/repos/private/committers`. See [Subversion basics](svn-basics.html) if you are unfamiliar with Subversion.

Once you have checked out this module, read all the documents contained in the `docs` directory, especially the `resources.txt` file. There are a number of private mailing lists you need to know about. Join in the Apache community by signing up to every list that interests you. It is better to sign up (even if you sign off later) than to miss out! Please respect the usage guidelines for these private lists.

<h3 id="get-to-know-the-apache-community">Get to know the Apache community<a class="headerlink" href="#get-to-know-the-apache-community" title="Permanent link">&para;</a></h3>

Taking part in the community makes Apache fun. The <a href="https://community.apache.org/" target="_blank">Community Development project</a>  has a central mailing list for topics that cut across PMC boundaries. Discussions of all kinds are on topic as long as the matter is not sensitive or confidential.

<h4 id="mailing-lists">Join email lists<a class="headerlink" href="#mailing-lists" title="Permanent link">&para;</a></h4>

A lot of Apache knowledge-sharing and all formal decision-making takes place on email lists. Most of the lists are public, and you can join and participate in any that attract you.

  - Your project probably has a `dev@` and a `users@` email list, and it is a good idea to join both.
  - We strongly urge all committers to join the `builds@` email list, where people from many projects, and the Infrastructure team, share insights and solve problems related to building and releasing software packages. People using Jenkins, or interested in CI/CD (continuous integration and continuous development) find this list invaluable. Infra also posts notifications to this list regarding outages, upgrades, app add/removals and more.

Instructions for joining and leaving lists, and a browsable list of Apache mailing lists, are <a href="https://www.apache.org/foundation/mailinglists.html" target="_blank">here</a>.

<h3 id="committer-responsibilities">Committer Responsibilities<a class="headerlink" href="#committer-responsibilities" title="Permanent link">&para;</a></h3>

Join your project's `commits@` and `dev@` mailing lists to keep up with project activity. Answering questions on `users@` is also very much appreciated and noticed by your PMC.

Each committer has a responsibility to monitor changes made for potential issues, both coding and legal. If you spot any potential issues in a commit, the right course of action is to post a reply (to the email) raising your concerns to the `dev@` list. In extreme situations, it may be necessary to veto (-1) a commit, but this is an extreme sanction and rarely warranted. Read the <a href="https://www.apache.org/foundation/voting.html" target="_blank">voting guidelines</a> before deploying a veto.

Do not be surprised if your first commit has a delayed diff email. It needs to go through the human moderators.

<h3 id="attending-apachecon">Attending Community Over Code<a class="headerlink" href="#attending-apachecon" title="Permanent link">&para;</a></h3>

If you do not have one already, make a note in your diary about the next <a href="https://www.communityovercode.org/" target="_blank">Community Over Code</a>. This is a great opportunity to meet other Apache folks, hack code and learn about great new open source projects. Watch the lists as the conference dates approach for details about special deals for committers and opportunities to speak.

<h3 id="identity-theft">Identity theft<a class="headerlink" href="#identity-theft" title="Permanent link">&para;</a></h3>

Please be aware that Apache Software Foundation committers are targets for identity theft. These spoof attacks resemble <a href="https://en.wikipedia.org/wiki/Phishing" target="_blank">phishing</a> attacks used to gain access to bank accounts and other web subscriptions. They typically seek to persuade you to enter your access details into a fake website. The ASF will **never** solicit such 'verification'.

Leaking your access to Apache can have very destructive consequences. **Never** disclose your ASF password to anyone.

The Apache Infrastructure team is clueful about DNS maintenance: do **not** trust any redirection by IP address. Your access to Apache will be through the
machines serving the `svn.apache.org` domain. The SSH/SSL fingerprints of machines are listed on the <a href="/machines" target="_blank">machines</a> page, and our <a href="https://infra.apache.org/version-control.html#cert" target="_blank">SVN server fingerprints</a> are also listed.

Please use caution. Do not hesitate to ask if you have doubts: post a question to infrastructure before taking any action.

<h3 id="share-your-wisdom">Share your wisdom<a class="headerlink" href="#share-your-wisdom" title="Permanent link">&para;</a></h3>

Please help to improve this document (see <a href="https://www.apache.org/dev/infra-site.html" target="_blank">guidelines</a> for updating <a href="https://github.com/apache/infrastructure-website" target="_blank">this website</a>).

[Volunteer](infra-volunteer.html) if you would like to help the Infrastructure team keep the good ship ASF afloat.

<h3 id="last">The last word</h3>

Welcome!!
