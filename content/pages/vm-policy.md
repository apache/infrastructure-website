Title: Project VM policy

Projects may request from Infra **one** Ubuntu virtual machine for use as they see fit.

Infra will maintain this VM via our existing configuration management tooling. The project's designated committers can obtain sudo access. The project may either maintain the system _in situ_, or provide PR updates to the Infra <a href="https://cwiki.apache.org/confluence/display/INFRA/Puppet" target="_blank">Puppet</a> code if they wish to use configuration management.

- Do not "do-release-upgrade" the VM without discussing with Infra.
- The project must designate three committers who agree and have the knowledge to maintain the VM.
- Infra reserves the right to patch/update/restart the system at will to maintain security.

See also:

  - the process to [request a VM for your project](vm-for-project.html)
  - [Managing virtual machines](vm-management.html)
