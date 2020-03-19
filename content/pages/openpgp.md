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

<p id="generation-final-steps-new-key" />

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

<h3 id="find-key-id-with-secret-key">When you have the secret key</h3>

When you have the secret key, listing the secret key details allows the key ID to be read from the `sec` lines in the output.

**Note** that it is possible for an attacker to introduce a new secret key into your keyring (for example, as part of an import). It is vital that you know how many secret keys each keyring should hold. If any unexpected secret keys are present, this probably indicates an attack.

For example, Alice is [transitioning](key-transition.html) and so expects two secret keys in her main keyring. (The case of a single key is similar but less complex.) She lists all secret keys on the keyring:

```
    :::console
    $ gpg --list-secret-keys
    alice/secring.gpg
    -----------------
    sec   1024D/AD741727 2009-08-20
    uid                  Alice Example (EXAMPLE OF OLD KEY) <alice@example.org>
    ssb   1024g/268883A9 2009-08-20

    sec   4096R/E2B054B8 2009-08-20
    uid                  Alice Example (EXAMPLE NEW KEY) <alice@example.org>
    ssb   4096R/4A6D5217 2009-08-20
```

Alice verifies that details for only two keys are listed and that there are no unexpected additions.

The `sec` lines are:

```
    :::text
    sec   1024D/AD741727 2009-08-20
```

and

```
    :::text
    sec   4096R/E2B054B8 2009-08-20
```

