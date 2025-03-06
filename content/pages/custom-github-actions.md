Title: Custom GitHub Actions
license: https://www.apache.org/licenses/LICENSE-2.0

The GitHub community, including several ASF projects, has created an extensive catalog of **custom GitHub Actions** (GHAs) to streamline and automate varioous stages in their development, build and release processes. Not all of the available custom GHAs are reliable, and some may include harmful code. The ASF has created an **AllowList** of useful and reliable custom GHAs, and projects can with confidence incorporate any custom GHA they find on the list into their own processes.

The marketplace for custom GHAs is at <a href="https://github.com/marketplace" target="_blank">github.com/marketplace</a>. When you find a custom GHA you want to use, chcek the AllowList to see if it appears there. If it does not, you can submit it for approval.

## Checking the AllowList
The ASF AllowList is at <a href="https://github.com/apache/infrastructure-actions/blob/main/approved_patterns.yml" target="_blank">github.com/apache/infrastructure-actions/blob/main/approved_patterns.yml</a>. 

## Submitting a custom GHA for approval
Here are the steps for submitting a custom GHA for ASF approval and inclusion in the AllowList:

  - Create a branch of <a href="https://github.com/apache/infrastructure-actions" target="_blank">github.com/apache/infrastructure-actions</a>
  - In the branch, create a subdirectory for your proposed GHA (at the top level, select 'add file' and provide `/NameOfAction`)
  - In the subdirectory, add all the required files for your proposed GHA. Make sure to add a README file that says what the Action does, and any particular configurations or considerations a user would find helpful.
  - Modify your GHA's `actions.yml` file: 

A valid change looks like this:

```
actions/checkout:
  v3:
    expires_at: 2025-02-04          # Should expire in 4 weeks because v4 exists
    keep: true                      # but is marked as permanent reference
  v4:
    expires_at: 2100-01-01
  932lkj3457890gsdasfasdf1237894343ds987af:
    expires_at: 2100-01-01
```

The actions are composed of tags and hashes which may be used in the workflow.
  
  - Create a pull request to merge the branch you created into the trunk of the repository.


Infra will review each proposed Action for usefulness to the community and make an estimate of its difficulty of maintenance. Infra may raise questions in pull request comments.

Once everything seems in order, Infra will approve the pull request and add the new Action to the AllowList.
