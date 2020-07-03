Title: Subversion basics

Our developers are located all around the world. To enable them to work together on our software, we keep the source code in Internet-accessible revision control systems, [Git](git.html) and Subversion (SVN).

Apache committers have write access to the Apache Subversion repository so they can make changes to their project's source code. Everyone has read access to the repositories, so you may download the most up-to-date development version of software that interests you.

If you are looking for a stable release of a project's source code, you should download it from the <a href="http://www.apache.org/dyn/closer.cgi/" target="_blank">distribution directory</a>. Only download directly from the SVN repository if you want to be on the *bleeding-edge* of the development effort. The code contained there may fail to work, and may even eat your hard drive.

## Accessing the Subversion repository ##

There are several ways to access the Subversion repository:

**Web Access**

If you just wish to browse around or download a few individual files, the best tool is the web-based <a href="http://svn.apache.org/viewvc/" target="_blank">ViewVC interface for Subversion</a>. You can also go straight to the <a href="http://svn.apache.org/repos/asf/" target="_blank">public repository</a>.

**Anonymous Subversion**

To access the Subversion repository anonymously, you need a Subversion client. 

**Finding the project you want**

You can <a href="http://svn.apache.org/repos/asf/" target="_blank">browse</a> for the project that interests you and check it out. For example, to get the Spamassassin module, use:

`$ svn checkout http://svn.apache.org/repos/asf/spamassassin/trunk spamassassin`

For more help on using Subversion, consult the <a href="http://subversion.tigris.org/" target="_blank">Subversion website</a> or this free <a href="http://subversion.tigris.org/" target="_blank">Subversion book</a>. The website provides a list of clients and useful links.

**Committer Subversion access**

We currently use HTTPS basic authentication for logging in to Subversion (certificate info below). To change your password, visit <a href="https://svn.apache.org/change-password" target="_blank">svn.apache.org/change-password</a>.

This will prompt you to enter a svn password of your choice. If you cannot log in, or have lost your password, visit the <a href="https://id.apache.org" target="_blank">Apache Account Utility</a> to reset it.

When you make changes to the repository, you can commit them with your username/password combination, i.e.
```
$ svn co https://svn.apache.org/repos/asf/excalibur/trunk/ excalibur-trunk
$ cd excalibur-trunk
$ echo "test" > test.txt
$ svn add test.txt
$ svn commit --username your-name --password your-password \
  --message "Trying out svn"
```

`svnserve` is not supported, nor is `svn+ssh`.

## Configuring the Subversion client ##

Committers need to configure their svn client properly. One particular issue is OS-specific line endings for text files. When you add a new text file, especially when applying patches from Bugzilla, first ensure that the line-endings are appropriate for your system, then do:

svn add test.txt svn propset svn:eol-style native test.txt

Your svn client can be configured to do that automatically for some common file types.

Add the contents of the file http://www.apache.org/dev/svn-eol-style.txt to the bottom of your ~/.subversion/config file. For Windows this is normally found at C:\\Documents and Settings\\{username}\\Application Data\\Subversion\\config -or- For Windows 7 at C:\\Users\\{username}\\AppData\\Roaming\\Subversion\\config]

Some files may need additional properties to be set. For example, apply svn:executable=* to those script files (e.g..bat,.cgi,.cmd,.sh) that are intended to be executed. Since not all such files are necessarily intended to be executed, the executable property should not be made an automatic default.

However, you should still pay attention to the messages from your svn client when you do 'svn commit'.

Tip: If you use TortiseSVN, a popular Windows GUI client that integrates with Windows Explorer, you can simply right-click in Explorer and select TortiseSVN - Settings, and then press the "Edit" button to update your "Subversion configuration file:". Copy the above svn-eol-style.txt file's contents into the end of the config editor (usually Notepad) that appears, and save the file.

SSL Server certificate
The server certificate for https://svn.apache.org/ is a real SSL certificate. However, Subversion, by default, does not currently ship with a list of trusted CAs. So, here's some information to help you verify the validity of our cert:

Hostname: *.apache.org
Valid: from Mon, 19 Dec 2011 22:00:00 GMT until Mon, 17 Feb 2014 21:59:59 GMT
Issuer: Thawte, Inc., US
Fingerprint: bc:5f:40:92:fd:6a:49:aa:f8:b8:35:0d:ed:27:5e:a6:64:c1:7a:1b


Note that the SSL certificate for our Subversion repository is different from certificates used when logging into Apache infrastructure - please see the New Committer guide for more information.

Problems with Subversion?
"Error validating server certificate" errors
Error validating server certificate for 'https://svn.apache.org:443':
 - The certificate is not issued by a trusted authority. Use the
   fingerprint to validate the certificate manually!
Certificate information:
 - Hostname: *.apache.org
 - Valid: from Tue, 20 Dec 2011 00:00:00 GMT until Mon, 17 Feb 2014 23:59:59 GMT
 - Issuer: Thawte, Inc., US
 - Fingerprint: bc:5f:40:92:fd:6a:49:aa:f8:b8:35:0d:ed:27:5e:a6:64:c1:7a:1b
