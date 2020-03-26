Title: Signing Releases

<h2 id="abstract">Introduction</h2>

The first part of this document gives release managers a basic introduction to release signing. See under [Further reading](#reading) for links to authoritative sources of deeper information.

The second part answers some frequently-asked questions from people who downlaod releases from Apache projects.

This document is informative and does not constitute policy.

<h2>Contents</h2>

<h3>For release managers</h3>

<ul>
<li><a href="#abstract">Introduction</a></li>
<li><a href="#note">Important notes</a></li>
<li><a href="#basic-facts">Basic facts</a></li>
<li><a href="#signing-basics">Signing basics</li>
<li><a href="#key-basics">Keys basics</a></li>
<li><a href="#safe-practice">How can I safely practice using OpenPGP?</a></li>
<li><a href="#web-of-trust">Web of Trust basics</a></li>
<li><a href="#passphrase">What is a Passphrase?</a></li>
<li><a href="#revocation-cert">Revocation Certificate basics</a></li>
  



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
<li><a href="#reading">Further Reading</a></li>
</ul>

<h3>FAQs from those downloading releases</h3>
<ul>
  <li><a href="#verifying-signature">What does verifying a signature mean?</a></li>
  <li><a href="#check-integrity">How can I check the integrity of a release?</a></li>
  <li><a href="#public-key-not-found">What does 'Public key not found' mean when verifying a signature?</a></li>
  <li><a href="#trust">What is a trusted key?</a></li>
  <li><a href="#valid-untrusted-vs-invalid-trusted">What is the difference between a valid signature from an untrusted key and an invalid signature from a trusted key?</a></li>
  <li><a href="#fingerprint">What is a public key fingerprint?</a></li>
  <li><a href="#local-sig">Can I mark a key as locally trusted?</a></li>
</ul>
<a href="#help">Add your wisdom</a>



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

<h3 id="infeasible">Why infeasible and not impossible?</h3>

Responsible cryptography talks about infeasible cracks (rather than impossible ones) since this is more accurate. All current practical methods can be subjected to brute force attacks and so can be cracked. So a better question is whether attacks are feasible _given the current state of the art_.

<h3 id="openpgp-applications">Applications that create OpenPGP-compatible signatures</h3>

Many applications are available (some commercial, some freeware, some software libre) to help you sign releases. Whichever one you choose, please subscribe to the appropriate security lists and keep the application fully patched.

Apache recommends that ASF release managers use <a href="https://www.gnupg.org" target="_blank">GNU Privacy Guard</a>.

<h3 id="where">Where should I create the signatures?</h3>

Creating signatures requires the private key. Keep limited copies of the private key securely and confidentially. Though the file used
to store the private key is typically protected by encryption, it is vulnerable to dictionary attacks on the <a href="#passphrase">passphrase</a>. So keep this file secret. 

Create signatures on the machine where you store the private key, on secure hardware with limited read permissions, protected by a good
<a href="#passphrase">passphrase</a>. Consider using removable media or an <a href="#isolated-installation">isolated
installation</a>.

A master private key used to sign Apache artifacts (or to secure communications with the ASF) is particularly valuable. If you want or need to be able to create signatures for other purposes (for example, signing email messages) in other, less secure, locations, create multiple <a href="#email-subkey">sub keys</a> for these purposes.

Do **not** store your private key on any ASF machine. Do **not** create signatures on ASF machines.

<h3 id="insecure-memory">What is 'insecure memory'?</h3>

When you use <a href="http://www.gnupg.org">GNU Privacy Guard</a> you may see a warning similar to:

```
gpg: WARNING: using insecure memory!
gpg: please see http://www.gnupg.org/faq.html for more information
```

If you are using GnuPG on Apache hardware, please read <a href="#where">this</a>. Do **not** carry out sensitive operations using a private key on ASF hardware.

If you encounter this issue elsewhere, it indicates that GnuPG cannot lock memory pages, so they may be swapped out to disc. It would
then be feasible for an attacker who had gained access to the machine to read the private key from the swap file. For more details, read the <a href="https://www.gnupg.org/faq.html">FAQ</a>.</p>

<h3 id="secure-machine">How secure does the machine I use to sign releases need to be?</h3>

If the code signing machine is <a href="http://www.catb.org/~esr/jargon/html/O/owned.html">owned</a>, it is only a matter of time before the key is compromised.

At a minimum, the machine should well maintained: kept up to date with security patches and with appropriate anti-virus and firewall software. The ideal is an isolated, well-maintained installation that you only use for creating releases. You can achieve this with a little effort by creating an <a href="#isolated-installation">isolated installation</a> on a separate hard disc (which is physically disconnected when not in use signing releases) or a live CD.

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

<h2 id="safe-practice">How can I safely practice using OpenPGP?</h2>

To practice using OpenPGP, use separate environments. each with a different practice keyring.

For example, using <a href="http://www.gnupg.org" target="_blank">GNU Privacy Guard</a>:

  - (First time only)Create a directory to contain the keyring
  - Open the shell to be configured to use this keyring
  - Change to the directory
  - (First time only) `$ mkdir -m 700.gnupg`
  - Set up the environment: `export GNUPGHOME=.gnupg`

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

<h3 id="public-private">The difference between a public and a private key</h3>

A public key is for verifying signatures and encrypting messages; a private key is for generating signatures and decrypting messages. You can freely distribute public keys safely , but you must keep private keys <a href="#safe-and-secure">protected</a>. More details <a href="#pke">here</a>.

<h3 id="private-key-protection">How to protect your code signing private key</h3>

Anyone who possesses a copy of a <a href="#public-private">private key</a> used to <a href="#sign-release">sign</a> releases can create doctored releases with valid signatures. If this person intends harm then the consequences could be serious indeed. It is therefore very important to keep the private key secret.

  - Only sign releases on a <a href="#secure-machine">secure machine</a>.
  - Keep your <a href="#openpgp-applications">signing application</a> fully patched.
  - Keep the key file <a href="#safe-and-secure">safe and secret</a>.
  - Choose a good <a href="#passphrase">passphrase</a>.
  
<h3 id="safe-and-secure">How safe does the private key need to be?</h3>

It is vital that the private key is kept safe and secure. Though the file is encrypted using a <a href="#passphrase">passphrase</a> , given enough time any determined cracker will be able to break that encryption. Basic precautions should include ensuring that only the user can read the directories.

However, for code signing keys we recommend taking additional measures. Reduce the window of vulnerability by using an
<a href="#isolated-installation">isolated installation</a> or by storing the private key on removable media (which you should remove and store securely when not actually signing a release.).


<h3 id="isolated-installation">The meaning of 'isolated installation'</h3>

An isolated installation is inaccessible when you are not using it to sign releases. For example, create an installation on a separate hard disc or use a live CD.

<h3 id="key-length">Recommended key length</h3>

The number of operations required to break a key by brute force increases with key size. However, the cost of using the key also rises. You must take into account the planned use of the key. You will use keys for code signing rarely and in situations where performance is not the main concern, so you can use long keys.

Over time, the cost of attacking a key of a given length by brute force falls as computing power increases. So a key whose length
seems adequate today may be seem too short in a few years time. This is a significant issue for long-lived keys such as those used to sign ASF releases, and another reason to use longer keys with releases.

<p>Now that there is doubt about the medium term security of <a href="#sha1">SHA-1</a>, avoid the DSA keys and 1024 bit RSA keys which depend on this algorithm. We recommended that new keys be at least 4096 bit RSA (the longest widely supported key length).</p>





<h2 id="passphrase">What is a Passphrase?</h2>

In cryptography <em>passphrase</em> is often used for what might be known as a password in other contexts. For example, an
<a href="#openpgp">OpenPGP</a> private key is typically stored to disc in a file encrypted by a symmetric cypher keyed by a passphrase. This passphrase is one of the weakest elements in the system: should anyone else gain access to the file then a dictionary attack will be feasible on a weak passphrase. So choosing a strong passphrase is very important.

Passphrases, unlike passwords, are typically unlimited in length. We recommend using long passphrases. You can use sequences of (at least seven) unrelated words or more conventional mixtures of symbols and alphanumerics.

Even a good passphrase offers only limited protection. Given the encrypted file and enough time, a determined cracker will be able to
break any passphrase. A good passphrase will buy important time in the event of a compromise, but is no substitute for keeping the private key <a href="#safe-and-secure">safe and secure</a> in the first place.

<h2 id="revocation-cert">Revocation Certificate basics</h2>

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

<h3 id="revoke-key">Revoking a key</h3>

To revoke a key with a <a href="#revocation-cert">revocation certificate</a> using <a href="https://www.gnupg.org" target="_blank">GNU Privacy Guard</a>, import the certificate:

```
$ gpg --import revoke.asc 
gpg: key 4A03679A: "Some User &lt;someuser@example.org&gt;" revocation
certificate imported
gpg: Total number processed: 1
gpg:    new key revocations: 1
```

<h3 id="revocation-certificate-storage">Where to store revocation certificates</h3>

Store each revocation certificate securely and separately from the key it revokes. Burning the certificate onto a CDROM or printing it out as a hard copy are good solutions.

<h3 id="revoke-cert">Distributing a revocation certificate</h3>

If a key has been compromised, distribute its <a href="#revocation-cert">revocation certificate</a> to those using the key. This process is a mirror of the process by which you distributred the original key.

  - Inform the Apache infrastructure team by a post containing the revocation certificate.
  - Update the KEYS files containing the original key with the revocation certificate.
  - Upload the revocation certificate to the major keyserver networks.
  - Post an announcement to the appropriate lists with the revocation certificate attached.

<h3 id="delete-vs-revoke">The difference between deleting and revoking a key</h3>

When you _delete_ a key from a keyring, it is simply removed. You can add it again later.

When you _revoke_ a key, it is marked in the key ring. Whenever a message signed by this key is verified in the future, the user will get a warning that the key has been revoked.

For example, when you verify a revoked key, <a href="https://www.gnupg.org" <target="_blank">>GNU Privacy Guard</a> issues the following comment:

```
$ gpg --verify message.asc.message 
gpg: Signature made Sat Apr  8 09:28:31 2006 BST using DSA key ID 4A03679A
gpg: Good signature from "Some User &lt;someuser@example.org&gt;"
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

<h3 id="verifying-signature">What does verifying a signature mean?</h3>

You can use <a href="#pke">public key cryptography</a> to test whether a particular file is identical in content to an original by verifying a <a href="#detach-sig">signature</a>. The signature file is a <a href="#message-digest">digest</a> of the original file signed by a private key which attests to the digest's authenticity.

For example, when using <a href="https://www.gnupg.org/" target="_blank">GNU Privacy Guard</a> you verify the signature `foo-1.0.tar.gz.asc` for release `foo-1.0.tar.gz` using the following command:

```
$ gpg --verify foo-1.0.tar.gz.asc foo-1.0.tar.gz
</pre></code>
A signature is valid, if <code>gpg</code> verifies the <code>.asc</code>
as a <code>good signature</code>, and doesn't complain about expired
or revoked keys. Technically :
<code><pre>
$ gpg --verify --status-fd 1 foo-1.0.tar.gz.asc foo-1.0.tar.gz
```

should classify the `.asc` as a `GOODSIG`.

Trust is required in the identity of the public key that made the signature and that the signature is for the original file and not some other file. When verifying a release from an untrusted source (for example, over P2P file sharing or from a mirror) it is important to download the signature from a trusted source. Signatures for all Apache releases are available directly for download from `www.apache.org`.

<h3 id="check-integrity">How can I check the integrity of a release?</h3>
  
<a href="#md5">MD5</a> and <a href="#sha-checksum">SHA</a> checksums provide a simple way to verify the integrity of a download. You can simply create a checksum (in the same way as the release manager) after download, and compare the result to the checksum downloaded from the main Apache site. However, this process does not provide for authentication and non-repudiation</a> as anybody can create the same checksum.

You can also check the integrity of a release by <a href="#verifying-signature">verifying the signature</a>. You need more knowledge to correctly interpret the result, but it does provide authentication and non-repudiation. If you are connected to the Apache <a href="#web-of-trust">web of trust</a>, this also offers superior security.

<h3 id="public-key-not-found">What does 'Public key not found' mean when I try to verify a signature?</h3>
To verify a signature, you need the release's public key. For example, when using <a href="https://www.gnupg.org/">GNU Privacy Guard</a>, if you have never imported the appropriate public key, you will see a message like this:

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

<h3 id="trust">What is a trusted key?</h3>

<a href="#openpgp">OpenPGP</a> uses a <a href="#web-of-trust">web of trust</a>. The owner of a public key who trusts the identity of a second key may mark this key as trusted by signing it. This has several major effects:

  - In future, no <a href="#valid-untrusted-vs-invalid-trusted">untrusted key warning</a> appears when a valid signature for
this key is verified.
  - Keys the owner of the key trusts may also become trusted. In other words, if the owner of a key whose identity you trust confirms the identity of a key, that key may be automatically trusted. This behavior is typically configurable.
   - The next time you export your key, those who trust your key may start to trust the identity of the trusted key.

The transitive nature of the web of trust places a responsibility on the owner to verify the identity of the owner of those keys marked as trusted.

For more information read the <a href="https://www.gnupg.org/(en)/documentation/guides.html" target="_blank">GNU Privacy Guard User
Guide</a>.

<h3 id="valid-untrusted-vs-invalid-trusted">What is the difference between a valid signature from an unterusted key an invalid signature from a trusted key?</h3>

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

<h3 id="fingerprint">What is a public key fingerprint?</h3>

Public keys are long and even when <a href="#ascii">ASCII armored</a> are not very easy for humans to understand or compare. A fingerprint is a short <a href="#message-digest">digest</a> of the key formatted in a way that makes it easier for humans to read and compare.

<h3 id="local-sig">Can I mark a key as locally trusted?</h3>

On occasion, the user (who understands the risks) may trust a key but not consider it trustworthy enough to exported to the <a href="#web-of-trust">web of trust</a>. <a href="#openpgp">OpenPGP</a> lets you sign keys as local only. These trust relationships will not be exported to the public web of trust but are treated as trusted when you use the key ring locally.

For example, with <a href="https://www.gnupg.org" target="_blank">GNU Privacy Guard</a> use:

```
$ gpg --lsign-key someuser
```












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
