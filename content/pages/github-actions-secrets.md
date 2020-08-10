Title: GitHub Actions and Secrets

**GitHub <a href="https://help.github.com/en/actions/getting-started-with-github-actions/about-github-actions" target="_blank">Actions</a>** help you automate your software development workflows in the same place you store code and collaborate on pull requests and issues. You can write individual tasks, called actions, and combine them to create a custom workflow. Workflows are custom automated processes that you can set up in your repository to build, test, package, release, or deploy any code project on GitHub.

**GitHub <a href="https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets" target="_blank">Secrets</a>** are encrypted environment variables that you create in a repository or organization. The secrets you create are available to use in GitHub Actions workflows.

A **GitHub <a href="https://docs.github.com/en/developers/apps/about-apps#personal-access-tokens" target="_blank">Token</a>** is a string of characters that functions similarly to an OAuth token in that you can specify its permissions via scopes. A personal access token is also similar to a password, but you can have many of them and you can revoke access to each one at any time. As an example, you can enable a personal access token to write to your repositories. If then you run a cURL command or write a script that creates an issue in your repository, you would pass the personal access token to authenticate. You can store the personal access token as an environment variable to avoid typing it every time you use it.

See <a href="https://cwiki.apache.org/confluence/display/INFRA/Github+Secrets+and+Tokens" target="_blank">GitHub secrets and tokens</a>.

### Examples ###

#### GitHub Secrets ####

<a href="https://arrow.apache.org/" target="_blank">Apache Arrow</a> has GitHub Secrets added to their Arrow GitHub repos with the name 'DOCKERHUB_USER' and token 'DOCKERHUB_TOKEN' created as the user account on DockerHub (those account details are in LP).
Additionally, in DockerHub, an 'arrow-dev' repository was created and the DockerHub 'jenkins' team (containing  the DockerHub 'DOCKERHUB_USER' user) was given admin access.

#### GitHub Actions ####

Using Apache Arrow again as an example, the tokens above can be called using this code:

```
run: |
docker login -u ${{ secrets.DOCKERHUB_USER }} \
-p ${{ secrets.DOCKERHUB_TOKEN }}
docker-compose push ...
```