(R)eject or accept (t)emporarily


On some platforms, the root Thawte certificate, used to sign the Apache SSL cert, is not made available to OpenSSL and Subversion. Fix this by downloading the Thawte root certificate, and updating your Subversion servers file accordingly to use it for SSL validation:

Save the [Thawte root certificate] (in .pem format) to a suitable path, for example, in your ~/.subversion/ directory, or on Windows, in %USERPROFILE%\AppData\Roaming\Subversion\ folder.
In the servers file, found in the same folder, add the following to the [global] section, adding the section if required, and amending the path appropriately:
    [global]
    ssl-authority-files = /full/path/to/thawte_Premium_Server_CA.pem
    ssl-trust-default-ca = true


Re-trying the Subversion operation should now succeed. In some cases, you may additionally need to move to a more recent svn client. Version 1.6 or higher should be sufficient.

[Thawte root certificate]: https://www.thawte.com/roots/thawte_Premium_Server_CA.pem

"svn: No such revision 765287" errors
If you're getting an error message like the following:

svn: No such revision 765287


This may be because of a short lag in the synchronization between Subversion mirrors, and can occur if multiple commits are run immediately after each other. This error will usually only happen if you are located in Europe, or are explicitly using the European mirror.

Waiting for ten seconds and repeating the command should succeed.

"specified baseline is not the latest baseline" errors
If you're getting an error message like the following:

svn: Commit failed (details follow):
svn: The specified baseline is not the latest baseline, so it may not be
checked out.


This may be because of a short lag in the synchronization between Subversion mirrors, and can occur if multiple commits are run immediately after each other. This error will usually only happen if you are located in Europe, or explicitly using the European mirror.

Waiting for ten seconds and repeating the command should succeed.

"Compressed stream invalid" errors
If you're getting an error message like the following:

svn: PROPFIND of '/repos/asf/foobar':
Compressed stream invalid (https://svn.apache.org)


That's a known issue in the neon client library which has been fixed in neon 0.24.7. A workaround is to disable compression in your client. Edit ~/.subversion/servers. Uncomment the [global] section if neccessary, and add a line that reads

http-compression = no


That should "fix" the problem until you can upgrade neon.

Problems using date revisions
If you are using a date revision such as -r{2004-09-12}:{2004-08-12} and not getting any or all of the revisions you expected, this is a known problem specific to the ASF repository.

Unfortunately, there is nothing that can be done to improve this situation, so you must use a workaround. You can use svn log or ViewVC to locate the first actual revision number after the date you desire, and substitute that into your -r argument to the svn command.

For example, consider the desired command:

$ svn diff -rHEAD:{2005-01-01}


When this produces no output, running svn log alone shows:

...
------------------------------------------------------------------------
r124032 | aheritier | 2005-01-04 09:58:16 +1100 (Tue, 04 Jan 2005) | 1 line


Switch to subversion
------------------------------------------------------------------------
r123911 | brett | 2005-01-03 09:48:57 +1100 (Mon, 03 Jan 2005) | 1 line


remove nagoya references
------------------------------------------------------------------------
r116173 | brett | 2004-10-23 22:11:51 +1000 (Sat, 23 Oct 2004) | 2 lines


remove old requires descriptions
...


So, the comand above should become:

$ svn diff -rHEAD:123911


The particular reason this occurs is because the order of the revisions is not identical to the order of dates in the repository. This is a side effect of loading CVS repositories with history with dates prior to the latest date in the Subversion repository.

Frequently Asked Questions
When Do I Need To Use svn lock?
Very rarely. Commits in subversion are transactional. This means that locks are almost always unnecessary.

An oft-quoted use case is to prevent concurrent editing of a large unmergeable binary document. However, for open development, good communication is preferable to locking even in this use case. A clear, timely post to the list to let your fellow developers know that you're going to start editing that huge PDF is better than locking the file.

How frequently can I run a cron that connects to the repository?
Hourly is fine. Please do not use programs that poll the repository more frequently than hourly. People who run automated scripts that continuously poll the repository wind up getting their access denied, which may impact other folks connecting through the same host. If you need to stay more in-sync than an hourly cron allows, subscribe your script to the relevant commit mailing list.

How do I mirror the entire SVN repository for my experimental $foo?
First, ask yourself: do I really want the *entire* ASF repository? Generally most people really want only a single project. In that case, just check out that source directory from the repo.

If you really do want the entire ASF repository, *don't* use svnsync. Instead, start by looking here: [http://svn-master.apache.org/dump/][1] Use that to bootstrap your repo.

Why Do I Get a 403 When I Try To Commit?
Run svn info and check that the URL starts with https://. If it starts with http://, run:

$ svn switch --relocate http://svn.apache.org https://svn.apache.org


If you still get 403 Forbidden errors, ask your PMC to double-check the authz file and LDAP/Unix group membership.
