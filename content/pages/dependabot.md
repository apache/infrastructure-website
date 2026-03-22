Title: Dependabot for Dependency Management
license: https://www.apache.org/licenses/LICENSE-2.0

<a href="https://docs.github.com/en/code-security/dependabot" target="_blank">GitHub Dependabot</a> automatically opens pull requests to keep your project's dependencies up to date and free of known vulnerabilities. Dependabot works the same way for ASF repositories as it does for any other GitHub repository; there is nothing ASF-specific about its configuration.

**Note**: All repositories using GitHub Actions **must** have Dependabot (or <a href="https://docs.renovatebot.com/" target="_blank">Renovate</a>) enabled for the `github-actions` ecosystem. See the [GitHub Actions Policy](github-actions-policy.html) for details.

<h2 id="quickstart">Getting started<a class="headerlink" href="#quickstart" title="Permanent link">&para;</a></h2>

Follow the <a href="https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide" target="_blank">Dependabot Quickstart Guide</a> to enable Dependabot for your repository.

In short, create a `.github/dependabot.yml` file in your repository. The file must start with `version: 2` and contain an `updates` list with one entry per package ecosystem your project uses.

A minimal example:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
```

<h2 id="ecosystems">Identify your ecosystems<a class="headerlink" href="#ecosystems" title="Permanent link">&para;</a></h2>

Look at which dependency files exist in your repository and add a `package-ecosystem` entry for each one. Common ecosystems include:

| Ecosystem | Manifest files | `package-ecosystem` value |
|---|---|---|
| GitHub Actions | `.github/workflows/*.yml` | `github-actions` |
| Maven | `pom.xml` | `maven` |
| Gradle | `build.gradle`, `build.gradle.kts` | `gradle` |
| npm | `package.json` | `npm` |
| pip | `requirements.txt`, `setup.py`, `pyproject.toml` | `pip` |
| Go modules | `go.mod` | `gomod` |
| Cargo (Rust) | `Cargo.toml` | `cargo` |
| Bundler (Ruby) | `Gemfile` | `bundler` |
| Composer (PHP) | `composer.json` | `composer` |
| NuGet (.NET) | `*.csproj`, `*.fsproj` | `nuget` |
| Docker | `Dockerfile` | `docker` |
| Terraform | `*.tf` | `terraform` |

For the full list of supported ecosystems, see the <a href="https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#package-ecosystem" target="_blank">Dependabot configuration reference</a>.

Set the `directory` field to the location of the manifest file relative to the repository root (for example, `"/"` or `"/frontend"`). For GitHub Actions, use `"/"` (Dependabot knows to look in `.github/workflows`).

<h2 id="recommendations">Recommendations<a class="headerlink" href="#recommendations" title="Permanent link">&para;</a></h2>

<h3 id="weekly-schedule">Use weekly updates with grouped pull requests<a class="headerlink" href="#weekly-schedule" title="Permanent link">&para;</a></h3>

A weekly schedule avoids an overwhelming number of pull requests while still keeping dependencies reasonably current. If your project has many dependencies, use **groups** to combine related updates into a single pull request:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      all-dependencies:
        patterns:
          - "*"
```

You can also split groups by update type or dependency kind:

```yaml
    groups:
      minor-and-patch:
        update-types:
          - "minor"
          - "patch"
      major:
        update-types:
          - "major"
```

<h3 id="cooldown">Use a cooldown period<a class="headerlink" href="#cooldown" title="Permanent link">&para;</a></h3>

A **cooldown** delays Dependabot from proposing a new dependency version until it has been published for a minimum number of days. This gives the community time to discover issues with a release &mdash; including compromised packages &mdash; before your project adopts it. See <a href="https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns" target="_blank">Why you should use dependency cooldowns</a> for background on the security rationale.

A 4-day cooldown is a good default:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    cooldown:
      default-days: 4
```

**Note**: Cooldowns apply only to version updates, not to security updates, so critical fixes are never delayed.

<h2 id="full-example">Full example<a class="headerlink" href="#full-example" title="Permanent link">&para;</a></h2>

Below is a complete example for a project that uses GitHub Actions, Maven, and npm:

```yaml
version: 2
updates:
  # Keep GitHub Actions up to date
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    cooldown:
      default-days: 4
    groups:
      actions-dependencies:
        patterns:
          - "*"

  # Keep Maven dependencies up to date
  - package-ecosystem: "maven"
    directory: "/"
    schedule:
      interval: "weekly"
    cooldown:
      default-days: 4
    groups:
      maven-dependencies:
        patterns:
          - "*"

  # Keep npm dependencies up to date
  - package-ecosystem: "npm"
    directory: "/frontend"
    schedule:
      interval: "weekly"
    cooldown:
      default-days: 4
    groups:
      npm-dependencies:
        patterns:
          - "*"
```

<h2 id="further-reading">Further reading<a class="headerlink" href="#further-reading" title="Permanent link">&para;</a></h2>

  - <a href="https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates" target="_blank">Configuring Dependabot version updates</a>
  - <a href="https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file" target="_blank">Configuration options for the dependabot.yml file</a>
  - [GitHub Actions Policy](github-actions-policy.html) (Dependabot is **required** for the `github-actions` ecosystem)
