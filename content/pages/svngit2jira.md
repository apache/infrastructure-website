Title: Subversion and Git integration with Jira tickets

Many projects use Jira for managing tracking bugs, milestones, feature requests and so on, and many of these projects keep track of which commit affects which ticket. To make things even easier, we have a service called `svngit2jira`, which integrates
Subversion and Git commits with Jira tickets.

<h2 id="how-it-works">How it works<a class="headerlink" href="#how-it-works" title="Permanent link">&para;</a></h2>
<p>The amount of work a committer has to do to achieve this integration is very light; 
Simply mention a JIRA ticket in a
commit, and the specific JIRA ticket will receive an update indicating that a
certain commit has been made in reference to the ticket. As an example, you may
want to check out, for instance,
<a href="https://issues.apache.org/jira/browse/CLOUDSTACK-1638">this CloudStack ticket</a> 
(just scroll down a bit and you'll see the commit mentioned). </p>
<p>This service also plugs into the
ReviewBoard instance if you use JIRA ticket names there, as for example the 
CloudStack project does.</p>
<h2 id="general-use-of-the-service">General use of the service<a class="headerlink" href="#general-use-of-the-service" title="Permanent link">&para;</a></h2>
<p>As explained, the most common scenario is simply mentioning a JIRA ticket in your 
commit, and the JIRA ticket will be updated to reflect your new commit. Some 
projects have this trigger set, so that it only updates a ticket if the first 
sentence is the JIRA ticket number, but we can tailor this to suit your project's 
needs.</p>
<h2 id="getting-set-up-for-svngit2jira">Getting set up for svngit2jira<a class="headerlink" href="#getting-set-up-for-svngit2jira" title="Permanent link">&para;</a></h2>
<p>Enabling the service for your project is as easy as creating a 
<a href="https://issues.apache.org/jira/browse/INFRA">JIRA</a> ticket with 
Infrastructure. We'll need to know the following things in order to proceed:</p>
<ul>
<li>Which project is interested in this service</li>
<li>Is the project in agreement on using this? (please ensure this before requesting 
    the feature, as it does tend to add quite a lot of new information to JIRA)</li>
<li>What JIRA name does your project use? (for example, INFRA, GIRAPH etc)</li>
<li>Do you use git or subversion</li>
<li>How would you like commits to trigger an update of a JIRA ticket (this can be 
    anything from the standard catch-all FOO-1234 trigger to more specific rules 
    you thought of yourself)</li>
<li>If you are using Git, are there any specific branches you'd like the service to ignore </li>
</ul>
<h2 id="source-code">Source code<a class="headerlink" href="#source-code" title="Permanent link">&para;</a></h2>
<p>The source for this feature is freely available at 
<a href="https://svn.apache.org/repos/infra/infrastructure/trunk/projects/svngit2jira/">this location</a>.</p></div>
