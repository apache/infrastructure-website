Title: Approving Jira Account Requests
license: https://www.apache.org/licenses/LICENSE-2.0

The ASF uses Jira as one of its main systems for receiving and tracking bug reports and feature requests for our many projects. We require people who are not already part of the ASF community to have an ASF Jira account in order to submit Jira tickets. To get that account, a person who does not already have an ASF identity has to apply in one of two ways:

1. Using this form on our self-serve system: <a href="https://selfserve.apache.org/jira-account.html" target="_blank">https://selfserve.apache.org/jira-account.html</a>, which asks them to identify the project to which they want to submit tickets. ASF members associated with that project then review the application to make sure the information is correct and the reason for the account is valid.
2. Some projects ask requesters to send their request to the `users@` list for review, giving the same information in their email that they would provide on the self-serve form.

**Note**: a person does not need a Jira account to view existing issue reports and enhancement requests.

## Why we use this pattern
The ASF put the requirement to have an ASF Jira account in place for two reasons:

1. Our system was being swamped with a flood of bot-created spammy tickets. Requiring an account in order to submit a ticket has largely resolved this issue.
2. We currently host our Jira system on an ASF server. We intend to move it to a hosted cloud solution. However, that solution has a hard maximum to the number of accounts it can support, and we are trying to reduce the number of ASF Jira accounts to below that maximum.

## Approving account requests
In general, if the request seems valid--all fields are filled in with appropriate information, the reason for the account does not seem suspicious (or machine-written), and the reason given is not about a security vulnerability (see above)--approve it. Do not worry too much about increasing the number of ASF Jira accounts, as Infra is working on addressing that issue in other ways than rejecting valid requests.

If you are in doubt, consult with colleagues on your PMC.
