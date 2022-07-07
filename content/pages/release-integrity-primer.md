title: Handling of Release Artifact Integrity Errors at the ASF


This page acts as a primer for resolving [release distribution policy](https://infra.apache.org/release-distribution) errors discovered by our [Download Integrity Checker](https://github.com/apache/infrastructure-download-integrity-checker).
Each reported error has an accompanying error code (`CHKxx`), allowing you to resolve issues by using the matrix below:


| Error Code | Error Description | How to Address the Issue |
|------------|-------------------|------------|
| `CHK01`    | Key used for signing artifact is missing from the [`KEYS`](https://infra.apache.org/release-signing.html#key-basics) file | Make sure the key that signed the release was expected. <br/>Update your [`KEYS`](https://infra.apache.org/release-signing.html#key-basics) file to include the key |
| `CHK02`    | Weak or missing checksum file(s) | <ul><li>If the release artifact has a valid signature: generate a [conforming checksum](https://infra.apache.org/release-signing.html#sha-checksum) and add it, you can leave the old hash file</li><li>Otherwise: treat as if `CHK05`</li></ul> |
| `CHK03`    | No [`KEYS`](https://infra.apache.org/release-signing.html#key-basics) file was found in the project's distribution directory | Make sure the project directory has at least one KEYS file containing all signing keys used for distribution. Projects may have more than one [`KEYS`](https://infra.apache.org/release-signing.html#key-basics) file (per-component, per-version etc) but they *MUST* be called `KEYS` and exist within the project's dist directory. |
| `CHK04`    | The signature used for signing expired before signing the file | <ul><li>It’s possible the expiry has been changed, check and make sure the [`KEYS`](https://infra.apache.org/release-signing.html#key-basics) file is updated</li><li>If key has really expired treat as if it has no signature (`CHK05`) |
| `CHK05`    | No (or invalid) signature found for the release artifact | Check: <ul><li>Is there a signature file for this artifact?:<ul><li>If the signature is valid but has the wrong filename or extension, just rename it to the appropriate .asc filename</li><li>If the signature is invalid: See [handling invalid or missing signatures](#invalid-sig).</li></ul></li><li>If there is no signature file at all: See [handling invalid or missing signatures](#invalid-sig). |
| `CHK06`    | Checksum mismatch | Try to spot what the problem was (why are you generating the wrong checksum?): <ul><li>If the file has a valid signature (no `CHK04` or `CHK05` errors for this file): generate a [conforming checksum](https://infra.apache.org/release-signing.html#sha-checksum) and add it, remove the broken one</li><li>Otherwise: treat as if `CHK05`</li></ul> |

## <a id="invalid-sig">Handling invalid or missing signatures</a>
In case of an invalid or missing signature for a release artifact, the project MAY choose one of the following actions:
 - Remove the artifact(s)
 - Re-assert that the artifact is valid, sign and upload the correct .asc signature file
 
 Both decisions MUST be accompanied by informing the ASF Infrastructure and Security Team 
 at `private@infra.apache.org` and `security@apache.org` with clear evidence that the action 
 has been discussed and agreed upon (a link to a lists.apache.org thread will suffice)

If you have any further questions about the error reports, this page, or our release distribution polices in general, 
feel free to reach out to us at: users@infra.apache.org
