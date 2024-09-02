Title: Host a Jenkins or Buildbot agent

license: https://www.apache.org/licenses/LICENSE-2.0

Individuals and organizations can support the work of the ASF and its projects by hosting Jenkins or Buildbot agents on virtual machines in their own systems. Donors often provide this service to make available extra build resources for a project that needs more than Infra can easily provide.

**Notes** 
  - Ubuntu is a core supported OS at the ASF and we do not need any external hosting by individuals at this time.
  - Organizations wanting to donate multiple VMs for Jenkins and/or Buildbot use should email `private@infra.apache.org` to start discussions.

## Getting ready to host ###

There are a few things you'll need to know and to adhere to.

  - Keep up to date with security patches etc,, the obvious stuff; we may want to be added to root alias for security reporting etc.
  - Spec requirements: 
      - minimum 16GB RAM
      - 500GB Hard disk 
      - A permanent static IP address
  - You must be an ASF Committer.
  - You must subscribe to the `builds@a.o` email list.
  - Maintain and provide a link to a public page that lists software you add to your agent.
  - Open an INFRA Jira ticket so we can complete your hosting set up when you are completely ready.

### For Buildbot ###

Make sure it's a stock, latest buildbot-worker install for your OS variant.

When you are ready, liaise with `root@a.o` to negotiate connection credentials. Keep your agent secure and only open the one required port.

### For Jenkins ###

  - Create a Jenkins user and group using /home/jenkins.
  - Add the Jenkins ssh public key into the users' `~/.ssh/authorized` keys.
