Title: How to transition to a new PGP key
license: https://www.apache.org/licenses/LICENSE-2.0

<h2 id="status">Introduction<a class="headerlink" href="#status" title="Permanent link">&para;</a></h2>

This document is for project **committers** who wish to change the PGP key they use at Apache (for example to sign releases). It explains how to create a new PGP key and break it in, gradually having it replace the old key.

## Contents ##

<ul>
<li><a href="#important">Important note</a></li>
<li><a href="#motivation">Why replace a key?</a></li>
<li><a href="#single-keyring">Using a single keyring for two keys</a></li>
<li><a href="#transition-export">Exporting both new and old keys</a></li>
<li><a href="#transition-fingerprints">Fingerprinting new and old keys</a></li>
</ul>

<h2 id="important">Important note<a class="headerlink" href="#important" title="Permanent link">&para;</a></h2>

If your key has been compromised, you **must not** use a transition period as described below. Revoke the compromised key immediately and create a new one. Consider all <a href="/release-signing.html#web-of-trust" target="_blank">web of trust</a> links signed by the old key as suspect. You must establish a completely new set of links.

<h2 id="motivation">Why replace a key?<a class="headerlink" href="#motivation" title="Permanent link">&para;</a></h2>

When replacing one uncompromised key with a newer (typically longer) one, using a transition period when both keys are trustworthy and participate in the <a href="/release-signing.html#web-of-trust" target="_blank">web of trust</a> uses _trust transitivity_ to use links to the old key to trust signatures and links created by the new key. During a transition, both keys are trustworthy but you only use the newer one to sign documents and certify links in the web of trust.

This document describes how to use [GnuPG](openpgp.html) to create a new key and manage both keys during this transition period.

<h2 id="single-keyring">Using a single keyring for two keys<a class="headerlink" href="#single-keyring" title="Permanent link">&para;</a></h2>

It is best to use a single keyring containing both keys.

<h3 id="generate-new-key">Generate a new key<a class="headerlink" href="#generate-new-key" title="Permanent link">&para;</a></h3>

Generate the new key either:

  - directly in the keyring containing the old key
  - in a new keyring, and then transfer the new key to the keyring containing the old key

