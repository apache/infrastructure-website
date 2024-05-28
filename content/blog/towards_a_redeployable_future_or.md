
layout: post
Title: Towards a redeployable future, or how I stopped worrying and learned to love setting the execute bit on CGI files
date: '2015-02-27T13:08:05+00:00'
permalink: towards_a_redeployable_future_or

<p>Things change, even within the ASF.</p> 
  <p>One of these changes is to our infrastructure, and is a move from manually managed and maintained web servers towards re-deployable, configuration managed servers that tend to themselves and rarely, if ever, require manual intervention. As such, we have started moving towards no longer manually fixing bugs that creep up on various project web sites, in particular setting the correct permission on files. This means that all projects are now required to check their download scripts and verify that the executable flag is set on these CGI files. If not, your download page will likely not work.</p> 
  <p>Whenever we receive an email from a user of an Apache project about an error on a project web site, we will forward this to the respective project, but we ask that projects take proactive measures and check their download scripts (and any other scripts they may have) to ensure that they have the right permissions set and work.</p> 
  <p>&nbsp;Projects using the CMS system will, for the time being, have to commit the execute bit changes directly to the staging repo for their site. <br /></p> 
  <p>With regards,<br />Daniel on behalf of the Infrastructure Team.<br /></p>
