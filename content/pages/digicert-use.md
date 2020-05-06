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

You can then download the signed files





