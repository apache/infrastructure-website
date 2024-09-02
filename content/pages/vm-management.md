Title: Managing virtual machines

license: https://www.apache.org/licenses/LICENSE-2.0

The ASF provides a virtual machine (VM) for any ASF project that need one, with the expectation that the project will actively work to maintain their VM. Note the text in bold in Google's definition of a VM:

<blockquote>
A virtual machine (VM) is a digital version of a physical computer. Virtual machine software can run programs and operating systems, store data, connect to networks, and do other computing functions, and <b>requires maintenance</b> such as updates and system monitoring.
</blockquote>

When an Apache project requests a VM, it identifies three project committers who will be responsible for the tasks related to maintaining the VM in a good state. Infra is there to help when complex problems arrive, but is not the first line of support for your VM.

## Managing your VM
Infra is responsible for most VM high-level management tasks:

  - Starting the VM.
  - Shutting down the VM (projects can halt, but not re-start the VM as it requires access to the VM provider). If you have stopped your VM, you will need to ask Infra to re-start it.
  - Cloning the VM. This occurs very rarely.
  - Migrating to a new VM. Infra creates the new VM and can assist with puppet (re)config as needed.

## Maintenance
Your project is responsible for maintenance tasks like

  - renewing or replacing expired letsencrypt certificates
  - resolving disk space issues
  - maintaining any software configured by the project
  - addressing security issues in software configured by the project in a timely and appropriate manner
  - replying to Infra and Security queries regarding the VM in a timely and appropriate manner

You do not need to worry about upgrading the base operating system or other packages Infra installed when setting up the VM. They receive upgrades automatically, and the system will be rebooted automatically when a security patch requires it.

## What Infra will do

  - Create your VM upon request. Each project can have one VM. Make your case to vp-infra if you feel you absolutely need more than one.
  - Configure the base operating system, install Infra configuration management (puppet)
  - Add users to host ACL and sudoers as needed/requested by the PMC
  - Back up the system (see [backup policy](backup-policy.html))
  - Apply operating system updates and security patches automatically
  - Reboot the system with or without notice as Infra deems necessary
  - Assist the project in defining Puppet configuration management where desired and appropriate

## What Infra will not do

  - Develop advanced software configurations for your project's workflow
  - Fix or maintain software deployed by the project
  - Develop advanced Puppet configuration automation for your project's deployments
  - Provide access to ASF infrastructure build deployment secrets

## When you get stuck

Open a Jira ticket for Infra with the details of the problem you are running into with your VM. We will help to resolve it.
