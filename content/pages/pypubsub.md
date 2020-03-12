Title: PyPubSub at the Apache Software Foundation

The ASF employs a plain-text publisher/subscriber service called PyPubSub at `pubsub.apache.org:2069`, which lists most events that happen within the Foundation's infrastructure.

Currently, the service streams the following events:

* Subversion commits
* Git commits and pushes
* Emails to publicly archived lists
* Pull Requests and Issues from GitHub
* Staging and publishing notifications sent via our <a href="https://s.apache.org/asfyaml" target="_blank">.asf.yaml</a> offering.

Events are delivered as JSON objects in a <a href="https://en.wikipedia.org/wiki/Chunked_transfer_encoding" target="_blank">chunked response stream</a>), with each new chunk being either an event payload or a keep-alive ping. 

## How to subscribe
Subscribers can pick one or multiple topics to subscribe to, with more specific subscriptions getting fewer, but tailored event payloads. Construct subscriptions in the form of: `http://pubsub.apache.org:2069/topics/go/here`, and separate the topics you want to subscribfe to with forward slashes. 

The service returns events that match _all_ of the topics you list will be returned.

Some examples:

* To subscribe to all git commits; `http://pubsub.apache.org:2069/git/commit`
* To subscribe to all `netbeans.apache.org` emails: `http://pubsub.apache.org:2069/email/netbeans.apache.org`
* To subscribe to PRs opened against `beam-foo.git`: `http://pubsub.apache.org:2069/github/beam-foo.git/pr`
* To subscribe to all commits, both Subversion and git: `http://pubsub.apache.org:2069/commit`

## Event payload examples

Pings are simple objects like this:
~~~
{"stillalive": 1583973410.9620552}
~~~

An example of a real event payload, in this case a git commit, could be (emails redacted in this example):

~~~
{
	"commit": {
		"body": "[maven-release-plugin] prepare for next development iteration\n",
		"committer": "sblackmon <s...@apache.org>",
		"hash": "8e6f956",
		"log": "[maven-release-plugin] prepare for next development iteration",
		"repository": "git",
		"sha": "8e6f956c2eda06ca9debf21634cedcecc96293ff",
		"author": "sblackmon",
		"files": ["pom.xml", "streams-cli/pom.xml", "streams-components/pom.xml"],
		"server": "gitbox",
		"project": "streams",
		"autopublish": false,
		"date": "Wed Mar 11 19:25:06 2020 -0500",
		"commited": "Wed Mar 11 19:25:06 2020 -0500",
		"subject": "[maven-release-plugin] prepare for next development iteration",
		"ref": "refs/heads/master",
		"email": "s...@apache.org",
		"authored": "Wed Mar 11 19:25:06 2020 -0500",
		"ref_names": ""
	},
	"pubsub_topics": ["git", "streams", "commit"],
	"pubsub_path": "/git/streams/commit"
}
~~~

Payloads vary depending on what they represent, so check both what sub-objects are present in the payload and the `pubsub_path` variable, which will show the full payload event path and explain which type is being sent.

## Try it yourself
To try it out and take a look at the event stream, just use <a href="https://en.wikipedia.org/wiki/CURL" targe"_blank">cURL</a> in your terminal:
~~~
curl http://pubsub.apache.org:2069/git/commit
~~~

## Want to know more? Have questions?
To learn more, or just get some questions answered, please contact us at `users@infra.apache.org`, and we'll try our best to help you out.

## Acknowledgements
PyPubSub is based on <a href="https://paul.querna.org/articles/2010/10/22/evolution-of-apaches-websites/" target="_blank">SvnPubSub</a>) 
and <a href="https://www.apache.org/dev/gitpubsub.html" target="_blank">gitPubSub</a>. We wish to thank the Subversion project for building the precursor to this service.
