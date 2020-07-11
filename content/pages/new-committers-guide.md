Title: Guide for new project committers

Here's how to set up the technical and social environment that will support your work as a committer to an Apache project. Some projects have more specific guidelines which the project website or the PMC provide for you. We also have a thorough [Committers' FAQs](commiters.html) for both new and experienced comnmitters.

  - <a href="#what-is-a-committer">What is a committer?</a>
  - <a href="#becoming-a-committer">Becoming a committer</a>
      - <a href="#the-committers-way">The Committer's Way</a>
      - <a href="#submitting-your-individual-contributor-license-agreement-icla">Submitting Your Individual Contributor License Agreement (ICLA)</a>
      - <a href="#acceptance-of-your-icla">Acceptance of your ICLA</a>
      - <a href="#apache-committer-account-creation">Apache Committer Account Creation</a>
      - <a href="#set-up-your-apacheorg-email-address">Set up Your @apache.org email address</a>
      - <a href="#set-up-subversion-or-git-access">Set up Subversion or Git access</a>
      - <a href="#set-up-security-and-pgp-keys">Set up Security and PGP Keys</a>
  - <a href="#committer-resources">Committer resources</a>
      - <a href="#check-out-the-committers-only-subversion-module">he Committers-only Subversion Module</a>
  - <a href="#get-to-know-the-apache-community">The Apache Community</a>
  - <a href="#committer-responsibilities">Committer Responsibilities</a>
  - <a href="#attending-apachecon">Attending ApacheCon</a>
  - <a href="#personal-web-space">Personal web space</a>
  - <a href="#identity-theft">Identity theft</a>
  - <a href="#share-your-wisdom">Share your wisdom</a>

<h3 id="what-is-a-committer">What is a committer?<a class="headerlink" href="#what-is-a-committer" title="Permanent link">&para;</a></h3>

The plain sense of the word "committer" is that you have access rights to your project's repository so you can read and write the source code. Rather than creating a patch and submitting it to be actively reviewed and then committed, you can now create a local patch and commit it yourself - or even review and commit patches created by others. Your fellow committers will review your patches, usually after you commit them.

<h3 id="becoming-a-committer">Becoming a committer<a class="headerlink" href="#becoming-a-committer" title="Permanent link">&para;</a></h3>

If you are not yet a committer, but would like to become one, review:
<ul>
<li><a href="/foundation/getinvolved.html#become-a-committer">Become a committer</a></li>
<li><a href="/foundation/how-it-works.html#committers">ASF committers</a></li>
<li><a href="/foundation/how-it-works.html#meritocracy">Meritocracy</a></li>
</ul>
<h2 id="the-committers-way">The Committer's Way<a class="headerlink" href="#the-committers-way" title="Permanent link">&para;</a></h2>
<p>As a committer, you have access rights to a specific Apache project's repository so you can create and edit source code files, not just read them..
Instead of having to create and submit a patch which other committers would have to review and approve, you can now create a local patch and commit it
yourself; you can also review and commit patches that other project contributors and committers create. Your
patches can still be reviewed by your fellow committers. </p>
<p>Note that some projects use RTC (Review then Commit) rather than CTR (Commit then Review). Check which pattern your project uses, and then follow it..</p>
<p>Take more care than you may have done before when working on the code, since you
 can now change things directly, without review. Make sure you understand how your project's committers work and coordinate with each other. Ask your project PMC, or any active committer on the project, for guidance if there are things you are not sure about.</p>
