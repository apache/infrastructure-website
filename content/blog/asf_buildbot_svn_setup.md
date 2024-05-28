
layout: post
Title: ASF Buildbot svn setup
date: '2010-03-29T10:25:59+00:00'
permalink: asf_buildbot_svn_setup

<p>Here at the ASF we have a subversion setup with all our projects code in one repository, with each of those projects having their own style of trunk/branches/tags/site etc.. This works well for us, but did present us with some initial problems when setting up our Buildbot instance to work with it.</p>
  <p>Knowing that others have the same or similar arrangement with their svn instance, we thought we would share how we got Buildbot working well for us. Note that this is not a tutorial on Buildbot, more of a quick mini guide with more code than explanation, hoping you'll work out the rest for your needs.We will be working with four files:- svn_buildbot.py, post-commit, buildbot_project_paths and master.cfg.</p>
  <p>First off, we needed to alter a section of the svn_buildbot.py file that comes in the buildbot/contrib directory. We copied this file to our svn host machine and edited this section:</p>
  <pre>def split_file_branches(changed_file, project_paths):

    pieces = changed_file.split(os.sep)
    #Assume the layout is something like :
    # trunk =&gt; foo/bar/baz/trunk/file
    # branches/test  =&gt; foo/bar/baz/branches/test/file
    # Slurp everything up to one of these 2 'markers' and call that the branch
    found = False

    f = open(project_paths, 'r')
    for line in f.readlines():
        line = line.strip()
        regexp = re.compile(line)
        m = regexp.match(changed_file)
        if m:
            branch = m.group(1)
            path =   m.group(2)
            print &gt;&gt; sys.stderr, &quot;branch=%s, path=%s&quot; % (branch, path)
            return (branch, path)
  
    
    i = 0
    for piece in pieces:
        i = i + 1	
        # Find trunk, we are done
        if piece == 'trunk':
            found = True
            break
        elif piece == 'branches':
            i = i + 1
            found = True
            break
        
    # We found a layout we know, so send it to buildbot
    if found:
        branch = os.path.join(*pieces[0:i]) 
        path =   os.path.join(*pieces[i:])
    else:        
        branch = pieces[0]
        path = os.path.join(*pieces[1:])
            
    print &gt;&gt; sys.stderr, &quot;branch=%s, path=%s&quot; % (branch, path)
    return (branch, path)     
       
    #return (pieces[0], os.path.join(*pieces[1:]))

    raise RuntimeError(&quot;cannot determine branch for '%s'&quot; % changed_file)

split_file = split_file_branches
</pre>
  <p>Next up , the relevant entry in our subversion/hooks/post-commit file looks like this (with&nbsp;constants defined earlier in the file): </p>
  <pre>    $SVNLOOK dirs-changed -r &quot;$REV&quot; &quot;$REPOS&quot; | egrep -qf &quot;$BUILDBOT_PROJECT_PATHS&quot; &amp;&amp; 
( $BUILDBOT --repository &quot;$REPOS&quot; --revision &quot;$REV&quot; --bbserver &quot;$BBSERVER&quot; --bbport &quot;$BBPORT&quot; 
--project-paths &quot;$BUILDBOT_PROJECT_PATHS&quot; &gt;&gt;/var/log/svn_buildbot.log 2&gt;&amp;1 &amp; )
</pre>
  <p>And, last but not least for the svn host side of things, our buildbot_project_paths file which contains entries such as :</p>
  <pre>^(<strong>incubator/wookie/trunk</strong>)/(.*)
^(stdcxx/trunk)/(.*)
^(incubator/trafficserver/traffic/trunk)/(.*)
^(incubator/trafficserver/traffic/branches/2.0.x)/(.*)
^(subversion/trunk)/(.*)
</strong /></strong /></pre>
  <p>So you create an entry from the svn base directory for each projects trunk or branch that you want Buildbot to take notice of, the rest being ignored.</p>
  <p>Now, we match those buildbot_project_paths entries in our master.cfg file with an AnyBranchScheduler like this:</p>
  <pre># schedulers
from buildbot.scheduler import AnyBranchScheduler

c['schedulers'].append(AnyBranchScheduler(name=&quot;on-wookie-commit&quot;,
                         branches=[&quot;<strong>incubator/wookie/trunk</strong>&quot;],
                         treeStableTimer=2,
                         builderNames=[&quot;wookie-trunk&quot;]))

#builders

f28 = factory.BuildFactory()
f28.addStep(SVN(
    mode=&quot;clobber&quot;,
    baseURL=&quot;http://svn.apache.org/repos/asf/&quot;,
    defaultBranch=&quot;<strong>incubator/wookie/trunk</strong>&quot;,
    haltOnFailure=True,
))

etc...
</pre>
  <h4>Summary</h4>
  <p>So, to tie it all together, what we have done is created a workflow like this:-</p>
  <ol>
    <li>A commit happens, the post-commit file checks the buildbot_project_paths file to see if it is relevant to any of our projects. If not, nothing else happens. </li>
    <li>If we have a match then svn_buildbot.py is called, and uses the entry in buildbot_project_paths as the branch with the root dir of svn as the base, then sends these two pieces of information over to the Buildbot master. </li>
    <li>The Buildbot master checks its config, finds a match in the 'branches' entry for our AnyBranchScheduler and triggers the appropriate build. </li>
  </ol>
  <p>I hope that helps someone out there , at least, until Buildbot project changes again, it is a fast moving project currently! - 0.80 for instance has introduced the 'project' property and the 'repository' property for schedulers which may negate the need for some of this, but I haven't investigated to date. (See&nbsp;<a href="http://github.com/djmitche/buildbot/blob/buildbot-0.8.0/NEWS">http://github.com/djmitche/buildbot/blob/buildbot-0.8.0/NEWS</a>&nbsp;for more info on that.)</p>
