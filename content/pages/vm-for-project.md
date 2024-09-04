Title: Requesting a virtual machine for a project
license: https://www.apache.org/licenses/LICENSE-2.0

When your PMC wants to run an application that is not part of the offered services (like a demo setup of your project), you need to request a dedicated virtual machine (VM). It is not possible to request a physical machine. Physical machines are shared resources for all ASF projects.

Infra maintains hosts in different computer centers around the world to run virtual machines, so we can relocate your VM as requirements change without you having to reinstall anything.

### Contents ###

  - <a href="#request">Requesting a virtual machine</a>
  - <a href="#deploy">Deploying the virtual machine</a>
  - <a href="#maintain">Project maintainers</a>
  - <a href="#ssh-keys">Obtaining SSH keys</a>
  - <a href="#maintenance">General maintenance</a>
  - <a href="#cautions">Cautions</a>

<h3 id="request">Requesting a virtual machine<a class="headerlink" href="#request" title="Permanent link">&para;</a></h3>

To request a virtual machine, open a <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">Jira</a> ticket with at least the following information:

1. The project's plans for the virtual machine:
    - Why the project needs a dedicated VM
    - Is logging in used in the project's application (HTTPS is mandatory for use of login)?
    - Do any special ports need to be opened?
2. VM resources requested (the operating system will be the latest Ubuntu LTS release):
    - CPU cores (default is 1)
    - RAM (default is 1Gb)
    - Disk capacity (default is 40Gb)
    - Name (default is `<project>-vm.a.o`)
    - Apache ID of project administrator (one of the maintainers you specify below)
3. Application resources:
    - Database (Infra recommends SQLite, given the small size, but can configure an on-box mySQL or PostgreSQL database for the VM.)
    - Httpd (installed pr default, configuration is to be agreed upon)
    - Non-standard packages (will be maintained by infra-p6)
    - DNS names needed (default is to create `vmname` only)
    - Backup needed (default is **no** backups other than what is in Infra-p6)
4. Maintainers:
    - Provide the name, Apache ID, and contact info for at least three PMC members who will maintain the VM.
5. Acknowledgement:
    - Name of a PMC member who acknowledges this request on behalf of the project.

CPU and RAM are expensive resources, so unless you make a really compelling case we will start the VM with default values. If you/we see problems later we can always add more. We can add CPU cores and RAM can without reinstalling anything.

The operating system needs to be supported by our standard applications, therefore we currently only offer Ubuntu.

**Important**: a PMC member must acknowledge the request ticket.

<h3 id="deploy">Deploying the virtual machine<a class="headerlink" href="#deploy" title="Permanent link">&para;</a></h3>

Infra may ask questions to clarify the request. When all is clear, we will create the VM according to specifications, install the OS and the mandatory standard (Infra) applications. The mandatory application guarantee a level of security and provide ssh access common to all vms.

Once we have tested the VM, we will ask a project maintainer to do ssh to the VM.

<h3 id="maintain">Project maintainers<a class="headerlink" href="#maintain" title="Permanent link">&para;</a></h3>

The project maintainers are responsible for maintaining the VM. Infra will normally not maintain the VM, but will check on security from time to time.

Each project maintainer needs to have ssh keys uploaded to `id.a.o` before requesting the VM. Maintainers use the ssh keys stored in LDAP to log in to the VM.

When the VM is created, each maintainer gets karma to access the VM (ldap add host to userid). Once that has been tested, it is time to get sudo karma if it is required.

To prepare for sudo karma follow the <a href="https://reference.apache.org/committer/opie" target="_blank">OPIE guidelines</a>.

When OPIE works, contact us on #asfinfra, or by commenting on the issue, and sudo karma will be granted (ldap add userid to sudoer group).

<h3 id="ssh-keys">Obtaining SSH keys<a class="headerlink" href="#ssh-keys" title="Permanent link">&para;</a></h3>

To use key-based login, you need to generate a key on your local desktop (do not use a publicly accessible server for this) and then add your public key to LDAP using the self-service app at `https://id.apache.org`.

Once you have done this, wait at least 10 mins. You should then be able to log in as follows:

```
:::shell $ ssh [username]@$project-vm.apache.org
```

Depending on your client setup, you may need to run the following command to ensure the key(s) are made available to the SSH client on your system:

```
:::shell $ ssh-add
```

If you use PuTTY, make sure it is configured to force SSH v2 protocol. And use keyboard-interactive.

Once you have logged in, there are few tasks best performed right away. Please take care when using your shell account.

Check that your umask is set in a group-friendly fashion. This ensures that the documents you create are editable by your fellow committers. To do this, (depending on which shell you use) edit the `.cshrc` file or `.profile` (sh derivatives) so the umask is set as follows:

```
umask 002
```

If a umask line already exists, modify it. Otherwise, add a new line. You will need to use a `*nix` command-line editor such as `vi`.

Tip: You can review the files of some other committer: `ls -al ~mymentor; cat ~mymentor/.cshrc`.

<h3 id="maintenance">General maintenance<a class="headerlink" href="#maintenance" title="Permanent link">&para;</a></h3>

There are no mandatory rules, but here are some suggestions:

  - Keep all changes in Git/Puppet. See: `https://github.com/apache/infrastructure-p6`
    - If you do not have karma, please create PRs in a branch against our GitHub repository.
    - Keep all application data in `/x1` if possible.
  - Update Puppet with all extra installed packages.
    - See `https://github.com/apache/infrastructure-p6/tree/production/modules/<vmname>/manifests/init.pp`
    - See also the <a href="https://cwiki.apache.org/confluence/display/INFRA/Git+workflow+for+infrastructure-puppet+repo" target="_blank">Git workflow for an Infrastructure Puppet repository</a>.

See also [Managing virtual machines](vm-management.html)


    
<h3 id="cautions">Cautions<a class="headerlink" href="#cautions" title="Permanent link">&para;</a></h3>

  - Do not try to change items controlled by puppet, such as:
    - iptables
    - sshd
    - ldap
    - /root/bin
    - anything else relevant for security
  - As sudoer you are expected to know what you do, and are expected to clear any problems you create.

Before doing something, you are always welcome to join #asfinfra on Slack and ask about it.
