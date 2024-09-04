Title: Mailing list moderation
license: https://www.apache.org/licenses/LICENSE-2.0

Mailing lists are the virtual rooms where ASF communities live, form and grow. All formal decisions the project's PMC makes need to have an email thread (possibly with a recorded vote) as an audit trail that this was an official decision.

  - <a href="#new-mailing-list">How do we create a new mailing list?</a>
  - <a href="#mailing-list-moderators">How do I change moderators?</a>
  - <a href="#subscribers">How do I find who is subscribed to a list?</a>
  - <a href="#mail-moderate">What should I do with MODERATE emails?</a>

Dealing with

  - <a href="#spam">MODERATE requests for spam</a>
  - <a href="#allowing_posts">allowing posts from non-subscribers</a>
  - <a href="#problem_posts">problem posts</a>
  - <a href="#missing">reports of missing mail</a>
  - <a href="#bounce">reports of message bounces</a>
 
See also Infra's general guidelines on <a href="https://infra.apache.org/content-moderation.html" target="_blank">content moderation</a>.

<h3 id="new-mailing-list">How do we create a new mailing list?<a class="headerlink" href="#new-mailing-list" title="Permanent link">&para;</a></h3>

It is wise to keep the number of mailing lists per codebase the smallest possible to allow the community to reach that critical mass that is necessary to bootstrap a codebase and keep it in good shape.

At the same time, as communities grow, the need for more specialized mailing lists appears. If you think your project requires a new list:

  - Float the idea in the `dev@` or `users@` mailing list.
  - If there seems to be some support for the idea, request a community vote.
  - If the community approves adding a mailing list, the PMC chair or another Apache Member on the PMC can do so through the <a href="https://selfserve.apache.org" target="_blank">ASF Self-Service Platform</a>

**WARNING**: Creating a user email list can harm a project community if the developers don't pay attention to their users and reply to their emails. One would expect a well-behaving user community to reply to one another in a civil, adult manner that is focused on whatever the list was created for, but it can take time for a community to learn and take to heart such good behavior.

<h3 id="mailing-list-moderators">How do I change moderators?<a class="headerlink" href="#mailing-list-moderators" title="Permanent link">&para;</a></h3>

You can manage the list of moderators for a project's email list if you are:

  - a Foundation member and on the PMC of the project
  - chair of the project
  - an existing moderator of the list
 
    - Log in to <a href="https://webmod.apache.org/" target="_blank">WebMod</a> with your ASF credentials. 
    - Select the 'List moderator management' tab.
    - In the dropdown list, select the project which has the email list in question.
    - In the list of email lists that appears, select the list whose moderators you want to manage.

The current list of moderators for this list appears. You can:

  - **Remove a moderator**: Click the `Remove as moderator` link beside their name.
  - **Add a moderator**: In the `Add a moderator` field, enter the email address of the new moderator. Make sure this is an address that the person has registered with the ASF.

To determine who the existing moderators are, any committer can use the technique described in the "committers" SVN module at <a href="https://svn.apache.org/repos/private/committers/docs/resources.txt" target="_blank">resources.txt</a>.

<h3 id="subscribers">How do I find who is subscribed to a list?<a class="headerlink" href="#subscribers" title="Permanent link">&para;</a></h3>

Moderators can send an email to `listname-list@tlp.apache.org`.

Anyone with access to the apmail account can run the following command to get a count of the subscribers:

```
ezmlm-list~/lists/project/listname| wc -l
```

Remember that there often are people subscribed to the digest version of the list. To find them:

```
~lists/project/listname/digest
```

However, most committers do not have access to apmail. See the notes in the "committers" SVN module (`https://svn.apache.org/repos/private/committers`) at `/docs/resources.txt` for another way.

<h3 id="mail-moderate">What should I do with "MODERATE" emails?<a class="headerlink" href="#mail-moderate" title="Permanent link">&para;</a></h3>

You can review and manage email that is waiting for moderation in two ways:

#### WebMod 

<a href="https://webmod.apache.org/" target="_blank">WebMod</a> simplifies reviewing and responding to emails that require moderation.

  - Log in to WebMod using your Apache credentials.
  - A tab appears for each email list for which you are a moderator and that has emails needing review. Select a tab.
  - You can approve or reject multiple emails in one action by checking the checkboxes to the left of the email titles and selecting either `accept` or `spam` from the bulk-actions dropdown list.
  - You have many options for reviewing each individual email, including displaying just the text body or viewing the source. The options appear as links to the right of the email title.

#### Manual moderation
Review the mail to see if it is spam (or other severely misguided mail). If it is spam, just ignore the mail to have it silently dropped after 5 days.

To bounce non-spam with a notice to the sender, reply to the `-reject` address in the mail header. If you wish to include a comment with the rejection, the body of the message should look like this:

```
%%% Start comment
Your message goes here...
%%% End comment
```

If it is legitimate mail from a non-subscriber (or someone sending with a different envelope sender than the one subscribed), reply to the `-accept` address. If you also send mail to the `-allow` address (i.e. reply to all), future postings from that address will be allowed through automatically.

If there is no `-allow` address in the moderate requests, the list is misconfigured. Contact `apmail@apache.org` and ask them to enable remote administration.

See the <a href="http://www.ezmlm.org/" target="_blank">EZMLM</a> "Moderator's and Administrator's Manual". You can also send a request for advice to `{listname}-help@tlp.apache.org` from your moderation address.

