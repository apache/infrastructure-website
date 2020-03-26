Title: Self-hosted runners

In GitHub, the runner is the application that runs a job from a GitHub Actions workflow. The runner can run on the hosted machine pools or on self-hosted environments.

A project may want to use a self-hosted runner which, according to GitHub, "offer[s} more control of hardware, operating system, and software tools than GitHub-hosted runners provide. With self-hosted runners, you can choose to create a custom hardware configuration with more processing power or memory to run larger jobs, install software available on your local network, and choose an operating system not offered by GitHub-hosted runners. Self-hosted runners can be physical, virtual, container, on-premises, or in a cloud."

Apache permits projects to use self-hosted runners, but does **not** recommend them because of significant security issues they introduce.
