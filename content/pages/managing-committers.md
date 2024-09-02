Title: Managing Project Committers

license: https://www.apache.org/licenses/LICENSE-2.0

The PMC of each project encourages and guides their new committers, ensures that they have access to the proper resources, advises them about relevant ASF documentation such as the <a href="/new-committers-guide.html" target="_blank">Guide for New Committers</a>, and generally eases their way.

### Account creation ###

Make sure the new committer fills out the appropriate forms, including the <a href="https://www.apache.org/licenses/contributor-agreements.html" target="_blank">Contributior License Agreement</a>, or CLA. A committer account cannot be processed until the ASF secretary or a board member acknowledges receipt of the CLA. 

Work with your new committer to ensure that their CLA is received and recorded properly; monitor the file iclas.txt in the `foundation/officers` repository. Only ASF members and officers (including PMC chairs) have access. The page <a href="https://people.apache.org/committer-index.html" target="_blank">Apache Committers</a> has a link to "Unlisted CLAs". This list is generated daily from the iclas.txt file, so recently received CLAs appear there.

Encourage your new committer to include both the PMC and the desired account id on the submitted ICLA so the secretary or assistant filing the ICLA can request the account. If the new account information is not provided on the ICLA, the PMC chair is responsible for getting the new committer's desired account ID and requesting the new account. Use the <a href="https://whimsy.apache.org/officers/acreq" target="_blank"> New Account Request form</a> on Whimsy. Should the PMC chair be unavailable for any reason, any ASF member can use the same form in their stead.

Most PMCs decide on new committers through an **election process** on their private mailing list. Please include a URL or message-id reference to the final vote tally using the Mail Search tool. If the election was held on a public list, you can supply the URL using <a hrefg="https://mail-archives.apache.org/mod_mbox/" target="_blank">mail-archives.apache.org</a>.

ASF only accepts **requests for new committer accounts** from PMC chairs and ASF members. If you are acting on behalf of a project which was accepted for incubation, please get in touch with the sponsoring PMC and let them take care of requesting any new accounts.

The request will be CC'd to the PMC mailing list. Barring objections from the PMC, a person with root access will create the account and assign the appropriate group permissions. This may take a few days. ASF sends a message confirming the new account to the PMC mailing list and to the new committer.

### Committer access to code repositories ###

After that, the PMC takes over and provides the committer's infrastructure needs, in particular, write access to the **project's source repository**.

To grant or deny access to directories in SVN, the PMC chair needs to update the appropriate **group entry** in LDAP:

Go to the <a href="https://whimsy.apache.org/roster/committee/" target="_blank">Whimsy roster tool</a>, select the appropriate committee, and either double click on the person or the plus sign to modify or add a person.

If the SVN access group is not defined as an LDAP group (e.g. it is an Incubator podling) then edit the appropriate entry in the <a href="https://svn.apache.org/repos/infra/infrastructure/trunk/subversion/authorization/asf-authorization-template" target="_blank">asf-authorization-template file</a> and commit the change.
