Title: Guide to new committers
slug: reference/committer/newaccount

[TOC]

This document aims to bring together in one place all of the general
information that a newbie committer needs to know. There will be other
details (some project-specific) that cannot be covered here. Those should
be covered by your project community.

The plain sense of the word "committer" is that you will have access rights
to your project's repository to write (as well as read) the source.
Rather than creating a patch and submitting it to be actively reviewed and
then (hopefully) committed, you can now create a local patch and commit it
yourself - or even review and commit patches created by others. Your
patches will still be reviewed by your fellow committers. This will happen
after the event (usually through commit emails, although the exact
convention for the review may differ between projects).

Take more care than you did before and expect existing committers to be
particularly vigilant.
You would already know well (by example) how a committer should behave.
If you are *not* familiar, you can always ask your [PMC](pmc.html) for guidance.

# Contributor license agreement # {#cla}

The very first thing you need to do is to complete and submit an [Individual
Contributor License Agreement](../licenses/#clas) (ICLA). This is a formal
delcaration declaration of the terms under which you will contribute
intellectual property to the ASF.

You can send in the ICLA either by postal mail, fax or by emailing a scan of
the signed copy to secretary@apache.org.
Please ensure that it is clearly written. Your PMC will keep track to know
when the ICLA is received and recorded by the ASF Secretary (this might take time).

Note that you may need to hold discussions with your employer before
signing the agreement. Your employer might even need to provide a
[Corporate CLA](../licenses/#clas) - determining that is your
responsibility. Also make sure that you keep up-to-date with this
requirement.

It is important to read and understand the agreements and strive to meet
the standards expected. Correct title to the source is of great importance
to ASF and it must be to you too. Some procedures may appear a little
bureaucratic, but they are there to protect you as well as ASF. For a clearer
understanding read the [ASF license guide](../licenses/).

Please take care to ensure that patches are original works which have been
clearly contributed to the ASF in public. In the case of any doubt (or when
a contribution with a more complex history is presented) please consult your
project PMC before committing it.

# Before account creation #

You will also be asked for a preferred Apache user name. Please think also
of an alternative, in the case that the primary is unsuitable or taken.
Note that your user name must not contain punctuation. ([This
list](http://people.apache.org/committer-index.html) may prove helpful).

The acceptance process may well take some time. The ASF is staffed by
volunteers working in their free time. It often takes some time for
requests to be processed and new accounts set up. Please be patient. You
will be informed when the process is complete (and your [PMC chair](./pmc.html#chair)
will monitor the progress).

This quiet lull is a good time to familiarize yourself with the Apache
Software Foundation in general. Browse the [developer information](../dev/)
and the [Foundation website](../foundation/). Remember, that the website is
being continually updated, so you should regularly visit these pages.

You will also need to familiarize yourself with some Apache policies and
procedures. Do not worry, this isn't as intimidating as it seems: you will
probably have learnt a lot by osmosis already. But it is important to know
where authoritative information is held when you need to consult it.
Unfortunately it is currently scattered. There is ongoing an effort to
bring it all together. What follows is a partial list:

If there is anything that you are not sure about, then just ask on the
"dev" list for your particular project.

-  [ASF Developer Resources](index.html) 

- the [ASF How it works](../foundation/how-it-works.html) document

- the [Incubator Learn](http://incubator.apache.org/learn/) pages

- the [ASF Bylaws](../foundation/bylaws.html) 

- and the ASF general [wiki](http://wiki.apache.org/general).

# Account creation #

You will receive an email when your account has been created.  (This may take
a week or two.)

There are a number of general things you need to do. These will be covered
in separate sections below. There may some other things that the particular
project requires, but you should be told of those by your fellow
committers.

Setting up the account at this time is convenient (since the logon needs to
be tested).

# Setting up SSH # {#ssh-setup}

We are not going to describe how to use ssh (there are plenty of good
[tutorials](user-ssh.html) elsewhere).

All ASF servers require that you use a key based login. The first steps are to
generate the key on your local desktop (not on minotaur.apache.org) and then upload your
authorized keys to your Apache LDAP account. You can do this via the
[Apache Account Utility](https://id.apache.org).
Do not try to configure an authorized\_keys file in your `~/.ssh` directory. It won't work.
Each line that would normally be in your authorized_keys should be added to your
Apache LDAP account via the [Apache Account Utility](https://id.apache.org).
You can add multiple lines.

Once you have configured your ssh client, you will be able to log onto your account at
minotaur.apache.org using ssh:

    $ ssh [username]@minotaur.apache.org
 
If you cannot login, you need to check (via the project PMC) that the
account has been created correctly. Please check your ssh configuration
first (do `ssh -e`).

If you use PuTTY then ensure that it is configured to force SSH v2
protocol. And use keyboard-interactive.

Once you are logged on, there are few tasks best performed right away.
Please take care when using your shell account.

You need to check that your `umask` is set in a group friendly fashion.
This ensures that the documents you create are editable by your fellow
committers. To do this, (depending on which shell you use) edit the
`.cshrc` file or `.profile` (sh derivatives) and ensure that the `umask`
is set as follows:

    :::shell
    umask 002 

You may find that a `umask` line already exists, in which case
it should be modified. Otherwise, a new line needs to be added. (You will
need to use a \*nix command-line editor such as `vi`.) Tip: You can view the
files of some other committer, e.g. `ls -al ~mymentor; cat
~mymentor/.cshrc` 

# Setting up email #

See these [instructions](user-email.html).

# Subversion access and Web sites #

All the information you need is contained [here](version-control.html).

If your project has a page about the developers and committers, go right
ahead and add your name and information to it! Really. This is a great way
to make your first commit.

It also serves another purpose: you will learn how to add documentation to
your project's website and the technology used to build it. Documentation
is vital, and being able to improve the project's web site is a skill that
you will need. If your project has not documented how to rebuild the
website, then ask on your dev mailing list and use the answer to create a
document describing how to do that. It will be gratefully received!

Here are some general infrastructure notes about how to manage your
[project website](project-site.html).

# Security and PGP #

Security is vital and Apache pays great attention to it. Please remember
that at all times.

Security is vital and Apache pays great attention to it. Please remember
that at all times.

[OpenPGP](http://www.openpgp.org/) is a
[standard](http://www.ietf.org/rfc/rfc2440.txt) which provides (amongst
other things) methods to create digital signatures for documents. These
documents could be emails or could be ASF releases. A variety of
applications exist which provide OpenPGP compatible signatures including
the well known [GPG](http://www.gnupg.org/) and [PGP](http://www.pgp.com/).

It is recommended that you create a PGP key for your `apache.org` address now
(or add that address to an existing key, if you have one). <b>DO NOT</b> create
this key on minotaur.apache.org or any other machine to which multiple
users have access and <b>DO NOT</b>, ever, copy your private
key to people.apache.org or any other shared machine. Release managers need
to take particular [care of keys used to sign releases](/dev/release-signing.html#private-key-protection).

Upload the public key to a public key server (for example [MIT](http://pgp.mit.edu/)).
Afterwards, add your keys' primary fingerprints to [your LDAP
profile](https://id.apache.org/); this will cause your to be added to the
individual and per-project pre-fetched KEYS files on
[https://people.apache.org/keys/committer/](https://people.apache.org/keys/committer/), and allow
automated tools to encrypt communications to you.
Start to build up a good
web of trust now before you need to use it in earnest. Be prepared to
exchange key information at any face-to-face events where ASF folks may be
present. The best practice is to insist on identification before signing
another's key. See [signing guide](http://www.apache.org/dev/release-signing.html#link-into-wot) and
Henk's [Key Signing
HOWTO](http://people.apache.org/~henkp/sig/pgp-key-signing.txt). 

Henk's [Apache home page](http://home.apache.org/~henkp/) provides some useful information
related to the use of signatures both in general and specifically at
Apache. See also the [signing
guide](http://www.apache.org/dev/release-signing.html).

# Other resources #
[Apache People](http://people.apache.org) maintains public resources about
Apache committers.
[Participation](http://people.apache.org/foaf/index.html) is easy but
optional. If you want to take part, now is a good time to add your details.

Although the Apache Way is to keep things as public as possible, there are
some resources here at Apache which are closed to those who are not
committers.

# Committers-only Subversion modules #

You should do a checkout of the private `committers` module. This is stored
in the subversion repository with url
`https://svn.apache.org/repos/private/committers`. (See
[notes](index.html#svn) for those unfamiliar with subversion.)

Once you have checked out this module, you need to read all the documents
contained in the `docs` directory, especially the resources.txt file. There
are a number of private mailing lists you need to know about. Join in the
Apache community by signing up to every list that interests you. It is
better to sign up (even if you sign off later) than to miss out! Please
respect the usage guidelines for these private lists.

# Community #

The community makes Apache fun. The community list is a public
[readable](http://mail-archives.apache.org/mod_mbox/www-community/) list
for topics that cut across [PMC](pmc.html) boundaries. Discussions of all
kinds are on topic as long as the matter doesn't need to be sensitive or
confidential.

The [Apache Labs](http://labs.apache.org/) project is open to all ASF
Committers (and only them).

[Apache Labs](http://labs.apache.org/) is a place for innovation where
committers of the foundation can experiment with new ideas. The aim is to
provide the necessary resource to promote and maintain the innovative power
within the Apache community without the burden of community building.

If you have an idea that you want to explore and collaborate on with other
committers then come and discuss it at [Labs](http://labs.apache.org/).
Even if you don't have anything at the moment, then come and take a look at
what other committers are working on.

# Responsibilities #

Join your project's commit mailing list if one exists (some projects send
all commit emails to the dev list).

Each committer has a responsibility to monitor the changes made for
potential issues, both coding and legal. If you spot any potential issues
in a commit, the right course of action is to post a reply (to the email)
raising your concerns to the dev list. In extreme situations, it may be
necessary to veto (-1) a commit but please beware that this is an extreme
sanction and rarely warranted.

Do not be surprised if your first commit has a delayed diff email. It needs
to go through the human moderators.

# ApacheCon #

If you don't have one already, make a note in your diary about the next
[ApacheCon](http://www.apachecon.com/). This is a great opportunity to meet
other Apache folks, hack code and dream about great new open source
projects. Watch the lists as the conference dates approach for details
about special deals for committers and opportunities to speak.

# Personal web space # {#personal-web-space}

You might already be aware that some Apache folks have content served from
Apache web servers. For example, Henk and Vadim both provide
[statistics](committers.html#statistics). The server does not enforce rules
about appropriate content: committers should know how to behave! Most other
folks use it for Apache related content and some for interesting private
projects. If you do use it, please use it responsibly.

Material placed in the `public_html` directory will be available under
the <code>http://home.apache.org/~*username*/</code> url (where
*username* is your ASF account Id).

The following are NOT permitted to be hosted in your personal web space:
 
* Releases - These should be uploaded to https://dist.apache.org/repos/dist
* Release candidates - These should be uploaded to https://dist.apache.org/repos/dist
* Nightly builds - These should be hosted by https://ci.apache.org/
* Maven repositories - These should be hosted by https://repository.apache.org/
* Project documentation
* Project data backups
* Installation media for any software

As a guide, your personal web space is not expected to exceed a few hundred MB. If it does, you may be required to justify to the infrastructure team why you require so much personal web space.

# Identity theft #

Please be aware that Apache Software Foundation committers are targets for
identity theft. These spoof attacks resemble the
[phishing](http://en.wikipedia.org/wiki/Phishing) attacks used to gain
access to bank accounts and other web subscriptions. They typically seek to
persuade you to enter your access details into a fake website.
The foundation will **never** solicit such 'verification'.

Leaking your access to Apache can have very destructive consequences. 
**Never** disclose your ASF password to anyone.

The Apache team is clueful about DNS maintenance: do **not** trust any
redirection by IP address. Your access to Apache will be through the
machines serving the `svn.apache.org` and `git-wip.apache.org` domains. The
ssh/ssl fingerprints are [listed on the machines page](machines).

Please use caution. Do not hesitate to ask if you have doubts: post a
question to infrastructure before taking any action.

**Note:** the fingerprint for the key used for ssh is different to the
fingerprint of the certificate used to [securely serve the
website](version-control.html#cert).  A full list of fingerprints is maintained
on the [machines](machines) page.

# Unofficial resources #

If you like, get involved with unofficial resources open to ASF committers:

-  [Join](committers.html#planetapache) 
[PlanetApache](http://planet.apache.org/committers/) 

Please help to improve this document (see [guidelines](infra-site.html) for
website update). [Subscribe](infra-volunteer.html) to the Infrastructure
list if you want to discuss the improvements, or just to find out how the
good ship Apache is kept afloat (and to help).