<p>In general. the more visible and engaged you are in the project, the more fun you will have and the more access you will have to advice and feedback.</p>
<h3 id="submitting-your-individual-contributor-license-agreement-icla">Submitting Your Individual Contributor License Agreement (ICLA)<a class="headerlink" href="#submitting-your-individual-contributor-license-agreement-icla" title="Permanent link">&para;</a></h3>
<p>If you are a brand-new committer, you must complete and submit an <a href="../licenses/#clas">Individual Contributor License Agreement</a> (ICLA) before the ASF can active your
committer account. Note that an account can only be created
if a PMC (or Incubator podling) has invited you. </p>
<p>The ICLA is a formal contract that declares the terms under which you will contribute
intellectual property to the ASF. Note that the ICLA does <strong>not</strong> assign copyright to the ASF; you retain copyright to your own work.
However it does grant the ASF sufficient rights to release any work you submit under the Apache license.</p>
<ul>
<li>Choose an Apache ID before submitting your ICLA. Also select an alternative, in case the ID you want is unsuitable or already taken. Your ID must consist of at least 3 lower-case alphanumeric characters, starting with a letter. (<a href="http://home.apache.org/committer-index.html">This list</a> shows the IDs that are already taken).</li>
<li>Identify your project (PMC or incubator podling).</li>
<li><strong>IMPORTANT:</strong> you may need to hold discussions with your employer before signing the ICLA, since your employer may have rights to the coding 
work you do, even outside of your employment. Your employer might even need to provide a <a href="../licenses/#clas">Corporate CLA</a> - determining that is your
responsibility. Make sure that you keep up-to-date with this requirement.</li>
<li>Read and understand the agreements ICLA specifies and strive to meet
the standards expected. Correct title to code sources is of great importance
to ASF and it must be to you, too. </li>
<li>Make sure that any code you contribute is original work, and that you publicly contribute it to the ASF. In the case of any doubt (or when
a contribution has a complex history) please consult your project PMC before committing it.</li>
</ul>
<p>Some procedures may appear a little bureaucratic, but they are there to protect you as well as ASF. For a clearer
understanding read the <a href="../licenses/">ASF license guide</a>.</p>
<p>For details on how to submit your ICLA, please see <a href="../licenses/#submitting">Submitting License Agreements</a>.
Make sure you fill out the ICLA clearly. To minimize the chance of typographical errors, submit the ICLA as an attachment to an email you send from the email address you provide in the ICLA.</p>
<h3 id="acceptance-of-your-icla">Acceptance of your ICLA<a class="headerlink" href="#acceptance-of-your-icla" title="Permanent link">&para;</a></h3>
<p>After the ASL Secretary records your ICLA, your PMC can submit your requested ID for activation. The acceptance process may take some time. The ASF will inform you and your PMC chair when the process is complete.</p>
<p>This quiet lull is a good time to familiarize yourself with the Apache
Software Foundation in general. Browse the <a href="../dev/">developer guides and information</a>, material about the ASF <a href="https://infra.apache.org/" target="_blank">infrastructure</a>, and the <a href="../foundation/">Foundation website</a>. We update the websites regularly, so visit these pages regularly.</p>
<p>You will also need to familiarize yourself with some Apache policies and procedures. You have probably picked up a lot of this by osmosis already, and your fellow committers and PMC members on your project's dev@ mailing list are the first place to ask questions.</p>
<p>Key Committer resources:</p>
<ul>
<li>
<p><a href="index.html">ASF Developer Guides &amp; Resources</a> contains pointers to the most important information</p>
</li>
<li>
<p>the <a href="../foundation/how-it-works.html">ASF How it works</a> document</p>
</li>
<li>
<p>the <a href="http://incubator.apache.org/learn/">Incubator Learn</a> pages</p>
</li>
<li>
<p>the <a href="../foundation/bylaws.html">ASF Bylaws</a> </p>
</li>
</ul>
<h3 id="apache-committer-account-creation">Apache Committer Account Creation<a class="headerlink" href="#apache-committer-account-creation" title="Permanent link">&para;</a></h3>
<p>You will receive an email when your account has been created. (This may take
a week or two.) It is now time to do several general tasks, and possibly take some other steps specific to your project that your PMC will share with you.</p>
<h3 id="set-up-your-apacheorg-email-address">Set up Your @apache.org email address<a class="headerlink" href="#set-up-your-apacheorg-email-address" title="Permanent link">&para;</a></h3>
<p>Read the <a href="https://infra.apache.org/committer-email.html" target="_blank">guide</a> to connecting to and working with your Apache email inbox.</p>
<p>Record any email aliases you use in the 'asf-altEmail' field in your LDAP record. You can do this through the the <a href="https://id.apache.org/" target="_blank">self-serve application</a>.</p>
<p>The system uses the address in the LDAP 'mail' field to forward email sent to your @apache.org address.
This field must have at least one entry, which must not be your @apache.org address.</p>
<p>The 'asf-altEmail' field is used to validate subscription requests and correlate subscriptions.
(There is no need to duplicate 'mail' entries in 'asf-altEmail'.)</p>
<h3 id="set-up-subversion-or-git-access">Set up Subversion or Git access<a class="headerlink" href="#set-up-subversion-or-git-access" title="Permanent link">&para;</a></h3>
<p>Read the <a href="version-control.html">Version Control Setup Guide</a>.</p>
<p>If your project has a page for its developers and committers, add your name and information to it This is a great way to make your first commit, and helps your team get to know you.</p>
<p>It also serves another purpose: you will learn how to add documentation to your project's website and the technology used to build it. Documentation is vital, and being able to improve the project's web site is a skill that you will need. If your project has not documented how to rebuild the website, then ask on your dev mailing list and use the answer to create a
document describing how to do that. It will be gratefully received! Every team has a lot of "tribal" knowledge" that team members hold in their heads or in private notes, but that the whole team needs to know in order to function well and survive a disaster like a key team member suddenly becoming unavailable.</p>
<p>Many Apache projects still use the centralized <a href="project-site.html">Apache CMS system</a> to manage their websites. However, Apache is encouraging projects to migrate to options like Jekyll or Pelican with Buildbot. Consult your PMC about which system your project is using now and, if it is the CMS, what the plans are to migrate to a different system.</p>
<h3 id="set-up-security-and-pgp-keys">Set Up Security And PGP Keys<a class="headerlink" href="#set-up-security-and-pgp-keys" title="Permanent link">&para;</a></h3>
<p>Security is vital and Apache pays great attention to it. Remember that at all times, and ensure that all your Apache passwords are sufficiently secure, and that any code you check in is safe.</p>
<p><a href="https://www.openpgp.org/" target="_blank">OpenPGP</a> is a <a href="https://www.ietf.org/rfc/rfc2440.txt" target="_blank">standard</a> that provides (among other things) methods to create digital signatures for documents ranging from emails to ASF releases. Many applications provide OpenPGP compatible signatures, including the well-known <a href="https://gnupg.org/" target="_blank">GPG</a>.</p>
<p>We recommend that you create a PGP key for your <code>apache.org</code> address (or add that address to an existing key). <b>DO NOT</b> create this key on any machine to which many users have access and <b>DO NOT</b>, ever, copy your private key to any other shared machine. Release managers need to take particular <a href="/dev/release-signing.html#private-key-protection">care of keys used to sign releases</a>.</p>
<p>Upload the public key to a public key server, for example the <a href="https://pgp.mit.edu/" target="_blank">MIT PGP Public Key Server</a>.
Then add your keys' primary fingerprints to <a href="https://id.apache.org/" target="_blank">your LDAP
profile</a>. The system adds your key to the <a href="https://home.apache.org/keys/" target="_blank">individual and per-project pre-fetched KEYS files</a>, and lets automated tools encrypt communications to you.</p>
<p>Start to build up a good web of trust now before you need to use it in earnest. Be prepared to
exchange key information at face-to-face events where ASF folks may be present. The best practice is to insist on identification before signing
another person's key. See the <a href="release-signing.html#link-into-wot">Apache release signing guide</a>. </p>
<h2 id="committer-resources">Committer Resources<a class="headerlink" href="#committer-resources" title="Permanent link">&para;</a></h2>
<p>The <a href="https://infra.apache.org/doc.html" target="_blank">Infra documentation page</a> provides a list of resources for committers and other Apache folks.</p>
<h2 id="check-out-the-committers-only-subversion-module">Check out The Committers-only Subversion Module<a class="headerlink" href="#check-out-the-committers-only-subversion-module" title="Permanent link">&para;</a></h2>
<p>You should do a checkout of the private <code>committers</code> module. This is stored
in the subversion repository with url
<code>https://svn.apache.org/repos/private/committers</code>. (See
<a href="index.html#svn">notes</a> for those unfamiliar with subversion.)</p>
<p>Once you have checked out this module, you need to read all the documents
contained in the <code>docs</code> directory, especially the resources.txt file. There
are a number of private mailing lists you need to know about. Join in the
Apache community by signing up to every list that interests you. It is
better to sign up (even if you sign off later) than to miss out! Please
respect the usage guidelines for these private lists.</p>
<h2 id="get-to-know-the-apache-community">Get To Know The Apache Community<a class="headerlink" href="#get-to-know-the-apache-community" title="Permanent link">&para;</a></h2>
<p>The community makes Apache fun. The <a href="http://community.apache.org/">Community Development project</a>
 has a central mailing list for topics that cut across <a href="pmc.html">PMC</a> boundaries. Discussions of all
