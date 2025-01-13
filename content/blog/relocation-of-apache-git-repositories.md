title: Relocation of Apache git repositories on git-wip-us.apache.org to gitbox.apache.org
date: '2018-12-07T17:33:33+00:00'
permalink: relocation-of-apache-git-repositories
layout: post

<p>[IF YOUR PROJECT DOES NOT HAVE GIT REPOSITORIES ON GIT-WIP-US PLEASE DISREGARD THIS POST]<br /><br />Hello Apache projects,<br /><br />I am writing to you because you may have git repositories on the git-wip-us server, which is slated to be decommissioned in the coming months. All repositories will be moved to the new gitbox service which includes direct write access on GitHub as well as the standard ASF commit access via gitbox.apache.org.</p> 
  <p><strong>Why this move?</strong><br />The move comes as a result of retiring the git-wip service, as the hardware it runs on is longing for retirement. In lieu of this, we have decided to consolidate the two services (git-wip and gitbox), to ease the management of our repository systems and future-proof the underlying hardware. The move is fully automated, and ideally, nothing will change in your workflow other than added features and access to GitHub.<br /></p> 
  <p><strong>Timeframe for relocation</strong><br />Initially, we are asking that projects voluntarily request to move their repositories to gitbox. The voluntary time frame is between now and January 9th 2019, during which projects are free to either move over to gitbox or stay put on git-wip. After this phase, we will be requiring the remaining projects to move within one month, after which we will move the remaining projects over.<br /><br />To have your project moved in this initial phase, you will need:<br /></p> 
  <ul> 
    <li>Consensus in the project (documented via the mailing list)</li> 
    <li>File a JIRA ticket with INFRA to voluntarily move your project repos over to gitbox (as stated, this is highly automated and will take between a minute and an hour, depending on the size and number of your repositories)<br /></li> 
  </ul> 
  <p>To sum up the preliminary timeline;<span style="background-color: #02ff00;"></span></p> 
  <ul> 
    <li><span style="background-color: #02ff00;">December 9th 2018 -&gt; January 9th 2019: Voluntary (coordinated) relocation</span></li> 
    <li><span style="background-color: #ffff00;">January 9th -&gt; February 6th: Mandated (coordinated) relocation</span></li> 
    <li><span style="background-color: #ff0000;">February 7th: All remaining repositories are mass migrated</span></li> 
  </ul> 
  <p><br />This timeline may change to accommodate various scenarios.<br /></p> 
  <p><strong>Using GitHub with ASF repositories</strong><br />When your project has moved, you are free to use either the ASF repository system (gitbox.apache.org) OR GitHub for your development and code pushes. To be able to use GitHub, please follow the primer at: <a href="https://reference.apache.org/committer/github">https://reference.apache.org/committer/github</a> We appreciate your understanding of this issue, and hope that your project can coordinate voluntarily moving your repositories in a timely manner.<br /><br />All settings, such as commit mail targets, issue linking, PR notification schemes etc will automatically be migrated to gitbox as well.<br /></p>
