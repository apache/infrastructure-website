Title: Machines and Fingerprints

This page serves as a secure source for validating host keys on various ASF servers and services.

Check fingerprints with: `ssh-keygen -t rsa -l -E md5 -lf <(ssh-keyscan foo.apache.org 2>/dev/null)`.

Note that some hosts may have multiple keys (RSA, ECDSA, ED25519). We only list the RSA AND ECDSA fingerprints on this page.

If SSH warns that the site is not known, and shows a fingerprint that is not in the table below, that could be because SSH is showing something other than RSA/ECDSA. To change the fingerprint to RSA, try the following: `ssh -o HostKeyAlgorithms=ssh-rsa foo.apache.org` <br/>

You can change the hash type with the option: `ssh -o FingerprintHash=sha256 ... `

Please note that `people.apache.org` and `home.apache.org` are aliases and appear in the table as `home-lw-us`.

<<<<<<< HEAD
If you'd like to update this page or learn more about the data, <a href="https://cwiki.apache.org/confluence/display/INFRA/machines.html" target="_blank">we have a docco for that.</a>

**The hashes shown below are what the real machines SHOULD have. If it differs from what you see, please contact infra.**
=======
**The hashes shown below are what the real machines SHOULD have. If an entry differs from what you see, please contact infra.**
>>>>>>> f34ca63dd3acbf0b484e4b11010f17c402999a15

`spu:fetch('https://infra-reports.apache.org/machines/index.html')`
