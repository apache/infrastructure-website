Title: Requesting access to the Digicert code signing service
license: https://www.apache.org/licenses/LICENSE-2.0

The <a href="https://www.digicert.com/" target="_blank">DigiCert</a> code signing service is for JARs and Windows executables.

To gain access to the service, create a <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank"> Jira ticket</a> with the following information:

  - Set the component to `code signing`
  - The name of the PMC requesting the code signing service
  - The Apache IDs of the committer(s) who will act as release managers
  - The Apache IDs of any additional PMC members who require access to monitor the service

The infra team will then request the account creation and (after a few e-mails and configuring a OTP token) you will have an account that lets you access the <a href="https://one.digicert.com/signingmanager/dashboard" target="_blank">web GUI</a>. Each PMC member must have their own account to access the web GUI.

The code signing is performed locally (no need to upload large files, just the hashes are passed to the central signing service). You can download a client for your preferred tool and platform from the resources section of the web GUI.