The key ID forms part of the second column, to the right of the key length. In this case the key IDs are `AD741727` and `E2B054B8`. The
[comments](release-signing.html#key-comment) help Alice identify each key.

<h3 id="find-key-id-otherwise">When you do not have the secret key</h3>

Unless you have the [private key](release-signing.html#public-private) or a [fingerprint](release-signing.html#fingerprint), the only safe way to find the key ID is to ask the owner of the key, using a secure communication channel.

Trusting that an import contains only the owner's public key is **not recommended**. The import may contain additional public keys (intentionally or not). So, when using an import, always verify the key ID of interest from another source.

For example, a <a href="http://home.apache.org/~rdonkin/" target="_blank">web page with an embedded export</a> should also list the key IDs of interest. 

<h2 id="backup">How to back up</h2>

<h3 id="backup-public">Back up public information</h3>

The [key ID](release-signing.html#key-id) is not confidential but without access to this information from a trusted source, substitution attacks are [feasible](release-signing.html#infeasible) (see this [discussion](#find-key-id)).

So, for each [key pair](release-signing.html#public-private) you generate, the [key ID](release-signing.html#key-id) needs to recorded in a form that makes tampering difficult. Defense in depth is the best strategy. We recommend that you use a range of methods::

  - Print a hard copy of the key ID and store it securely
  - Include the key ID on your business cards
  - ASF Members should include the key ID on their Apache business cards
  - Include a text document containing the key ID in your [secure, tamperproof private backups](#backup-private)
  
<h3 id="backup-private">Back up private information</h3>

Keep your [private key](release-signing.html#public-private) both safe and away from attackers. If a private key is destroyed or lost, it must be revoked and should no longer be used. Given the effort that's needed to build a strong [web of trust](release-signing.html#web-of-trust), it is important to back up the private key without compromising security.

The best way to back up a private key is to securely archive the entire [GnuPG home](#home) by copying the contents into secure, encrypted storage. We recommended that you version each archived copy and store it permenantly.

Full disk encryption is the best storage solution for disks containing the private key. How to encrypt a full disc is platform dependent and is beyond the scope of this guide, but many major platforms now support this.

Choose a strong passphrase. If this is not possible then use strong, [symmetric](#symmetric) encryption to protect a compressed archive.

We recommend a removable medium type with good long term storage characteristics:

  - A small capacity, high quality USB flash drive
  - A CDROM

Make and securely store multiple copies.

<h2 id="export-key">How to export a key</h2>

Exporting public keys is a common operation. It is rarely necessary to export a [private key](release-signing.html#public-private) and use of that operation should be kept to a minimum (see [below](#export-secret-key) ). So, the unqualified term *exporting a key*
almost always means *exporting a public key*.

GnuPG seeks to limit accidental private key exports by using different operations for each export. Both operations share common options.

<h3 id="export-option-output">Output options</h3>

By default, operations print their results to the command line. For example, to export all public keys (with ASCII encoding) to the command line, do:

```
    :::console
    $ gpg --export --armor 
```

The `--output` option followed by the name of a file creates that file and stores the output in it. To export all public keys (with ASCII encoding) into a newly created file named `export.asc`, use:

```
    :::console
    $ gpg --export --output export.asc --armor 
```

Though most of the examples in this guide choose to output to a file, command line output is often useful (for example, the output can be piped into a second command) and is equally valid for most operations. The exception is [secret key export](#export-secret-key), which should always be to a secure temporary file.

<h3 id="export-option-armor">The armor option</h3>

The *--armor* option encodes the output using [ASCII characters only](release-signing.html#ascii). This permits embedding the output easily in documents and displaying it on the command line.

For example, to export all public keys (to the command line) encoded in ASCII, use:

```
    :::console
    $ gpg --export --armor 
```

The binary format is shorter but has few other advantages. For all uses at Apache, use ASCII armor.

<h3 id="export-public-key">How to export public keys</h3>

The `--export` operation exports public keys.

When you don't specify a key, the system exports all public keys in the keyring. For example, to export all public keys to the [command
line](#export-option-output) with [ASCII encoding](#export-option-armor):

```
    :::console
    $ gpg --export --armor 
```

To export specific keys, add identifiers for these keys to the end of the command. There are a number of ways to identify keys, but only the [key ID](release-signing.html#key-id) will definitely select a single key. This [guide](#find-key-id) discusses how to find the key ID when it is unknown.

For example, to export to the [command line](#export-option-output) with [ASCII encoding](#export-option-armor) the public key with ID `AD741727`, use:

```
    :::console
    $ gpg --export --armor AD741727
```

<h3 id="export-all-or-some-public-keys">Should I export all or some public keys"</h3>

This is often a tricky question. An import should not be trusted for key identification (see [discussion](#find-key-id)). So, for an import to be useful, usually the key ID of interest needs to be known.

Keys used at Apache should be available through the global [public keyserver](release-signing.html#keyserver) network. Using this network, given the [key ID](release-signing.html#key-id) the person who needs it can download the public key.

So an export is really only useful for someone who cannot use the global keyserver network. But in this case, the import really needs to include all the public keys on the ring to maximise the chances of a trusted path being found in the [web of trust](release-signing.html#web-of-trust).

The risk of exporting all keys is that users who don't understand that they should not use an export for key identification may be mislead by the other keys in the export. The risk with exporting just one public key is that users may mistakenly think that imports are trustworthy for key identification.

So neither is a very satisfactory solution. Now that global keyserver network works so well, Apache may move away from the use of exports in the future.

<h3 id="export-secret-key">How to export secret keys</h3>

This is a risky operation. The most vulnerable part of the system is the [passphrase](release-signing.html#passphrase) that encrypts the private key. If an attacker obtains a copy of the encrypted private key file, an attack on the passphrase is likely to be
[feasible](release-signing.html#infeasible). So it is vital to store the [private key](release-signing.html#public-private) securely at
all times.

There are very few occasions when this risk is justified. When people talk about exporting keys, this means the export of the *public* key only (unless the secret key is mentioned explicitly). Whenever a private key export is necessary for a task covered in this guide,  we describe the process completely in the section. We do not recommend secret key export in other circumstances.

To ensure that you do not accidentally expose private keys, the GnuPG `--export` operation exports only public keys.

**Never** export secret keys to the command line. Instead, use a secure temporary file that you can securelyi delete after use. Here is one way to do this:

<h2 id="secret-key-transfer">How to transfer a secret key</h2>

Start by [switching](#switch-home) GnuPG [home](#home) to the source. To export all secret keys to a temporary file such as `/tmp/new.sec`, do this:

```
    :::console
    $ gpg --export-secret-keys --armor --output /tmp/new.sec
```

Import this temporary file into the target keyring. Ensure that GnuPG [home](#home) is set to the target keyring (by either
[switching](#switch-home) the current session or opening a new terminal configured to use the target keyring). Then do this:

```
    :::console
    $ gpg --import /tmp/new.sec 
    gpg: key E2B054B8: secret key imported
    gpg: key E2B054B8: public key "Alice Example (EXAMPLE NEW KEY)
    <alice@example.org>" imported
    gpg: Total number processed: 1
    gpg:               imported: 1  (RSA: 1)
    gpg:       secret keys read: 1
    gpg:   secret keys imported: 1
```

Check for *secret keys imported* in the output. Listing secret keys for the target keyring should now show the existence of the secret key:

```
    :::console
    $ gpg --list-secret-keys
    alice/secring.gpg
    -----------------
    sec   1024D/AD741727 2009-08-20
    uid                  Alice Example (EXAMPLE OF OLD KEY) <alice@example.org>
    ssb   1024g/268883A9 2009-08-20

    sec   4096R/E2B054B8 2009-08-20
    uid                  Alice Example (EXAMPLE NEW KEY) <alice@example.org>
    ssb   4096R/4A6D5217 2009-08-20
```

Finally make sure that the temporary file you used cannot be read. We recommend secure deletion. If you are working on Linux, for example, you can use the <a href="http://www.linfo.org/shred.html" target="_blank">shred</a> command:

```
    :::console
    $ shred /tmp/new.sec 
    $ rm /tmp/new.sec 
```

Those using encrypted `tmp` should now restart the machine.

<h2 id="transition">How to transition from an old to a new key</h2>

If you have a short but uncompromised key and would like to [transition](release-signing.html#transition) to a longer one, follow these
[instructions](key-transition.html).

If your key has been compromised, you **must not** transition. Instead, [revoke](release-signing.html#revoke-key) the old key and replace it with a new one immediately. **Do not** use a transition period.

<h2 id="revocation-certs">How to use revocation certificates</h2>

When a private key is lost or compromised, a [revocation
certificate](release-signing.html#revocation-cert) should be
[distributed](release-signing.html#revoke-cert) to
[publicly](release-signing.html#keyserver)  [revoke the
key](release-signing.html#delete-vs-revoke). In the event of a compromise
or loss, it is best to create a new revocation certification including the
particulars of the case. Since this may not always be possible, generic
revocation certificates should be created for each new key pair
[generated](#generate-key) and [securely
stored](release-signing.html#revocation-certificate-storage).



















