Title: News from Infra
license: https://www.apache.org/licenses/LICENSE-2.0

**April 3, 2026**: Infra has created a new email address, `security@infra.apache.org`, where people can report emerging security issues related to ASF infrastructure. You cannot subscribe to this list; someone from the Infra team will reply to the message if further information is needed.

**March 13, 2026**: The parallel PUT issue reported below (February 3) is **resolved** in Apache Maven 3.9.13.

**February 23, 2026**: The Apache instance of **Reviewboard** will cease operation on March 31, 2026. Details are in the <a href="https://infra.apache.org/blog/newsletter_02_26.html">February newsletter</a>.

**February 3, 2026**: Apache Maven 3.9.12 has a change that causes a problem in repository.apache.org (the Sonatype Nexus 2 Pro staging suite): if your build uses parallel PUT deployment, the build creates a separate staging repository for each of the requests instead of assembling everything in one repository.

The Maven team is working on a resolution to this issue. Until the fix is available, they suggest **disabling parallel PUTs**.

For details on disabling parallel PUTs, and what to do if you have already run into this problem in a build, see this article in the Infra blog: <a href="https://infra.apache.org/blog/parallelputissue.html">Parallel PUT problem in repository.apache.org with Apache Maven 3.9.12]</a>. 
