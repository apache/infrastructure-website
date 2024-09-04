Title: Signing Releases
license: https://www.apache.org/licenses/LICENSE-2.0

<h2 id="abstract">Introduction<a class="headerlink" href="#abstract" title="Permanent link">&para;</a></h2>

The first part of this document gives release managers a basic introduction to release signing. See under [Further reading](#reading) for links to authoritative sources of deeper information.

The second part answers some frequently-asked questions from people who download releases from Apache projects.

This document is informative and does not constitute policy.

<h2>Contents</h2>

<h3>For release managers</h3>

- <a href="#note">Important notes</a>
- <a href="#basic-facts">Basic facts</a>
- <a href="#signing-basics">Signing basics</a>
- <a href="#key-basics">Keys basics</a>
- <a href="#safe-practice">How can I safely practice using OpenPGP?</a>
- <a href="#web-of-trust">Web of Trust basics</a>
- <a href="#passphrase">What is a Passphrase?</a>
- <a href="#revocation-cert">Revocation Certificate basics</a>
- <a href="#automated-release-signing">Automated Release Signing</a>
- <a href="#reading">Further Reading</a>


### FAQs from those downloading releases

  - <a href="#verifying-signature">What does verifying a signature mean?</a>
  - <a href="#check-integrity">How can I check the integrity of a release?</a>
  - <a href="#public-key-not-found">What does 'Public key not found' mean when verifying a signature?</a>
  - <a href="#trust">What is a trusted key?</a>
  - <a href="#valid-untrusted-vs-invalid-trusted">What is the difference between a valid signature from an untrusted key and an invalid signature from a trusted key?</a>
  - <a href="#fingerprint">What is a public key fingerprint?</a>
  - <a href="#local-sig">Can I mark a key as locally trusted?</a>

## For release managers

<h3 id="note">Important notes<a class="headerlink" href="#note" title="Permanent link">&para;</a></h3>

All new **RSA** keys generated should be at least **4096** bits. **Do not** generate new **DSA** keys.

Recent research has revealed weaknesses in SHA-1, and thus in the DSA and 1024 bit RSA OpenPGP keys which must use this algorithm. Though no realistic attacks have been made public, experience with similar weaknesses in MD5 suggests that further advances may well lead to practical attacks within the next few years. This accords with current NIST guidance on DSA.

The impact of this weakness on Apache can be mitigated by action now. What needs to be done is a little involved, so we have provided complete instructions.

  - Committers without a code signing key should read this document and follow these [instructions](openpgp.html#generate-key).
  - Committers with a DSA key or an RSA key of length less than 2048 bits should generate a new key for signing releases. The original key does not need to be revoked yet. Follow this [guide](key-transition.html).
  - Committers with RSA keys of length 2048 or more do not need to generate a new key yet. They should reconfigure their client to avoid the weakness by following these [instructions](openpgp.html#sha1) and wait for the next major OpenPGP revision.

How to find the length of your key is described [here](#key-length-how-to).

<h3 id="basic-facts">The basics<a class="headerlink" href="#basic-facts" title="Permanent link">&para;</a></h3>

Every artifact distributed by the Apache Software Foundation  **must** be accompanied by one file containing an <a href="#openpgp-ascii-detach-sig">OpenPGP-compatible ASCII armored detached signature</a> and another file containing a <a href="release-signing#sha-checksum">SHA</a> or <a href="release-signing#md5">MD5</a>) checksum.

  - MD5 hashes are **deprecated**; please use SHA for new releases.
  - **Avoid** further use of `SHA-1`</code>.

Form the names of these files by adding to the name of the artifact the following suffixes:</p>

  - the signature by suffixing `.asc`
  - the checksum by suffixing `.md5` or `.sha[1|256|512]` (as appropriate)

Release managers **must not** store private keys used to sign Apache releases on ASF hardware. 

See the <a href="release-distribution.html#sigs-and-sums">release distribution policy</a> for details.

<h3 id="motivation">Why we sign releases<a class="headerlink" href="#motivation" title="Permanent link">&para;</a></h3>

A signature allows anyone to verify that a file is identical to the one your project's release manager created. Since your project's release has a signature:

  - users can make sure that what they received has not been modified in any way, either accidentally via a faulty transmission channel, or intentionally (with or without malicious intent).
  - the Apache infrastructure team can verify the identity of a file.

<a href="#openpgp">OpenPGP</a> <a href="#verifying-signature">signatures</a> confer the usual advantages of digital signatures: authentication, integrity and non-repudiation. <a href="#md5">MD5</a> and <a href="#sha-checksum">SHA</a> checksums only provide the integrity part as they are not encrypted.

<h3 id="security-basics">Security checklist<a class="headerlink" href="#security-basics" title="Permanent link">&para;</a></h3>

  - <a href="#private-key-protection">Protect</a> your <a href="#public-private">private key</a>
  - Choose a <a href="#passphrase">good passphrase</a>
  - Opt for a reasonably <a href="#key-length">long key length</a>

<h3 id="signing-basics">Signing basics<a class="headerlink" href="#signing-basics" title="Permanent link">&para;</a></h3>

  - Signatures should be <a href="#openpgp-ascii-detach-sig">ASCII armored and detached</a>.
  - You should <a href="#export">export</a> your <a href="#public-private">public key</a> and append the result to the appropriate <a href="#keys-policy">KEYS</a> file(s).

<h3 id="sign-release">How do I sign a release?<a class="headerlink" href="#sign-release" title="Permanent link">&para;</a></h3>

Create a <a href="#openpgp-ascii-detach-sig">OpenPGP compatible ASCII armored detached signature</a> for the released artifact. Upload the signature with the released artifact. See <a href="#basics">here</a> for a basic overview.

<h3 id="openpgp-ascii-detach-sig">What Is an OpenPGP compatible ASCII armored detached signature?<a class="headerlink" href="#openpgp-ascii-detach-sig" title="Permanent link">&para;</a></h3>

It is

  - an <a href="#openpgp">OpenPGP</a> compatible 
  - <a href="#ascii">ASCII armored</a> 
  - <a href="#detach-sig">detached signature</a>

To create one using <a href="https://www.gnupg.org" target="_blank">GNU Privacy Guard</a> for file
`foo.tar.gz`, type:

```
$ gpg --armor --output foo.tar.gz.asc --detach-sig foo.tar.gz 
```

<h3 id="md5">What is an MD5 checksum?<a class="headerlink" href="#md5" title="Permanent link">&para;</a></h3>

MD5 is a <a href="http://www.faqs.org/rfcs/rfc1321.html" target="_blank">well known</a>  <a href="#message-digest">message
digest algorithm</a>. Many tools are available to calculate these sums. For example, you can use <a href="https://www.openssl.org/" target="_blank">OpenSSL</a>:

```
$ openssl md5 < file
```

Platform-specific applications are also common, such as `md5sum` on linux:

```
$ md5sum file
```

With GnuPG:

```
$ gpg --print-md MD5 [fileName] > [fileName].md5

```

Run the command in the same directory as the file so the output only contains the file name with no directory prefixes.

**Note** that the security of MD5 is now <a href="#md5-security">questionable</a> and is only useful as part of a defense in depth.

<h3 id="sha-checksum">What is an SHA checksum?<a class="headerlink" href="#sha-checksum" title="Permanent link">&para;</a></h3>

Like <a href="#md5">MD5</a>, <a href="http://www.ietf.org/rfc/rfc3174.txt">SHA</a> is a <a href="#message-digest">message digest</a> algorithm. Using GnuPG, you can create a SHA1 signature as follows:

```
  $ gpg --print-md SHA1 [fileName] > [fileName].sha1
```

**Avoid** further use of <a href="#sha1">SHA-1</a>. `SHA256` and `SHA512` use the same `SHA` algorithm family with longer hash
lengths (256 and 512 bits respectively). These longer variations are less vulnerable to the weaknesses found in the algorithm family than `SHA1`. Apache recommends using <a href="#sha1">SHA512</a>.

To create a `SHA512` checksum use:

```
  $ sha512sum [fileName] > [fileName].sha512
```

Run the command in the same directory as the file so the output only contains the file name with no directory prefixes.

There are other members of the `SHA` family that are rarely used.

<h3 id="message-digest">Message digest algorithms<a class="headerlink" href="#message-digest" title="Permanent link">&para;</a></h3>

A message digest algorithm takes a document and produces a much smaller hash of that document. A good algorithm will produce different digests for very similar documents. A good algorithm makes it <a href="#infeasible">infeasible</a> to create a message matching a given hash.</p>

You can use a trusted digest for a document can be used to verify the contents of an untrusted file. You can deliver the digest, which has a small size over a secure but expensive channel while delivering the untrusted file over an insecure but inexpensive one. This is useful when distributing releases.

<h3 id="infeasible">Why infeasible and not impossible?<a class="headerlink" href="#infeasible" title="Permanent link">&para;</a></h3>

Responsible cryptography talks about infeasible cracks (rather than impossible ones) since this is more accurate. All current practical methods can be subjected to brute force attacks and so can be cracked. So a better question is whether attacks are feasible _given the current state of the art_.

<h3 id="openpgp-applications">Applications that create OpenPGP-compatible signatures<a class="headerlink" href="#openpgp-applications" title="Permanent link">&para;</a></h3>

Many applications are available (some commercial, some freeware, some software libre) to help you sign releases. Whichever one you choose, please subscribe to the appropriate security lists and keep the application fully patched.

Apache recommends that ASF release managers use <a href="https://www.gnupg.org" target="_blank">GNU Privacy Guard</a>.

<h3 id="where">Where should I create the signatures?<a class="headerlink" href="#where" title="Permanent link">&para;</a></h3>

Creating signatures requires the private key. Keep limited copies of the private key securely and confidentially. Though the file used
to store the private key is typically protected by encryption, it is vulnerable to dictionary attacks on the <a href="#passphrase">passphrase</a>. So keep this file secret. 

Create signatures on the machine where you store the private key, on secure hardware with limited read permissions, protected by a good
<a href="#passphrase">passphrase</a>. Consider using removable media or an <a href="#isolated-installation">isolated
installation</a>.

A master private key used to sign Apache artifacts (or to secure communications with the ASF) is particularly valuable. If you want or need to be able to create signatures for other purposes (for example, signing email messages) in other, less secure, locations, create multiple <a href="#email-subkey">sub keys</a> for these purposes.

Do **not** store your private key on any ASF machine. Do **not** create signatures on ASF machines.

<h3 id="insecure-memory">What is 'insecure memory'?<a class="headerlink" href="#insecure-memory" title="Permanent link">&para;</a></h3>

When you use <a href="http://www.gnupg.org">GNU Privacy Guard</a> you may see a warning similar to:

```
gpg: WARNING: using insecure memory!
gpg: please see http://www.gnupg.org/faq.html for more information
```

If you are using GnuPG on Apache hardware, please read <a href="#where">this</a>. Do **not** carry out sensitive operations using a private key on ASF hardware.

If you encounter this issue elsewhere, it indicates that GnuPG cannot lock memory pages, so they may be swapped out to disc. It would
then be feasible for an attacker who had gained access to the machine to read the private key from the swap file. For more details, read the <a href="https://www.gnupg.org/faq.html" target="_blank">FAQ</a>.</p>

<h3 id="secure-machine">How secure does the machine I use to sign releases need to be?<a class="headerlink" href="#secure-machine" title="Permanent link">&para;</a></h3>

If the code signing machine is <a href="http://www.catb.org/~esr/jargon/html/O/owned.html">owned</a>, it is only a matter of time before the key is compromised.

At a minimum, the machine should well maintained: kept up to date with security patches and with appropriate anti-virus and firewall software. The ideal is an isolated, well-maintained installation that you only use for creating releases. You can achieve this with a little effort by creating an <a href="#isolated-installation">isolated installation</a> on a separate hard disc (which is physically disconnected when not in use signing releases) or a live CD.

<h3 id="md5-security">Is MD5 still secure?<a class="headerlink" href="#md5-security" title="Permanent link">&para;</a></h3>

Though <a href="#infeasible">feasible</a> collision attacks that can defeat MD5 are known, they are still computationally expensive. MD5 may still be useful as an additional layer in a defense in depth, but Apache does **not recommend** it as your single security option.

<h3 id="sha1">Is SHA-1 still secure?<a class="headerlink" href="#sha1" title="Permanent link">&para;</a></h3>

Research has revealed weaknesses in this algorithm. Though there are no practical attacks known at the time of writing, experience with similar weaknesses in <a href="#md5-security">MD5</a> suggest that code signers should move away from this algorithm.

Breaking the longest members of this family (`SHA512` and `SHA256`) is still considered <a href="#infeasible">infeasible</a>. Until <a href="#sha3">SHA-3</a> is available, avoid new uses of `SHA-1` and use `SHA512` or `SHA256` instead.

<h4 id="sha3">What is SHA-3?<a class="headerlink" href="#sha3" title="Permanent link">&para;</a></h4>

SHA-3 is the designation for a new <a href="#message-digest">cryptographic hash algorithm</a> to replace the SHA family. The full standard was issued in 2015, but it hasn't yet been officially introduced into the OpenPGP standard. For that reason GnuPG doesn't support it yet.

<h3 id="secure-hash-algorithms">Which standard cryptographic hash algorithms are secure?<a class="headerlink" href="#secure-hash-algorithms" title="Permanent link">&para;</a></h3>

<a href="#infeasible">Feasible</a> - though expensive - attacks on MD5 have been made public. Similar weaknesses have been found in the SHA family of hashes, though practical attacks are not yet publicly known. However, longer hash sizes offer considerable protection, so larger members of the SHA family still look likely to be secure enough for a number of years.

SHA512 is the strongest well-studied, widely-used cryptographic hash. It is therefore the best recommendation until <a href="#sha3">SHA3</a> is available.</p>

<h3 id="generate">How to generate a code signing key<a class="headerlink" href="#generate" title="Permanent link">&para;</a></h3>

The exact mechanics are <a href="#openpgp-applications">application</a>-dependent. For GnuPG (recommended): 

  - Follow the <a href="openpgp.html#generate-key">strong key generation instructions</a>
  - Decide on the <a href="#key-length">right key length</a>
  - Configure the tool to <a href="#sha1">avoid SHA-1</a>
  - Choose a good <a href="#passphrase">passphrase</a>
  - Use the recommended <a href="#user-id">id</a> and <a href="#key-comment">comment</a>
  
<h3 id="user-id">The OpenPGP User-ID to use for your code-signing key<a class="headerlink" href="#user-id" title="Permanent link">&para;</a></h3>

We recommend that you use your Apache email address as the primary `User-ID` for the code signing key. For example, `rdonkin@apache.org`.

<h3 id="key-comment">The OpenPGP comment to choose for your code-signing key<a class="headerlink" href="#key-comment" title="Permanent link">&para;</a></h3>

The comment should include _CODE SIGNING KEY_. This makes clear the primary use for this key. This can be helpful if you later
generate keys for other uses.

Include the comment _NOT FOR CODE SIGNING_ for keys you generate for other purposes.

<h3 id="keyserver">What is a public key server?<a class="headerlink" href="#keyserver" title="Permanent link">&para;</a></h3>

A public key server manages <a href="#public-private">public keys</a>. Available functions may vary but typically include <a href="#keyserver-upload">upload</a>, search, and download.

Public key servers exist to distribute public keys. They do not vouch for the actual identity of the owner of each key. You must establish this either directly or through a <a href="#web-of-trust">web of trust</a>. Do not trust a key just because it has been downloaded from a key server.

The major public key servers synchronize their records regularly so you only need to upload a key to one and rely on that server to disseminate it to the other key servers. We recommend using <a href="https://keys.openpgp.org/" target="_blank">OpenPGP Public Key Server</a>.

<h3 id="keyserver-upload">How to upload a key to a public key server<a class="headerlink" href="#keyserver-upload" title="Permanent link">&para;</a></h3>

There are two common ways to upload a key to a <a href="#keyserver">public key server</a>:

  - Most key servers let you upload <a href="#export">exports</a> through their websites
  - Use automatic facilities built into most <a href="#openpgp">OpenPGP</a> <a href="#openpgp-applications">implementations</a>
  
For example, using <a href="https://www.gnupg.org" target="_blank">GNU Privacy Guard</a>, send the key with <a href="#key-id">ID</a> B1313DE2 to the default public key server by:

```
$ gpg --send-key B13131DE2
```

You must export each changed key separately.

<h3 id="update-web-of-trust">How to make sure your local web of trust is up-to-date<a class="headerlink" href="#update-web-of-trust" title="Permanent link">&para;</a></h3>

The public web of trust grows constantly as people sign new keys and upload the new signatures onto the network of <a href="#keyserver">public key servers</a>. You should refresh public keys periodically to make sure that your local web of trust is as full as possible. Many <a href="#openpgp">OpenPGP</a> <a href="#openpgp-applications">clients</a> make it easy to refresh keys by
querying a public key server. For example, to refresh all keys using <a href="https://www.gnupg.org" target="_blank">GNU Privacy Guard</a>, use:

```
$ gpg --refresh-keys
```

<h3 id="export">How to export a key</h3>

You can export a public key through <a href="https://www.gnupg.org" target="_blank">OpenPGP</a> by using
`--export`. Typically, the export should be ASCII armored. 

To export all public keys to the command line use:

```
gpg --export --armor
```

In most cases, it is better to export all keys - this ensures that signatures made on other keys will be exported. However, it is possible to export just one key by specifying it on the command line.

You can export secret keys. However, this poses a security risk and there are better solutions for most common use cases. For
example, copying the `GNUPGHOME` directory (typically `~/.gnupg`) is a better way to transfer an <a href="https://www.gnupg.org" target="_blank">OpenPGP</a> keyring from one machine to another.

<h3 id="key-id">What a key ID is<a class="headerlink" href="#key-id" title="Permanent link">&para;</a></h3>

A key ID is similar to a <a href="#fingerprint">fingerprint</a> but is much smaller in length. There is no guarantee that key IDs are unique. Consequently, we strongly recommend that you check the key's fingerprint before signing with it. People us key IDs for locating keys and identifying keys already contained within the keyring.

A short guide to discovering the key ID for a key is <a href="openpgp.html#find-key-id">available</a>.

<h3 id="subkey">What a sub key is<a class="headerlink" href="#subkey" title="Permanent link">&para;</a></h3>

Each <a href="#openpgp">OpenPGP</a> keyring has a single master key. This key is for signing only. It may also optionally have a number of sub keys for encryption and signing.

If you want to sign emails using a key related to one you use to sign code, we recommend that you use a signing <a href="#email-subkey">sub key</a>.

<h3 id="email-subkey">How to use a sub key to sign emails<a class="headerlink" href="#email-subkey" title="Permanent link">&para;</a></h3>

To keep a code signing key <a href="#safe-and-secure">safe and secure</a> we recommend that you don't keep the key on a drive on a regular development machine. This means that you should not use the master key directly to sign emails. However, there are occasions when digitally signed emails are desirable.

To do that, create a sub key for email signing and export it to your regular machine. You can then keep the master key safely
offline. For more details, read <a href="https://www.gnupg.org/(en)/faq/subkey-cross-certify.html" target="_blank">Subkey cross
certification</a>.

**Note** that some <a href="#keyserver">public key servers</a> do not handle sub keys correctly. It may be necessary to use one on the
<a href="https://bitbucket.org/skskeyserver/sks-keyserver/wiki/Home" target="_blank">SKS</a> network.

<h3 id="quick-signing">A quick way to sign several distributions<a class="headerlink" href="#quick-signing" title="Permanent link">&para;</a></h3>

The private `https://svn.apache.org/repos/private/committers` repository contains scripts that assist with batch signing several distributions at one time.

<h3 id="transfer-secret-keys">How to transfer a secret key<a class="headerlink" href="#transfer-secret-keys" title="Permanent link">&para;</a></h3>

The way to transfer secret keys depends on the application you are using. Instructions for GnuPG are <a href="openpgp.html#secret-key-transfer">available</a>.

<h3 id="two-keys">Why some people have two keys<a class="headerlink" href="#two-keys" title="Permanent link">&para;</a></h3>

When you switch from an uncompromised key to another, usually stronger, one, it is convenient to use a <a href="#transition">transition period</a>. During a transition, both keys are trustworthy but you only use the newer one to sign documents and certify links in the <a href="#web-of-trust">web of trust</a>.

<h3 id="transition">What a transition period for keys is<a class="headerlink" href="#transition" title="Permanent link">&para;</a></h3>

When you replace one uncompromised key with a newer and usually larger one, a transition period during which both keys are trustworthy and participate in the <a href="#web-of-trust">web of trust</a> allows - by <a href="#web-of-trust">trust transitivity</a> - links to the old key to be used to trust signatures and links created by the new key. During a transition, both keys are trustworthy but you only use the newer oneto sign documents and certify links in the <a href="#web-of-trust">web of trust</a>.

<h3 id="how-to-transition">How to transition from a short to a longer key<a class="headerlink" href="#how-to-transition" title="Permanent link">&para;</a></h3>

If you have a short but uncompromised key and would like to <a href="#transition">transition</a> to a longer one, follow these
<a href="key-transition.html">instructions</a>.

If your key has been compromised then you **must not** transition. <a href="#revoke-key">Revoke</a> the old key and replace it with a new one immediately. **Do not** use a transition period.

<h3 id="update-document">I have a new key. What Apache documents do I have to update?<a class="headerlink" href="#update-document" title="Permanent link">&para;</a></h3>

There are several Apache documents you have to update when you have a new key. Follow these <a href="openpgp.html#update">instructions</a>.

<h3 id="rsa">What RSA is<a class="headerlink" href="#rsa" title="Permanent link">&para;</a></h3>
<p>RSA is a well known public key cryptography algorithm which supports signing and encryption. See <a href="#reading">further reading</a> for more details.</p>

<h3 id="key-length-how-to">How to find the length of a key<a class="headerlink" href="#key-length-how-to" title="Permanent link">&para;</a></h3>

The easiest way to discover the length of a key with id `KEYID` is to use `gpg --list-keys KEYID`. This prints basic information about the key. The first line includes the size in the second column, just before the id.
For example:

```
$ gpg --list-keys B1313DE2
pub   1024D/B1313DE2 2003-01-15
uid                  Robert Burrell Donkin (CODE SIGNING KEY) <rdonkin@apache.org>
uid                  Robert Burrell Donkin <robertburrelldonkin@gmail.com>
uid                  Robert Burrell Donkin <robertburrelldonkin@blueyonder.co.uk>
sub   4096R/40A882CB 2009-06-18 [expires: 2010-06-18]</p>

$ gpg --list-keys A6EE6908
pub   8192R/A6EE6908 2009-08-07
uid                  Robert Burrell Donkin (CODE SIGNING KEY) <rdonkin@apache.org>
sub   8192R/B800EFC1 2009-08-07
```

shows that key `B1313DE2` has length 1024 and `A6EE6908` length 8192.


<h2 id="key-basics">Key basics<a class="headerlink" href="#key-basics" title="Permanent link">&para;</a></h2>

To sign releases, you need to <a href="#generate">generate</a> a new master key-pair for code signing. Follow these <a href="openpgp.html#generate-key" target="_blank">instructions</a>.

<h3 id="keys-policy">The KEYS File<a class="headerlink" href="#keys-policy" title="Permanent link">&para;</a></h3>

The KEYS file is a plain-text file containing the public key signatures of the release managers (and optionally other committers) for the project. A good example is the <a href="https://downloads.apache.org/ant/KEYS" target="_blank">Apache Ant KEYS file</a>. 

It is traditional to include the following header to explain how to use the file. These commands generate a descriptive comment describing the key, followed by the key itself. Key handling software ignores the comments when importing a key file:

```
This file contains the PGP keys of various developers.</p>
Users: pgp < KEYS
or
       gpg --import KEYS
       
Developers: 
    pgp -kxa <your name> and append it to this file.
or
    (pgpk -ll <your name> && pgpk -xa <your name>) >> this file.
or
    (gpg --list-sigs <your name> && gpg --armor --export <your name>) >> this file.
```

Store the KEYS file with the release archives to which it applies at the top level of the ASF mirror area for the project. This makes it  available for users to download, and for automatic archiving with its release. For example, the Ant KEYS file is in the directory `https://downloads.apache.org/ant`. The corresponding SVN area is at `https://dist.apache.org/repos/dist/release/ant`.

Since users may need the KEYS file to check signatures for archived releases, it is important to retain in the file all keys that have ever been used to sign releases. Add entries with eadch new key the project uses, but do not remove entries.

<a href="#pke">Applied cryptography</a> is a subject that has considerable depth. Luckily, it's possible to get started signing releases without being an expert. Just remember that you will encounter some situations that require research and learning. We hope the
<a href="#faq">FAQ</a> will be a reasonable first port of call.

You need an <a href="#openpgp-applications">application</a> to manage keys and create signatures. We recommend <a href="http://www.gnupg.org/">GNU Privacy Guard</a>, and the Apache documentation generally assumes that's what
you're using. (We welcome contributions that document use of other tools.) Read the <a href="openpgp.html#gnupg">Apache PGP user guide</a> and keep the <a href="https://www.gnupg.org/gph/en/manual.html" target="_blank">manual</a> handy. 

GnuPG can handle MD5 and SHA checksums as well as PGP signatures. It is your all-in-one cross-platform tool for release signing and verification.

**Note:** It can be hard for newbies to be confident that they have executed operations correctly. Consider doing some <a href="#safe-practice">practice</a> before you try to sign an actual release.

<h3 id="openpgp">What is OpenPGP?<a class="headerlink" href="#openpgp" title="Permanent link">&para;</a></h3>
[OpenPGP](openpgp.html) is an <a href="http://www.ietf.org/rfc/rfc2440.txt" target="_blank">RFC</a> describing a system for interoperable <a href="#pke">public key cryptography</a>. Various implementations exist. Apache recommends <a href="https://www.gnupg.org/" target="_blank">GNU Privacy Guard</a> (GnuPG), an open-source, OpenPGP compatible implementation. It comes with <a href="https://www.gnupg.org/(en)/documentation/guides.html" target="_blank">good documentation</a> that describes GnuPG and gives a good general introduction to public key cryptography.

<h3 id="pke">What is public key cryptography?<a class="headerlink" href="#pke" title="Permanent link">&para;</a></h3>
Public key cryptography is asymmetric. You use one key to encrypt a message which only the other key can decrypt. You can share the first key publicly without compromising the security of the second key. One key is therefore called the _public key_ and one the _private key_.

When you use public key cryptography, you can freely distribute the public key, but you must keep the private key secret. It is vital to <a href="#private-key-protection">protect</a> private key files.. Private keys are typically stored in files protected by symmetric encryption. Choose a strong <a href="#passphrase">passphrase</a> to protect the file.</p>

<h3 id="detach-sig">What is a detached signature?<a class="headerlink" href="#detach-sig" title="Permanent link">&para;</a></h3>

You create a digital signature from an original document using a <a href="#pke">private key</a>. Possession of the corresponding public key allows verification that a given file is identical to the original document. An _attached signature_ is attached to the document whereas a _detached signature_ is contained in a separate file.

<h3 id="ascii">What is ASCII armoring?<a class="headerlink" href="#ascii" title="Permanent link">&para;</a></h3>

ASCII armoring is an encoding format that converts a binary file into a string of ASCII characters. This format is more human readable and more portable than other formats.

<h2 id="safe-practice">How can I safely practice using OpenPGP?<a class="headerlink" href="#safe-practice" title="Permanent link">&para;</a></h2>

To practice using OpenPGP, use separate environments. each with a different practice keyring.

For example, using <a href="http://www.gnupg.org" target="_blank">GNU Privacy Guard</a>:

  - (First time only)Create a directory to contain the keyring
  - Open the shell to be configured to use this keyring
  - Change to the directory
  - (First time only) `$ mkdir -m 700 .gnupg`
  - Set up the environment: `export GNUPGHOME=.gnupg`

<h2 id="web-of-trust">What is a Web Of Trust?<a class="headerlink" href="#web-of-trust" title="Permanent link">&para;</a></h2>

It is difficult to personally verify the identity of all useful <a href="#pke">public keys</a>. However, having verified the identity of only a small number of public keys it is possible to deduce the identity of public keys trusted by the owners of these keys. This process can be repeated. This extended graph of trusted identities is termed a <a href="http://en.wikipedia.org/wiki/Web_of_trust" target="_blank">>web of trust</a>.

You can use webs of trust to solve the problem of verifying the identity of public keys.

**Note:** to take full advantage of a web of trust, it is important to actively build your personal web of trust into the major public webs of trust. Conferences are an ideal opportunity for exchanging key information, but you must come <a href="#link-into-wot">prepared</a>. 

For more information read the <a href="https://www.gnupg.org/(en)/documentation/guides.html" target="_blank">GNU Privacy Handbook</a>.

<h3 id="link-into-wot">How do I link into a public web of trust?<a class="headerlink" href="#link-into-wot" title="Permanent link">&para;</a></h3>

You join a web of trust when an existing member of that web signs your public key to verify your identity. See <a href="openpgp.html#wot">a short explanation</a>.

<h3 id="key-signing-party">What is a key-signing party?<a class="headerlink" href="#key-signing-party" title="Permanent link">&para;</a></h3>

A key signing party is a meeting organised to allow the exchange of public keys to extend the <a href="#web-of-trust">web of trust</a>. See the <a href="https://www.cryptnet.net/fdp/crypto/keysigning_party/en/keysigning_party.html" target="_blank">Keysigning Party HOWTO</a>.

<h3 id="apache-wot">How can I link my key into the Apache Web of Trust?<a class="headerlink" href="#apache-wot" title="Permanent link">&para;</a></h3>

You can link into the Apache web of trust by meeting other Apache committers face-to-face and <a href="#link-into-wot">exchanging public
keys</a>:

  - Apache committers organizes <a href="#key-signing-party">key signing parties</a> at each <a href="https://www.apachecon.com" target="_blank">ApacheCon</a>.
  - If you are not able to attend ApacheCon, or it will not happen for several months, consider organising a face-to-face meeting of <a href="https://people.apache.org/map.html" target="_blank">local committers</a>.

Subscribe to the `party` list and when you visit a new city, see if committers want to meet up.

<h3 id="public-private">The difference between a public and a private key<a class="headerlink" href="#public-private" title="Permanent link">&para;</a></h3>

A public key is for verifying signatures and encrypting messages; a private key is for generating signatures and decrypting messages. You can freely distribute public keys safely , but you must keep private keys <a href="#safe-and-secure">protected</a>. More details <a href="#pke">here</a>.

<h3 id="private-key-protection">How to protect your code signing private key<a class="headerlink" href="#private-key-protection" title="Permanent link">&para;</a></h3>

Anyone who possesses a copy of a <a href="#public-private">private key</a> used to <a href="#sign-release">sign</a> releases can create doctored releases with valid signatures. If this person intends harm then the consequences could be serious indeed. It is therefore very important to keep the private key secret.

  - Only sign releases on a <a href="#secure-machine">secure machine</a>.
  - Keep your <a href="#openpgp-applications">signing application</a> fully patched.
  - Keep the key file <a href="#safe-and-secure">safe and secret</a>.
  - Choose a good <a href="#passphrase">passphrase</a>.
  
<h3 id="safe-and-secure">How safe does the private key need to be?<a class="headerlink" href="#safe-and-secure" title="Permanent link">&para;</a></h3>

It is vital that the private key is kept safe and secure. Though the file is encrypted using a <a href="#passphrase">passphrase</a> , given enough time any determined cracker will be able to break that encryption. Basic precautions should include ensuring that only the user can read the directories.

However, for code signing keys we recommend taking additional measures. Reduce the window of vulnerability by using an
<a href="#isolated-installation">isolated installation</a> or by storing the private key on removable media (which you should remove and store securely when not actually signing a release.).


<h3 id="isolated-installation">The meaning of 'isolated installation'<a class="headerlink" href="#isolated-installation" title="Permanent link">&para;</a></h3>

An isolated installation is inaccessible when you are not using it to sign releases. For example, create an installation on a separate hard disc or use a live CD.

<h3 id="key-length">Recommended key length<a class="headerlink" href="#key-length" title="Permanent link">&para;</a></h3>

The number of operations required to break a key by brute force increases with key size. However, the cost of using the key also rises. You must take into account the planned use of the key. You will use keys for code signing rarely and in situations where performance is not the main concern, so you can use long keys.

Over time, the cost of attacking a key of a given length by brute force falls as computing power increases. So a key whose length
seems adequate today may be seem too short in a few years time. This is a significant issue for long-lived keys such as those used to sign ASF releases, and another reason to use longer keys with releases.

<p>Now that there is doubt about the medium term security of <a href="#sha1">SHA-1</a>, avoid the DSA keys and 1024 bit RSA keys which depend on this algorithm. We recommended that new keys be at least 4096 bit RSA (the longest widely supported key length).</p>

<h2 id="passphrase">What is a Passphrase?<a class="headerlink" href="#passphrase" title="Permanent link">&para;</a></h2>

In cryptography <em>passphrase</em> is often used for what might be known as a password in other contexts. For example, an
<a href="#openpgp">OpenPGP</a> private key is typically stored to disc in a file encrypted by a symmetric cypher keyed by a passphrase. This passphrase is one of the weakest elements in the system: should anyone else gain access to the file then a dictionary attack will be feasible on a weak passphrase. So choosing a strong passphrase is very important.

Passphrases, unlike passwords, are typically unlimited in length. We recommend using long passphrases. You can use sequences of (at least seven) unrelated words or more conventional mixtures of symbols and alphanumerics.

Even a good passphrase offers only limited protection. Given the encrypted file and enough time, a determined cracker will be able to
break any passphrase. A good passphrase will buy important time in the event of a compromise, but is no substitute for keeping the private key <a href="#safe-and-secure">safe and secure</a> in the first place.

<h2 id="revocation-cert">Revocation Certificate basics<a class="headerlink" href="#revocation-cert" title="Permanent link">&para;</a></h2>

<a href="#openpgp">OpenPGP</a> defines a special type of signed message called a **revocation certificate**. This message indicates that the signer believes that the key is no longer trustworthy. Typically, the revocation certificate will be signed by the key to be revoked (though the key may specify that other keys should be trusted for revocation). Use the type of revocation and the comment included to judge how much trust to place in a good signature by a revoked key.

You should generate a revocation certificate for each public key you use. Store the revocation certificates safely, securely and separately from their public keys.

Each revocation certificate has a type specifying a general (machine readable) reason for the revocation:

  - No reason specified
  - Key has been compromised
  - Key is superseded
  - Key is no longer used
  
Create certificates to cover the first two cases. Note that if a key is lost or can no longer be accessed (due to
media failure or some other reason), assume that the key has been potentially compromised. Print copies of the revocation certificates and store them safely to guard against media failure.

You can generate an <a href="#ascii">ASCII armored</a> revocation certificate for key `bob` and save it to `revoke.asc` using <a href="https://www.gnupg.org" target="_blank:>GNU Privacy Guard</a>:

```
$ gpg --output revoke.asc --armor --gen-revoke bob
```

<a href="#revocation-certificate-storage">Securely store</a> the certificate.

If you are preparing a revocation certificate for future use, you should test it before storing it. See <a href="#safe-practice">safe practice.

<h3 id="revoke-key">Revoking a key<a class="headerlink" href="#revoke-key" title="Permanent link">&para;</a></h3>

To revoke a key with a <a href="#revocation-cert">revocation certificate</a> using <a href="https://www.gnupg.org" target="_blank">GNU Privacy Guard</a>, import the certificate:

```
$ gpg --import revoke.asc 
gpg: key 4A03679A: "Some User<someuser@example.org>" revocation
certificate imported
gpg: Total number processed: 1
gpg:    new key revocations: 1
```

<h3 id="revocation-certificate-storage">Where to store revocation certificates<a class="headerlink" href="#revocation-certificate-storage" title="Permanent link">&para;</a></h3>

Store each revocation certificate securely and separately from the key it revokes. Burning the certificate onto a CDROM or printing it out as a hard copy are good solutions.

<h3 id="revoke-cert">Distributing a revocation certificate<a class="headerlink" href="#revoke-cert" title="Permanent link">&para;</a></h3>

If a key has been compromised, distribute its <a href="#revocation-cert">revocation certificate</a> to those using the key. This process is a mirror of the process by which you distributred the original key.

  - Inform the Apache infrastructure team by a post containing the revocation certificate.
  - Update the KEYS files containing the original key with the revocation certificate.
  - Upload the revocation certificate to the major keyserver networks.
  - Post an announcement to the appropriate lists with the revocation certificate attached.

<h3 id="delete-vs-revoke">The difference between deleting and revoking a key<a class="headerlink" href="#delete-vs-revoke" title="Permanent link">&para;</a></h3>

When you _delete_ a key from a keyring, it is simply removed. You can add it again later.

When you _revoke_ a key, it is marked in the key ring. Whenever a message signed by this key is verified in the future, the user will get a warning that the key has been revoked.

For example, when you verify a revoked key, <a href="https://www.gnupg.org" target="_blank" target="_blank">GNU Privacy Guard</a> issues the following comment:

```
$ gpg --verify message.asc.message 
gpg: Signature made Sat Apr  8 09:28:31 2006 BST using DSA key ID 4A03679A
gpg: Good signature from "Some User <someuser@example.org>"
gpg: checking the trustdb
gpg: checking at depth 0 signed=0 ot(-/q/n/m/f/u)=0/0/0/0/0/1
gpg: WARNING: This key has been revoked by its owner!
gpg:          This could mean that the signature is forgery.
gpg: reason for revocation: Key has been compromised
gpg: revocation comment: 
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the
owner.
Primary key fingerprint: 82D1 169B E6F1 9D14 DA76  A5DD 968E 66E4 4A03 679A
```


<h2>FAQs from those downloading releases</h2>

<h3 id="verifying-signature">What does verifying a signature mean?<a class="headerlink" href="#verifying-signature" title="Permanent link">&para;</a></h3>

You can use <a href="#pke">public key cryptography</a> to test whether a particular file is identical in content to an original by verifying a <a href="#detach-sig">signature</a>. The signature file is a <a href="#message-digest">digest</a> of the original file signed by a private key which attests to the digest's authenticity.

For example, when using <a href="https://www.gnupg.org/" target="_blank">GNU Privacy Guard</a> you verify the signature `foo-1.0.tar.gz.asc` for release `foo-1.0.tar.gz` using the following command:

```
$ gpg --verify foo-1.0.tar.gz.asc foo-1.0.tar.gz
```

A signature is valid, if `gpg` verifies the `.asc` as a _good signature_, and doesn't complain about expired
or revoked keys. Technically :

```
$ gpg --verify --status-fd 1 foo-1.0.tar.gz.asc foo-1.0.tar.gz
```

should classify the `.asc` as a `GOODSIG`.

Trust is required in the identity of the public key that made the signature and that the signature is for the original file and not some other file. When verifying a release from an untrusted source (for example, over P2P file sharing or from a mirror) it is important to download the signature from a trusted source. Signatures for all Apache releases are available directly for download from `www.apache.org`.

<h3 id="check-integrity">How can I check the integrity of a release?<a class="headerlink" href="#check-integrity" title="Permanent link">&para;</a></h3>
  
<a href="#md5">MD5</a> and <a href="#sha-checksum">SHA</a> checksums provide a simple way to verify the integrity of a download. You can simply create a checksum (in the same way as the release manager) after download, and compare the result to the checksum downloaded from the main Apache site. However, this process does not provide for authentication and non-repudiation</a> as anybody can create the same checksum.

You can also check the integrity of a release by <a href="#verifying-signature">verifying the signature</a>. You need more knowledge to correctly interpret the result, but it does provide authentication and non-repudiation. If you are connected to the Apache <a href="#web-of-trust">web of trust</a>, this also offers superior security.

<h3 id="public-key-not-found">What does 'Public key not found' mean when I try to verify a signature?<a class="headerlink" href="#public-key-not-found" title="Permanent link">&para;</a></h3>
To verify a signature, you need the release's public key. For example, when using <a href="https://www.gnupg.org/" target="_blank">GNU Privacy Guard</a>, if you have never imported the appropriate public key, you will see a message like this:

```
$ gpg --verify foo-1.0.tar.gz.asc foo-1.0.tar.gz
gpg: Signature made Mon Sep 26 22:26:18 2005 BST using RSA key ID 00000000
gpg: Can't check signature: public key not found
```

You can often download unknown keys from a <a href="#keyserver">public key servers</a>. However, only rely on these if you can confirm them through your <a href="#web-of-trust">web of trust</a>.

Apache projects normally keep the developers' public keys in a file called `KEYS`. You may be able to find that file on the project's website, or in their code repository. Use

```
  $ gpg --import KEYS
```

to import the public keys.</p>

<h3 id="trust">What is a trusted key?<a class="headerlink" href="#trust" title="Permanent link">&para;</a></h3>

<a href="#openpgp">OpenPGP</a> uses a <a href="#web-of-trust">web of trust</a>. The owner of a public key who trusts the identity of a second key may mark this key as trusted by signing it. This has several major effects:

  - In future, no <a href="#valid-untrusted-vs-invalid-trusted">untrusted key warning</a> appears when a valid signature for
this key is verified.
  - Keys the owner of the key trusts may also become trusted. In other words, if the owner of a key whose identity you trust confirms the identity of a key, that key may be automatically trusted. This behavior is typically configurable.
   - The next time you export your key, those who trust your key may start to trust the identity of the trusted key.

The transitive nature of the web of trust places a responsibility on the owner to verify the identity of the owner of those keys marked as trusted.

For more information read the <a href="https://www.gnupg.org/(en)/documentation/guides.html" target="_blank">GNU Privacy Guard User
Guide</a>.

<h3 id="valid-untrusted-vs-invalid-trusted">What is the difference between a valid signature from an untrusted key an invalid signature from a trusted key?<a class="headerlink" href="#valid-untrusted-vs-invalid-trusted" title="Permanent link">&para;</a></h3>

Trustfulness and validity are different concepts. You may elect to trust the identity of a key to various degrees (or not at all). For a particular key, a particular signature for a particular file may be valid (created by the private key from an identical file) or invalid
(either corrupt or created from a different file).

Do not trust a file with an invalid signature. You can trust a file with a valid signature as much as you trust the identity of the key that was used to verify the signature.

For example, when you use <a href="https://www.gnupg.org/" target="_blank">GNU Privacy Guard</a>, a message similar to the following indicates that the signature is invalid:

```
$ gpg --verify foo-1.0.tar.gz.asc foo-1.0.tar.gz
gpg: Signature made Mon Sep 26 22:26:18 2005 BST using RSA key ID 00000000
gpg: BAD signature from "someone@example.org"
```

A message similar to the following indicates that the signature is valid but for an untrusted key:

```
$ gpg --verify foo-1.0.tar.gz.asc foo-1.0.tar.gz
gpg: Signature made Mon Sep 26 22:05:28 2005 BST using RSA key ID 00000000
gpg: Good signature from "someone@example.org"
gpg:                 aka "someone@anotherdomain.org"
gpg: checking the trustdb
gpg: checking at depth 0 signed=1 ot(-/q/n/m/f/u)=0/0/0/0/0/1
gpg: checking at depth 1 signed=0 ot(-/q/n/m/f/u)=1/0/0/0/0/0
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the
owner.
Primary key fingerprint: 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00
```

You can use the <a href="#fingerprint">fingerprint</a> to decide how much trust to assign to the key.

<h3 id="fingerprint">What is a public key fingerprint?<a class="headerlink" href="#fingerprint" title="Permanent link">&para;</a></h3>

Public keys are long and even when <a href="#ascii">ASCII armored</a> are not very easy for humans to understand or compare. A fingerprint is a short <a href="#message-digest">digest</a> of the key formatted in a way that makes it easier for humans to read and compare.

<h3 id="local-sig">Can I mark a key as locally trusted?<a class="headerlink" href="#local-sig" title="Permanent link">&para;</a></h3>

On occasion, the user (who understands the risks) may trust a key but not consider it trustworthy enough to exported to the <a href="#web-of-trust">web of trust</a>. <a href="#openpgp">OpenPGP</a> lets you sign keys as local only. These trust relationships will not be exported to the public web of trust but are treated as trusted when you use the key ring locally.

For example, with <a href="https://www.gnupg.org" target="_blank">GNU Privacy Guard</a> use:

```
$ gpg --lsign-key someuser
```

<h3 id="automated-release-signing">Automated Release Signing<a class="headerlink" href="#automated-release-signing" title="Permanent link">&para;</a></h3>

Projects may make use of automated signing for artifacts built by a CI system such as GitHub Actions, provided that:

- All artifacts being signed can be built <a href="https://reproducible-builds.org" target="_blank">reproducibly</a>
- CI deploys the artifacts to a staging environment
- The release procedure contains a validation step where all artifacts are reproduced on <a href="https://www.apache.org/legal/release-policy.html#owned-controlled-hardware" target="_blank">trusted hardware</a> before publication to pages intended for end users

The project must request a signing key through an Infra Jira ticket, and Infra will provide a signing key for the project:

- The key will be 4096 bit RSA
- It will be a signing-only key
- Infra will put a PGP-encrypted revocation key in the project's private svn/git dir
- The private key will never be shared with the project or anyone outside of the infra-root team, but will be available to the chosen CI system
- The public key will be sent to the project or added to their KEYS file

The Apache Security Team should be notified of any pending requests for CI signing keys, and should approve the workflow before it is being put into use.
See <a href="https://issues.apache.org/jira/browse/INFRA-23996" target="_blank">INFRA-23996</a> for background on this.


<h2 id="reading">Further reading<a class="headerlink" href="#reading" title="Permanent link">&para;</a></h2>

There are many other excellent resources on signing releases, but these make a good start:

  - The <a href="openpgp.html#gnupg">Guide to using GnuPG</a> at Apache
  - The <a href="key-transition.html">Apache Key Transition Guide</a>
  - RFC <a href="http://www.ietf.org/rfc/rfc1321.txt" target="_blank">1321</a> MD5 message-digest algorithm
  - RFC <a href="http://www.ietf.org/rfc/rfc2440.txt">2440</a> OpenPGP message format
  - The GNU Privacy Guard project <a href="https://www.gnupg.org/documentation/" target="_blank">documentation</a>
  - An introduction to <a href="https://www.pgpi.org/doc/pgpintro/" target="_blank">PGP public key cryptography</a>
  - <a href="https://www.schneier.com/book-applied.html" target="_blank">Applied Cryptography</a> by Bruce Schneier
  - Windows-centric <a href="http://www.mccune.cc/PGPpage2.htm" target="_blank">PGP FAQ</a> by Tom McCune</p>
