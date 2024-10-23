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

When the infrastructure team creates your account you will receive TBD. Your username is your ASF email address.

You should configure your account to use 2FA.
Note: This 2FA is separate to the 2FA you will need to configure to perform code signing.

### Step 2: Obtaining credentials for code signing

Whatever you need to sign and however you choose to sign it, you need to create 2FA credentials.
You create these via the ssl.com web interface.
Depending on your chosen signing method, you will need either to configure 2FA using the QR code you create or make a note of the base 64 encoded secret code associated.

1. Log on to [ssl.com](https://www.ssl.com/).
1. TBD.

### Step 3: Install the OS integration

#### None

If you use JSign 4.0, you can skip this step.

#### Windows integration

1. TBD.

#### Linux integration

1. TBD.

#### MacOS

1. TBD


### Step 4: Configure your chosen signing tool

#### Signing Windows binaries on Windows using signtool.exe

TBD.

#### Signing on Windows binaries on Windows or Linux with JSign 4.0+ Ant task

1. Make the JSign JAR from [Maven Central](https://search.maven.org/artifact/net.jsign/jsign) available to Ant.
1. The eSigner specific properties for the JSign task in Ant should be as follows:

          storetype="ESIGNER"
          alias="d97c5110-c66a-4c0c-ac0c-1cd6af812ee6"
          storepass="<ssl.com user name>|<ssl.com password>"
          keypass="<ssl.com eSigner TOTP secret>"
          tsaurl="http://ts.ssl.com"
          tsmode="RFC3161"
          alg="SHA256"

#### Signing Windows binaries on Linux with JSign 4.0+

1. Download jsign `wget https://github.com/ebourg/jsign/releases/download/4.0/jsign_4.0_all.deb`.
1. Install jsign `sudo dpkg --install jsign_4.0_all.deb`.
1. You should then be able to sign with:

        jsign --storetype ESIGNER --alias d97c5110-c66a-4c0c-ac0c-1cd6af812ee6 --storepass "<ssl.com user name>|<ssl.com password>" --keypass "<ssl.com eSigner TOTP secret>" --tsaurl="http://ts.ssl.com" --tsmode RFC3161 --alg SHA256 application.exe

#### Other signing formats, tools and operating systems

See the ssl.com eSigner on-line help.
