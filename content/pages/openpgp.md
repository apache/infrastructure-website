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
    uid   Alice Example (EXAMPLE NEW KEY) <alice@example.org>
    ssb   4096R/4A6D5217 2009-08-20
```

<h3 id="configuration">Configuration</h3>

GnuPG supports a wide range of configuration options. You can specify them on the command line, but it is usually more convenient to set them in the `gpg.conf` file. By default, this is located in the [GnuPG Home](#home) directory.

<h3 id="sha1">Avoid SHA-1</h3>

[Avoid](release-signing.html#sha1) using `SHA-1`. Use `SHA512` or `SHA256` instead. `SHA512` is stronger than `SHA256`. Though some old
clients lack `SHA512` support, we recommend switching to `SHA512` if possible.

<h3 id="sha-defaults">Setting defaults</h3>

To configure `gpg` to avoid SHA-1, edit the options in [`gpg.conf`](#configuration). Options need to be added or given the correct values for:

  -  `cert-digest-algo` - the certificate digest used when linking into the [web of trust](release-signing.html#link-into-wot) 
  -  `personal-digest-preferences` - the digest used for [signing messages](release-signing.html#detach-sig) 
  -  `default-preference-list` - the default algorithm preferences for [new keys](release-signing.html#generate) (this does not affect existing keys: see next paragraph)

To use `SHA512` (recommended):

```
    :::text
    personal-digest-preferences SHA512
    cert-digest-algo SHA512
    default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 ZLIB BZIP2 ZIP Uncompressed
```

To use SHA256:

```
    :::text
    personal-digest-preferences SHA256
    cert-digest-algo SHA256
    default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 ZLIB BZIP2 ZIP Uncompressed
```
    
<h3 id="key-prefs">Setting preferences for keys</h3>

The digest preferences for each key (from the [configuration defaults](#sha-defaults) ) are set when the key is generated. Once the
configuration has been updated to avoid SHA-1, all new keys generated will use these defaults, but keys generated before the configuration won't be affected.

All existing private keys in the ring need to be updated to indicate that stronger hashes are preferred. For each public-private key pair (generated with the previous defaults):

```
    :::console
    $ gpg --edit-key F8B7B4FD
    gpg (GnuPG) 1.4.9; Copyright (C) 2008 Free Software Foundation, Inc.
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions. See the file COPYING for details.

    Secret key is available.

    pub  1024D/F8B7B4FD  created: 2009-08-12  expires: 2009-09-11  usage: SC  
                         trust: ultimate      validity: ultimate
    sub  1024g/D55BD150  created: 2009-08-12  expires: 2009-09-11  usage: E   
    [ultimate] (1). Example Key (NOT FOR DISTRIBUTION) <bogus@example.org>

    Command> showpref
    [ultimate] (1). Example Key (NOT FOR DISTRIBUTION) <bogus@example.org>
         Cipher: AES256, AES192, AES, CAST5, 3DES
         Digest: SHA1, SHA256, RIPEMD160
         Compression: ZLIB, BZIP2, ZIP, Uncompressed
         Features: MDC, Keyserver no-modify

    Command>  setpref SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 ZLIB BZIP2 ZIP Uncompressed
    Set preference list to:
         Cipher: AES256, AES192, AES, CAST5, 3DES
         Digest: SHA512, SHA384, SHA256, SHA224, SHA1
         Compression: ZLIB, BZIP2, ZIP, Uncompressed
         Features: MDC, Keyserver no-modify
    Really update the preferences? (y/N) y

    You need a passphrase to unlock the secret key for
    user: "Example Key (NOT FOR DISTRIBUTION) <bogus@example.org>"
    1024-bit DSA key, ID F8B7B4FD, created 2009-08-12

    pub  1024D/F8B7B4FD  created: 2009-08-12  expires: 2009-09-11  usage: SC  
                         trust: ultimate      validity: ultimate
    sub  1024g/D55BD150  created: 2009-08-12  expires: 2009-09-11  usage: E   
    [ultimate] (1). Example Key (NOT FOR DISTRIBUTION) <bogus@example.org>

    Command> save
```

Then upload the modified public key to a public keyserver. For example:

```
    :::console
    $ gpg --send-keys F8B7B4FD
```

<h2 id="generate-key">How to generate a strong key</h2>

The weaknesses found in [SHA-1](release-signing.html#sha1) threaten all DSA keys and those RSA keys with length less than 2048 bits. Though no realistic attack against those keys have been made public and these keys continue to be useful (and do not need to be revoked), Projects should not generate new keys that are exposed to this weakness.

The next generation of [OpenPGP](release-signing.html#openpgp) will use [SHA-3](release-signing.html#sha3). For now, the 2048 bit RSA keys with SHA256 hash should be strong enough. For those with 2048 bit RSA keys, the best advice is to [switch](#sha1) to SHA256 or SHA512 as soon as possible. All new keys generated should be RSA with at least 4096 bits.

Though 8192 bit keys are stronger, they are slower and may be incompatible with some older clients. For the present, 4096 bit RSA should be strong enough for code signing at Apache. To generate RSA keys with length more
than 4096 bits, <a href="https://www.jroller.com/robertburrelldonkin/entry/gnupg_8192bit_rsa_keys" target="_blank">changes are needed</a>. Then you can follow the procedure for 4096 bits.

<h3 id="key-gen-install-latest-gnupg">Install and configure GnuPG</h3>













