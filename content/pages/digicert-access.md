Title: Requesting access to the Digicert code signing service

The <a href="https://www.digicert.com/" target="_blank">Digicert</a> code signing service is for JARs and Windows executables.

To gain access to the service, create a <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank"> Jira ticket</a> with the following information:

  - Set the component to `code signing`
  - The name of the PMC requesting the code signing service
  - Whether the PMC wants to use the web based GUI and/or the SOAP API
  - The Apache IDs of the committer(s) who will act as release managers
  - The Apache IDs of any additional PMC members who require access to monitor the service

The infra team will then request the account creation and (after a few e-mails and registration) you will have a certificate that lets you access the <a href="https://securesigning.pki.digicert.com/csportal/production" target="_blank">web GUI</a>. Each PMC member must have their own certificate to access the web GUI.

If your PMC has requested access to the SOAP API, you will receive the necessary credentials. You can share them among the PMC members.
