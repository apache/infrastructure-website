
layout: post
Title: Bringing GitPubSub to the Apache Jenkins build server
date: '2017-03-26T01:07:08+00:00'
permalink: bringing-gitpubsub-to-the-apache

<p>
When it comes to <a href="#Jenkins">[Jenkins</a>], it has long been known that [polling must die].
</p> 
  <p>While we could go and create post commit hooks in all the ASF hosted Git repositories, that is something that realistically is just creating an added maintenance burden.

In any case, we have [GitPubSub]. </p> 
  <p>The question then becomes, how do we integrate [GitPubSub] with [Jenkins]?

Thankfully, ASF committer stephenc is also an active committer to the [Jenkins] project and created a [plugin] that connects to [GitPubSub] parses the events and passes them through to the Jenkins [SCM API].
</p> 
  <p>
What does this mean?

</p> 
  <p>* You can turn your Git polling down - way way down - to something like once per day.
This should significantly reduce the load on both the ASF git servers and builds.apache.org<br />* Your builds will be triggered in seconds rather than having to wait for the next polling run.<br />* You can try out using Multi-branch projects much like the [Maven] project has been doing for [Maven core] and [Maven Surefire]
</p> 
  <p>
If the reaction to this change proves positive, the next step will be to integrate SvnPubSub with Jenkins and bring the benefits to the Subversion based projects too

  </p> 
  <p> </p> 
  <p>See also this blog post by Stephen Connolly:</p> 
  <p> <a href="https://www.cloudbees.com/blog/using-multi-branch-pipelines-apache-maven-project">https://www.cloudbees.com/blog/using-multi-branch-pipelines-apache-maven-project</a><br /></p> 
  <p>[polling must die]: http://kohsuke.org/2011/12/01/polling-must-die-triggering-jenkins-builds-from-a-git-hook/<br />[GitPubSub]: https://www.apache.org/dev/gitpubsub.html
<br /> <a name="Jenkins">[Jenkins]</a>: https://jenkins.io/
  <br />[plugin]: https://github.com/stephenc/asf-gitpubsub-jenkins-plugin
  <br />[SCM API]: https://plugins.jenkins.io/scm-api
  <br />[Maven]: https://maven.apache.org
  <br />[Maven core]: https://builds.apache.org/job/maven-3.x-jenkinsfile/
<br />  [Maven Surefire]: https://builds.apache.org/job/maven-surefire-pipeline/

</p> 
  <p>Posted on behalf of Committer Stephen Connolly (stephenc)
</p>
