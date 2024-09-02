Title: Working with .asf.yaml
license: https://www.apache.org/licenses/LICENSE-2.0

`.asf.yaml` is a branch-specific <a href="https://en.wikipedia.org/wiki/YAML" target="_blank">YAML</a> configuration file that a project may create (using a text editor of your choice) and put in the root of a Git repository to control features such as

  - notification schemes
  - website staging
  - GitHub settings
  - Pelican builds

It operates on a per-branch basis, meaning you can have different settings for different branches, and only those with an active `.asf.yaml` file will kick off a feature. Metadata settings (repo settings, features, labels) are not branch-dependent and should exist in the main (default) branch.

Full documentation and examples for using `.asf.yaml` are currently in the <a href="https://github.com/apache/infrastructure-asfyaml/blob/main/README.md" target="_blank">README file</a> of the GitHub repository for `.asf.yaml`.
