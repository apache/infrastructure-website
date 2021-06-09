Title: Using the Digicert code signing service

## Transition in progress
We are currently transitioning from the old Symantec service to the new DigiCert service. The Symanetc service is no longer supported. While it is currently still available, it may be decommissioned at any time. Perform all new signing via the DigiCert service.

If you require assistance migrating to the DigiCert service, please open an <a href="https://issues.apache.org/jira/browse/INFRA">INFRA Jira ticket</a> and select code signing as the component.

## DigiCert Secure Software
DigiCert Secure Software supports a range of signing tools and formats. For the full list see the client user guide in the <a href="https://svn.apache.org/repos/private/committers/code-signing/digicert/" target="blank">private repository for ASF committers</a>.

### Obtaining a DigiCert ONE account

Adding a new PMC or a new user to an existing PMC needs to be performed by the infrastructure team. Please open an <a href="https://issues.apache.org/jira/browse/INFRA">INFRA Jira ticket</a> and select code signing as the component.

When the infrastructure team create your accout you will be sent a password reset email. The link in that email is only valid for 12 hours. If you are unable to complete the creation of your account in that time you can request a new password reset email by going to [DigiCert ONE](https://one.digicert.com/) and clicking on the password reset link. Your username is the same as your ASF id. You should then receive a new password reset email you can use to set your password. You will also need to configure your OTP token. Officially, only Google authenticator is supported but any similar tool should also work.

### Obtaining credentials for code signing

Whatever you need to sign and however you choose to sign it, the fist step is to create the necessary credentials via the DigiCert ONE web interface.

1. Log on to [DigiCert ONE](https://one.digicert.com/).
1. Select "Account" from the menu in the top right-hand corner.
1. Select "Access" in the left-hand menu.
1. Select "API token" and create a new API token with your ASF id as the name and an expiry date ~1 year in the future.
1. Keep a record of the token value
1. Select "Client Auth" and create a new client certificate with your ASF id as the name and an expiry date ~1 year in the future.
1. Download the certificate and keep a record of the password

### Windows binaries on Windows

To configure your system:

1. Obtain your DigiCert ONE credentials as above.
1. Return to DigiCert ONE and select "Secure Software" from the menu in the top right-hand corner.
1. Select "Resources" in the left-hand menu.
1. Download and install the "Secure Software Manager Windows Clients Installer".
1. As per sections 4.3 and 4.5 of the client user guide, create the four system environment variables. Note that the URL for `SM_HOST` should be `https://clientauth.one.digicert.com` (no `demo` in the URL)
1. Test with `smctl.exe keypair ls` (see section 4.6 of the client user guide). You should see at least one certificate listed.
1. Test with `certutil.exe -csp "DigiCert Signing Manager KSP" -key -user` (see section 4.7 of the client user guide).
1. Synchronise certificates with `smksp_cert_sync.exe` (see section 4.8 of the client user guide).
1. Open `certmgr.msc` (see section 4.9 of the client user guide) and you should see your code signing certificate(s) listed under personal certificates. If a new certificate is issued to your PMC you will need to repeat this step.

To sign Windows binaries you will need a copy of SignTool.exe. This can be found in both Visual Studio and the Windows SDK. Very old versions only support SHA-1 signing. Version 6.1.7600.16385 (2009-07-14) supports newer hashes for signing.

Signing Windows binary is covered by section 14 of the client user guide. You'll need the fingerprint of the certificate you want to use for signing (view via `certmgr.msc`). You can then sign a file with `signtool.exe sign /sha1 <cert-fingerprint> /fd sha512 /tr http://timestamp.digicert.com <file-to-be-signed>`

To sign a file with SHA-256 rather than SHA-512 use `... /fd sha256...` rather than `... /fd sha512 ...`.

### Windows binaries on Linux

Currently under investigation by the Apache Tomcat project. Looks to be possible via OpenSSL (see section 9 of client user guide) and osslsigncode.

To configure your system:
1. Obtain your DigiCert ONE credentials as above.
1. Return to DigiCert ONE and select "Secure Software" from the menu in the top right-hand corner.
1. Select "Resources" in the left-hand menu.
1. Download and install the "Secure Software Manager Linux Clients Installer (Portable tar.gz)".
1. Unpack the tar.gz. This guide assumes it is unpacked in `/opt`
1. As per the DigiCert ONE documentation, create the four required environment variables. You may wish to store your certifcate in `~/.digicertone/`.
1. Test with `/opt/smtools-linux-x64/smctl keypair ls`. You should see at least one certificate listed.
1. ... TBD

### Other signing formats, tools and operating systems

See the client user guide.
