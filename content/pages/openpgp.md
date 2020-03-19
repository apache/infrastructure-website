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

<a href="https://www.gnupg.org" target="_blank">GnuPG</a> comes in two flavors. To easily generate a 4096 bit RSA signing and encryption key pair with strong digests, use either GnuPG version:

  -  `2.0.12` or higher (well-known, portable version)
  -  `1.4.10` or higher (version with advanced features)

Once you generate the key, you can use it with the widely available `1.4.9` and `2.x` releases. 

If the right version of GnuPG is not currently distributed for your platform, you need to <a href="http://www.gnupg.org/download/index.en.html" target="_blank">install it</a>. You only need this version to generate keys, so you do not need to repace the version distributed with your platform. You can install the new version into a working directory.

Checking that the installation has worked and that the version is correct, using either

```
    :::console
    $ gpg  --version 
    gpg (GnuPG) 1.4.10
    Copyright (C) 2008 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later
    <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Home: ~/.gnupg
    Supported algorithms:
    Pubkey: RSA, RSA-E, RSA-S, ELG-E, DSA
    Cipher: 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH, CAMELLIA128, 
            CAMELLIA192, CAMELLIA256
    Hash: MD5, SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
    Compression: Uncompressed, ZIP, ZLIB, BZIP2
```

or

```
    :::console
    $ gpg2 --version
    gpg (GnuPG) 2.0.12
    libgcrypt 1.4.4
    Copyright (C) 2009 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later
    <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Home: ~/.gnupg
    Supported algorithms:
    Pubkey: RSA, ELG, DSA
    Cipher: 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH, CAMELLIA128, 
            CAMELLIA192, CAMELLIA256
    Hash: MD5, SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
    Compression: Uncompressed, ZIP, ZLIB, BZIP2
```

