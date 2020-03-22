Title: Signing Releases

<h2 id="abstract">Abstract</h2>

This document gives release managers a basic introduction to release signing. See under [Further reading](#reading) for links to
authoritative sources of deeper information.

This document is informative and does not constitute policy.

<h2>Contents</h2>

<ul>
<li><a href="#abstract">Abstract</a></li>
<li><a href="#note">Important notes</a></li>
<li><a href="#help">Help Wanted!</a></li>
<li><a href="#reading">Further Reading</a></li>
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
</ul>

<h2 id="note">Important notes</h2>

All new **RSA** keys generated should be at least **4096** bits. **Do not** generate new **DSA** keys.

Recent research has revealed weaknesses in SHA-1, and thus in the DSA and 1024 bit RSA OpenPGP keys which must use this algorithm. Though no realistic attacks have been made public, experience with similar weaknesses in MD5 suggests that further advances may well lead to practical attacks within the next few years. This accords with current NIST guidance on DSA.

The impact of this weakness on Apache can be mitigated by action now. What needs to be done is a little involved, so we have provided complete instructions.

  - Committers without a code signing key should read this document and follow these [instructions](openpgp.html#generate-key).
  - Committers with a DSA key or an RSA key of length less than 2048 bits should generate a new key for signing releases. The original key does not need to be revoked yet. Follow this [guide](key-transition.html).

- Committers with RSA keys of length 2048 or more do not need to generate a
new key yet. They should reconfigure their client to avoid the weakness by
following these [instructions](openpgp.html#sha1) and wait for the next
major OpenPGP revision.

How to find the length of your key is described [here](#key-length-how-to).




_information will come here from https://www.apache.org/dev/release-signing.html_
