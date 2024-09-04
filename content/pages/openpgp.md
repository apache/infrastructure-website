Title: Cryptography with OpenPGP
license: https://www.apache.org/licenses/LICENSE-2.0

### Contents ###

  - <a href="#introduction">Introduction</a>
  - <a href="#gnupg">Gnu Privacy Guard</a>
  - <a href="#generate-key">How to generate a strong key</a>
  - <a href="#private-keyring-management">Private keyring management</a>
 
 How to...
 
   - <a href="#find-key-id">find a key ID</a>
   - <a href="#backup">back up keys</a>
   - <a href="#export-key">export a key</a>
   - <a href="#secret-key-transfer">transfer a secret key</a>
   - <a href="#transition">transition from an old to a new key</a>
   - <a href="#revocation-certs">use revocation certificates</a>
   - <a href="#symmetric">use symmetric encryption</a>
   - <a href="#update">update Apache documents with details of a new key</a>
   - <a href="#wot">use the Web of Trust</a>


<h2 id="introduction">Introduction<a class="headerlink" href="#introduction" title="Permanent link">&para;</a></h2>

<a href="https://keys.openpgp.org/" target="_blank">OpenPGP</a> is encryption software. The program provides cryptographic privacy and authentication for data communication, covering signing, encrypting, and decrypting texts, e-mails, files, directories, and whole disk partitions and increasing the security of e-mail communications.

Reliable cryptography applications follow OpenPGP, an open standard of Pretty Good Privacy (PGP) encryption software, standard (RFC 4880), for encrypting and decrypting data.

<h2 id="gnupg">Gnu Privacy Guard (GPG)<a class="headerlink" href="#gnupg" title="Permanent link">&para;</a></h2>

The Apaches Software Foundation recommends using <a href="https://www.gnupg.org" target="_blank">Gnu Privacy Guard (GPG)</a>, a well-known open source cryptography tool with OpenPGP support. Always use the latest version.

GnuPG has a good set of <a href="https://www.gnupg.org/documentation" target="_blank">documentation</a>. This guide covers only some important points.

<h3 id="home">GnuPG Home<a class="headerlink" href="#home" title="Permanent link">&para;</a></h3>

GnuPG stores important files, including keyrings and configuration files, in a home directory. You can specify your project's home directory in an environmental variable or on the command line. This allows different configurations and keys to be used.

For example:

```
    $ gpg --homedir /home/alice/keys --list-keys
```

Projects generally rely on the default. For `\*nux` (linux, BSD, MacOSX, Solaris, AIX) this is:

```
    $HOME/.gnupg
```

<h4 id="switch-home">How to switch Home<a class="headerlink" href="#switch-home" title="Permanent link">&para;</a></h4>

