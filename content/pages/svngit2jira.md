Title: Subversion and Git integration with Jira tickets

license: https://www.apache.org/licenses/LICENSE-2.0

Many projects use Jira for managing tracking bugs, milestones, feature requests and so on, and many of these projects keep track of which commit affects which ticket. To make things even easier, we have a service called `svngit2jira`, which integrates
Subversion and Git commits with Jira tickets.

<h2 id="how-it-works">How it works<a class="headerlink" href="#how-it-works" title="Permanent link">&para;</a></h2>

Simply mention a Jira ticket in a commit, and the specific ticket receives an update indicating that the commit has been made in reference it. For example, scroll down in <a href="https://issues.apache.org/jira/browse/CLOUDSTACK-1638" target="_blank">this CloudStack ticket</a> to see the commit mentioned.

This service also plugs into the <a href="https://reviews.apache.org/r/" target="_blank">ReviewBoard</a> instance if you use Jira ticket names there, as the CloudStack project does.</p>

<h2 id="general-use-of-the-service">General use<a class="headerlink" href="#general-use-of-the-service" title="Permanent link">&para;</a></h2>

The most common scenario is to mention a Jira ticket in your commit, and the service updates the ticket to reflect your new commit. Some 
projects have a trigger set so that it only updates a ticket if the first  sentence is the Jira ticket number, but we can tailor this to suit your project's needs.

<h2 id="getting-set-up-for-svngit2jira">Setting up svngit2jira<a class="headerlink" href="#getting-set-up-for-svngit2jira" title="Permanent link">&para;</a></h2>

To enable the service for your project, create an 
<a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">Infra Jira ticket</a>. Include this information:

  - The name of the project.
  - Has the PMC agreed to use this? (Make sure of this before requesting the feature, as it does tend to add quite a lot of new information to a Jira ticket.)
  - What Jira name does your project use?
  - Does the project use Git or Subversion?
  - How would you like commits to trigger an update of a JIRA ticket. This can be anything from the standard catch-all FOO-1234 trigger to more specific rules you thought of yourself.
  - If you are using Git, are there any specific branches you'd like the service to ignore?
  
<h2 id="source-code">Source code<a class="headerlink" href="#source-code" title="Permanent link">&para;</a></h2>

The source for this feature is <a href="https://svn.apache.org/repos/infra/infrastructure/trunk/projects/svngit2jira/" target="_blank">freely available</a>.
