Title: Requesting access to the code signing service
license: https://www.apache.org/licenses/LICENSE-2.0

The ASF currently uses <a href="https://www.ssl.com/" target="_blank">ssl.com</a>'s <a href="https://www.ssl.com/esigner/" target="_blank">eSigner</a> to sign JARs and Windows executables.

To gain access to the service, create a <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank"> Jira ticket</a> with the following information:

  - Set the component to `code signing`
  - The name of the PMC requesting the code signing service
  - The Apache IDs of the committer(s) who will act as release managers

The infra team will then request the account creation and (after a few e-mails and configuring a OTP token) you will have an account that lets you access the service. Each PMC member must have their own account to access the service.

Release managers can then sign release artifacts via:

  - the API using a tool such as <a href="https://ebourg.github.io/jsign/" target="_blank">Jsign<a/>
  - the standard Windows tools (signtool.exe / certutil.exe) by installing the <a href="https://www.ssl.com/downloads/#cka" target="_blank">eSigner Cloud Key Adapter (CKA)</a>
  - ssl.com's Java based <a href="https://www.ssl.com/guide/esigner-codesigntool-command-guide/" target="_blank">CodeSignTool</a>
  - the eSigner <a href="https://app.esigner.com/" target="_blank">web interface</a>

For the first three options, the code signing is performed locally (no need to upload large files, just the hashes are passed to the central signing service).
