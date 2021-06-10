Title: Using the Digicert code signing service

## Transition to DigiCert
We have moved from the old Symantec service to the new DigiCert service. The Symanetc service is no longer avaialble. All new signing must be via the DigiCert service.

If you require assistance migrating to the DigiCert service, please open an <a href="https://issues.apache.org/jira/browse/INFRA">INFRA Jira ticket</a> and select code signing as the component.

## DigiCert Secure Software
DigiCert Secure Software supports a range of signing tools and formats. For the full list see the [client user guide](https://digicert.github.io/snowbird-doc/#/administration-guides/secure-software-manager/index). Whichever signing option you choose, you will need to complete four steps:

1. Obtain a DigiCert ONE account
1. Obtain credentials for code signing
1. Install the OS integration for your chosen OS (Windows or Linux)
1. Configure your chosen signing tool.

### Step 1: Obtaining a DigiCert ONE account

Adding a new PMC or a new user to an existing PMC needs to be performed by the infrastructure team. Please open an <a href="https://issues.apache.org/jira/browse/INFRA">INFRA Jira ticket</a> and select code signing as the component.

When the infrastructure team create your accout you will be sent a password reset email. The link in that email is only valid for 12 hours. If you are unable to complete the creation of your account in that time you can request a new password reset email by going to [DigiCert ONE](https://one.digicert.com/) and clicking on the password reset link. Your username is the same as your ASF email address. You should then receive a new password reset email you can use to set your password. You will also need to configure your OTP token. Officially, only Google authenticator is supported but any similar tool should also work.

### Step 2: Obtaining credentials for code signing

Whatever you need to sign and however you choose to sign it, you will need to create credentials to use the signing API. You create these via the DigiCert ONE web interface.

1. Log on to [DigiCert ONE](https://one.digicert.com/).
1. Select "Account" from the menu in the top right-hand corner.
1. Select "Access" in the left-hand menu.
1. Select "API token" and create a new API token with your ASF id as the name and an expiry date ~1 year in the future.
1. Keep a record of the token value
1. Select "Client Auth" and create a new client certificate with your ASF id as the name and an expiry date ~1 year in the future.
1. Download the certificate and keep a record of the password

### Step 3: Install the OS integration

#### Windows integration

1. Log on to DigiCert ONE and select "Secure Software" from the menu in the top right-hand corner.
1. Select "Resources" in the left-hand menu.
1. Download and install the "Secure Software Manager Windows Clients Installer".
1. As per the [Windows Configuration](https://digicert.github.io/snowbird-doc/#/administration-guides/secure-software-manager/windows-configuration) section of the client user guide, create the four system environment variables. These **must** always be set to use the DigiCert signing service.
1. Test with `smctl.exe keypair ls`. You should see at least one certificate listed. (smctl.exe is installed as part of the DigiCert client and won't be on your path.)
1. Test with `certutil.exe -csp "DigiCert Signing Manager KSP" -key -user`. You should see at least one key listed. (certutil.exe will be on your path.)
1. Synchronise certificates with `smksp_cert_sync.exe`.
1. Open `certmgr.msc` (it will be on your path) and you should see your code signing certificate(s) listed under personal certificates. If a new certificate is issued to your PMC you will need to repeat this step.

#### Linux integration

1. Log on to DigiCert ONE and select "Secure Software" from the menu in the top right-hand corner.
1. Select "Resources" in the left-hand menu.
1. Download and install the "Secure Software Manager Linux Clients (Portable tar.gz)".
1. Unpack the tar.gz. Infra recommends, and this guide assumes, it is unpacked to `/opt`
1. As per the DigiCert ONE documentation, create the four required environment variables. These **must** always be set to use the DigiCert signing service. Infra recommends you store your certifcate in `~/.digicertone/`.
1. Test with `/opt/smtools-linux-x64/smctl keypair ls`. You should see at least one certificate listed.

### Step 4: Configure your chosen signing tool

#### Signing Windows binaries on Windows using signtool.exe

To sign Windows binaries you will need a copy of SignTool.exe. This can be found in both Visual Studio and the Windows SDK. Very old versions only support SHA-1 signing. Version 6.1.7600.16385 (2009-07-14) supports newer hashes for signing.

You'll need the fingerprint of the certificate you want to use for signing (view via `certmgr.msc`). You can then sign a file with `signtool.exe sign /sha1 <cert-fingerprint> /fd sha512 /tr http://timestamp.digicert.com <file-to-be-signed>`

To sign a file with SHA-256 rather than SHA-512 use `... /fd sha256...` rather than `... /fd sha512 ...`.

#### Signing on Windows binaries on Windows with JSign Ant task

1. Make JSign JAR from [Maven Central](https://search.maven.org/artifact/net.jsign/jsign) available to Ant.
1. Create the PKCS11 configuration file. Infra recommends saving this as `%USERPROFLE%\.digicertone\pkcs11properties.cfg`. The contents should be:

        name=DigiCertONE
        library="C:/Program Files/DigiCert/DigiCert One Signing Manager Tools/smpkcs11.dll"
        slotListIndex=0

    `name` can be anything you like (although names with spaces and special characters haven't been tested). `library` must point to where you installed the Secure Software Manager Windows Clients. Note the use of `/` rather than `\` in the path even though this is Windows.

When configuring the [JSign Ant task](https://ebourg.github.io/jsign/#ant) `keystore` should be set to the full path of the `pkcs11properties.cfg` file.

#### Signing Windows binaries on Linux with JSign

1. Download jsign `wget https://github.com/ebourg/jsign/releases/download/3.1/jsign_3.1_all.deb`
1. Install jsign `sudo dpkg --install jsign_3.1_all.deb`
1. Create the PKCS11 configuration file. Infra recommends saving this as `~/.digicertone/pkcs11properties.cfg`. The contents should be:

        name=DigiCertONE
        library="/opt/smtools-linux-x64/smpkcs11.so"
        slotListIndex=0

    `name` can be anything you like (although names with spaces and special characters haven't been tested). `library` must point to where you installed the Secure Software Manager Linux Clients.
1. You should then be able to sign with:

        jsign --keystore ~/.digicertone/pkcs11properties.cfg --storepass NONE --storetype PKCS11 --alias "<Your PMC Key alias>" --alg SHA-512 --tsaurl http://timestamp.digicert.com <file-to-be-signed>

#### Signing Windows binaries on Linux with JSign Ant task

1. Make JSign JAR from [Maven Central](https://search.maven.org/artifact/net.jsign/jsign) available to Ant.
1. Create the PKCS11 configuration file. Infra recommends saving this as `~/.digicertone/pkcs11properties.cfg`. The contents should be:

        name=DigiCertONE
        library="/opt/smtools-linux-x64/smpkcs11.so"
        slotListIndex=0

    `name` can be anything you like (although names with spaces and special characters haven't been tested). `library` must point to where you installed the Secure Software Manager Linux Clients.

When configuring the [JSign Ant task](https://ebourg.github.io/jsign/#ant) `keystore` should be set to the full path of the `pkcs11properties.cfg` file.


#### Other signing formats, tools and operating systems

See the client user guide.
