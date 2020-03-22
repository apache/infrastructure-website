Title: Signing Releases

<h2 id="abstract">Abstract</h2>

This document gives release managers a basic introduction to release signing. See under [Further reading](#reading) for links to
authoritative sources of deeper information.

This document is informative and does not constitute policy.

<h2>Contents</h2>




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