Some lists are only open to ASF committers. The moderators have methods to ensure that subscribers are committers, so subscribers can use whatever email address that they want. Moderators see the tips described in the "committers" SVN module at <a href="https://svn.apache.org/repos/private/committers/docs/resources.txt" target="_blank">resources.txt</a>.

<h3 id="spam">Dealing with MODERATE requests for spam<a class="headerlink" href="#spam" title="Permanent link">&para;</a></h3>

**NOTE**: You may receive a moderation email that contains email identified as spam. Moderation emails containing spam emails are **not spam**. **DO NOT** report mod emails as spam because this causes our legitimate moderation email and the ASF servers themselves to lose sender reputation. Various email providers may block the ASF as a whole as a result of your action.

If the content of the MODERATE request is clearly spam, the simplest solution is just to delete the request. Do not reject it. However, if you are receiving a lot of such requests, it may perhaps be worth taking additional action.

Some SPAM emails have an opt-out link. Whether this will actually do anything useful is another matter, but it might be worth trying if the spam seems to be from a legitimate business.

To avoid revealing your personal IP address, you may wish to use an anonymizing service such as Tor.

If the spam emails are all sent from the same address, try adding them to the 'deny' list:

```
{listname}-deny-subscribe-badposter=menace.com@tlp.apache.org</code>
```

You can find the sender's address in the moderation request in the `cc:` area:
  
```
Cc: {listname}-allow-tc.<digits>.<alphanumeric>-badposter=menace.com@tlp.apache.org
```

The sender's e-mail address is contained between the '-' (hyphens) immediately following the "alphanumerics" and the '@' sign.

This is already in the correct form for use in the 'deny' subscription request, as the '@' has been changed to '='. In the example above this is:

```
badposter=menace.com
```

If this address contains random alphanumerics, it is probably a short-lived address, in which case there is no point trying to use the deny list.


<h3 id="allowing_posts">Allowing posts from non-subscribers<a class="headerlink" href="#allowing_posts" title="Permanent link">&para;</a></h3>

Most lists require people to subscribe in order to post messages. However, subscribers receive copies of all mails (or digests). This is obviously unsuitable for bots, or for private lists which need to accept posts from non-subscribers.

A moderator can fix this by using 'Reply All' to a moderation message from the poster. This will both 'accept' the message and 'allow' further posts.

It's also possible to set this up in advance, by subscribing the poster to the 'allow' list. For example, if you want `mailbot@host.com` to be able to post, use:

```
{listname}-allow-subscribe-mailbot=host.com@tlp.apache.org
```

Replace the '@' in the sender email with '='.

<h3 id="problem_posts">Dealing with problem posts<a class="headerlink" href="#problem_posts" title="Permanent link">&para;</a></h3>

If you have a troublesome poster, you can un-subscribe them from the list using

```
{listname}-unsubscribe-badboy=menace.com@tlp.apache.org
```

Send a courtesy email to them to let them know they have been unsubscribed, and why.

Occasionally you will get someone with a poorly-configured spam filter sending automated replies to the list. You can deny their postings using

```
{listname}-deny-subscribe-badposter=menace.com@tlp.apache.org
```

Send a courtesy email suggesting how they can resolve the problem.

If an unsubscribed user was added to the moderation list and is sending spam to the list, remove them by sending an email to:

```
{listname}-allow-unsubscribe-badposter=menace.com@tlp.apache.org
```

To see a list of who is allowed to post on the moderation list, send an email to `{listname}-allow-list@tlp.apache.org`.

There is an <em>opt-in</em> configuration for problem posters, which lets you subscribe him or her to a 'sendsubscribertomod' list. It works in exactly the same way as adding or removing someone from an 'allow' or 'deny' list. File an INFRA ticket to have it enabled for your list (you don't have to use it, but having it enabled adds an option for you to consider).

To use it (once it has been enabled) do this:

```
{listname}-sendsubscribertomod-subscribe-badposter=menace.com@tlp.apache.org

```

All emails from this person now go to a moderator for approval before they appear in the mailing list.

Once a bad poster starts behaving in the proper manner again, feel free to 'unsubscribe' them from the 'sendsubscriberstomod' list so they can resume normal operations.

Send moderation commands from your **moderator address**.  You can tell if you're sending from the right address by emailing the `-help` address (e.g.,
`dev-help@tlp.apache.org`) and checking if the subject of the reply contains the word "Moderator help".

<h3 id="missing">Dealing with reports of missing mail<a class="headerlink" href="#missing" title="Permanent link">&para;</a></h3>

If a subscriber reports that they are not receiving some e-mails, check which ones are involved. If they are not seeing their own e-mails, note that GMail hides duplicates.
Also check whether the emails could have been treated as SPAM by their e-mail client.

<h3 id="bounce">Dealing with reports of message bounces<a class="headerlink" href="#bounce" title="Permanent link">&para;</a></h3>

If a subscriber reports getting a  bounce message from ezmlm, ask them to provide the details.
For example:

```
Hi! This is the ezmlm program.
I'm managing the user@tlp.apache.org mailing list.

Messages to you from the user mailing list seem to
have been bouncing
...
Here are the message numbers:
    12345

```

This can occur if the recipient's mail system has strict SPAM detection rules. 

One way to find such emails is to request an index listing from ezmlm, for example
by sending an email to `dev-index-12345@tlp.apache.org`. This will show the subject, timestamp and sender of the email. That may be sufficient to identify it as spam.
If not, the subject and date should make it easy to find the email in the archives.
