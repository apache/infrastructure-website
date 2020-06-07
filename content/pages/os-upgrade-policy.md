Title: Operating system upgrade policy

Infra supports Ubuntu long-term support (LTS) releases and Windows platforms. 

We are migrating from older Unix-derived operating systems such as FreeBSD and Solaris to one of our supported options, usually as we migrate from older servers to newer (more robust, more reliable) machines. Some services end up on a virtual machine (VM) on a host physical server, and some services run on "bare metal". However, we refer to all these migrations as "VM migrations."

  - When we move to new machine running Ubuntu, we install the current stable version of the operating system.
  - Windows servers typically run Windows Server 2016 Standard. As we replace older physical machines with newer ones, we install the most recent stable version of Windows Server Standard that is available at the time of migration.
  - ASF Windows desktops typically run Windows 10 Professional. The migration pattern is as for the servers.
  
