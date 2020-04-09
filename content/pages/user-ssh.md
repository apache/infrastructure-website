Title: Committer SSH Access

<h2 id="contents"">Contents</h2>
                  
  - <a href="#intro">Introduction</a>
  - <a href="#openssh">Using OpenSSH to connect to Apache</a>
  - <a href="#openssh-ssh2">Configuring OpenSSH to use SSH2 (*nix)</a>
  - <a href="#debug-ssh">Debugging an OpenSSH client connection</a>
  - <a href="#troubleshooting">Troubleshooting</a>
  - <a href="#FAQ">FAQs</a>
  - <a href="#elsewhere">More information</a>


<h2 id="intro">Introduction</h2>

Apache uses SSH (a cryptographic protocol for operating services securely over an unsecured network) to let committers access their home directories on `people.apache.org`. Remember to keep your client up to date with security patches. When using SSH to connect to `people.apache.org` pay close attention to any <a href="#known-host">known host warnings</a>.

<h2 id="openssh">Using Open SSH to connect to Apache</h2>


<h2 id="open-ssh2">Configuring OpenSSH to use SSH2 (*nix)</h2>

<h2 id="debug-ssh">Debugging an Open SSH client connection</h2>

<h2 id="troubleshooting">Troubleshooting</h2>

  - If you encounter a problem with SSH and you are not running the most modern stable release of the client software you are connecting with, please upgrade and retry.
  - Configure the client to use <a href="#ssh2-configuration"> SSH2</a> where possible so the connection to Apache uses the SSH2 protocol. This protocol more secure and lets you use an interactive keyboard (type in password) or <a href="#pki">PKI</a>. If you must use SSH1 then you will need to use PKI.
  - Read <a href="#ssh-debug">the section on debugging SSH</a> and try to diagnose the problem.
  
<h3 id="common-problems">Some common problems</h3>

<p id="exposed"> </p>

**Do not expose your private key**. Generate your key on a computer that is in your control, then upload only the public part to the `people.apache.org` server. Do not make the mistake of generating the key on the `people.apache.org` server.

<h3 id="too-many-groups">Too Many Groups<a class="headerlink" href="#too-many-groups" title="Permanent link">&para;</a></h3>
<p>FreeBSD only allows a user to be in 16 groups. An user who is too popular
will not be allowed to log on. It is easy to mistake this for a ssh
problem. If <code>Authentication succeeded</code> is present in the <a href="#ssh-debug">debug
logs</a> then this indicates that the issue lies on the machine
login (rather than ssh).</p>
<h3 id="batch-mode">Batch Mode<a class="headerlink" href="#batch-mode" title="Permanent link">&para;</a></h3>
<p>Batch mode should only be used by automated scripts. You will not be able
to login if ssh is configured to use batch mode.</p>
<h2 id="FAQ">FAQs</h2>
        


<h2 id="elsewhere">More information<a class="headerlink" href="#elsewhere" title="Permanent link">&para;</a></h2>

  - See instructions for new committers to <a href="https://www.apache.org/dev/new-committers-guide.html#ssh#ssh" target="_blank">configure your account</a>.
  - See instructions for setting up [SSH on Windows](user-ssh-windows.html).


