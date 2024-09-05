Title: GitHub Actions and Secrets
license: https://www.apache.org/licenses/LICENSE-2.0

**Notice**: December 27, 2020: We only allow Actions that are official "Made by GitHub" or local to the Apache org on GitHub, to address a potential security vulnerability. This  is an incident-related policy change. We are researching the situation, and the policy may evolve based on what we learn.

**GitHub <a href="https://help.github.com/en/actions/getting-started-with-github-actions/about-github-actions" target="_blank">Actions</a>** help you automate your software development workflows in the same place you store code and collaborate on pull requests and issues. You can write individual tasks, called actions, and combine them to create a custom workflow. Workflows are custom automated processes that you can set up in your repository to build, test, package, release, or deploy any code project on GitHub.

***A note on testing***: Some projects would like to use GitHub Actions for complex processes, such as automating their tests of software builds. 

The _time_ runners are in use (measured in minutes) is unlimited for public repositories so how long a test takes isn't the issue. The issue is tying up limited 'runners' (nodes) while those minutes are running. Apache has a limited number of runners for over 1200 repositories, so the concern would be how many runners the test requires, which are then unavailable to other projects for the duration of the test.

The ASF maxes out its runner allocation quite often, so a project needs to plan carefully to make best use of them for everyone's sake. For example, it would be important not to trigger a full release test with a pull request that is correcting a typo on one page in one module.

**Evolving knowledge**

-  If you are considering using GitHub Actions with buildsy, please subscribe to the `builds@ a.o` mailing list, where there is a continuing discussion on this topic and others related to continuous integration development.

- The community is curating a <a href="https://cwiki.apache.org/confluence/display/BUILDS/GitHub+Actions+status" target="_blank">Wiki page</a> about the current state of using GitHub Actions for ASF projects.

- See <a href="https://cwiki.apache.org/confluence/display/INFRA/Github+Actions+to+DockerHub" target="_blank">Apache Airflow's experience</a> with Actions.

**GitHub <a href="https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets" target="_blank">Secrets</a>** are encrypted environment variables that you create in a repository or organization. The secrets you create are available to use in GitHub Actions workflows.

A **GitHub <a href="https://docs.github.com/en/developers/apps/about-apps#personal-access-tokens" target="_blank">Token</a>** is a string of characters that functions similarly to an OAuth token in that you can specify its permissions via scopes. A personal access token is also similar to a password, but you can have many of them and you can revoke access to each one at any time. As an example, you can enable a personal access token to write to your repositories. If then you run a cURL command or write a script that creates an issue in your repository, you would pass the personal access token to authenticate. You can store the personal access token as an environment variable to avoid typing it every time you use it.

See <a href="https://cwiki.apache.org/confluence/display/INFRA/Github+Secrets+and+Tokens" target="_blank">GitHub secrets and tokens</a>.

### Examples

#### GitHub Secrets

<a href="https://arrow.apache.org/" target="_blank">Apache Arrow</a> has GitHub Secrets added to their Arrow GitHub repos with the name 'DOCKERHUB_USER' and token 'DOCKERHUB_TOKEN' created as the user account on DockerHub (those account details are in LP).
Additionally, in DockerHub, an 'arrow-dev' repository was created and the DockerHub 'jenkins' team (containing  the DockerHub 'DOCKERHUB_USER' user) was given admin access.

#### GitHub Actions

Using Apache Arrow again as an example, the tokens above can be called using this code:

```
run: |
docker login -u ${{ secrets.DOCKERHUB_USER }} \
-p ${{ secrets.DOCKERHUB_TOKEN }}
docker-compose push ...
```

#### Using an argument to extend the validity of a token for Develocity

If you use the `setup-gradle` Action, it creates a short-lived Develocity token, which expires by default after two hours. If your build takes longer than two hours to run, the token becomes invalid and the build fails.

To extend the validity of the token, adjust the `develocity-token-expiry` action parameter:

```
 develocity-token-expiry:
    description: The Develocity short-lived access tokens expiry in hours. Default is 2 hours.
    required: false
```

Further information is at these pages: 

  - <a href="https://github.com/gradle/actions/blob/main/docs/setup-gradle.md#managing-develocity-access-keys" target="_blank">Managing Develocity access keys</a>
  - <a href="https://docs.gradle.com/develocity/gradle-plugin/current/#short_lived_access_tokens" target="_blank">Short-lived access tokens</a>
