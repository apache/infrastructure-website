Title: Cryptography with OpenPGP

<h2 id="introduction">Introduction</h2>
OpenPGP is encryption software. The program provides cryptographic privacy and authentication for data communication, covering signing, encrypting, and decrypting texts, e-mails, files, directories, and whole disk partitions and increasing the security of e-mail communications.

Reliable cryptography applications follow OpenPGP, an open standard of Pretty Good Privacy (PGP) encryption software, standard (RFC 4880), for encrypting and decrypting data.

<h2 id="gnupg">Gnu Privacy Guard (GPG)</h2>

The Apaches Software Foundation recommends using <a href="https://www.gnupg.org" target="_blank">Gnu Privacy Guard (GPG)</a>, a well-known open source cryptography tool with OpenPGP support. Always use the latest version.

GnuPG has a good set of <a href="https://www.gnupg.org/documentation" target="_blank">documentation</a>. This guide covers only some important points.

<h3 id="home">GnuPG Home</h3>

GnuPG stores important files, including keyrings and configuration files, in a home directory. You can specify your proejct's home directory in an environmental variable or on the command line. This allows different configurations and keys to be used.

For example:

```
    ::console
    $ gpg --homedir /home/alice/keys --list-keys
```

Projects generally rely on the default. For `\*nux` (linux, BSD, MaxOSX, Solaris, AIX) this is:

```
    :::shell
    $HOME/.gnupg
```

<h4 id="switch-home">How to switch Home</h4>

You can set Home using an envionmental variable. This lets you select a specific configuration and keyring for the duration of a
command line session. This is useful when [practicing](release-signing.html#safe-practice) and when using multiple keyrings.

For example, to set home directory to `alice` when using Linux:

```
    :::console
    $ export GNUPGHOME=alice
```

When switching key rings, check that the required keyring has been selected by examining the secret keys. For example:

```
    :::console
    $ gpg --list-secret-keys
    alice/secring.gpg
    -----------------

    sec   4096R/E2B054B8 2009-08-20
    uid                  Alice Example (EXAMPLE NEW KEY) <alice@example.org>
    ssb   4096R/4A6D5217 2009-08-20
```

<h3 id="configuration">Configuration</h3>

GnuPG supports a wide range of configuration options. You can specify them on the command line, but it is usually more convenient to set them in the `gpg.conf` file. By default, this is located in the [GnuPG Home](#home) directory.

<h3 id="sha1">Avoid SHA-1</h3>

Avoid using SHA-1 should now be [avoided](release-signing.html#sha1). Until
[SHA3](release-signing.html#sha3) is available, `SHA512` or `SHA256` should
be used instead. `SHA512` is stronger than `SHA256`. Though some old
clients lack `SHA512` support, switching to `SHA512` is recommended since
it is more likely to be strong enough to bridge the gap until `SHA3`.






