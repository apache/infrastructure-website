Title: PyPubSub at the Apache Software Foundation

# PyPubSub at the Apache Software Foundation

The ASF employs a plain-text publisher/subscriber service called PyPubSub at 
`pubsub.apache.org:2069`, which lists most events that happens at the 
foundation.

Currently, the following events are streamed:

* Subversion commits
* Git commits and pushes
* Emails to publicly archived lists
* Pull Requests and Issues from GitHub
* Staging and publishing notifications sent via our [.asf.yaml](https://s.apache.org/asfyaml) offering.

Events are delivered as JSON objects in a 
[chunked response stream](https://en.wikipedia.org/wiki/Chunked_transfer_encoding), 
with each new chunk being either an event payload or a keep-alive ping. 


## How to subscribe
Subscribers can pick one or multiple topics to subscribe to, with more specific 
subscriptions getting fewer, but tailored event payloads. Subscriptions can be 
constructed in the form of: `http://pubsub.apache.org:2069/topics/go/here`, where 
topics to subscribe to are separated by forward slashes. 
Only events that match all of the subscribers topics will be returned.

Some examples:

* To subscribe to all git commits; `http://pubsub.apache.org:2069/git/commit`
* To subscribe to all netbeans.apache.org emails: `http://pubsub.apache.org:2069/email/netbeans.apache.org`
* To subscribe to PRs opened against beam-foo.git: `http://pubsub.apache.org:2069/github/beam-foo.git/pr`
* To subscribe to all commits, both subversion and git: `http://pubsub.apache.org:2069/commit`


## Event payload examples

Pings are simple objects like this:
~~~
{"stillalive": 1583973410.9620552}
~~~

An example of a real event payload, in this case a git commit, could be:

~~~
{
	"commit": {
		"body": "[maven-release-plugin] prepare for next development iteration\n",
		"committer": "sblackmon <sblackmon@apache.org>",
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
		"email": "sblackmon@apache.org",
		"authored": "Wed Mar 11 19:25:06 2020 -0500",
		"ref_names": ""
	},
	"pubsub_topics": ["git", "streams", "commit"],
	"pubsub_path": "/git/streams/commit"
}
~~~

Payloads vary depending on what they represent, so keep in mind to check both what sub-objects 
are present in the payload, as well as the `pubsub_path` variable, which will show the 
full payload event path and explain which type is being sent.

## Try it yourself
To try it out and take a look at the event stream, just use cURL in your terminal:
~~~
curl http://pubsub.apache.org:2069/git/commit
~~~

## Want to know more? Have questions?
To learn more, or just get some questions answered, please contact us at users@infra.apache.org, 
and we'll try our best to help you out.
