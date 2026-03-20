title: Trivy Security Incident 
date: '2026-03-20' 
permalink: trivysecurity layout: post

### A security incident
Trivy, Agua Security's open-source vulnerability scanner, appears to have experienced a security incident March 19, 2026, based on the details available here: <a href="https://www.stepsecurity.io/blog/trivy-compromised-a-second-time---malicious-v0-69-4-release" target="_blank">stepsecurity.io/blog/trivy-compromised-a-second-time---malicious-v0-69-4-release</a>

ASF Infrastructure and ASF Security have provided the following summary based on what we believe to be true:

  - Trivy version 0.69.4 contained malicious code that could potentially steal credentials present in GitHub Secrets.
  - The trivy-action GitHub Action and trivy-setup were also compromised.

### Impact on ASF projects
A small number of ASF projects include the trivy GitHub Action in their build workflows.

### Infra response
  - ASF Infra and ASF Security agreed to disable all previously allowed "verified creator" actions while the incident is being investigated
  - This may cause build failures, and require projects request newly-failed actions be added via the Infra GHA approval process: <a href="https://github.com/apache/infrastructure-actions?tab=readme-ov-file#adding-a-new-version-to-the-allow-list" target="_blank">github.com/apache/infrastructure-actions?tab=readme-ov-file#adding-a-new-version-to-the-allow-list</a>
  - Infra and the Security team are investigating if any secrets and Git repositories of ASF projects may have been compromised.

### For further information
If you are involved in an ASF project that is impacted by this situation, you can open a Jira ticket for Infra. You can also join the conversation in the #asfinfra channel in the the-asf space on Slack, or send an email to `users@infra.apache.org`.