You can set Home using an environmental variable. This lets you select a specific configuration and keyring for the duration of a
command line session. This is useful when [practicing](release-signing.html#safe-practice) and when using multiple keyrings.

For example, to set home directory to `alice` when using Linux:

```
    $ export GNUPGHOME=alice
```

When switching key rings, check that the required keyring has been selected by examining the secret keys. For example:

```
    $ gpg --list-secret-keys
    alice/secring.gpg
    -----------------

    sec   4096R/E2B054B8 2009-08-20
    uid   Alice Example (EXAMPLE NEW KEY) <alice@example.org>
    ssb   4096R/4A6D5217 2009-08-20
```

<h3 id="configuration">Configuration<a class="headerlink" href="#configuration" title="Permanent link">&para;</a></h3>

GnuPG supports a wide range of configuration options. You can specify them on the command line, but it is usually more convenient to set them in the `gpg.conf` file. By default, this is located in the [GnuPG Home](#home) directory.

<h3 id="sha1">Avoid SHA-1<a class="headerlink" href="#sha1" title="Permanent link">&para;</a></h3>

[Avoid](release-signing.html#sha1) using `SHA-1`. Use `SHA512` or `SHA256` instead. `SHA512` is stronger than `SHA256`. Though some old
clients lack `SHA512` support, we recommend switching to `SHA512` if possible.

<h3 id="sha-defaults">Setting defaults<a class="headerlink" href="#sha-defaults" title="Permanent link">&para;</a></h3>

To configure `gpg` to avoid SHA-1, edit the options in [`gpg.conf`](#configuration). Options need to be added or given the correct values for:

  -  `cert-digest-algo` - the certificate digest used when linking into the [web of trust](release-signing.html#link-into-wot) 
  -  `personal-digest-preferences` - the digest used for [signing messages](release-signing.html#detach-sig) 
  -  `default-preference-list` - the default algorithm preferences for [new keys](release-signing.html#generate) (this does not affect existing keys: see next paragraph)

To use `SHA512` (recommended):

```
    personal-digest-preferences SHA512
    cert-digest-algo SHA512
    default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 ZLIB BZIP2 ZIP Uncompressed
```

To use SHA256:

```
    personal-digest-preferences SHA256
    cert-digest-algo SHA256
    default-preference-list SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 ZLIB BZIP2 ZIP Uncompressed
```
    
<h3 id="key-prefs">Setting preferences for keys<a class="headerlink" href="#key-prefs" title="Permanent link">&para;</a></h3>

The digest preferences for each key (from the [configuration defaults](#sha-defaults) ) are set when the key is generated. Once the
configuration has been updated to avoid SHA-1, all new keys generated will use these defaults, but keys generated before the configuration won't be affected.

All existing private keys in the ring need to be updated to indicate that stronger hashes are preferred. For each public-private key pair (generated with the previous defaults):

```
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
    $ gpg --send-keys F8B7B4FD
```

<h2 id="generate-key">How to generate a strong key<a class="headerlink" href="#generate-key" title="Permanent link">&para;</a></h2>

The weaknesses found in [SHA-1](release-signing.html#sha1) threaten all DSA keys and those RSA keys with length less than 2048 bits. Though no realistic attack against those keys have been made public and these keys continue to be useful (and do not need to be revoked), Projects should not generate new keys that are exposed to this weakness.

The next generation of [OpenPGP](release-signing.html#openpgp) will use [SHA-3](release-signing.html#sha3). For now, the 2048 bit RSA keys with SHA256 hash should be strong enough. For those with 2048 bit RSA keys, the best advice is to [switch](#sha1) to SHA256 or SHA512 as soon as possible. All new keys generated should be RSA with at least 4096 bits.

Though 8192 bit keys are stronger, they are slower and may be incompatible with some older clients. For the present, 4096 bit RSA should be strong enough for code signing at Apache. To generate RSA keys with length more
than 4096 bits, <a href="https://www.jroller.com/robertburrelldonkin/entry/gnupg_8192bit_rsa_keys" target="_blank">changes are needed</a>. Then you can follow the procedure for 4096 bits.

<h3 id="key-gen-install-latest-gnupg">Install and configure GnuPG<a class="headerlink" href="#key-gen-install-latest-gnupg" title="Permanent link">&para;</a></h3>

<a href="https://www.gnupg.org" target="_blank">GnuPG</a> comes in two flavors. To easily generate a 4096 bit RSA signing and encryption key pair with strong digests, use either GnuPG version:

  -  `2.0.12` or higher (well-known, portable version)
  -  `1.4.10` or higher (version with advanced features)

Once you generate the key, you can use it with the widely available `1.4.9` and `2.x` releases. 

If the right version of GnuPG is not currently distributed for your platform, you need to <a href="http://www.gnupg.org/download/index.en.html" target="_blank">install it</a>. You only need this version to generate keys, so you do not need to replace the version distributed with your platform. You can install the new version into a working directory.

Checking that the installation has worked and that the version is correct, using either

```
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

<h3 id="key-gen-generate-key">Generate a new key<a class="headerlink" href="#key-gen-generate-key" title="Permanent link">&para;</a></h3>

Versions `2.0.12`and `1.4.10` introduced a new default key generation option - *RSA and RSA*. [RSA](release-signing.html#rsa)
keys are used for both encryption and signing. Longer key lengths are available. Select or accept this option when generating new keys.

Follow the recommendations about [user ID](release-signing.html#user-id) and [comment](release-signing.html#key-comment). Use a strong
[passphrase](release-signing.html#passphrase).

Follow either

```
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

<h3 id="key-gen-avoid-sha1">Check that the key avoids using SHA-1<a class="headerlink" href="#key-gen-avoid-sha1" title="Permanent link">&para;</a></h3>

Check that the configuration has correctly set the key preferences to avoid SHA-1, using either:

```
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

<h3 id="final-steps">Final steps<a class="headerlink" href="#final-steps" title="Permanent link">&para;</a></h3>

When you generate a new code signing key, you need to update a number of Apache documents and perform some other tasks.

<h5 id="generation-final-steps-transition">Final transition steps<a class="headerlink" href="#generation-final-steps-transition" title="Permanent link">&para;</a></h5>

If you are generating a key for use in a [transition](release-signing.html#transition), there is more you should do before updating these documents, so [go to the transition instructions now](key-transition.html#ContinueAfterGeneration).

<h5 id="generation-final-steps-new-key">New key final steps<a class="headerlink" href="#generation-final-steps-new-key" title="Permanent link">&para;</a>Final steps for a new key</h5>

If this is a new code signing key not involved with a transition:

  1.  [Upload](release-signing.html#keyserver-upload) the new [public key](release-signing.html#public-private) to a public
[keyserver](release-signing.html#keyserver) 

  1. Create backups by following these [instructions](#backup) 

  1. Follow these [instructions](#revocation-certs) to create and securely store generic [revocation
certificates](release-signing.html#revocation-cert) for the new key

  1. Follow these [instructions](#update) (ignoring the transition option) to create or update Apache documents

  1. Read this [guide](#wot) to the Apache use of the [web of trust](release-signing.html#web-of-trust) and make arrangements for your
new key to be included at the earliest opportunity.

<h2 id="private-keyring-management">Private keyring management<a class="headerlink" href="#private-keyring-management" title="Permanent link">&para;</a></h2>

  1. Never transmit your private keyring over the internet!

  2. Store your keys on unshared local disk storage. If your employer only provides networked storage, ask for permission to use a USB fob (or CD) to store your .gnupg directory.

  3. Destroy your retired disks appropriately using a disk wiping utility or similar tools to ensure your keyring is no longer available
on those disks once you are through with them. Failing that, drill through the disk platters so they are physically unusable.

<h2 id="find-key-id">Finding a key ID<a class="headerlink" href="#find-key-id" title="Permanent link">&para;</a></h2>

There are a number of ways to identify a key. Only one is unique: the [key fingerprint](release-signing.html#fingerprint).

Attackers can easily create new keys similar to yours with identical user IDs and comments. Such a public key may be introduced to your keyring when you download keys from a [public keyserver](release-signing.html#keyserver) or as part of an import. If this information is used to identify public keys then you may be misled into believing that another public key is yours. A cunning attacker may even introduce a matching secret key that lets you sign with that key.

Creating a different key with a matching identity is considered [infeasible](release-signing.html#infeasible). For all operations where
precise identity matters and that identity is specified on the command line, you should use the key ID to identify the key. Avoid using
user ID or other information.

<h3 id="find-key-id-from-trusted-source">Find a key ID from a trusted source<a class="headerlink" href="#finbd-key-id-from-trusted-source" title="Permanent link">&para;</a></h3>

The best way to find a key ID is to obtain it directly from a trusted source, for example, from a business card you obtain personally from the owner of the key.

<h3 id="find-key-id-with-fingerprint">Find a key ID with its fingerprint<a class="headerlink" href="#find-key-ide-with-fingerprint" title="Permanent link">&para;</a></h3>

If you have a [fingerprint](release-signing.html#fingerprint), the key ID should be the last 8 digits. For example, the ID of the key with this fingerprint:

```
    FF96 6261 C995 1DDE BF34  5150 D5D2 BDB5 E2B0 54B8
```

should be:

```
    E2B054B8
```

You can confirm this using:

```
    $ gpg --list-keys --fingerprint E2B054B8
    pub   4096R/E2B054B8 2009-08-20
          Key fingerprint = FF96 6261 C995 1DDE BF34  5150 D5D2 BDB5 E2B0 54B8
    uid                  Alice Example (EXAMPLE NEW KEY) <alice@example.org>
    sub   4096R/4A6D5217 2009-08-20
```

<h3 id="find-key-id-with-secret-key">When you have the secret key<a class="headerlink" href="#find-key-id-with-secret-key" title="Permanent link">&para;</a></h3>

When you have the secret key, listing the secret key details allows the key ID to be read from the `sec` lines in the output.

**Note** that it is possible for an attacker to introduce a new secret key into your keyring (for example, as part of an import). It is vital that you know how many secret keys each keyring should hold. If any unexpected secret keys are present, this probably indicates an attack.

For example, Alice is [transitioning](key-transition.html) and so expects two secret keys in her main keyring. (The case of a single key is similar but less complex.) She lists all secret keys on the keyring:

```
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
    sec   1024D/AD741727 2009-08-20
```

and

```
    sec   4096R/E2B054B8 2009-08-20
```

The key ID forms part of the second column, to the right of the key length. In this case the key IDs are `AD741727` and `E2B054B8`. The
[comments](release-signing.html#key-comment) help Alice identify each key.

<h3 id="find-key-id-otherwise">When you do not have the secret key<a class="headerlink" href="#find-key-id-otherwise" title="Permanent link">&para;</a></h3>

Unless you have the [private key](release-signing.html#public-private) or a [fingerprint](release-signing.html#fingerprint), the only safe way to find the key ID is to ask the owner of the key, using a secure communication channel.

Trusting that an import contains only the owner's public key is **not recommended**. The import may contain additional public keys (intentionally or not). So, when using an import, always verify the key ID of interest from another source.

For example, a <a href="http://home.apache.org/~rdonkin/" target="_blank">web page with an embedded export</a> should also list the key IDs of interest. 

<h2 id="backup">How to back up keys<a class="headerlink" href="#backup" title="Permanent link">&para;</a></h2>

<h3 id="backup-public">Back up public information<a class="headerlink" href="#backup-public" title="Permanent link">&para;</a></h3>

The [key ID](release-signing.html#key-id) is not confidential but without access to this information from a trusted source, substitution attacks are [feasible](release-signing.html#infeasible) (see this [discussion](#find-key-id)).

So, for each [key pair](release-signing.html#public-private) you generate, the [key ID](release-signing.html#key-id) needs to recorded in a form that makes tampering difficult. Defense in depth is the best strategy. We recommend that you use a range of methods::

  - Print a hard copy of the key ID and store it securely
  - Include the key ID on your business cards
  - ASF Members should include the key ID on their Apache business cards
  - Include a text document containing the key ID in your [secure, tamperproof private backups](#backup-private)
  
<h3 id="backup-private">Back up private information<a class="headerlink" href="#backup-private" title="Permanent link">&para;</a></h3>

Keep your [private key](release-signing.html#public-private) both safe and away from attackers. If a private key is destroyed or lost, it must be revoked and should no longer be used. Given the effort that's needed to build a strong [web of trust](release-signing.html#web-of-trust), it is important to back up the private key without compromising security.

The best way to back up a private key is to securely archive the entire [GnuPG home](#home) by copying the contents into secure, encrypted storage. We recommended that you version each archived copy and store it permanently.

Full disk encryption is the best storage solution for disks containing the private key. How to encrypt a full disc is platform dependent and is beyond the scope of this guide, but many major platforms now support this.

Choose a strong passphrase. If this is not possible then use strong, [symmetric](#symmetric) encryption to protect a compressed archive.

We recommend a removable medium type with good long term storage characteristics:

  - A small capacity, high quality USB flash drive
  - A CDROM

Make and securely store multiple copies.

<h2 id="export-key">How to export a key<a class="headerlink" href="#export-key" title="Permanent link">&para;</a></h2>

Exporting public keys is a common operation. It is rarely necessary to export a [private key](release-signing.html#public-private) and use of that operation should be kept to a minimum (see [below](#export-secret-key) ). So, the unqualified term *exporting a key*
almost always means *exporting a public key*.

GnuPG seeks to limit accidental private key exports by using different operations for each export. Both operations share common options.

<h3 id="export-option-output">Output options<a class="headerlink" href="#export-option-output" title="Permanent link">&para;</a></h3>

By default, operations print their results to the command line. For example, to export all public keys (with ASCII encoding) to the command line, do:

```
    $ gpg --export --armor 
```

The `--output` option followed by the name of a file creates that file and stores the output in it. To export all public keys (with ASCII encoding) into a newly created file named `export.asc`, use:

```
    $ gpg --export --output export.asc --armor 
```

Though most of the examples in this guide choose to output to a file, command line output is often useful (for example, the output can be piped into a second command) and is equally valid for most operations. The exception is [secret key export](#export-secret-key), which should always be to a secure temporary file.

<h3 id="export-option-armor">The armor option<a class="headerlink" href="#export-option-armor" title="Permanent link">&para;</a></h3>

The *--armor* option encodes the output using [ASCII characters only](release-signing.html#ascii). This permits embedding the output easily in documents and displaying it on the command line.

For example, to export all public keys (to the command line) encoded in ASCII, use:

```
    $ gpg --export --armor 
```

The binary format is shorter but has few other advantages. For all uses at Apache, use ASCII armor.

<h3 id="export-public-key">How to export public keys<a class="headerlink" href="#export-public-key" title="Permanent link">&para;</a></h3>

The `--export` operation exports public keys.

When you don't specify a key, the system exports all public keys in the keyring. For example, to export all public keys to the [command
line](#export-option-output) with [ASCII encoding](#export-option-armor):

```
    $ gpg --export --armor 
```

To export specific keys, add identifiers for these keys to the end of the command. There are a number of ways to identify keys, but only the [key ID](release-signing.html#key-id) will definitely select a single key. This [guide](#find-key-id) discusses how to find the key ID when it is unknown.

For example, to export to the [command line](#export-option-output) with [ASCII encoding](#export-option-armor) the public key with ID `AD741727`, use:

```
    $ gpg --export --armor AD741727
```

<h3 id="export-all-or-some-public-keys">Should I export all or some public keys"<a class="headerlink" href="#export-all-or-some-puiblic-keys" title="Permanent link">&para;</a></h3>

This is often a tricky question. An import should not be trusted for key identification (see [discussion](#find-key-id)). So, for an import to be useful, usually the key ID of interest needs to be known.

Keys used at Apache should be available through the global [public keyserver](release-signing.html#keyserver) network. Using this network, given the [key ID](release-signing.html#key-id) the person who needs it can download the public key.

So an export is really only useful for someone who cannot use the global keyserver network. But in this case, the import really needs to include all the public keys on the ring to maximise the chances of a trusted path being found in the [web of trust](release-signing.html#web-of-trust).

The risk of exporting all keys is that users who don't understand that they should not use an export for key identification may be mislead by the other keys in the export. The risk with exporting just one public key is that users may mistakenly think that imports are trustworthy for key identification.

So neither is a very satisfactory solution. Now that global keyserver network works so well, Apache may move away from the use of exports in the future.

<h3 id="export-secret-key">How to export secret keys<a class="headerlink" href="#export-secret-key" title="Permanent link">&para;</a></h3>

This is a risky operation. The most vulnerable part of the system is the [passphrase](release-signing.html#passphrase) that encrypts the private key. If an attacker obtains a copy of the encrypted private key file, an attack on the passphrase is likely to be
[feasible](release-signing.html#infeasible). So it is vital to store the [private key](release-signing.html#public-private) securely at
all times.

There are very few occasions when this risk is justified. When people talk about exporting keys, this means the export of the *public* key only (unless the secret key is mentioned explicitly). Whenever a private key export is necessary for a task covered in this guide,  we describe the process completely in the section. We do not recommend secret key export in other circumstances.

To ensure that you do not accidentally expose private keys, the GnuPG `--export` operation exports only public keys.

**Never** export secret keys to the command line. Instead, use a secure temporary file that you can securely delete after use. Here is one way to do this:

<h2 id="secret-key-transfer">How to transfer a secret key<a class="headerlink" href="#secret-key-transfer" title="Permanent link">&para;</a></h2>

Start by [switching](#switch-home) GnuPG [home](#home) to the source. To export all secret keys to a temporary file such as `/tmp/new.sec`, do this:

```
    $ gpg --export-secret-keys --armor --output /tmp/new.sec
```

Import this temporary file into the target keyring. Ensure that GnuPG [home](#home) is set to the target keyring (by either
[switching](#switch-home) the current session or opening a new terminal configured to use the target keyring). Then do this:

```
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
    $ shred /tmp/new.sec 
    $ rm /tmp/new.sec 
```

Those using encrypted `tmp` should now restart the machine.

<h2 id="transition">How to transition from an old to a new key<a class="headerlink" href="#transition" title="Permanent link">&para;</a></h2>

If you have a short but uncompromised key and would like to [transition](release-signing.html#transition) to a longer one, follow these
[instructions](key-transition.html).

If your key has been compromised, you **must not** transition. Instead, [revoke](release-signing.html#revoke-key) the old key and replace it with a new one immediately. **Do not** use a transition period.

<h2 id="revocation-certs">How to use revocation certificates<a class="headerlink" href="#revocation-certs" title="Permanent link">&para;</a></h2>

When a private key is lost or compromised, a [revocation certificate](release-signing.html#revocation-cert) should be
[distributed](release-signing.html#revoke-cert) to [publicly](release-signing.html#keyserver)  [revoke the key](release-signing.html#delete-vs-revoke). In the event of a compromise or loss of the key, it is best to create a new revocation certification including the particulars of the case. Since this may not always be possible, you can [generate](#generate-key) and [securely
store](release-signing.html#revocation-certificate-storage) generic revocation certificates for each new key pair.

<h3 id="revocation-cert-generic">Generic revocation certificates<a class="headerlink" href="#revocation-cert-generic" title="Permanent link">&para;</a></h3>

When you create a new [key pair](release-signing.html#public-private), also generate and store generic revocation certificates for that key pair. We recommend that you generate a certificate (following the instructions in the next section) for each appropriate
revocation reason type:

  - No reason specified
  - Key has been compromised
  - Key is no longer used

Note that *Key is superseded* is not appropriate for a new key since it is not possible to know which key will replace it.

Store your generic revocation certificates securely until you need to use them. If an attacker obtains a revocation certificate, they will be able to deny your use of the key by publishing it. The private key is not compromised by this act and this limits the harm they can do. However, you will need to generate a new key to replace the one that has been revoked, rebuild the [web of trust](release-signing.html#web-of-trust) and follow the [Apache revocation process](release-signing.html#revoke-cert).

We recommend that you store these certificates directly onto secure media with good long term stability (for example, an encrypted file
system on a top end USB drive or a CDROM). Print and store hard copies of the certificates yourself, and with trusted third parties.

<h3 id="revocation-cert-gen">How to generate a revocation certificate<a class="headerlink" href="#revocation-cert-gen" title="Permanent link">&para;</a></h3>

Revocation certificates include a small amount of additional information"

One of four machine readable reason types:

  - No reason specified - *a catch-all category* 
  - Key has been compromised - *also use this if you believe that the key may have been compromised (for example, when a storage device containing the private key has been lost)* 
 - Key is superseded - *the comment should suggest the replacement key* 
 - Key is no longer used - *useful when the key has been destroyed and so a generic revocation prepared earlier must be used* 

The certificate also includes a human-readable *comment*. Explain here the reason why you are revoking the key. This lets those affected by the revocation to formulate an appropriate response.

When a key has been compromised, lost or superseded, when possible generate a new certificate containing a comment explaining the
situation. For example, generate an [ASCII armored](release-signing.html#ascii) (for
ease of handling) revocation certificate for key `AD741727` like this:

```
    $ gpg --output revoke-AD741727.asc --armor --gen-revoke AD741727

    sec  1024D/AD741727 2009-08-20 Alice Example (EXAMPLE OF OLD KEY)
    <alice@example.org>

    Create a revocation certificate for this key? (y/N) y
    Please select the reason for the revocation:
      0 = No reason specified
      1 = Key has been compromised
      2 = Key is superseded
      3 = Key is no longer used
      Q = Cancel
    (Probably you want to select 1 here)
    Your decision? 1
    Enter an optional description; end it with an empty line:
    > THIS IS AN EXAMPLE MESSAGE DESCRIBING THAT THIS KEY WAS COMPROMISED    
    > 
    Reason for revocation: Key has been compromised
    THIS IS AN EXAMPLE MESSAGE DESCRIBING THAT THIS KEY WAS COMPROMISED
    Is this okay? (y/N) y

    You need a passphrase to unlock the secret key for
    user: "Alice Example (EXAMPLE OF OLD KEY) <alice@example.org>"
    1024-bit DSA key, ID AD741727, created 2009-08-20

    Revocation certificate created.

    Please move it to a medium which you can hide away; if Mallory gets
    access to this certificate he can use it to make your key unusable.
    It is smart to print this certificate and store it away, just in case
    your media become unreadable.  But have some caution:  The print system of
    your machine might store the data and make it available to others!
```

When preparing generic certificates (for use if the [private key](release-signing.html#public-private) is unavailable), the comment
cannot include the specifics and so should indicate this. 

The process for generating a generic certificate is identical, but you should add a different comment. For example, generate an [ASCII armored](release-signing.html#ascii) (for ease of handling) revocation certificate for key `AD741727` like this:

```
    $ gpg --output revoke-AD741727.asc --armor --gen-revoke AD741727

    sec  1024D/AD741727 2009-08-20 Alice Example (EXAMPLE OF OLD KEY)
    <alice@example.org>

    Create a revocation certificate for this key? (y/N) y
    Please select the reason for the revocation:
      0 = No reason specified
      1 = Key has been compromised
      2 = Key is superseded
      3 = Key is no longer used
      Q = Cancel
    (Probably you want to select 1 here)
    Your decision? 1
    Enter an optional description; end it with an empty line:
    > This revocation certificate was generate when the key was created.     
    > 
    Reason for revocation: Key has been compromised
    This revocation certificate was generate when the key was created.  
    Is this okay? (y/N) y

    You need a passphrase to unlock the secret key for
    user: "Alice Example (EXAMPLE OF OLD KEY) <alice@example.org>"
    1024-bit DSA key, ID AD741727, created 2009-08-20

    Revocation certificate created.

    Please move it to a medium which you can hide away; if Mallory gets
    access to this certificate he can use it to make your key unusable.
    It is smart to print this certificate and store it away, just in case
    your media become unreadable.  But have some caution:  The print system of
    your machine might store the data and make it available to others!
```

<h2 id="symmetric">How to use symmetric encryption<a class="headerlink" href="#symmetric" title="Permanent link">&para;</a></h2>
    
GnuPG supports symmetric (in addition to public key) cryptography, but the ciphers available sometimes differ. Use `gpg --version` to discover which ciphers are available in the current installation:

```
    $ gpg --version
    gpg (GnuPG) 1.4.9
    Copyright (C) 2008 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later
    <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Home: alice
    Supported algorithms:
    Pubkey: RSA, RSA-E, RSA-S, ELG-E, DSA
    Cipher: 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH
    Hash: MD5, SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
    Compression: Uncompressed, ZIP, ZLIB, BZIP2
```

In this case, the available ciphers are:

```
    3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH
```

Note that most of the ciphers early on the list are weak. This is typical. We recommend that you specify a strong cipher on the command
line. For example, to encrypt a document `INPUT_FILENAME` using `AES256` (a strong cipher) and output it to file `ENCRYPTED_FILE`:

```
    $ gpg --cipher-algo AES256 --output ENCRYPTED_FILE --symmetric INPUT_FILENAME
```

When prompted for a [passphrase](release-signing.html#passphrase), choose a strong one.

The file format contains metadata, including the cipher used. So to decrypt `ENCRYPTED_FILE` into `OUTPUT_FILE` use:

```
    $ gpg --output OUTPUT_FILE --decrypt ENCRYPTED_FILE
```

<h2 id="update">How to update Apache documents with details of a new key<a class="headerlink" href="#update" title="Permanent link">&para;</a></h2>

For the new key, you will need to provide both the [fingerprint](release-signing.html#fingerprint) and the [public key](release-signing.html#public-private) export more than once. We repeat the creation instructions below for each case but you may find it more convenient to create, store then reuse the results.

<h3 id="publish-in-web-space">Publish the new public key<a class="headerlink" href="#publish-in-web-space" title="Permanent link">&para;</a></h3>

**Note**: you must [upload signing keys to a public key server](release-signing.html#keyserver-upload). You must also add them to your LDAP record using the Apache <a href="https://id.apache.org" target="_blank">self-service app</a>.

A reliable, permanent URL for your new public key is useful. Your Apache web space is an ideal location for this. Copy an
[ASCII armored](release-signing.html#ascii) [public key](release-signing.html#public-private) 
[export](release-signing.html#export) (see instructions later, or use documents you created earlier) into the `public_html` subdirectory of your home on <a href="https://home.apache.org" target="_blank">home.apache.org</a>.

The suffix `.asc` is conventional for ASCII armored public key exports. So, for example, `A6EE6908.asc` is a reasonable choice for the export of key `A6EE6908`. Record the URL (for example `http://home.apache.org/~rdonkin/A6EE6908.asc` ) for use later in your
[FOAF](#foaf).

If your Apache home page contains details of your keys (recommended), update the [fingerprints](release-signing.html#fingerprint) and the [ASCII armored](release-signing.html#ascii) [public key](release-signing.html#public-private) [export](release-signing.html#export). Any browser with a suitable [OpenPGP](release-signing.html#openpgp) plugin (for example, <a href="https://www.mozilla.com/firefox/" target="_blank">Firefox</a> with the <a href="https://www.getfiregpg.org" target="_blank">FireGPG plugin</a>) will let you download the key into the local keyring.

For example, <a href="https://home.apache.org/~rdonkin/" target="_blank">this home page contains a section with fingerprints and a for exporting them. At the bottom, the export has been inlined so browsers with [OpenPGP](release-signing.html#opengpg) support can import the keys.

To create an [ASCII armored](release-signing.html#ascii) [public key](release-signing.html#public-private) [export](release-signing.html#export):

  - When using a [transition](release-signing.html#transition), follow these [instructions](key-transition.html#transition-export).
  - Otherwise this [discussion](#export-key) describes how to export public keys.

To find the [fingerprint](release-signing.html#fingerprint) for a key:

  - When using a [transition](release-signing.html#transition), follow these [instructions](key-transition.html#transition-fingerprints).
  - Otherwise use `gpg --fingerprint`.
  
Ensure that each `pubkeyAddress` points to the new export [uploaded into your Apache home web space](#publish-in-web-space).

 When [transitioning](release-signing.html#transition), include one entry for the old and one for the new key. Yu can use the same URL for both since the target should be the [dual export](key-transition.html#transition-export) you [uploadedearlier](#publish-in-web-space). For example, for keys A6EE6908 (new) and B1313DE2 (old):

```
    <wot:hasKey>
      <wot:PubKey>
        <wot:hex_id>A6EE6908</wot:hex_id>
        <wot:fingerprint>597C729B02371932E77CB9D5EDB8C082A6EE6908</wot:fingerprint>
        <wot:pubkeyAddress
            rdf:resource="http://home.apache.org/~rdonkin/A6EE6908.asc"/>
      </wot:PubKey>
      <wot:PubKey>
        <wot:hex_id>B1313DE2</wot:hex_id>
        <wot:fingerprint>EA6141E8E49E560C224B2F74D5334E75B1313DE2</wot:fingerprint>
        <wot:pubkeyAddress
            rdf:resource="http://home.apache.org/~rdonkin/A6EE6908.asc"/>
      </wot:PubKey>
    </wot:hasKey>
```

<h3 id="update-KEYS">Update keys on the next release<a class="headerlink" href="#update-KEYS" title="Permanent link">&para;</a></h3>

Projects maintain [KEYS](release-signing.html#keys-policy) files containing the public keys used to sign Apache releases. These documents need not be updated immediately, but you **must** update your project's file with the new key, with an export, before publishing a release using the new key.

To create an [ASCII armored](release-signing.html#ascii) [export](release-signing.html#export):

  - When using a [transition](release-signing.html#transition), follow these [instructions](key-transition.html#transition-export).
  - Otherwise this [discussion](#export-key) describes how to export public keys

If there is an older export in the `KEYS` file, only remove it if it has not been used to sign a release. It is important
that the KEYS file can also be used to check archived releases.

<h3 id="members-details">ASF Members only: update details<a class="headerlink" href="#members-details" title="Permanent link">&para;</a></h3>

<a href="https://www.apache.org/foundation/members.html" target="_blank">ASF Members</a> should add the new key to their details stored in Subversion.

Update your Apache business card with fingerprints (see `Cards` directory in the members area in Subversion) and place a new order for cards.

<h2 id="wot">How to use the Web of Trust<a class="headerlink" href="#wot" title="Permanent link">&para;</a></h2>

A link to a new key from a [web of trust](release-signing.html#web-of-trust) is made when a key that is part of that network signs the new key.

Each link is only one way. By signing a key, you indicate that you have verified the identity of the owner of that key. Links are established in both directions once the owner of that key also signs your key. When the owner has suitable identification, expect the owner to ask you to sign their key in return.

You can use directional links to establish trust in the identity of a key whose owner you haven't met.

<h3 id="wot-verifying-links">How to verify identity<a class="headerlink" href="#wot-verifying-links" title="Permanent link">&para;</a></h3>

Verifying identities is usually automated, but here is an example to explain the process. If you already understand the process, feel free to [skip forward](#apache-wot).

<h4 id="wot-manual-example">Example - the hard way<a class="headerlink" href="#wot-manual-example" title="Permanent link">&para;</a></h4>

Take Alice, Bob and Charlie. Alice has verified Bob's identity in person. Bob has verified Charlie's identity in person. But Alice has
never met Charlie. So

  - Bob's key has been signed by Alice's key
  - Charlie's key has been signed by Bob's key

Alice has obtained a file ( `document` in this example) which Charlie may have created, and a detached signature for that file ( `document.asc` in this example). Alice wishes to discover whether Charlie signed this file.

The basic idea is easy. If Alice has verified Bob's identity and trusts Bob to verify the Charlie's identity before signing, then Alice should be able to work out whether Charlie owns the key which was used to sign the file.

Alice starts by verifying the signature:

```
    $ gpg --verify document.asc 
    gpg: Signature made Wed Sep  9 14:33:12 2009 BST using RSA key ID 8F8A2525
    gpg: Can't check signature: public key not found
```

This indicates that the key used to create this signature is missing from Alice's keyring. This is not unexpected. Alice adds the public key, perhaps by using a public key server or by importing an export, and tries again:

```
    $ gpg --verify document.asc 
    gpg: Signature made Wed Sep  9 14:33:12 2009 BST using RSA key ID 8F8A2525
    gpg: checking the trustdb
    gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
    gpg: depth: 0  valid:   1  signed:   1  trust: 0-, 0q, 0n, 0m, 0f, 1u
    gpg: depth: 1  valid:   1  signed:   0  trust: 1-, 0q, 0n, 0m, 0f, 0u
    gpg: Good signature from "Charlie (EXAMPLE ONLY NOT FOR DISTRIBUTION)
    <charlie@example.org>"
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the
    owner.
    Primary key fingerprint: B7F6 17FA 4DEF E61F 37A4  7463 41F4 40D4 8F8A 2525
```

This output indicates that this key says that Charlie created it. This is a reasonable start but is easily faked.

Alice examines the signatures on this key:

```
    $ gpg --list-sigs 8F8A2525
    pub   2048R/8F8A2525 2009-09-09
    uid                  Charlie (EXAMPLE ONLY NOT FOR DISTRIBUTION) <charlie@example.org>
    sig 3       8F8A2525 2009-09-09  Charlie (EXAMPLE ONLY NOT FOR DISTRIBUTION) <charlie@example.org>
```

This key is signed only by itself. This is not indicative. Unless all keys in the ring have been refreshed, it is possible that a signature has been made but is missing from the ring. Alice refreshes the keys on the ring then verifies once more:

```
    $ gpg --list-sigs 8F8A2525
    pub   2048R/8F8A2525 2009-09-09
    uid                  Charlie (EXAMPLE ONLY NOT FOR DISTRIBUTION) <charlie@example.org>
    sig 3       8F8A2525 2009-09-09  Charlie (EXAMPLE ONLY NOT FOR DISTRIBUTION) <charlie@example.org>
    sig         1B912854 2009-09-09  Bob___ (EXAMPLE ONLY NOT FOR DISTRIBUTION) <bob@example.org>
```

The key now has a signature from Bob's key - or so says the key. But Alice has met Bob. So, she lists the signatures for that key that may - or may not - be owned by Bob:

```
    $ gpg --list-sigs 1B912854
    pub   2048R/1B912854 2009-09-09
    uid                  Bob___ (EXAMPLE ONLY NOT FOR DISTRIBUTION) <bob@example.org>
    sig 3       1B912854 2009-09-09  Bob___ (EXAMPLE ONLY NOT FOR DISTRIBUTION) <bob@example.org>
    sig         81590910 2009-09-09  Alice (EXAMPLE ONLY NOT FOR DISTRIBUTION) <alice@example.org>
```

Alice finds it signed by `81590910` - the master key for this keyring. Alice can therefore trust that Charlie has signed the file provided so long as Alice trusts Bob to verify Charlie's identity.

<h4 id="wot-automated">Automated trust<a class="headerlink" href="#wot-automated" title="Permanent link">&para;</a></h4>

Most clients allow automation of this process of transitive trust resolution. This is easier and more convenient than by hand but clients differ in the amount of human control they provide. Some clients (including GnuPG) are highly configurable (allowing different trust models to be used) and allow finely grained control over trust placed in each signed key. For more details see <a href="https://www.gnupg.org/gph/en/manual.html" target="_blank">The GNU Privacy Handbook</a<

<h3 id="apache-wot">Code signing keys and the Web of Trust<a class="headerlink" href="#apache-wot" title="Permanent link">&para;</a></h3>

It is vital that Apache code signing keys are linked into a strong [web of trust](release-signing.html#web-of-trust). This allows independent verification of the fidelity of Apache releases by anyone strongly linked to this web. In particular, this lets two important groups independently verify releases:

  - The Apache Infrastructure Team
  - Downstream packagers

The Apache web of trust is reasonably well connected to the wider-open source web of trust. Though every opportunity should be taken to link into wider networks, the most important action needs to be to plan to exchange signatures with other Apache committers.

<h3 id="apache-wot-link">How to link into the Apache Web of Trust<a class="headerlink" href="#apache-wot-link" title="Permanent link">&para;</a></h3>

The process (explained below) is the same but the people are different: this means arranging to meet in person with Apache committers. For a global distributed organisation like Apache, this is not always easy and usually takes some planning.

<h4 id="wot-apachecon">Keysigning at ApacheCon<a class="headerlink" href="#wot-apachecon" title="Permanent link">&para;</a></h4>

Apache organizes a major [keysigning party](release-signing.html#key-signing-party) at every <a href="https://apachecon.com/" target="_blank">ApacheCon</a>. This is a great opportunity to collect dozens of signatures.

<h4 id="wot-apache-other-events">Keysigning at other Apache events<a class="headerlink" href="#wot-apache-other-events" title="Permanent link">&para;</a></h4>

Other Apache events may also hold keysigning parties (and most will if asked). Typically, these will be smaller and less informal.

<h4 id="wot-apache-party">Informal Apache meetings<a class="headerlink" href="#wot-apache-party" title="Permanent link">&para;</a></h4>

Smaller, informal Apache-sponsored meetings are also an opportunity to swap keys (as well as gossip) with other committers.

Subscribe to the party list (see committer documentation) to find out about informal meetings. When you travel, take advantage of this opportunity to meet up with other Apache committers by posting to the party list. The <a href="https://community.zones.apache.org/map.html" target="_blank>committer map</a> shows locations for many committers. If there are committers near you, you can organise an informal meetup.

<h3 id="wot-link-in">How to link into a public web of trust<a class="headerlink" href="#wot-link-in" title="Permanent link">&para;</a></h3>

In short, expect that:

  - this will involve a face-to-face meeting
  - you will have to provide some sort of real-world identification, like a driver's license
  - you will be asked to verify their identity and sign their public key in
exchange

Bring the key [fingerprint](release-signing.html#fingerprint) but keep the private key safely at home.

<h4 id="wot-public-preparations">Be prepared<a class="headerlink" href="#wot-public-preparations" title="Permanent link">&para;</a></h4>

A small amount of preparation (before attending technical conferences or meetings) lets you exchange keys easily (if the other person is suitably prepared) or get your key signed if the opportunity presents itself. All that is required is suitable identification and the [public key fingerprint](release-signing.html#fingerprint) (which can can be conveniently printed onto a small card).

<h4 id="wot-public-keysigning">Keysigning parties<a class="headerlink" href="#wot-public-keysigning" title="Permanent link">&para;</a></h4>

The most effective way to achieve this is to attend a [key signing party](release-signing.html#key-signing-party). Apache and many other open-source organisations organize parties at their conferences. It may also be possible to arrange such a party at other events.

Expect to:

  - bring identification
  - bring a hard copy of your key's [fingerprint](release-signing.html#fingerprint) 
  - supply the key ID or public key to the organiser before the party
  - check that the [fingerprint](release-signing.html#fingerprint) for your key supplied by the organiser matches your hard copy
  - confirm this to those present

Do **not** bring your private key. This **must** stay safe and secure at all times. Wait until the conference has finished and you have returned home before signing keys.

For more information, see this <a href="https://www.cryptnet.net/fdp/crypto/keysigning_party/en/keysigning_party.html" target="_blank">guide</a>.
