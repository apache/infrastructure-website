Title: Operating system upgrade policy

license: https://www.apache.org/licenses/LICENSE-2.0

Infra supports Ubuntu long-term support (LTS) releases and Windows platforms. 

Some services are on a virtual machine (VM) on a host physical server, and some services run on "bare metal". 

  - When we move to a new machine running Ubuntu, we install the current stable version of the operating system.
  - Windows servers typically run Windows Server 2016 Standard. As we replace older physical machines with newer ones, we install the most recent stable version of Windows Server Standard that is available at the time of migration.
  - ASF Windows desktops typically run Windows 10 Professional. The migration pattern is as for the servers.
  - For builds, we run <a href="https://cwiki.apache.org/confluence/display/INFRA/Buildbot" target="_blank">Buildbot</a> on Windows desktops and <a href="https://cwiki.apache.org/confluence/display/INFRA/Jenkins" target="_blank">Jenkins</a> on Windows servers.
  
