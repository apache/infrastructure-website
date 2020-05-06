Title: Using the Digicert code signing service

The Digicert service is available for JARs and Windows executables and code signing for both test and production builds.

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

| Artifact type                           | Text signing service   | Production signing service |
| Windows binary (.exe, .dll, .cab, etc.) | Microsoft TEST Signing | Microsoft Windows Signing  |

### Ant task ###

The Apache Tomcat project has written an Ant task that uses the SOAP interface (see below) to sign release artifacts as part of the build process. To use the SOAP interface, your PMC account needs to be enabled for API access. Open an Infra Jira ticket against the code signing component to request this. Once this is approved you will receive your:

  - User name
  - Password
  - Partner code

You need all three to access the API.

This Tomcat Ant task uses a fixed buffer of 16MB to store the zipped artifacts for signing. If your artifacts are larger than that, you need to use a larger buffer. Patches to switch to streaming the artifacts rather than buffering them are welcome.

### Maven plug-in ###

A Maven plug-in to facilitate code signing is a work in progress.

#### SOAP API ####

The <a href="https://svn.apache.org/repos/private/foundation/Correspondence/Symantec/" target="_blank">SOAP API documentation</a> is under an NDA, and this link is only availabe to ASF members. Please do not share the documentation outside your PMC, and make sure those you share it with are aware of the NDA. If you need a copy of the API docs, request it via a PMC member who is also an ASF member. If that is not possible, request it from Infra.


