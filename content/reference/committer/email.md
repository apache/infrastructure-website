Title: Committer e-mail configuration
slug: reference/committer/email

[TOC]

An e-mail address at `apache.org` is associated with every committer
account. Occasional official Apache e-mails will be directed to this
account. It is very important that you check mail sent to your `apache.org`
e-mail address regularly for announcements. You are also free to use this
address for other ASF work related to projects you work on.

Note that the infrastructure group provides an e-mail address for you;
however they do not provide a mailbox -- you **must**
setup forwarding for this address to be able to read your mails.
Instructions on how to [setup your forwarding address](#configure) file
are available.  Be sure to keep your forwarding address up to date in the
future as well.

# Registering an e-mail alias # {#alias}

You can register e-mail aliases with your committer account.  Registered 
e-mail aliases are inspected when you subscribe to a restricted mailing list
with an e-mail other than your `apache.org` e-mail address. It is these
registered e-mail addresses that will be allowed to registered to restricted
mailing lists, assuming that you are actually allowed to subscribe to the list
in the first place.

On the Web, use the Selfserve app
 at [https://id.apache.org/](https://id.apache.org/)

# Reading e-mail from your apache.org address # {#configure}

When your committer account is first created by Infrastructure, the forwarding
e-mail address is set to the address provided in the account request (and,
typically, in the ICLA).  You must keep your forwarding address up-to-date.
(You can have more than one forwarding address.)
You can view and change your forwarding addresses here:

- On the Web, by using the Selfserve app
  at [https://id.apache.org/](https://id.apache.org/)


**Note**: It used to be possible to change the forwarding address by editing
~/.forward and/or ~/.qmail files.  This is no longer possible.  Any manual
changes made to these files will be lost!

**Note**: It used to be possible to not have a forwarding address.  This is
no longer possible.

Users of GMail (Googlemail) please note that only one copy of an e-mail is
shown by GMail. If you try to test forwarding by sending a message to your
ASF account from the GMail account that is the target of the .forward, it
can be difficult to tell if it has worked. Send the test e-mail from a
different account.


# Sending email from your apache.org email address

If you wish to send email using your apache.org email address you will need to submit this via the committer mail-relay service. This can be configured in your mail environment using the following configuration: 

    Server:     mail-relay.apache.org 
    Port:       587 (STARTTLS), 465 (SSL) 
    User/Pass:  {Your LDAP credentials}
 

**Note:** If you are using *Gmail* for your `apache.org` e-mail, there is 
a way to configure it to take advantage of this service. See 
[Gmail's feature](http://gmailblog.blogspot.com/2009/07/send-mail-from-another-address-without.html)
to allow outbound mail from your `apache.org` address to be directed to 
the mail-relay service, instead of to a Gmail server, for delivery.


<!-- vim: set noet ts=2: -->