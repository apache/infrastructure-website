Title: Committer Email
license: https://www.apache.org/licenses/LICENSE-2.0

Every Apache project committer account has an associated apache.org email address. Some official Apache emails go to these addresses, so you need to check your apache.org email regularly for announcements. You can also use this address for correspondence related to ASF projects you work on.

You cannot work **directly** with your Apache email address. You must set up **forwarding** for this address. Then, when people write to your ASF address, the system forwards the email to your forwarding address. When you reply, the message goes back through the ASF system so the person you are writing with sees it come from your ASF address. See below for how to write a new email from your ASF address.

## Configuring your Apache email address ##

When Infra creates your committer account, it sets the forwarding email address, or alias, to the address you provided in the account request and, typically, in the <a href="https://www.apache.org/licenses/icla.pdf" target="_blank">Independent Contributor Licensing Agreement (ICLA)</a> you provided. Keep your forwarding address (or addresses) up to date. 

To review and update your forwarding addresses:

- Use the <a href="https://id.apache.org/" target="_blank">Selfserve app</a>.
- Use <a href="https://whimsy.apache.org/roster/committer/__self__" target="_blank">Whimsy</a>. Double-click the green "Email forwarded to" label.

*Known Issues*

- GMail

Users of Google's Gmail should note that the app sometimes shows only one copy of an email, even if copies come to several email aliases that all point to the same inbox. If you try to test forwarding by sending a message to your ASF account from the Gmail account that is the target of the .forward, it can be difficult to tell if it has worked. Send the test e-mail from a different account.

- Microsoft

There have been ongoing problems with Microsoft domains partly because many of their users report our legitimate email as spam.

The Infrastructure team have been trying to get the bans removed, but with no success. At present mails from one of the two ASF outbound servers are being rejected; i.e. on average 50% of mails will not be delivered.

The following Microsoft domains are all affected (as of September 2021):

- outlook.com
- hotmail.com
- live.com
- live.cn


### Registering an email alias ###

To register an email alias, you can:

- Use the <a href="https://id.apache.org/" target="_blank">Selfserve app</a>.
- Use <a href="https://whimsy.apache.org/roster/committer/__self__" target="_blank">Whimsy</a>. Double-click the green "Email addresses (alt)" label.

You can register multiple email aliases with your committer account. Apache inspects registered e-mail aliases when you subscribe to a restricted mailing list with an email other than your apache.org e-mail address. If you are allowed to subscribe to a restricted Apache mailing list and use an address other than your Apache email address, the Apache system approves the request if you have registered the email as one of your aliases. 

### Sending email from your Apache address ###

Since you can't use your Apache mailbox directly, send email using your apache.org email address from the committer mail-relay service. Configure this in your email environment:

``Server:     mail-relay.apache.org 
Port:       587 (STARTTLS), 465 (SSL) 
User/Pass:  {Your LDAP credentials}``

Your email provider may have a simple form for this in its "Settings" area.

Note: If you are using Gmail with your apache.org email address, there is a way to configure it to take advantage of this service. See Gmail's feature to allow outbound mail from your apache.org address to be directed to the mail-relay service, instead of to a Gmail server, for delivery.


