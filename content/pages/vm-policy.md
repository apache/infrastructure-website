Title: Project VM policy
license: https://www.apache.org/licenses/LICENSE-2.0

Projects may request from Infra **one** Ubuntu virtual machine for use as they see fit.

Infra will maintain this VM via our existing configuration management tooling. The project's designated committers can obtain sudo access. The project may either maintain the system _in situ_, or provide PR updates to the Infra <a href="https://cwiki.apache.org/confluence/display/INFRA/Puppet+Documentation" target="_blank">Puppet</a> code if they wish to use configuration management.

- Do not "do-release-upgrade" the VM without discussing with Infra.
- The project must designate three committers who agree and have the knowledge to maintain the VM.
- Project VMs will be rebooted automatically to apply security updates at 0200 UTC when necessary, based on the Ubuntu unattended-upgrades software determination. To request an opt-out of automated patch reboots, you may open an Infra Jira ticket with your justification, but it is unlikely to be granted without a compelling rationale. Notifications of reboot completion can be sent to a project list if desired. Infra is planning on making the reboot time configurable in the future.
- Infra reserves the right to patch/update/restart the system regardless of the opt-out policy as needed to maintain current patch levels and security.

See also:

  - the process to [request a VM for your project](vm-for-project.html)
  - [Managing virtual machines](vm-management.html)
