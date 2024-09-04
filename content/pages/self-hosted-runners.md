Title: Self-hosted runners
license: https://www.apache.org/licenses/LICENSE-2.0

In GitHub, the runner is the application that runs a job from a GitHub Actions workflow. The runner can run on the hosted machine pools or on self-hosted environments.

A project may want to use a self-hosted runner which, according to GitHub, offers

> more control of hardware, operating system, and software tools than GitHub-hosted runners provide. With self-hosted runners, you can choose to create a custom hardware configuration with more processing power or memory to run larger jobs, install software available on your local network, and choose an operating system not offered by GitHub-hosted runners. Self-hosted runners can be physical, virtual, container, on-premises, or in a cloud.

Read the GitHub <a href="https://help.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners#self-hosted-runner-security-with-public-repositories" target="_blank">documentation</a> about self-hosted runners if you are evaluating this option.

Apache permits projects to use self-hosted runners, but does **not recommend** them because of significant security issues they introduce.

If your project, after careful consideration, wants to use a self-hosted runner, open an Infra Jira ticket to ask Infra to do the required configuration work to enable your project's runner.