<h1 id="FAQ">FAQ<a class="headerlink" href="#FAQ" title="Permanent link">&para;</a></h1>
<h2 id="ssh2">What Is SSH2?<a class="headerlink" href="#ssh2" title="Permanent link">&para;</a></h2>
<p>The second generation in the ssh family of protocols. It is believed to be
more secure than the first generation and the implementations are now
mature. Certain flaws exist in the first generation protocols which do not
exist in the second generation. SSH2 is therefore recommended.</p>
<p>Most clients can be configured to <a href="#ssh2-configuration">use SSH2</a> (where
possible).</p>
<h2 id="ssh-debug">How Can I Debug My Connection?<a class="headerlink" href="#ssh-debug" title="Permanent link">&para;</a></h2>
<p>The easiest way to diagnose a failing connection is to run your client in
verbose mode. This will print up descriptions of the actions that the
client is taking. How to do this using <a href="http://www.openssh.org">OpenSSH</a> is
<a href="#debug-ssh">here</a> </p>
<p>If <code>Authentication succeeded</code> is present then this indicates that the issue
lies in the machine login (rather than ssh).</p>
<h2 id="ssh2-configuration">How Do I Configure My Client To Use SSH2?<a class="headerlink" href="#ssh2-configuration" title="Permanent link">&para;</a></h2>
<p>If you are using OpenSSH some instructions are <a href="#openssh-ssh2">available</a>.
Otherwise, please consult the manual.</p>
<h2 id="what-client">What Client Can I Use?<a class="headerlink" href="#what-client" title="Permanent link">&para;</a></h2>
<p>Any client that supports the <a href="#ssh2">SSH2</a>. (It is possible to use older
clients that support only SSH1 but that requires more knowledge.)</p>
<p><a href="http://www.openssh.org">OpenSSH</a> is a well known and trusted client that
is available for most *nixes. Some notes on how to use OpenSSH to connect
to Apache are given <a href="#openssh">here</a>.</p>
<h2 id="pki">What Is PKI?<a class="headerlink" href="#pki" title="Permanent link">&para;</a></h2>
<p>Public key infrastructure (PKI) enables the ssh family of protocols to
operate without passing a password to the server. A passphrase is used to
unlock a private key on the client machine. A corresponding public key on
the server is used for authentication the during the handshake.</p>
<p>This method of connection is recommended (as the most secure).</p>
<h2 id="no-connection">Why Can't I Connect Using SSH1?<a class="headerlink" href="#no-connection" title="Permanent link">&para;</a></h2>
<p>You can connect to <code>people.apache.org</code> using the SSH1 protocols but only
when using <a href="#pki">PKI</a> </p>
<h2 id="known-host">What Is A Known Host?<a class="headerlink" href="#known-host" title="Permanent link">&para;</a></h2>
<p>SSH employs the <em>known hosts</em> mechanism to prevent <a href="#middle-man-attacks">man in the
middle</a> attacks. The first time that the client
connects to a server, the fingerprint of the key used by that server is
displayed to the user who may to asked to confirm the identity of that
server. For example:</p>
<p><code><pre>
The authenticity of host 'people.apache.org (209.237.237.194)' can't be
established.
RSA key fingerprint is 51:85:7d:8f:57:54:e7:6f:27:26:98:7a:c7:c1:47:87.
Are you sure you want to continue connecting (yes/no)? 
</pre></code></p>
<p>The fingerprints for <code>people.apache.org</code> can be found
<a href="new-committers-guide.html#spoof">here</a>. If the user elects to continue
then this value will be written to a <code>known_hosts</code> file. In future, when
the user connects to the same server, this value will be checked and the
user alerted if it has changed.</p>
<p>Please do not continue the connection after such an alert: contact
infrastructure. This is of crucial importance when using keyboard
interactive authentication.</p>
<p><strong>Note:</strong> the fingerprint for the key used for ssh is different to the
fingerprint of the certificate used to <a href="version-control.html#cert">securely serve the
website</a>.</p>
<h2 id="middle-man-attacks">What Is A Man-In-The-Middle-Attack?<a class="headerlink" href="#middle-man-attacks" title="Permanent link">&para;</a></h2>
<p>A class of attacks where the attacker masquerades as the server to the
client and the client to the server.</p>
<h1 id="openssh">Using OpenSSH To Connect To Apache<a class="headerlink" href="#openssh" title="Permanent link">&para;</a></h1>
<p><a href="http://www.openssh.org">OpenSSH</a> is a widely used and trusted suite of
software using the SSH family of protocols.</p>
<h2 id="openssh-ssh2">Configuring OpenSSH To Use SSH2 (*nix)<a class="headerlink" href="#openssh-ssh2" title="Permanent link">&para;</a></h2>
<p>The OpenSSH client uses (by default) configuration files in the <code>~/.ssh</code>
directory. The main configuration file is <code>~/.ssh/config</code> and is optional.
In other words, it may or may not exist already. If it does not then it
should be created.</p>
<p>A simple text format is used. Instructions for a particular host (or group
of hosts) are grouped together. The following is a suggested basic
configuration:</p>
<p><code></p>
<pre>
# Apply to all hosts

# Alternatively replace with: 

#Host \*.apache.org
Host \*
  FallBackToRsh no
  Protocol 2,1
</pre>