To generate a strong [RSA key](release-signing.html#rsa) follow [these instructions](openpgp.html#generate-key). If you use a separate keyring, follow [these instructions](openpgp.html#secret-key-transfer) to transfer it.

Both new and old keys should now be contained in the same keyring. Verify this by:

```
$ gpg --list-secret-keys  

alice/secring.gpg


sec   1024D/AD741727 2009-08-20
uid                  Alice Example (EXAMPLE OF OLD KEY) <alice@example.org>
ssb   1024g/268883A9 2009-08-20


sec   4096R/E2B054B8 2009-08-20
uid                  Alice Example (EXAMPLE NEW KEY) <alice@example.org>
ssb   4096R/4A6D5217 2009-08-20
```

Both new and old keys should be listed.

<h3 id="open-interaction-edit">Open interactive edit mode<a class="headerlink" href="#open-interaction-edit" title="Permanent link">&para;</a></h3>

You need to perform a number of operations on the new key. Though you can perform them individually, saving and closing after each one, it is more convenient to use _interactive edit_ mode.

Start by opening an edit session on the new key, for example E2B054B8

```
$ gpg --edit-key E2B054B8
gpg (GnuPG) 1.4.9; Copyright (C) 2008 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Secret key is available.


pub  4096R/E2B054B8  created: 2009-08-20  expires: never       usage: SC

                     trust: unknown       validity: unknown
sub  4096R/4A6D5217  created: 2009-08-20  expires: never       usage: E 

[ unknown] (1). Alice Example (EXAMPLE NEW KEY) <alice@example.org>


Command> 
```

<h3 id="trust-new-key">Trust the new key<a class="headerlink" href="#trust-new-key" title="Permanent link">&para;</a></h3>

The new key needs to be marked as ultimately trusted in this keyring. This will ensure that the <a href="release-signing.html#web-of-trust" target="_blank">web of trust</a> links signed by this key will be trusted automatically.

```
Command> trust
pub  4096R/E2B054B8  created: 2009-08-20  expires: never       usage: SC

                     trust: unknown       validity: unknown
sub  4096R/4A6D5217  created: 2009-08-20  expires: never       usage: E 

[ unknown] (1). Alice Example (EXAMPLE NEW KEY) <alice@example.org>

Please decide how far you trust this user to correctly verify other users' keys
(by looking at passports, checking fingerprints from different sources, etc.)


1 = I don't know or won't say
  2 = I do NOT trust
  3 = I trust marginally
  4 = I trust fully
  5 = I trust ultimately
  m = back to the main menu


Your decision? 5
Do you really want to set this key to ultimate trust? (y/N) y


pub  4096R/E2B054B8  created: 2009-08-20  expires: never       usage: SC

                     trust: ultimate      validity: unknown
sub  4096R/4A6D5217  created: 2009-08-20  expires: never       usage: E

[ unknown] (1). Alice Example (EXAMPLE NEW KEY) <alice@example.org>
Please note that the shown key validity is not necessarily correct
unless you restart the program.
```

<h/3 id="sign-new-key">Use the old key to sign the new key<a class="headerlink" href="#sign-new-key" title="Permanent link">&para;</a></h3>

Use the old key (AD741727, say) to sign the new key:

```
Command> sign AD741727

pub  4096R/E2B054B8  created: 2009-08-20  expires: never       usage: SC

                     trust: ultimate      validity: ultimate
Primary key fingerprint: FF96 6261 C995 1DDE BF34  5150 D5D2 BDB5 E2B0 54B8


 Alice Example (EXAMPLE NEW KEY) &lt;alice@example.org&gt;



Are you sure that you want to sign this key with your
key "Alice Example (EXAMPLE OF OLD KEY) <alice@example.org>"
(AD741727)


Really sign? (y/N) y


You need a passphrase to unlock the secret key for
user: "Alice Example (EXAMPLE OF OLD KEY) <alice@example.org>"
1024-bit DSA key, ID AD741727, created 2009-08-20
```

<h3 id="check-sha">Check preferences<a class="headerlink" href="#check-sha" title="Permanent link">&para;</a></h3>

Make sure you are [avoiding SHA-1](openpgp.html#sha1) in the [key preferences](openpgp.html#key-prefs) of both the new and old keys.

<h3 id="finish-off">Complete the edit<a class="headerlink" href="#finish-off" title="Permanent link">&para;</a></h3>

It is convenient to add secondary user ids for current email accounts at this point.

Then save your changes, which will exit you from edit mode:

```
Command> save
```

<h3 id="sign-old-with-new">Whether to sign the old key with the new<a class="headerlink" href="#sign-old-with-new" title="Permanent link">&para;</a></h3>

Arguments can be made for and against signing the old key with the new. The old key is less trustworthy now and will be revoked in future, so signing with it may be misleading for those unaware of the potential weaknesses. However, without this signature, signers of the new key will not receive the transitive benefit of the links made from the old key. Anyone who chooses not to sign the old key with the new should made efforts to re-sign links made by the old key with the new key.

<h3 id="set-default-to-new">Set the default to the new key<a class="headerlink" href="#set-default-to-new" title="Permanent link">&para;</a></h3>

Next, change the default key on the keyring to the new. This ensures that all future signatures use the new key. Though you could still use the old key for signing by explicitly specifying it, avoid this since the signatures will be weak.

To make the new key the default, set the `default-key` in the `gpg.conf` configuration file. For example, to set the default to `E2B054B8` add:

```
default-key E2B054B8
This setting can be tested by creating a test signature:
$ gpg --detach-sig --armor document

You need a passphrase to unlock the secret key for
user: "Alice Example (EXAMPLE NEW KEY) <alice@example.org>"
4096-bit RSA key, ID E2B054B8, created 2009-08-20
```

Verify that the new key has been chosen by default.

<h3 id="update-keys">Upload both keys<a class="headerlink" href="#update-keys" title="Permanent link">&para;</a></h3>

Finish the process by uploading the new and old keys to the keyserver:

```
$ gpg --send-keys E2B054B8 AD741727
```

<h3 id="backups">Create backups<a class="headerlink" href="#backups" title="Permanent link">&para;</a></h3>

Follow [these instructions](openpgp.html#backup).

<h3 id="revocation-certificates">Generate and store revocation certificates<a class="headerlink" href="#revocation-certificates" title="Permanent link">&para;</a></h3>

Follow [these instructions](openpgp.html#revocation-certs) to create and securely store [generic revocation certificates](release-signing.html#revocation-cert" for the new key.

<h3 id="update-documents">Update documents<a class="headerlink" href="#update-documents" title="Permanent link">&para;</a></h3>

The final stage in the process is to update documents containing references to the old key so that they contain both the new and old keys. For Apache documents, follow [this checklist](openpgp.html#update). Use the instructions for a transition when there is a choice.

For other documents:

  - Update those that contain an [export](release-signing.html#export) with a <a href="#transition-export">dual export</a>.
  - Update those that contain a [fingerprint](release-signing.html#fingerprint") with [both fingerprints](#transition-fingerprints).
  
<h3 id="wot">Web of trust<a class="headerlink" href="#wot" title="Permanent link">&para;</a></h3>

Read this [Guide to Apache use](openpgp.html#wot) of the [web of trust](release-signing.html#web-of-trust) and make arrangements to include your new key at the earliest opportunity.

<h2 id="transition-export">Exporting both new and old keys<a class="headerlink" href="#transition-export" title="Permanent link">&para;</a></h2>

During the transition period, use a single export containing both new and old public keys whenever you need an export. 

To create a suitable export, supply both key IDs on the command line. For example, to export keys AD741727 (old) and E2B054B8 (new) to FILENAME use:

```
$ gpg --export --armor --output FILENAME AD741727 E2B054B8
```

This exports only the public keys, and so isn't confidential. Replace the old public key with this dual export everywhere it was published.

<h2 id="transition-fingerprints">Fingerprinting new and old keys<a class="headerlink" href="#transition-fingerprints" title="Permanent link">&para;</a></h2>

During the transitions, use both fingerprints. For example, to fingerprint old key `AD741727` and new key `E2B054B8`, use:

```
$ gpg --fingerprint AD741727 E2B054B8
pub   1024D/AD741727 2009-08-20
      Key fingerprint = CD0C 5281 D0A9 E963 19AF  F365 AD81 612A AD74 1727
uid                  Alice Example (EXAMPLE OF OLD KEY) <alice@example.org>
sub   1024g/268883A9 2009-08-20

pub   4096R/E2B054B8 2009-08-20
      Key fingerprint = FF96 6261 C995 1DDE BF34  5150 D5D2 BDB5 E2B0 54B8
uid                 Alice Example (EXAMPLE NEW KEY) <alice@example.org>
sub   4096R/4A6D5217 2009-08-20
```

So the fingerprints are:

  - `CD0C 5281 D0A9 E963 19AF F365 AD81 612A AD74 1727` for `AD741727`
  - `FF96 6261 C995 1DDE BF34 5150 D5D2 BDB5 E2B0 54B8` for `E2B054B8`

For every fingerprint, the last 8 digits are the key ID.
