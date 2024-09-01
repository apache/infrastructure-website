Title: Committer SSH Access

Apache uses SSH (a cryptographic protocol for operating services securely over an unsecured network) to let committers access their project VMs (if configured). 

Remember to keep your client up to date with security patches. Pay close attention to any <a href="#known-host">known host warnings</a>. 

## Contents ##

  - <a href="#openssh">Using OpenSSH to connect to Apache</a>
  - <a href="#openssh-ssh2">Configuring OpenSSH to use SSH2 (*nix)</a>
  - <a href="#debug-ssh">Debugging an OpenSSH client connection</a>
  - <a href="#troubleshooting">Troubleshooting</a>
  - <a href="#FAQ">FAQs</a>
  - <a href="#elsewhere">More information</a>

<h2 id="openssh">Using OpenSSH to connect to Apache<a class="headerlink" href="#openssh" title="Permanent link">&para;</a></h2>

<a href="https://www.openssh.org" target="_blank">OpenSSH</a> is a widely used and trusted suite of software using the SSH family of protocols.

<h2 id="openssh-ssh2">Configuring OpenSSH to use SSH2 (*nix)<a class="headerlink" href="#openssh-ssh2" title="Permanent link">&para;</a></h2>

The OpenSSH client uses by default configuration files in the `~/.ssh` directory. The main configuration file is `~/.ssh/config` and is optional. It may exist already. If it does not, you can create it in a simple text format. Group together instructions for a particular host (or group of hosts). Here is a suggested basic configuration:

```
<pre>
# Apply to all hosts

# Alternatively replace with: 

#Host \*.apache.org
Host \*
  FallBackToRsh no
  Protocol 2,1
</pre>
```

Many other options are available.

<h2 id="debug-ssh">Debugging an OpenSSH client connection<a class="headerlink" href="#debug-ssh" title="Permanent link">&para;</a></h2>

To diagnose what's going wrong with an OpenSSH connection, run the client in verbose mode. To do this just add `-v`:

```
ssh -v -l yourApacheID some-project-server.apache.org
```

<h2 id="troubleshooting">Troubleshooting<a class="headerlink" href="#troubleshooting" title="Permanent link">&para;</a></h2>

  - If you encounter a problem with SSH and you are not running the most modern stable release of the client software you are connecting with, upgrade and retry.
  - Configure the client to use <a href="#ssh2-configuration"> SSH2</a> where possible so the connection to Apache uses the SSH2 protocol. This protocol is more secure and lets you use an interactive keyboard (type in password) or <a href="#pki">PKI</a>. If you must use SSH1, you will need to use PKI.
  - Read <a href="#ssh-debug">the section on debugging SSH</a> and try to diagnose the problem.

<h3 id="common-problems">Some common problems<a class="headerlink" href="#common-problems" title="Permanent link">&para;</a></h3>

<h4 id="too-many-groups">Too Many Groups<a class="headerlink" href="#too-many-groups" title="Permanent link">&para;</a></h4>
FreeBSD only allows a user to be in 16 groups. A user who is too popular will not be allowed to log on. It is easy to mistake this for an ssh problem. If `Authentication succeeded` is present in the <a href="#ssh-debug">debug logs</a>, this indicates that the issue lies on your machine's login rather than with ssh.

<h4 id="batch-mode">Batch Mode<a class="headerlink" href="#batch-mode" title="Permanent link">&para;</a></h4>

Only use batch mode in automated scripts. You will not be able to log in if ssh is configured to use batch mode.

<h2 id="FAQ">FAQ<a class="headerlink" href="#FAQ" title="Permanent link">&para;</a></h2>

<h4 id="ssh2">What is SSH2?<a class="headerlink" href="#ssh2" title="Permanent link">&para;</a></h4>

The second generation in the ssh family of protocols. It is believed to be more secure than the first generation and the implementations are now mature. Certain flaws exist in the first generation protocols which do not exist in the second generation, so we recommend <a href="#ssh2-configuration">using SSH2</a> where possible.

<h4 id="ssh-debug">How can I debug my connection?<a class="headerlink" href="#ssh-debug" title="Permanent link">&para;</a></h4>

The easiest way to diagnose a failing connection is to run your client in verbose mode. This will print up descriptions of the actions that the client is taking. <a href="#debug-ssh">Here</a> is how to do this using <a href="https://www.openssh.org" target="_blank">OpenSSH</a>.

If <code>Authentication succeeded</code> is present then this indicates that the issue
lies in your machine login rather than in ssh.

<h4 id="ssh2-configuration">How do I configure my client to use SSH2?<a class="headerlink" href="#ssh2-configuration" title="Permanent link">&para;</a></h4>

If you are using OpenSSH, <a href="#openssh-ssh2">some instructions</a> are available. Otherwise, please consult the manual.

<h4 id="what-client">What client can I use?<a class="headerlink" href="#what-client" title="Permanent link">&para;</a></h4>

You can use any client that supports <a href="#ssh2">SSH2</a>. (It is possible to use older
clients that support only SSH1 but that requires more knowledge.)

<a href="http://www.openssh.org">OpenSSH</a> is a well known and trusted client that
is available for most *nixes. Some notes on how to use OpenSSH to connect
to Apache are <a href="#openssh">here</a>.

<h4 id="pki">What is PKI?<a class="headerlink" href="#pki" title="Permanent link">&para;</a></h4>

Public key infrastructure (PKI) enables the ssh family of protocols to operate without passing a password to the server. You use a passphrase to unlock a private key on the client machine, and a corresponding public key on the server for authentication the during the handshake. We recommend this as the most secure method of connection.

<h4 id="no-connection">Why can't I connect using SSH1?<a class="headerlink" href="#no-connection" title="Permanent link">&para;</a></h4>

Because it has been deprecated in OpenSSH.

<h4 id="known-host">What is a known host?<a class="headerlink" href="#known-host" title="Permanent link">&para;</a></h4>

SSH employs the <em>known hosts</em> mechanism to prevent <a href="#middle-man-attacks">man in the
middle</a> attacks. The first time that the client connects to a server, the fingerprint of the key used by that server is
displayed to the user, who may to asked to confirm the identity of that server. For example:

```
The authenticity of host 'home.apache.org (209.237.237.194)' can't be established.
RSA key fingerprint is 1c:5d:3f:a2:89:97:2e:39:eb:b0:09:9e:cf:c6:8d:f3.
Are you sure you want to continue connecting (yes/no)? 
```

The fingerprints for <code>home.apache.org</code> can be found
<a href="/new-committers-guide.html#identity-theft">here</a>. If the user elects to continue,
this value is written to a `known_hosts` file. In future, when the user connects to the same server, the system checks this value and alerts the user if it has changed. **Do not continue the connection** after such an alert: contact infrastructure. This is of crucial importance when using keyboard interactive authentication.

**Note**: The fingerprint for the key used for ssh is different from the fingerprint of the certificate used to securely serve the
website.

<h4 id="middle-man-attacks">What Is a Man-in-the-Middle attack?<a class="headerlink" href="#middle-man-attacks" title="Permanent link">&para;</a></h4>

A class of attacks where the attacker masquerades as the server to the client and as the client to the server.

<h2 id="elsewhere">More information<a class="headerlink" href="#elsewhere" title="Permanent link">&para;</a></h2>

  - <a href="/new-committers-guide.html#identity-theft" target="_blank">Identity theft</a>
