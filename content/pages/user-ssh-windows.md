Title: Committer SSH configuration on Windows

When using SSH (Secure Shell, a cryptographic network protocol)  to access <code>people.apache.org</code>, Windows users have two choices: 

  - Install <a href="https://www.cygwin.com" target="_blank">cygwin</a>, a collection of GNU and Open Source tools which provide functionality similar to a Linux distribution on Windows, and use the standard command line tools
  - Use <a href="#setup">Putty</a>, which provides a graphical user interface

[Non-Windows-specific documentation](user-ssh.html) is also available, and contains details not repeated in this document.

## Contents ##
<ul>
  <li><a href="#setup-cygwin">Setting up Cygwin</a></li>
  <li><a href="#setup">Setting up Putty</a></li>
  <li><a href="#links">Relevant Links</a></li>
</ul>

<h2 id="setup-cygwin">Setting up Cygwin<a class="headerlink" href="#setup-cygwin" title="Permanent link">&para;</a></h2>

1. Download the latest version of <a href="https://www.cygwin.com" target="_blank">cygwin</a>.
1. Install the program by running `setup-x86_64.exe`. Cygwin strongly advises against installing the 32-bit version.
1. Consult the <a href="https://www.cygwin.com/cygwin-ug-net.html" target="_blank">user guide</a> to learn how to make use of its many features.

<h2 id="setup">Setting up Putty<a class="headerlink" href="#setup" title="Permanent link">&para;</a></h2>

This section describes how to create a public/private key pair and how to configure Putty to use them to access <code>people.apache.org</code>.

<h3 id="download">Download and install Putty<a class="headerlink" href="#download" title="Permanent link">&para;</a></h3>

1. Download the latest version of <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/" target="_blank">Putty</a>. 
1. Double-click on the downloaded installer package to install Putty to a suitable location.
1. Once the install is complete it will be easier to transfer files using PSFTP if the Putty
directory is in your <code>Path</code>.

Putty comes with **Puttygen**, **Pageant** and **PSFTP**, which you will be using.

<h3 id="keys">Create a public/private key pair with PuttyGen<a class="headerlink" href="#keys" title="Permanent link">&para;</a></h3>

1. Double-click `Puttygen` to start the authentication keys creation process.
2. Ensure that `Type of key to generate` has `SSH RSA` selected.
3. Click <`Generate` to create a random key (and move the mouse around to supply the required entropy).
4. Provide a decscription of the key in the `Comment` field or accept the default.
5. Enter and confirm a `>Key Passphrase`to protect your private key.
6. Click `Save Public Key` and save it as `yourapacheusername.pub<`.
7. Click `Save Private Key` and save it as `yourapacheusername.ppk`.
8. To create an `authorized_keys` file, copy the Public Key information in the top box, paste it into a text file (using a tool like `notepad`) and save the file as `authorized_keys`. The file must have that exact name and no extension like `.txt`. Make sure your text editor did not add an extension when you saved the file.
9. Close Puttygen.

<h3 id="auth-keys">Upload the 'authorized_keys' file with PSFTP<a class="headerlink" href="#auth-keys" title="Permanent link">&para;</a></h3>

1. Open a Command Prompt box and navigate to the location where you stored your `authoriized_keys` file.
2. Enter `psftp people.apache.org`. A connection will be made to `people.apache.org`.
3. The first time you use PSFTP, you will have to provide your Apache login user name and password.
4. Create a new directory `.ssh` in your area.
5. Enter `chmod 700 .ssh`. This ensures only you have access to this directory.
6. Enter `cd.ssh` to navigate into the new directory.
7. Enter `put authorized_keys` to upload your `authoriized_keys` file.
8. Enter `exit` to log out from your`people.apache.org` private area and from PSFTP itself.

<h3 id="pageant">Add Key to Pageant and run Pageant<a class="headerlink" href="#pageant" title="Permanent link">&para;</a></h3>

This is probably the most overlooked but most important step for Windows users. You need to load a key into Pageant and have Pageant running all the time in memory so other applications can use the keys you created. If Pageant is not running, when you enter `people.apache.org` Putty or PSFTP will prompt for user and password again regardless of the work you just did.

1. Open Pageant and click `Add` to add a new key.
2. Browse to your `yourapacheusername.ppk` private key file and select it.
3. Click `Close` to close this window. 

Pageant is still running with an icon in the system tray.

You should now be able to log in without being asked for your user name or password any more. Try it:

In the Command Prompt box enter `psftp people.apache.org`.

You should be able to log right in without having to provide your credentials.

**Note** that whenever you exit Pageant, or restart your computer, you will need to restart Pageant and add your key in again. Pageant does not keep details of loaded keys between sessions.

<h3 id="configure-putty">Configure Putty to log in using your Keys<a class="headerlink" href="#configure-putty" title="Permanent link">&para;</a></h3>

1. Open up Putty.
2. Specify <code>people.apache.org</code> as the Hostname.
3. Make sure the SSH protocol radio button is selected.
4. Choose the `Data` sub-category of `Connection`.
5. Provide your Apache user name for `auto-login username`.
6. Select the `SSH` category.
7. Make sure the `SSH 2 Only` radio button is selected.
8. Select the `Auth` sub-category of the SSH category.
1. Make sure the `Attempt "Keyboard Interactive" auth (SSH 2)` checkbox is selected.
1. Click the `Browse` Button and locate and load your `Private Key` you
saved earlier as `yourapacheusername.ppk`.
1. Select the `Session` category and save this session with a suitable name.

All the details are now saved for future use. Now click the <code>Open</code> button to open a secure connection to the server and to
log in automatically to your personal area of `people.apache.org`. You will have to provide your password if this is the first time connecting to your area.

<h2 id="links">Relevant Links<a class="headerlink" href="#links" title="Permanent link">&para;</a></h2>

  - [Apache SSH Guide](user-ssh.html)
  - <a href="https://www.ssh.com/ssh/putty/putty-manuals/0.68/index.html" target="_blank">Putty Setup Guide</a>
  - <a href="https://files.fosswire.com/2007/08/fwunixref.pdf" target="_blank">Unix Command Quick Reference</a>