kinds are on topic as long as the matter doesn't need to be sensitive or
confidential.</p>
<p><a href="http://labs.apache.org/">Apache Labs</a> is a place for innovation where
committers of the foundation can experiment with new ideas. The aim is to
provide the necessary resource to promote and maintain the innovative power
within the Apache community without the burden of community building.</p>
<p>If you have an idea that you want to explore and collaborate on with other
committers then come and discuss it at <a href="http://labs.apache.org/">Labs</a>.
Even if you don't have anything at the moment, then come and take a look at
what other committers are working on.</p>
<h2 id="committer-responsibilities">Committer Responsibilities<a class="headerlink" href="#committer-responsibilities" title="Permanent link">&para;</a></h2>
<p>Join your project's commit@ and dev@ mailing lists to keep up 
with activity on your project.  Answering questions on users@ is also 
very much appreciated and noticed by your PMC.</p>
<p>Each committer has a responsibility to monitor the changes made for
potential issues, both coding and legal. If you spot any potential issues
in a commit, the right course of action is to post a reply (to the email)
raising your concerns to the dev list. In extreme situations, it may be
necessary to veto (-1) a commit but please beware that this is an extreme
sanction and rarely warranted; read the <a href="http://www.apache.org/foundation/voting.html">voting guidelines before a veto</a>.</p>
<p>Do not be surprised if your first commit has a delayed diff email. It needs
to go through the human moderators.</p>
<h2 id="attending-apachecon">Attending ApacheCon<a class="headerlink" href="#attending-apachecon" title="Permanent link">&para;</a></h2>
<p>If you don't have one already, make a note in your diary about the next
<a href="http://www.apachecon.com/">ApacheCon</a>. This is a great opportunity to meet
other Apache folks, hack code and dream about great new open source
projects. Watch the lists as the conference dates approach for details
about special deals for committers and opportunities to speak.</p>
<h2 id="personal-web-space">Personal web space<a class="headerlink" href="#personal-web-space" title="Permanent link">&para;</a></h2>
<p>Some Apache committers have personal content served from ASF web servers. There are no fixed guidelines
about appropriate content: committers should know how to behave! In general, people use this option to host ASF-related content or to showcase interesting private
projects. If you do use this feature, please do so responsibly.</p>
<p>Material placed in the`public_html directory is available under
the <code>http://home.apache.org/~<em>username</em>/</code>url (where
<em>username</em> is your ASF account ID).</p>
<h2 id="identity-theft">Identity theft<a class="headerlink" href="#identity-theft" title="Permanent link">&para;</a></h2>
<p>Please be aware that Apache Software Foundation committers are targets for
identity theft. These spoof attacks resemble the
<a href="http://en.wikipedia.org/wiki/Phishing">phishing</a> attacks used to gain
access to bank accounts and other web subscriptions. They typically seek to
persuade you to enter your access details into a fake website.
The foundation will <strong>never</strong> solicit such 'verification'.</p>
<p>Leaking your access to Apache can have very destructive consequences. 
<strong>Never</strong> disclose your ASF password to anyone.</p>
<p>The Apache Infrastructure team is clueful about DNS maintenance: do <strong>not</strong> trust any
redirection by IP address. Your access to Apache will be through the
machines serving the <code>svn.apache.org</code> domain. The
ssh/ssl fingerprints of machines are <a href="machines">listed on the machines page</a>
and our <a href="http://www.apache.org/dev/version-control.html#cert">SVN servers fingerprints</a> are also listed.</p>
<p>Please use caution. Do not hesitate to ask if you have doubts: post a
question to infrastructure before taking any action.</p>
<p><strong>Note:</strong> the fingerprint for the key used for ssh is different to the
fingerprint of the certificate used to <a href="version-control.html#cert">securely serve the
website</a>.  A full list of fingerprints is maintained
on the <a href="machines">machines</a> page.</p>
<h2 id="share-your-wisdom">Share your wisdom<a class="headerlink" href="#share-your-wisdom" title="Permanent link">&para;</a></h2>
<p>Please help to improve this document (see <a href="infra-site.html">guidelines</a> for 
updating this website). <a href="infra-volunteer.html">Subscribe</a> to the Infrastructure
list if you want to discuss the improvements, or just to find out how the
good ship Apache is kept afloat (and to help).  Welcome!</p></div>
