
layout: post
Title: LDAP and password policy
date: '2010-12-17T06:38:50+00:00'
permalink: ldap_and_password_policy

<p>As of approximately 03:00 (UTC) today the infrastructure team have enabled a password policy for all LDAP accounts.<br />
This policy has been implemented at the LDAP infrastructure level and will affect all users.  It has been deployed using OpenLDAP's password policy schema, and overlay.</p>

<p>At the time of launch we will be enforcing the following policy. </p> 

<ul>
<li>At the time of a given users 10th successive login failure the account will be locked.</li>  
<li>The account will then be automatically unlocked 24 hours later, or until a member of root@ unlocks it for you.</li> 
<li>If the user successfully completes a login before the tally reaches 10, the counter for failed logins is reset back to 0.</li>
</ul>

<p>We are enabling this to try and prevent any brute force attempt at guessing passwords.  It will also highlight potential issues with accounts. </p>

<p>As with all account related queries, you should be contacting root@ - We will be able to unlock your account for you, allowing you to gain access.</p>