<p></code></p>
<p>There are many other options available.</p>
<h2 id="debug-ssh">Debugging An OpenSSH Client Connection<a class="headerlink" href="#debug-ssh" title="Permanent link">&para;</a></h2>
<p>To diagnose what's going wrong with an OpenSSH connection, run the client
in verbose mode. To do this just add <code>-v</code>. For example:</p>
<div class="codehilite"><pre>$ <span class="n">ssh</span> <span class="o">-</span><span class="n">v</span>  <span class="o">-</span><span class="n">l</span> <span class="n">committer</span> <span class="n">people</span><span class="p">.</span><span class="n">apache</span><span class="p">.</span><span class="n">org</span>
</pre></div></div>

  <!-- Footer -->
  
  <footer class="bg-primary">
    <div class="container">
      <div class="row">
        <br />
        <div class="col-sm-1">

        </div>
        <div class="col-sm-2">
          <h5 class="white">Community</h5>
          <ul class="list-unstyled white" role="menu">
            <li><a href="http://community.apache.org/">Overview</a></li>
            <li><a href="/foundation/conferences.html">Conferences</a></li>
            <li><a href="http://community.apache.org/gsoc.html">Summer of Code</a></li>
            <li><a href="http://community.apache.org/newcomers/">Getting Started</a></li>
            <li><a href="/foundation/how-it-works.html">The Apache Way</a></li>
            <li><a href="/travel/">Travel Assistance</a></li>
            <li><a href="/foundation/getinvolved.html">Get Involved</a></li>
            <li><a href="/foundation/policies/conduct.html">Code of Conduct</a></li>
            <li><a href="http://community.apache.org/newbiefaq.html">Community FAQ</a></li>
            <li><a href="/memorials/">Memorials</a></li>
          </ul>
        </div>

        <div class="col-sm-2">
          <h5 class="white">Innovation</h5>
          <ul class="list-unstyled white" role="menu">
            <li><a href="http://incubator.apache.org/">Incubator</a></li>
            <li><a href="http://labs.apache.org/">Labs</a></li>
            <li><a href="/licenses/">Licensing</a></li>
            <li><a href="/foundation/license-faq.html">Licensing FAQ</a></li>
            <li><a href="/foundation/marks/">Trademark Policy</a></li>
            <li><a href="/foundation/contact.html">Contacts</a></li>
          </ul>
        </div>

        <div class="col-sm-2">
          <h5 class="white">Tech Operations</h5>
          <ul class="list-unstyled white" role="menu">
            <li><a href="/dev/">Developer Information</a></li>
            <li><a href="/dev/infrastructure.html">Infrastructure</a></li>
            <li><a href="/security/">Security</a></li>
            <li><a href="http://status.apache.org">Status</a></li>
            <li><a href="/foundation/contact.html">Contacts</a></li>
          </ul>
        </div>

        <div class="col-sm-2">
          <h5 class="white">Press</h5>
          <ul class="list-unstyled white" role="menu">
            <li><a href="/press/">Overview</a></li>
            <li><a href="https://blogs.apache.org/">ASF News</a></li>
            <li><a href="https://blogs.apache.org/foundation/">Announcements</a></li>
            <li><a href="https://twitter.com/TheASF">Twitter Feed</a></li>
            <li><a href="/press/#contact">Contacts</a></li>
          </ul>
        </div>

        <div class="col-sm-2">
          <h5 class="white">Legal</h5>
          <ul class="list-unstyled white" role="menu">
            <li><a href="/legal/">Legal Affairs</a></li>
            <li><a href="/legal/dmca.html">DMCA</a></li>
            <li><a href="/licenses/">Licensing</a></li>
            <li><a href="/foundation/marks/">Trademark Policy</a></li>
            <li><a href="/foundation/records/">Public Records</a></li>
            <li><a href="/foundation/policies/privacy.html">Privacy Policy</a></li>
            <li><a href="/licenses/exports/">Export Information</a></li>
            <li><a href="/foundation/license-faq.html">Licensing FAQ</a></li>
            <li><a href="/foundation/contact.html">Contacts</a></li>
          </ul>
        </div>

        <div class="col-sm-1">
        </div>

      </div>
      <hr class="col-lg-12 hr-white" />
      <div class="row">
        <div class="col-lg-12">
          <p class="text-center">Copyright &#169; 2019 The Apache Software Foundation, Licensed under the <a class="white" href="/licenses/LICENSE-2.0">Apache License, Version 2.0</a>.</p>
          <p class="text-center">Apache and the Apache feather logo are trademarks of The Apache Software Foundation. </p>
        </div>
      </div>
    </div>







_moving content from https://www.apache.org/dev/user-ssh.html_
