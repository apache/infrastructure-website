Title: Signing Releases

<h2 id="abstract">Abstract</h2>

This document gives release managers a basic introduction to release signing. See under [Further reading](#reading) for links to
authoritative sources of deeper information.

This document is informative and does not constitute policy.

<h2>Contents</h2>

<ul>
<li><a href="#abstract">Abstract</a></li>
<li><a href="#note">Important notes</a></li>
<li><a href="#basic-facts">Basic facts</a></li>
<li><a href="#keys-policy">The KEYS File</a></li>
<li><a href="#motivation">Why We Sign Releases</a></li>
<li><a href="#security-basics">Security Basics</a></li>
<li><a href="#key-basics">Key Basics</a></li>
<li><a href="#signing-basics">Signing Basics</a></li>
<li><a href="#sign-release">How Do I Sign A Release?</a></li>
<li><a href="#openpgp-ascii-detach-sig">What Is an OpenPGP Compatible ASCII Armored Detached Signature?</a></li>
<li><a href="#openpgp">What Is OpenPGP?</a></li>
<li><a href="#pke">What Is Public Key Cryptography?</a></li>
<li><a href="#detach-sig">What Is An Detached Signature?</a></li>
<li><a href="#ascii">What Is ASCII Armoring?</a></li>
<li><a href="#md5">What Is An MD5 Checksum?</a></li>
<li><a href="#sha-checksum">What is a SHA checksum?</a></li>
<li><a href="#message-digest">What Is A Message Digest Algorithm?</a></li>
<li><a href="#web-of-trust">What Is A Web Of Trust?</a></li>
<li><a href="#link-into-wot">How Do I Link Into A Public Web of Trust?</a></li>
<li><a href="#key-signing-party">What Is A Key Signing Party?</a></li>
<li><a href="#apache-wot">How Can I Link My Key Into The Apache Web of Trust?</a></li>
<li><a href="#verifying-signature">What Does Verifying A Signature Mean?</a></li>
<li><a href="#check-integrity">How Can I Check The Integrity Of A Release?</a></li>
<li><a href="#public-key-not-found">What Does 'Public Key Not Found' Mean (When Verifying A Signature)?</a></li>
<li><a href="#trust">What is a Trusted Key?</a></li>
<li><a href="#valid-untrusted-vs-invalid-trusted">What Is The Difference Between A Valid Signature from an Untrusted Key And An Invalid Signature from an Untrusted Key?</a></li>
<li><a href="#fingerprint">What Is A Public Key Fingerprint?</a></li>
<li><a href="#infeasible">Why Infeasible And Not Impossible?</a></li>
<li><a href="#where">Where Should I Create The Signatures?</a></li>
<li><a href="#insecure-memory">What Is 'Insecure Memory' And Should I Be Worried?</a></li>
<li><a href="#passphrase">What is a Passphrase?</a></li>
<li><a href="#revocation-cert">What Is A Revocation Certificate?</a></li>
<li><a href="#revoke-key">How Do I Revoke A Key?</a></li>
<li><a href="#revocation-certificate-storage">Where Should A Revocation Certificate Be Stored?</a></li>
<li><a href="#revoke-cert">How Do I Distribute A Revocation Certificate?</a></li>
<li><a href="#delete-vs-revoke">What Is The Difference Between Deleting And Revoking A Key?</a></li>
<li><a href="#local-sig">Can I Mark A Key As Locally Trusted?</a></li>
<li><a href="#safe-practice">How Can I Safely Practice Using OpenPGP?</a></li>
<li><a href="#public-private">What Is The Difference Between A Public And A Private Key?</a></li>
<li><a href="#private-key-protection">How Should My Code Signing Private Key Be Protected?</a></li>
<li><a href="#secure-machine">How Secure Does The Machine Used To Sign Releases Need To Be?</a></li>
<li><a href="#openpgp-applications">Which Applications Create OpenPGP Compatible Signatures?</a></li>
<li><a href="#safe-and-secure">How Safe Does The Private Key Need To Be?</a></li>
<li><a href="#isolated-installation">What Does 'Isolated Installation' Mean?</a></li>
<li><a href="#key-length">What Key Length Is Recommended?</a></li>
<li><a href="#md5-security">Is MD5 Still Secure?</a></li>
<li><a href="#sha1">Is SHA-1 Still Secure?</a></li>
<li><a href="#sha3">What is SHA-3?</a></li>
<li><a href="#secure-hash-algorithms">Which Standard Crytographic Hash Algorithms Are Secure?</a></li>
<li><a href="#generate">How Do You Generate A Code Signing Key?</a></li>
<li><a href="#user-id">What OpenPGP User-ID Should I Choose For My Code Signing Key?</a></li>
<li><a href="#key-comment">What OpenPGP Comment Should I Choose For My Code Signing Key?</a></li>
<li><a href="#keyserver">What Is A Public Key Server?</a></li>
<li><a href="#keyserver-upload">How Do You Upload A Key To A Public Key Server?</a></li>
<li><a href="#update-web-of-trust">How Can I Ensure My Local Web Of Trust Is Up To Date?</a></li>
<li><a href="#export">How Do You Export A Key?</a></li>
<li><a href="#key-id">What Is A Key ID?</a></li>
<li><a href="#subkey">What Is A Sub Key?</a></li>
<li><a href="#email-subkey">How Do I A Use Sub Key To Sign Emails?</a></li>
<li><a href="#more-information">How Can I Find Out More?</a></li>
<li><a href="#quick-signing">Is There A Quick Way To Sign Several Distributions?</a></li>
<li><a href="#transfer-secret-keys">How Can I Transfer A Secret Key?</a></li>
<li><a href="#two-keys">Why Do Some People Have Two Keys?</a></li>
<li><a href="#transition">What Is A Transition Period (For Keys)?</a></li>
<li><a href="#how-to-transition">How Should I Transition From A Short To A Longer Key?</a></li>
<li><a href="#update-document">I Have A New Key. Which Apache Documents Need To Be Updated?</a></li>
<li><a href="#rsa">What Is RSA?</a></li>
<li><a href="#key-length-how-to">How Do I Find The Length Of A Key?</a></li>
<li><a href="#help">Help Wanted!</a></li>
<li><a href="#reading">Further Reading</a></li>
</ul>

<h2 id="note">Important notes</h2>

All new **RSA** keys generated should be at least **4096** bits. **Do not** generate new **DSA** keys.

Recent research has revealed weaknesses in SHA-1, and thus in the DSA and 1024 bit RSA OpenPGP keys which must use this algorithm. Though no realistic attacks have been made public, experience with similar weaknesses in MD5 suggests that further advances may well lead to practical attacks within the next few years. This accords with current NIST guidance on DSA.

The impact of this weakness on Apache can be mitigated by action now. What needs to be done is a little involved, so we have provided complete instructions.

  - Committers without a code signing key should read this document and follow these [instructions](openpgp.html#generate-key).
  - Committers with a DSA key or an RSA key of length less than 2048 bits should generate a new key for signing releases. The original key does not need to be revoked yet. Follow this [guide](key-transition.html).
  - Committers with RSA keys of length 2048 or more do not need to generate a new key yet. They should reconfigure their client to avoid the weakness by following these [instructions](openpgp.html#sha1) and wait for the next major OpenPGP revision.

How to find the length of your key is described [here](#key-length-how-to).

<h2 id="basic-facts">Basic facts</h2>

Every artifact distributed by the Apache Software Foundation  **must** be accompanied by one file containing an <a href="#openpgp-ascii-detach-sig">OpenPGP-compatible ASCII armored detached signature</a> and another file containing a <a href="release-signing#sha-checksum">SHA</a> or <a href="release-signing#md5">MD5</a>) checksum.

  - MD5 hashes are **deprecated**; please use SHA for new releases.
  - **Avoid** further use of `SHA-1`</code>.

Form the names of these files by adding to the name of the artifact the following suffixes:</p>

  - the signature by suffixing `.asc`
  - the checksum by suffixing `.md5` or `.sha[1|256|512]` (as appropriate)

Release managers **must not** store private keys used to sign Apache releases on ASF hardware. 

See the <a href="release-distribution.html#sigs-and-sums">release distribution policy</a> for details.

<h2 id="keys-policy">The KEYS File</h2>

The KEYS file is a plain-text file containing the public key signatures of the release managers (and optionally other committers) for the project. A good example is the <a href="https://downloads.apache.org/ant/KEYS" target="_blank">Apache Ant KEYS file</a>. 

It is traditional to include the following header to explain how to use the file. These commands generate a descriptive comment describing the key, followed by the key itself. Key handling software ignores the comments when importing a key file:

```
This file contains the PGP keys of various developers.</p>
<p>Users: pgp &lt; KEYS
or
       gpg --import KEYS</p>
<p>Developers: 
    pgp -kxa &lt;your name&gt; and append it to this file.
or
    (pgpk -ll &lt;your name&gt; &amp;&amp; pgpk -xa &lt;your name&gt;) &gt;&gt; this file.
or
    (gpg --list-sigs &lt;your name&gt;
    &amp;&amp; gpg --armor --export &lt;your name&gt;) &gt;&gt; this file.
```


Store the KEYS file with the release archives to which it applies at the top level of the ASF mirror area for the project. This makes it  available for users to download, and for automatic archiving with its release. For example, the Ant KEYS file is in the directory `https://downloads.apache.org/ant`. The corresponding SVN area is at `https://dist.apache.org/repos/dist/release/ant`

Since users may need the KEYS file to check signatures for archived releases, it is important to retain in the file all keys that have ever been used to sign releases. Add entries with eadch new key the project uses, but do not remove entries.

<p><strong>Note:</strong> this system will be replaced by a better process in the near future. In preparation, please ensure that public keys are connected as strongly as possible to the Apache <a href="#web-of-trust">web of trust</a> and are
available from the major <a href="#keyserver">public key servers</a>.</p>
<p><a href="#pke">Applied cryptography</a> is a subject that has considerable depth.
Luckily, it's possible to get started signing releases without being an
expert. Just remember that (from time to time) you will encounter
situations that will require research and learning. Hopefully the
<a href="#faq">FAQ</a> will be a reasonable first port of call.</p>
<p>You will need an <a href="#openpgp-applications">application</a> to manage keys and
create signatures. <a href="http://www.gnupg.org/">GNU Privacy Guard</a> is
recommended and the Apache documentation generally assumes that's what
you're using. (Documentation patches for other tools welcomed.) Read the
<a href="openpgp.html#gnupg">Apache usage guide</a> and keep the
<a href="http://www.gnupg.org/gph/en/manual.html">manual</a> handy. Note that GnuPG
can handle MD5 and SHA checksums as well as PGP signatures. It is your
one-stop shop, cross-platform tool for release signing and verification.</p>
<p>It can be hard for newbies to be confident that they have executed
operations correctly. Consider doing some <a href="#safe-practice">practice</a> first.</p>



<h2 id="reading">Further reading</h2>

There are many other excellent resources on signing releases, but these make a good start:

  - The <a href="openpgp.html#gnupg">Guide to using GnuPG</a> at Apache
  - The <a href="key-transition.html">Apache Key Transition Guide</a>
  - RFC <a href="http://www.ietf.org/rfc/rfc1321.txt" target="_blank">1321</a> MD5 message-digest algorithm
  - RFC <a href="http://www.ietf.org/rfc/rfc2440.txt">2440</a> OpenPGP message format
  - The GNU Privacy Guard project <a href="https://www.gnupg.org/documentation/" target="_blank">documentation</a>
  - An introduction to <a href="https://www.pgpi.org/doc/pgpintro/" target="_blank">PGP public key cryptography</a>
  - <a href="https://www.schneier.com/book-applied.html" target="_blank">Applied Cryptography</a> by Bruce Schneier
  - Windows-centric <a href="http://www.mccune.cc/PGPpage2.htm" target="_blank">PGP FAQ</a> by Tom McCune</p>
