Title: Signing Releases

<h2 id="abstract">Introduction</h2>

This document gives release managers a basic introduction to release signing. See under [Further reading](#reading) for links to
authoritative sources of deeper information.

This document is informative and does not constitute policy.

<h2>Contents</h2>

<ul>
<li><a href="#abstract">Introduction</a></li>
<li><a href="#note">Important notes</a></li>
<li><a href="#basic-facts">Basic facts</a></li>
<li><a href="#signing-basics">Signing basics</li>
<li><a href="#key-basics">Keys basics</a></li>
<li><a href="#web-of-trust">What is a Web Of Trust?</a></li>


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

<h2 id="basic-facts">The basics</h2>

Every artifact distributed by the Apache Software Foundation  **must** be accompanied by one file containing an <a href="#openpgp-ascii-detach-sig">OpenPGP-compatible ASCII armored detached signature</a> and another file containing a <a href="release-signing#sha-checksum">SHA</a> or <a href="release-signing#md5">MD5</a>) checksum.

  - MD5 hashes are **deprecated**; please use SHA for new releases.
  - **Avoid** further use of `SHA-1`</code>.

Form the names of these files by adding to the name of the artifact the following suffixes:</p>

  - the signature by suffixing `.asc`
  - the checksum by suffixing `.md5` or `.sha[1|256|512]` (as appropriate)

Release managers **must not** store private keys used to sign Apache releases on ASF hardware. 

See the <a href="release-distribution.html#sigs-and-sums">release distribution policy</a> for details.

<h3 id="motivation">Why we sign releases</h3>

A signature allows anyone to verify that a file is identical to the one your project's release manager created. Since your project's release has a signature:

  - users can make sure that what they received has not been modified in any way, either accidentally via a faulty transmission channel, or intentionally (with or without malicious intent).
  - the Apache infrastructure team can verify the identity of a file.

<a href="#openpgp">OpenPGP</a> <a href="#verifying-signature">signatures</a> confer the usual advantages of digital signatures: authentication, integrity and non-repudiation. <a href="#md5">MD5</a> and <a href="#sha-checksum">SHA</a> checksums only provide the integrity part as they are not encrypted.

<h3 id="security-basics">Security checklist</h3>

  - <a href="#private-key-protection">Protect</a> your <a href="#public-private">private key</a>
  - Choose a <a href="#passphrase">good passphrase</a>
  - Opt for a reasonably <a href="#key-length">long key length</a>

<h2 id="signing-basics">Signing basics</h2>

  - Signatures should be <a href="#openpgp-ascii-detach-sig">ASCII armored and detached</a>.
  - You should <a href="#export">export</a> your <a href="#public-private">public key</a> and append the result to the appropriate <a href="#keys-policy">KEYS</a> file(s).

<h3 id="sign-release">How do I sign a release?</h3>

Create a <a href="#openpgp-ascii-detach-sig">OpenPGP compatible ASCII armored detached signature</a> for the released artifact. Upload the signature with the released artifact. See <a href="#basics">here</a> for a basic overview.

<h3 id="openpgp-ascii-detach-sig">What Is an OpenPGP compatible ASCII armored detached signature?</h3>
It is

  - an <a href="#openpgp">OpenPGP</a> compatible 
  - <a href="#ascii">ASCII armored</a> 
  - <a href="#detach-sig">detached signature</a>

To create one using <a href="https://www.gnupg.org" target="_blank">GNU Privacy Guard</a> for file
`foo.tar.gz`, type:

```
<code><pre>
   $ gpg --armor --output foo.tar.gz.asc --detach-sig foo.tar.gz 
</pre></code>
```

<h3 id="md5">What is an MD5 checksum?</h3>

MD5 is a <a href="http://www.faqs.org/rfcs/rfc1321.html" target="_blank">well known</a>  <a href="#message-digest">message
digest algorithm</a>. Many tools are available to calculate these sums. For example, you can use <a href="https://www.openssl.org/" target="_blank">OpenSSL</a>:

```
<code><pre>
$ openssl md5 &lt; file
</pre></code>
```

Platform-specific applications are also common, such as `md5sum` on linux:

```
<code><pre>
$ md5sum file
</pre></code>
With GnuPG:
<code><pre>
  $ gpg --print-md MD5 [fileName] &gt; [fileName].md5
</pre></code></p>
```

Run the command in the same directory as the file so the output only contains the file name with no directory prefixes.

**Note** that the security of MD5 is now <a href="#md5-security">questionable</a> and is only useful as part of a defense in depth.

<h3 id="sha-checksum">What is an SHA checksum?</h3>

Like <a href="#md5">MD5</a>, <a href="http://www.ietf.org/rfc/rfc3174.txt">SHA</a> is a <a href="#message-digest">message digest</a> algorithm. Using GnuPG, you can create a SHA1 signature as follows:

```
<code><pre>
  $ gpg --print-md SHA1 [fileName] &gt; [fileName].sha1
</pre></code>
```

**Avoid** further use of <a href="#sha1">SHA-1</a>. `SHA256` and `SHA512` use the same `SHA` algorithm family with longer hash
lengths (256 and 512 bits respectively). These longer variations are less vulnerable to the weaknesses found in the algorithm family than `SHA1`. Apache recommends using <a href="#sha1">SHA512</a>.

To create a `SHA512` checksum use:

```
<code><pre>
  $ gpg --print-md SHA512 [fileName] &gt; [fileName].sha512
</pre></code></p>
```

Run the command in the same directory as the file so the output only contains the file name with no directory prefixes.