Now confirm that the configuration file is [set up to avoid SHA-1](#sha1).

<h3 id="key-gen-generate-key">Generate a new key</h3>

Versions `2.0.12`and `1.4.10` introduced a new default key generation option - *RSA and RSA*. [RSA](release-signing.html#rsa)
keys are used for both encryption and signing. Longer key lengths are available. Select or accept this option when generating new keys.

Follow the recommendations about [user ID](release-signing.html#user-id) and [comment](release-signing.html#key-comment). Use a strong
[passphrase](release-signing.html#passphrase).

Follow either

```
    :::console
    $ gpg --gen-key 
    gpg (GnuPG) 1.4.10; Copyright (C) 2008 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Please select what kind of key you want:
       (1) RSA and RSA (default)
       (2) DSA and Elgamal
       (3) DSA (sign only)
       (4) RSA (sign only)
    Your selection? 1
    RSA keys may be between 1024 and 4096 bits long.
    What keysize do you want? (2048) 4096
    Requested keysize is 4096 bits
    Please specify how long the key should be valid.
             0 = key does not expire
          <n>  = key expires in n days
          <n>w = key expires in n weeks
          <n>m = key expires in n months
          <n>y = key expires in n years
    Key is valid for? (0) 
    Key does not expire at all
    Is this correct? (y/N) y

    You need a user ID to identify your key; the software constructs the user
    ID
    from the Real Name, Comment and Email Address in this form:
        "Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"

    Real name: Robert Burrell Donkin 
    Email address: rdonkin@apache.org
    Comment: CODE SIGNING KEY
    You selected this USER-ID:
        "Robert Burrell Donkin (CODE SIGNING KEY) <rdonkin@apache.org>"

    Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
    You need a Passphrase to protect your secret key.
```

or

```
    :::console
    $ gpg2 --full-gen-key
    gpg (GnuPG) 2.0.12; Copyright (C) 2009 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Please select what kind of key you want:
       (1) RSA and RSA (default)
       (2) DSA and Elgamal
       (3) DSA (sign only)
       (4) RSA (sign only)
    Your selection? 1
    RSA keys may be between 1024 and 4096 bits long.
    What keysize do you want? (2048) 4096
    Requested keysize is 4096 bits
    Please specify how long the key should be valid.
             0 = key does not expire
          <n>  = key expires in n days
          <n>w = key expires in n weeks
          <n>m = key expires in n months
          <n>y = key expires in n years
    Key is valid for? (0) 
    Key does not expire at all
    Is this correct? (y/N) y

    GnuPG needs to construct a user ID to identify your key.

    Real name: Robert Burrell Donkin
    Email address: rdonkin@apache.org
    Comment: CODE SIGNING KEY
    You selected this USER-ID:
        "Robert Burrell Donkin (CODE SIGNING KEY) <rdonkin@apache.org>"

    Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
    You need a Passphrase to protect your secret key.
```

<h3 id="key-gen-avoid-sha1">Check that the key avoids using SHA-1</h3>

Check that the configuration has correctly set the key preferences to avoid SHA-1, using either:

```
    :::console
    $ gpg --edit-key 773447FD
    gpg (GnuPG) 1.4.10; Copyright (C) 2008 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Secret key is available.

    pub  4096R/773447FD  created: 2010-02-16  expires: never       usage: SC  
                         trust: ultimate      validity: ultimate
    sub  4096R/436E0F7C  created: 2010-02-16  expires: never       usage: E   
    [ultimate] (1). Robert Burrell Donkin (CODE SIGNING KEY) <rdonkin@apache.org>

    Command> showpref
    [ultimate] (1). Robert Burrell Donkin (CODE SIGNING KEY)
    <rdonkin@apache.org>
         Cipher: AES256, AES192, AES, CAST5, 3DES
         Digest: SHA512, SHA384, SHA256, SHA224, SHA1
         Compression: ZLIB, BZIP2, ZIP, Uncompressed
         Features: MDC, Keyserver no-modify
```

or

```
    :::console
    $ gpg2 --edit-key A6EE6908
    gpg (GnuPG) 2.0.12; Copyright (C) 2009 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Secret key is available.

    pub  8192R/A6EE6908  created: 2009-08-07  expires: never       usage: SC  
                         trust: ultimate      validity: ultimate
    sub  8192R/B800EFC1  created: 2009-08-07  expires: never       usage: E   
    [ultimate] (1). Robert Burrell Donkin (CODE SIGNING KEY) <rdonkin@apache.org>

    Command> showpref 
    [ultimate] (1). Robert Burrell Donkin (CODE SIGNING KEY)
    <rdonkin@apache.org>
         Cipher: AES256, AES192, AES, CAST5, 3DES
         Digest: SHA512, SHA384, SHA256, SHA224, SHA1
         Compression: ZLIB, BZIP2, ZIP, Uncompressed
         Features: MDC, Keyserver no-modify

```

The `Digest` line should list SHA-512 first and SHA-1 last. Instructions for altering the preferences of a key are
[here](#key-prefs).

<h3 id="final-steps">Final steps</h3>

When you generate a new code signing key, you need to update a number of Apache documents and perform some other tasks.

<p id="generation-final-steps-transition" />

If you are generating a key for use in a [transition](release-signing.html#transition), there is more you should do before updating these documents, so [go to the transition instructions now](key-transition.html#ContinueAfterGeneration).

<p id="generation-final-steps-new-key" >

If this is a new code signing key not involved with a transition:

  1.  [Upload](release-signing.html#keyserver-upload) the new [public key](release-signing.html#public-private) to a public
[keyserver](release-signing.html#keyserver) 

  1. Create backups by following these [instructions](#backup) 

  1. Follow these [instructions](#revocation-certs) to create and securely store generic [revocation
certificates](release-signing.html#revocation-cert) for the new key

  1. Follow these [instructions](#update) (ignoring the transition option) to create or update Apache documents

  1. Read this [guide](#wot) to the Apache use of the [web of trust](release-signing.html#web-of-trust) and make arrangements for your
new key to be included at the earliest opportunity.

<h2 id="private-keyring-management">Private keyring management</h2>

1. Never transmit your private keyring over the internet!

2. Store your keys on unshared local disk storage. If your employer only provides networked storage, ask for permission to use a USB fob (or CD) to store your .gnupg directory.

3. Destroy your retired disks appropriately using a disk wiping utility or similar tools to ensure your keyring is no longer available
on those disks once you are through with them. Failing that, drill through the disk platters so they are physically unusable.

<h2 id="find-key-id">Find a key ID</h2>

There are a number of ways that a key may be identified. Only one is unique: the [key fingerprint](release-signing.html#fingerprint).

Attackers can easily create new keys similar to yours with identical user IDs and comments. Such a public key may be introduced to your keyring when you download keys from a [public keyserver](release-signing.html#keyserver) or as part of an import. If this information is used to identify public keys then you may be misled into believing that another public key is yours. A cunning attacker may even introduce a matching secret key taht lets you sign with that key.

Creating a different key with a matching identity is considered [infeasible](release-signing.html#infeasible). For all operations where
precise identity matters and that identity is specified on the command line, you should use the key ID to identify the key. Avoid using
user ID or other information.

<h3 id="find-key-id-from-trusted-source">Find a key ID from a trusted source</h3>

The best way to find a key ID is to obtain it directly from a trusted source, for example, from a business card you obtain personally from the owner of the key.

<h3 id="find-key-id-with-fingerprint">Find a key ID with its fingerprint</h3>

If you have a [fingerprint](release-signing.html#fingerprint), the key ID should be the last 8 digits. For example, the ID of the key with this fingerprint:

```
    :::text
    FF96 6261 C995 1DDE BF34  5150 D5D2 BDB5 E2B0 54B8
```

should be:

```
    :::text
    E2B054B8
```

You can confirm this using:

```
    :::console
    $ gpg --list-keys --fingerprint E2B054B8
    pub   4096R/E2B054B8 2009-08-20
          Key fingerprint = FF96 6261 C995 1DDE BF34  5150 D5D2 BDB5 E2B0 54B8
    uid                  Alice Example (EXAMPLE NEW KEY) <alice@example.org>
    sub   4096R/4A6D5217 2009-08-20
```














