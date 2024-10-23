Title: Using the ssl.com eSigner code signing service
license: https://www.apache.org/licenses/LICENSE-2.0

## Transition to ssl.com
The ASF used Symantec's Secure App Service to provide Windows and JAR code signing functionality from 2014 to 2019 and DigiCert ONE from 2019 to 2024.
In 2024 the ASF moved to the ssl.com eSigner service.
All new signing must be via the ssl.com eSigner service.

If you require assistance migrating to the ssl.com eSigner service, please open an <a href="https://issues.apache.org/jira/browse/INFRA">INFRA Jira ticket</a> and select code signing as the component.

## ssl.com eSigner
ssl.com's eSigner service supports a range of signing tools and formats.
For the full details see the [eSigner documentation](https://www.ssl.com/guide/remote-ev-code-signing-with-esigner). 
Whichever signing option you choose, you will need to complete four steps:

1. Obtain an ssl.com account
1. Obtain credentials for code signing
1. Install the OS integration for your chosen OS (Windows or Linux)
1. Configure your chosen signing tool

**Note**: The ASF has to pay for each signature using a signing certificate. Using Jenkins to build and sign **releases** using eSigner fine. Signing every single **CI build** is not necessary and can become expensive for the Foundation. Please make sure your build process only involves signing certificates for release candidates.

### Step 1: Obtaining an ssl.com account

Adding a new release manager needs to be performed by the infrastructure team. Please open an <a href="https://issues.apache.org/jira/browse/INFRA">INFRA Jira ticket</a> and select code signing as the component.

When the infrastructure team creates your account you will receive an email to your ASF email address.
You will be asked for a user name and password.
Use your ASF email address as the user name (if you enter anything else it should be ignored and your ASF email used anyway).
Provide a secure password.
It is recommended that you enabled 2FA for your account (Dashboard -> manage 2FA).
Note: The 2FA you configure here for account access is not the same as the 2FA you are required to configure later in these instructions to use eSigner.

You may be prompted to verify your account. It is not necessary to do this.

You will see a message saying you have been invited to enroll for eSigner for the given certificate.
You should click yes to accept the invitation.

### Step 2: Obtaining credentials for code signing

Whatever you need to sign and however you choose to sign it, you need to create 2FA credentials for eSigner.
You create these via the ssl.com web interface.
Depending on your chosen signing method, you will need either to configure 2FA using the QR code provided or make a note of the base 64 encoded secret code.

1. Log on to [ssl.com](https://www.ssl.com/).
1. On your Dashboard, there should be a single certificate listed under esigner enrolled orders. Click on it to take you to the certificate page.
1. On the right-hand side you will see a prompt to set up a pin. Provide a pin and click "create PIN". You should be shown a QR code and a secret code. Note that the warning that the QR code wll only be shown once is incorrect. You can always view the QR code and secret code by providing your pin on this page.

### Step 3: Install the OS integration

#### None

If you use JSign, you can skip this step.

#### Windows integration

1. TBD.

#### Linux integration

1. TBD.

#### MacOS

1. TBD


### Step 4: Configure your chosen signing tool

#### Signing on Windows binaries on Windows or Linux with JSign 4.0+ Ant task

1. Make the JSign JAR from [Maven Central](https://search.maven.org/artifact/net.jsign/jsign) available to Ant.
1. The eSigner specific properties for the JSign task in Ant should be as follows:

          storetype=ESIGNER
          alias=d97c5110-c66a-4c0c-ac0c-1cd6af812ee6
          storepass=<ssl.com user name>|<ssl.com password>
          keypass=<ssl.com eSigner TOTP secret>
          tsaurl=http://ts.ssl.com
          tsmode=RFC3161
          alg=SHA256

#### Signing Windows binaries on Linux with JSign 4.0+

1. Download jsign `wget https://github.com/ebourg/jsign/releases/download/4.0/jsign_4.0_all.deb`.
1. Install jsign `sudo dpkg --install jsign_4.0_all.deb`.
1. You should then be able to sign with:

        jsign --storetype ESIGNER --alias d97c5110-c66a-4c0c-ac0c-1cd6af812ee6 --storepass "<ssl.com user name>|<ssl.com password>" --keypass "<ssl.com eSigner TOTP secret>" --tsaurl="http://ts.ssl.com" --tsmode RFC3161 --alg SHA256 application.exe

#### Signing Windows binaries on Windows using signtool.exe

TBD.

#### Other signing formats, tools and operating systems

See the ssl.com eSigner on-line help.