There are other members of the `SHA` family that are rarely used.

<h3 id="message-digest">What is a message digest algorithm?</h3>

A message digest algorithm takes a document and produces a much smaller hash of that document. A good algorithm will produce different digests for very similar documents. A good algorithm makes it <a href="#infeasible">infeasible</a> to create a message matching a given hash.</p>

You can use a trusted digest for a document can be used to verify the contents of an untrusted file. You can deliver the digest, which has a small size over a secure but expensive channel while delivering the untrusted file over an insecure but inexpensive one. This is useful when distributing releases.

<h2 id="key-basics">Key basics</h2>

To sign releases, you need to <a href="#generate">generate</a> a new master key-pair for code signing. Follow these <a href="openpgp.html#generate-key" target="_blank">instructions</a>.

<h3 id="keys-policy">The KEYS File</h3>

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

<a href="#pke">Applied cryptography</a> is a subject that has considerable depth. Luckily, it's possible to get started signing releases without being an expert. Just remember that you will encounter some situations that require research and learning. We hope the
<a href="#faq">FAQ</a> will be a reasonable first port of call.

You need an <a href="#openpgp-applications">application</a> to manage keys and create signatures. We recommend <a href="http://www.gnupg.org/">GNU Privacy Guard</a>, and the Apache documentation generally assumes that's what
you're using. (We welcome contributions that document use of other tools.) Read the <a href="openpgp.html#gnupg">Apache PGP user guide</a> and keep the <a href="https://www.gnupg.org/gph/en/manual.html">manual</a> handy. 

GnuPG can handle MD5 and SHA checksums as well as PGP signatures. It is your all-in-one cross-platform tool for release signing and verification.

**Note:** It can be hard for newbies to be confident that they have executed operations correctly. Consider doing some <a href="#safe-practice">practice</a> before you try to sign an actual release.

<h3 id="openpgp">What is OpenPGP?</h3>
[OpenPGP](openpgp.html) is an <a href="http://www.ietf.org/rfc/rfc2440.txt" target="_blank">RFC</a> describing a system for interoperable <a href="#pke">public key cryptography</a>. Various implementations exist. Apache recommends <a href="https://www.gnupg.org/" target="_blank">GNU Privacy Guard</a> (GnuPG), an open-source, OpenPGP compatible implementation. It comes with <a href="https://www.gnupg.org/(en)/documentation/guides.html" target="_blank">good documentation</a> that describes GnuPG and gives a good general introduction to public key cryptography.

<h3 id="pke">What is public key cryptography?</h3>
Public key cryptography is asymmetric. You use one key to encrypt a message which only the other key can decrypt. You can share the first key publicly without compromising the security of the second key. One key is therefore called the _public key_ and one the _private key_.

When you use public key cryptography, you can freely distribute the public key, but you must keep the private key secret. It is vital to <a href="#private-key-protection">protect</a> private key files.. Private keys are typically stored in files protected by symmetric encryption. Choose a strong <a href="#passphrase">passphrase</a> to protect the file.</p>

<h3 id="detach-sig">What is a detached signature?</h3>

You create a digital signature from an original document using a <a href="#pke">private key</a>. Possession of the corresponding public key allows verification that a given file is identical to the original document. An _attached signature_ is attached to the document whereas a _detached signature_ is contained in a separate file.

<h3 id="ascii">What is ASCII armoring?</h3>
ASCII armoring is an encoding format that converts a binary file into a string of ASCII characters. This format is more human readable and more portable than other formats.

<h2 id="web-of-trust">What is a Web Of Trust?</h2>

It is difficult to personally verify the identity of all useful <a href="#pke">public keys</a>. However, having verified the identity of only a small number of public keys it is possible to deduce the identity of public keys trusted by the owners of these keys. This process can be repeated. This extended graph of trusted identities is termed a <a href="http://en.wikipedia.org/wiki/Web_of_trust" target="_blank">>web of trust</a>.

You can use webs of trust to solve the problem of verifying the identity of public keys.

**Note:** to take full advantage of a web of trust, it is important to actively build your personal web of trust into the major public webs of trust. Conferences are an ideal opportunity for exchanging key information, but you must come <a href="#link-into-wot">prepared</a>. 

For more information read the <a href="https://www.gnupg.org/(en)/documentation/guides.html" target="_blank">GNU Privacy Handbook</a>.

<h3 id="link-into-wot">How do I link into a public web of trust?</h3>

You join a web of trust when an existing member of that web signs your public key to verify your identity. See <a href="openpgp.html#wot">a short explanation</a>.

<h3 id="key-signing-party">What is a key-signing party?</h3>

A key signing party is a meeting organised to allow the exchange of public keys to extend the <a href="#web-of-trust">web of trust</a>. See the <a href="https://www.cryptnet.net/fdp/crypto/keysigning_party/en/keysigning_party.html">Keysigning Party HOWTO</a>.

<h3 id="apache-wot">How can I link my key into the Apache Web of Trust?</h3>

You can link into the Apache web of trust by meeting other Apache committers face-to-face and <a href="#link-into-wot">exchanging public
keys</a>:

  - Apache committers organizes <a href="#key-signing-party">key signing parties</a> at each <a href="https://www.apachecon.com" target="_blank">ApacheCon</a>.
  - If you are not able to attend ApacheCon, or it will not happen for several months, consider organising a face-to-face meeting of <a href="https://people.apache.org/map.html">local committers</a>.

Subscribe to the `party` list and when you visit a new city, see if committers want to meet up.




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
