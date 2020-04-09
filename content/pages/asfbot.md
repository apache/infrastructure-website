Title: ASF IRC services and archives

<h2 id="intro">Introduction</h2>
`ASFBot` on the Freenode network offers many services for Apache projects on Internet Relay Chat (IRC). IRC is an application layer protocol that facilitates text communication. The chat process works on a client/server networking model.

To enable these services, contact Infra, either with a <a href="https://issues.apache.org/jira/browse/INFRA" target="_blank">Jira ticket</a> or through `#asfinfra` on the official <a href="https://the-asf.slack.com/" target="_blank">Apache Slack instance</a>.

<h2 id="commits">Subversion, Git and Jira reporting</h2>

ASFBot can report on new commits to your Subversion or Git repository - 
similar to the old CIA services - 
or report when a JIRA ticket was created, updated, closed etc. These 
reports can be tailored to your individual needs; multiline logs, 
compacted paragraphs, coloring, different report styles etc.</p>
<p>You can subscribe to any repository you like, and get reports on any specific 
changes you prefer, as long as these changes are publicly available.</p>
<p>Subscriptions are <em>tag-based</em>, meaning that any one tag will apply to 
f.x. both Subversion and git commits.</p>
<h2 id="jiras">Latest JIRA change<a class="headerlink" href="#jiras" title="Permanent link">&para;</a></h2>
<p>If your channel is set up for JIRA reporting, ASFBot will keep track of the 
latest changes to a JIRA ticket. To view, for instance, the last comment pertaining 
to an issue, simply type: <code>ASFBot: comment [ticket]</code> where <code>ticket</code> could be fx. 
<code>INFRA-1234</code>.</p>
<h2 id="issues">Issue information fetching<a class="headerlink" href="#issues" title="Permanent link">&para;</a></h2>
<p><code>ASFBot</code> can assist people in finding the correct information or link regarding 
specific JIRA or Bugzilla issues. To use this feature, simply type f.x. <code>"issue #52230"</code> 
to get a link for the Bugzilla issue no. 52230 and a quick summary of the issue. 
Or you could type <code>"COUCHDB-1234"</code> to get a link to that specific JIRA ticket. 
Please note that issue summaries are only available for Bugzilla at the moment.</p>
<h2 id="secretary">Secretary feature<a class="headerlink" href="#secretary" title="Permanent link">&para;</a></h2>
<p>ASFBot provides a simple secretary feature for all to use. 
To leave a message for an absent person, simply write: 
<code>ASFBot: tell [recipient] [message]</code>, and that message will be passed on 
the next time that person logs onto the channel.</p>
<h2 id="meetings">Record keeping for meetings<a class="headerlink" href="#meetings" title="Permanent link">&para;</a></h2>
<p>ASFBot can keep a record of meetings done on IRC and publish these in HTML 
format with an agenda, actions to be taken and members present.</p>
<p>Record keeping is only allowed in channels where logging is enabled. 
To enable logging, please contact the infrastructure team, either via 
a JIRA ticket or on #asfinfra.</p>
<p>Record keeping works as follows:</p>
<ul>
<li>To initiate a meeting, type <code>"ASFBot: meeting start"</code>.</li>
<li>To set an agenda, either type <code>"#topic [agenda goes here]"</code> or use the <code>/topic</code> 
     command to change the channel's topic. ASFBot will keep the original topic of 
     the channel in memory, and change it back once the meeting is over.</li>
<li>To add an information to the meeting summary, type <code>"#info [something here]"</code>.</li>
<li>To add an action to be taken before the next meeting, type <code>"#action [action]"</code>.</li>
<li>To end a meeting and save a summary of it, type <code>"ASFBot: meeting end"</code>. 
     This will end the record keeping and produce an HTML document containing 
     the summary of the meeting as well as a log of everything that was said.</li>
<li>To send an IRC meeting summary as an email to a recipient, type 
     <code>"ASFBot: meeting send your@domain.tld"</code>. You will need to have been granted 
     karma by infrastructure to perform this task.</li>
</ul>
<p><em>Anything said with <code>[off]</code> at the beginning will be considered off-the-record 
and will not be written in the meeting log.</em>
In most regards, ASFBot will understand the <a href="http://meetbot.debian.net/Manual.html"><code>meetbot</code></a> commands, and as such, 
<code>#meetingstart</code> or <code>#meetingend</code> will also start or end a recording of a meeting.</p>
<p>For an example of what a meeting summary may look like, check out <a href="https://comments.apache.org/meetings/couchdb-meeting-16_01_2013-2439.html">this CouchDB meeting</a></p>
<h2 id="comments">Integration with comments.apache.org<a class="headerlink" href="#comments" title="Permanent link">&para;</a></h2>
<p><code>ASFBot</code> can relay comments provided via comments.apache.org to your IRC channel. 
If you have set up a karma list with Infrastructure, you can also reply to comments 
via IRC.</p>
<h2 id="sourcecode">Technical Information About ASFBot<a class="headerlink" href="#sourcecode" title="Permanent link">&para;</a></h2>
<p>There are more <a href="https://wilderness.apache.org/manual.html">documents about how ASFBot</a> works and the <a href="https://svn.apache.org/repos/infra/infrastructure/trunk/projects/asfbot/">ASFBot source code is available</a>. </p></div>


_moving contents from https://www.apache.org/dev/asfbot.html_
