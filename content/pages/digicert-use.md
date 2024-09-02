Title: Using the Digicert code signing service
license: https://www.apache.org/licenses/LICENSE-2.0

## Transition to DigiCert
The ASF used Symantec's Secure App Service to provide Windows and JAR code signing functionality from 2014 to 2019. In 2019 the ASF moved from the Symantec service to DigiCert ONE. All new signing must be via the DigiCert service.

If you require assistance migrating to the DigiCert service, please open an <a href="https://issues.apache.org/jira/browse/INFRA">INFRA Jira ticket</a> and select code signing as the component.

## DigiCert Secure Software
DigiCert Secure Software supports a range of signing tools and formats. For the full list see the [client user guide](https://digicert.github.io/snowbird-doc/#/administration-guides/secure-software-manager/index). Whichever signing option you choose, you will need to complete four steps:

1. Obtain a DigiCert ONE account
1. Obtain credentials for code signing
1. Install the OS integration for your chosen OS (Windows or Linux)
1. Configure your chosen signing tool

**Note**: The ASF has to pay for each signature using a signing certificate. Using Jenkins to build and sign **releases** using DigiCert ONE is fine. Signing every single **CI build** is not necessary and can become expensive for the Foundation. Please make sure your build process only involves signing certificates for release candidates.

### Step 1: Obtaining a DigiCert ONE account

Adding a new PMC or a new user to an existing PMC needs to be performed by the infrastructure team. Please open an <a href="https://issues.apache.org/jira/browse/INFRA">INFRA Jira ticket</a> and select code signing as the component.

When the infrastructure team creates your account you will receive a password reset email. The link in that email is only valid for 12 hours. If you are unable to complete the creation of your account in that time you can request a new password reset email by going to <a href="https://one.digicert.com/" target="_blank">DigiCert ONE</a> and clicking the password reset link. Your username is your ASF email address. You should then receive a new password reset email you can use to set your password. 

You also need to configure your OTP token. Officially, only Google authenticator is supported but any similar tool should also work.

### Step 2: Obtaining credentials for code signing

Whatever you need to sign and however you choose to sign it, you need to create credentials to use the signing API. You create these via the DigiCert ONE web interface.

1. Log on to [DigiCert ONE](https://one.digicert.com/).
1. Select "Account" from the menu in the top right-hand corner.
1. Select "Access" in the left-hand menu.
1. Select "API token" and create a new API token with a unique name (e.g. ASF ID + year) as the name and an expiry date ~1 year in the future.
1. Keep a record of the token value
1. Select "Client Auth" and create a new client certificate with a unique name (e.g. ASF ID + year) as the name and an expiry date ~1 year in the future.
1. Download the certificate and keep a record of the password

### Step 3: Install the OS integration

#### None

If you use JSign 4.0, you can skip this step.

#### Windows integration

1. Log on to DigiCert ONE and select "Secure Software" from the menu in the top right-hand corner.
1. Select "Resources" in the left-hand menu.
1. Download and install the "Secure Software Manager Windows Clients Installer".
1. As per the <a href="https://docs.digicert.com/en/digicert-one/software-trust-manager/general/secure-credentials/set-up-secure-credentials-for-windows.html" target="_blank">Windows Configuration</a> section of the client user guide, create the four system environment variables. These **must** always be set to use the DigiCert signing service.
1. Test with `smctl.exe keypair ls`. You should see at least one certificate listed. (smctl.exe is installed as part of the DigiCert client and won't be on your path.)
1. Test with `certutil.exe -csp "DigiCert Signing Manager KSP" -key -user`. You should see at least one key listed. (certutil.exe will be on your path.)
1. Synchronise certificates with `smksp_cert_sync.exe`.
1. Open `certmgr.msc` (it will be on your path) and you should see your code signing certificate(s) listed under personal certificates. If a new certificate is issued to your PMC you will need to repeat this step.

#### Linux integration

1. Log on to DigiCert ONE and select "Secure Software" from the menu in the top right-hand corner.
1. Select "Resources" in the left-hand menu.
1. Download and install the "Secure Software Manager Linux Clients (Portable tar.gz)".
1. Unpack the tar.gz. Infra recommends, and this guide assumes, it is unpacked to `/opt`
1. As per the DigiCert ONE documentation, create the four required environment variables. These **must** always be set to use the DigiCert signing service. Infra recommends you store your certificate in `~/.digicertone/`.
1. Test with `/opt/smtools-linux-x64/smctl keypair ls`. You should see at least one certificate listed.

#### MacOS

The DigiCert ONE client tools are not available for MacOS. Use JSign 4.0 so you can skip this step.


### Step 4: Configure your chosen signing tool

#### Signing Windows binaries on Windows using signtool.exe

To sign Windows binaries you need a copy of SignTool.exe. This utility is in both Visual Studio and the Windows SDK. Very old versions only support SHA-1 signing. Version 6.1.7600.16385 (2009-07-14) supports newer hashes for signing.

You need the fingerprint of the certificate you want to use for signing (view via `certmgr.msc`). You can then sign a file with `signtool.exe sign /sha1 <cert-fingerprint> /td sha1 /fd sha512 /tr http://timestamp.digicert.com <file-to-be-signed>`.

To sign a file with SHA-256 rather than SHA-512 use `... /fd sha256...` rather than `... /fd sha512 ...`.

#### Signing on Windows binaries on Windows or Linux with JSign 4.0+ Ant task

1. Make the JSign JAR from [Maven Central](https://search.maven.org/artifact/net.jsign/jsign) available to Ant.
1. The DigiCert ONE specific properties for the JSign task in Antshould be as follows:

          storetype="DIGICERTONE"
          storepass="<api-key>|<path-to-client-certificate>|<client-certificate-passphrase>"
          alias="<name-of-signing-certificate>"
          tsaurl="http://timestamp.digicert.com"


#### Signing Windows binaries on Linux with JSign 4.0+

1. Download jsign `wget https://github.com/ebourg/jsign/releases/download/4.0/jsign_4.0_all.deb`.
1. Install jsign `sudo dpkg --install jsign_4.0_all.deb`.
1. You should then be able to sign with:

        jsign --storetype DIGICERTONE --alias <name-of-signing-certificate> --storepass "<api-key>|<path-to-client-certificate>|<client-certificate-passphrase>" --tsaurl="http://timestamp.digicert.com" application.exe

#### Other signing formats, tools and operating systems

See the client user guide.
