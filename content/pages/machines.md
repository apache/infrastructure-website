Title: Machines and Fingerprints

This page serves as a secure source for validating host keys on various ASF servers and services.

Check fingerprints with: `ssh-keygen -lf <(ssh-keyscan foo.apache.org 2>/dev/null)`

Note that some hosts may have multiple keys (RSA, ECDSA, ED25519). We only list the RSA and ECDSA fingerprints on this page.

If SSH warns that the site is not known, and shows a fingerprint that is not in the table below, that could be because SSH is showing something other than RSA/ECDSA. To change the fingerprint to RSA, try the following: `ssh -o HostKeyAlgorithms=ssh-rsa foo.apache.org` <br/>

You can change the hash type with the option: `ssh -o FingerprintHash=sha256 ... `

Please note that `people.apache.org` and `home.apache.org` are aliases and appear in the table as `home-lw-us`.

For example, `ssh-keygen -lf <(ssh-keyscan home.apache.org 2>/dev/null)` currently (Sep 2023) shows:

```
256 SHA256:HZvgAd9EZi5cfyVhmhfk1gdn7a9zDzhsqNY5Umopr5I home.apache.org (ED25519)
3072 SHA256:Ek/qjqOOyyX5pNNSkNCIsLIf81X/sRcm7UVkkCSzdgY home.apache.org (RSA)
256 SHA256:Oz9+wOnlHvjYYXE06xENo3Z2l09ULBT3TO7gHHhdNnM home.apache.org (ECDSA)
```

The order of lines may differ, but the hashes should agree with the entry for `home-lw-us` in the table below.

**The hashes shown below are what the real machines SHOULD have. If an entry differs from what you see, please contact infra.**

`spu:fetch('https://infra-reports.apache.org/machines/index.html')`
