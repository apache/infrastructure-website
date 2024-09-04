Title: Open-access SVN
license: https://www.apache.org/licenses/LICENSE-2.0

This page collects arguments for and against running our Subversion service in a manner that permits committers the technical
ability (but not the social privilege) to make commits against any part of the `https://svn.apache.org/repos/asf` repository.

<ul>
<li><a href="#upsides">Upsides</a></li>
<li><a href="#downsides">Downsides</a></li>
<li><a href="#participating-projects">Participating Projects</a></li>
<li><a href="#alternate-proposal-1">Alternate proposal 1</a></li>
<li><a href="#alternative-proposal-2-slow-pedal-this-idea-and-focus-on-social-aspects-bimargulies">Alternative proposal 2</a></li>
</ul>

<h2 id="upsides">Upsides<a class="headerlink" href="#upsides" title="Permanent link">&para;</a></h2>

  - Simplifies administration of SVN ACL.
  - Allows more cross-collaboration into participating projects.
  - Changes the culture from a set of technically-closed communities to a set of mostly-open ones.

<h2 id="downsides">Downsides<a class="headerlink" href="#downsides" title="Permanent link">&para;</a></h2>

  - PMCs no longer control who has commit privileges (technically untrue. They are simply being asked to use blacklists instead of whitelists).
  - Increases leverage for abusive behavior, though this is mitigated by the relative ease by which bad commits can be reverted via reverse-merging, or, for more invasive changes, plastering over them by deleting the entire tree and copying the last known good revision to HEAD. This only starts getting complicated when good commits start being mingled with bad ones.
  - One hacked account can damage all of `/repos/asf` (disregard for basic tenet of security: provide access only to those who require it and only to the bare minimum of what they need).
  - May lead to confusion about the distinction between technical and social privileges.
  - No single usable accounting of who on a PMC has commit permissions. Impact on non SVN-related resources for PMC and foundation (example: `https://home.apache.org/committer-index.html`). 
  - Increases workload on PMCs and volunteer committers.
  - Creates a precedent where the foundation imposes its will on PMCs for no clearly defined or overwhelming reason (also technically untrue as allowances will be made for grandfathering projects).

<h2 id="participating-projects">Participating Projects<a class="headerlink" href="#participating-projects" title="Permanent link">&para;</a></h2>

  - Lucy
  - Onami
  - <a href="https://svn.apache.org/r1427834">Subversion</a>
  - Bloodhound
  - Hadoop Developer Tools
  - Helix
  - Kalumet
  - Infra buildbot config</li>

<h2 id="alternate-proposal-1">Alternate proposal 1<a class="headerlink" href="#alternate-proposal-1" title="Permanent link">&para;</a></h2>

Each project that is using svn shall have a top-level 'sandbox' directory where any committer may make branches of trunk (or of other branches). Members/Committers will be encouraged to participate in any ASF project via this sandbox area until such time as they are offered direct commit access to the rest of the project's svn tree.

Each project will additionally have a `sandbox-commits@project.apache.org` svn commit mailing list that anyone may join.

It would be wonderful from an Infra standpoint, if this alternate proposal gains traction, that we could "standardize" and "templatize" our authz rules. The authorization file is already preprocessed by a script before it becomes live, so this is something that could still lead to some simplification of our rulesets.

<h2 id="alternative-proposal-2-slow-pedal-this-idea-and-focus-on-social-aspects-bimargulies">Alternative Proposal 2: slow-pedal this and focus on social aspects<a class="headerlink" href="#alternative-proposal-2-slow-pedal-this-idea-and-focus-on-social-aspects-bimargulies" title="Permanent link">&para;</a></h2>

The  proposal from bimargulies here rests on two foundations:

  - Streamline administration
  - Push projects towards a more open view of participation

 Changing the authz scheme can give projects a push. However, we have many other possible means of encouraging projects to adopt a more open approach. `SCM authz` is a tool that the foundation provides to help projects manage themselves. The theory is that many projects could benefit from a shift in attitude toward authz and even commit rights. However, 'many' is not all. I've been talking to someone who might bring a project to the incubator. This project builds software that has very strict assurance requirements. If they were to come, they would probably feel the need to manage a tight ACL. In discussions, it seems to me that existing projects that are far along the sequence towards, 'a stable product that evolves very cautiously' are less likely to adopt an open ACL.

In any case, the argument about the ACL versus culture cuts both ways. Right now, with no change to the LDAP-based ACL, any project could adopt the following policy:

```
Commit Access is granted upon request and acceptance of an ICLA. 
If you request and receive commit access, you are expected to read, understand, and comply with the project's policies. 
If you abuse this, we will remove your access.
```

(Of course, this could be weakened to mention Foundation membership or committer status on other projects.) 

In any case, the eager would-be contributor with an existing ICLA would merely need to wait for the PMC chair to type a command in response to a request. Is this really much of a barrier? I submit that the cultural posture that accompanies the tight ACL on many projects today is a much stronger barrier.

Thus, my alternative proposal has two aspects. First, to focus attention via the Community Development PMC on exploring more open project cultures. Second, to look for ways to ease administration on the assumption that (some) projects will still maintain ACLs.

I offer a few thoughts on that:

  1. As per the 'Alternative Proposal' above, design a standard authz template for a project that wishes to maintain an ACL. It's not necessary for all projects to <em>have</em> a sandbox, I think. If the authz calls out a sandbox pathname with `@committers=rw`, then the project decides whether to have that sandbox by deciding whether to run `svn mkdir` on the pathname. If they never create it, it's not there. If they do create it, it has access.
  2. The incubator seems to me to be an authz accident waiting to happen. Maybe the solution here is simply to adopt the 'all committers' model for the incubator, or maybe we could have an LDAP group after all, so that fat-fingered IPMC chairs are not making many tiny edits.

In other words, could we significantly reduce the amount of template editing that goes on without clear-cutting all the existing ACLs?
