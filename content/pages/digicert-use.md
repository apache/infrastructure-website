Title: Using the Digicert code signing service

## Transition in progress
We are currently transitioning from the old Symantec service to the new DigiCert service. The Symanetc service will be available until end January 2021 but users should use the Digicert service from 1st January 2021.

## DigiCert Secure Software
DigiCert Secure Software supports a range of signing tools and formats. For the full list see the client user guide in the <a href="https://svn.apache.org/repos/private/committers/code-signing/digicert/" target="blank">private repository for ASF committers</a>.

Adding a new PMC or a new user to an existing PMC needs to be performed by the infrastructure team. Please open an <a href="https://issues.apache.org/jira/browse/INFRA">INFRA Jira ticket</a> and select code signing as the component.

### Obtaining DigiCert ONE credentials

Whatever you need to sign and however you choose to sign it, the fist step is to create the necessary credentials via the DigiCert ONE web interface.

1. Log on to <a href="one.digicert.com">DigiCert ONE</a>.
1. Select "Secure Software" from the menu in the top right-hand corner.
1. Select "Resources" in the left-hand menu.
1. Download and install the "Secure Software Manager Windows Clients Installer".
1. Return to DigiCert ONE and select "Account" from the menu in the top right-hand corner.
1. Select "Access" in the left-hand menu.
1. Select "API token" and create a new API token with your ASF id as the name and an expiry date ~1 year in the future.
1. Keep a record of the token value
1. Select "Client Auth" and create a new client certificate with your ASF id as the name and an expiry date ~1 year in the future.
1. Download the certificate and keep a record of the password

### Windows binaries on Windows

To configure your system for Windows signing:

1. Obtain your DigiCert ONE credentials as above.
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

### Other signing formats, tools and operating systems

See the client user guide.


## Symantec SAS (deprecated)
The Symantec service is available for JARs and Windows executables and code signing for both test and production builds.

Production signing **costs the ASF real money**. Only use the production signing service once the release process works using test signing.

Once you have access to the signing service, you receive a personal certificate from Symantec. You need this to access the code signing GUI.

The production system is available at: <a href="https://securesigning.pki.digicert.com/csportal/" target="blank">https://securesigning.pki.digicert.com/csportal/</a>. When you submit a signing request, you can choose to perform a test or a production signing.

### Adding users ###

To add users to your PMC's signing organization

1. Start at the dashboard
1. Click "Users"
1. Click "Add user"
1. Fill in the form using details (name, asf email, etc.) as shown in Whimsy
1. Choose a random enrollment password and send that to the new user
1. Normally, set all users as admins

### Signing files

To create a new signing set, you need to have a set of files to sign. The steps below uses the <a href="https://tomcat.apache.org/" target="_blank">Apache Tomcat</a> Windows installer as an example.

1. Start at the dashboard
1. Select "signing sets"
1. Click "Add Signing set"
1. Provide a name for the set, e.g "Apache Tomcat 8.5"
1. Provide a version e.g. "8.5.4"
1. Select the signing service e.g. "Microsoft Windows Signing"
1. Upload the file(s) to be signed
1. Click "Sign Now"
1. Select Test or Production
1. Click "Sign"

You can then download the signed files.

### Signing services ###

You need to specify the name of the signing service to use. The names are shown in the table below:

| Artifact type                             | Text signing service   | Production signing service |
| ---                                       | ---                    | ---                        |
| Windows binary (`.exe, .dll, .cab`, etc.) | Microsoft TEST Signing | Microsoft Windows Signing  |
| Java Signing (`*.jar`)                    | Java TEST Signing      | Java Signing               |

Both SHA1 and SHA256 versions of the Java Signing service are available. Apache recommends using the SHA256 service. However, if you are re-signing JARs that have already been signed, make sure to use the same hash algorithm as the original signature to avoid breaking the original signature.

Java signing is not intended to replace the current requirement for releases to be OpenPGP signed. Neither is it intended to replace the process of providing OpenPGP signatures for JARs uploaded to Maven Central. It is intended for those use cases that require individual JAR files to be signed using the standard Java JAR signing process where the signature is contained within the JAR. Such use cases include Java Web Start, Eclipse plug-ins, etc.

### Signing events ###

A signing event is the process of signing one or more files. Whether you use the web GUI or the SOAP API, the files must have unique names. You may have to rename files prior to signing and change the file names back afterwards. Reverting the name does not affect the signature of the file.

The signing service is particular about file extensions. If you do rename a file, make sure that it retains the correct file extension.

You can revert each signing event individually.

You can request production or test signing on both the production and test systems. Only a production signing event on the production system costs the ASF a code signing credit. We recommend that projects start testing with production signing on the test environment and get their process working there before moving to the production environment.

### Ant task ###

The Apache Tomcat project has written an Ant task that uses the SOAP interface (see below) to sign release artifacts as part of the build process. To use the SOAP interface, your PMC account needs to be enabled for API access. Open an Infra Jira ticket against the code signing component to request this. Once this is approved you will receive your:

  - User name
  - Password
  - Partner code

You need all three to access the API.

This Tomcat Ant task uses a fixed buffer of 16MB to store the zipped artifacts for signing. If your artifacts are larger than that, you need to use a larger buffer. Patches to switch to streaming the artifacts rather than buffering them are welcome.

### Maven plug-in ###

A Maven plug-in to facilitate code signing is a work in progress.

### SOAP API ###

The <a href="https://svn.apache.org/repos/private/foundation/Correspondence/Symantec/" target="_blank">SOAP API documentation</a> is under an NDA, and this link is only availabe to ASF members. Please do not share the documentation outside your PMC, and make sure those you share it with are aware of the NDA. If you need a copy of the API docs, request it via a PMC member who is also an ASF member. If that is not possible, request it from Infra.


