Title: Machines and Fingerprints

This page is maintained by Apache Infra and serves as a secure source for validating host keys on various ASF servers and services. <br/>
New Committers should see the guide for setting up SSH and the brief SSH how-to.

Check fingerprints with: `ssh-keygen -t rsa -l -E md5 -lf <(ssh-keyscan foo.apache.org 2>/dev/null)` <br/>
Note that some hosts may have multiple keys (RSA, ECDSA, ED25519). We only list the RSA fingerprints on this page.

If SSH warns that the site is not known, and shows a fingerprint that is not in the table below, that could be because SSH is showing something other than RSA. To change the fingerprint to RSA, try the following: `ssh -o HostKeyAlgorithms=ssh-rsa foo.apache.org` <br/>
You can change the hash type with the option: `ssh -o FingerprintHash=[md5|sha256] ... `

Please note that people.apache.org and home.apache.org are aliases and appear in the table as home-lw-us.

**The hashes shown below are what the real machines SHOULD have. If it differs from what you see, please contact infra.**


`spu:fetch('https://infra-reports.apache.org/machines/index.html')`

