title: Inside Infra October 2026 
date: '2026-10-22' 
permalink: newsletter1026 layout: post

## Welcome to *Inside Infra* for October, 2026

### Roundtable

October's Roundtable was an in-person event during Community Over Code Glasgow. A summary of the discussion is not yet available.

Note: the next online Roundtable will be **November 4, 1700 GMT**. We will be trying out a new format. Here are some of the changes:

  - The roundtable will run up to 90 minutes, rather than 60.
  - There will be two half-hour presentation slots at each meeting: Infra will select the topic and make the presentation for one, and Tooling will do the same for the other.
  - We will try to keep all questions for the final half hour.

For details about joining one of the online roundtables, and what goes on at one, are at: <a href="https://infra.apache.org/roundtable.html">The Infra Roundtable</a>.

### Infra at Community Over Code Glasgow

The Infra team was present in force at Community Over Code Glasgow, offering a full track of talks and discussions, and engaging in hallway conversations with all and sundry who had infrastructure-related questions or suggestions. The Infra track had 7 sessions, most of which attracted audiences of between 15-40 people. 

About fifty people took active and enthusiastic part in Games Night, confirming the role that event plays in creating a space for joy at the ASF.

A key takeaway for Infra from the conference was that community is our greatest strength, especially when it comes to sharing our resources. The build optimization workshop didn't just yield suggestions for build optimizations, but also made abundantly clear that all of the projects are expected to share our limited resources.

Another pleasant 'win' from the conference was the number of people who indicated they would like to get more involved in supporting or extending ASF infrastructure.

### Atlassian migration

Work continues on the migration of our in-house Jira and Confluence Wiki services to their cloud equivalents.

### Improvements to Boxer

Infra released a new version of Boxer in early September. With Boxer, first released in 2022, developers link their GitHub accounts with their ASF credentials, providing them with write access to GitHub.

The immediate upgrades in this release are an improved UI and the new opt-in public teams.

Longer term, Infra is looking into **multitenancy**, wherein each project gets their own organization within the ASF enterprise space. this would enable certain security features that have until now been root-only, as well as build quotas and better app isolation.

### Improvements to ASF mail delivery

Infra identified and resolved problems related to downstream handling of DKIM (domain keys identified mail) policies.

### Improvements to the ASF Mailing List Archive

The ASF mailing list archive, at lists.apache.org, has had a significant makeover.

_Enhanced security_: 2FA is now required for new sign-ins, using the ASF's official OIDC provider (`mfa.apache.org`). If you have not yet enrolled for 2FA, now is a good time to do so. Initiating a login will start the enrollment process if you have not yet set up 2FA for your account.

_Favorite lists_: Favorite any lists you like and you can see a compiled activity summary for just those lists, as if they were a single project..

_UI fixes/changes_:

  - `ctrl+c` now properly copies text instead of opening up the compose dialog.
  - middle mouse button works as intended again, no longer causes a 404 message.
  - The site now has dark and light modes, defaulting to your desktop or browser's display settings.
  - You can switch between the traditional list view and a new forum style view, where +1s count as upvotes on topics, for a more familiar feel for those who may not have the same love for mailing lists as some of us.
  - A new streaming API provides results for huge lists much faster, by streaming the results as you flip through the pages. No more waiting for a minute or three for a list with 25,000 monthly emails to load.
  - Feeds are back! Use your favorite atom feed app to subscribe to list updates.

### More MFA at the ASF

Multi-factor authentication (MFA) is a more secure way of logging in, and the infrastructure, security, and tooling teams are working hard to switch over any service that handles sensitive information to require MFA.

As we upgrade a service to use MFA, you'll notice that its login screen will change. Many services that today rely on a username and password prompt in your browser (or shell), as well as those using our `oauth.apache.org` login platform, will start using our new authentication platform at `mfa.apache.org`.

Currently, MFA is enabled for:

  - <a href="https://releases.apache.org/" target="_blank">Apache Trusted Releases (ATR)</a>
  - <a href="https://lists.apache.org/" target="_blank">Mailing list archives</a>
  - <a href="https://dash.security.apache.org/" target="_blank">Security reports dashboard</a>
  - <a href="https://webmod.apache.org/" target="_blank">WebMod</a>

Services that will be enabling MFA in the near future include, but are not limited to:

- <a href="https://agenda.apache.org/" target="_target">Board agenda tool (BAT)</a>
- Contingent Approval Platform (currently in beta at `https://cap-test.apache.org/`)
- <a href="https://gitbox.apache.org/boxer/" target="_blank">Boxer</a>
- <a href="https://selfserve.apache.org/" target="_blank">ASF Selfserve Platform</a>

While this is a much more secure method of authentication, the added steps can feel a bit confusing if you're not used to this type of login. We have a <a href="https://s.apache.org/mfa-user-guide" target="_blank">user guide available</a>.

Your first encounter with MFA usually happens the first time you log into a service that uses OIDC. That login kicks off the setup flow and guides you through enabling MFA on your account. You can also go directly to mfa.apache.org, which walks you through the same setup steps.

If you use a TOTP app such as Google Authenticator, the process will feel familiar: scan a QR code, then enter the six-digit code it generates to confirm everything is set up correctly. You'll also be given backup codes in case you lose access to the device you used to set up 2FA.

If you prefer WebAuthn (a passkey, YubiKey, or similar hardware key), you can use that instead. You're also welcome to enroll multiple 2FA methods if you'd like more than one option
available.

If you have questions or issues about using MFA at the ASF, contact us via email at `security@infra.apache.org`, or by filing a Jira ticket with Infrastructure.

### Infra 101

From November 2026, GitHub is disabling the `pull_request_target` trigger for ASF repositories. Projects still using it should migrate to the safer replacement described on the <a href="https://infra.apache.org/github-actions-policy.html" target="_blank">GitHub Actions Policy page</a>.

