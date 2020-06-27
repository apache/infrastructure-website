Title: Subscribe to Apache Software Foundation infrastructure events

The ASF employs a plain-text publisher/subscriber service called **PyPubSub** at `pubsub.apache.org:2069`, which lists most events that happen within the Foundation's infrastructure.

Currently, the service streams the following events:

* Subversion commits
* Git commits and pushes
* Emails to publicly archived lists
* JIRA updates
* Pull Requests and Issues from GitHub
* Staging and publishing notifications sent via our [.asf.yaml](https://s.apache.org/asfyaml) offering.

Events are delivered as JSON objects in a <a href="https://en.wikipedia.org/wiki/Chunked_transfer_encoding" target="_blank">chunked response stream</a>, with each new chunk being either an event payload or a keep-alive ping. 

## How to subscribe
Subscribers can pick one or multiple topics to subscribe to, with more specific subscriptions getting fewer, but more specific, event payloads. Construct subscriptions in the form of: `http://pubsub.apache.org:2069/topics/go/here`, and separate the topics you want to subscribe to with forward slashes. 

The service returns events that match _all_ of the topics you are subscribed to.

Some examples:

* To subscribe to all git commits; `http://pubsub.apache.org:2069/git/commit`
* To subscribe to all git events (push+commit) for whimsy.git; `http://pubsub.apache.org:2069/git/whimsy`
* To subscribe to all `netbeans.apache.org` emails: `http://pubsub.apache.org:2069/email/netbeans.apache.org`
* To subscribe to PRs opened against `beam-foo.git`: `http://pubsub.apache.org:2069/github/beam-foo.git/pr`
* To subscribe to all commits, both Subversion and git: `http://pubsub.apache.org:2069/commit`
* To subscribe to all JIRA events for the HADOOP JIRA instance: `http://pubsub.apache.org:2069/jira/HADOOP`

## Event payload examples

Pings are simple objects like this:
~~~ json
{"stillalive": 1583973410.9620552}
~~~

An example of a real event payload, in this case a git commit, could be (emails redacted in this example):

~~~ json
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
To try it out and take a look at the event stream, use [cURL](https://en.wikipedia.org/wiki/CURL) in your terminal:
~~~ bash
curl http://pubsub.apache.org:2069/git/commit
~~~

<br/>

A secure version also exists on port 2070:
~~~ bash
curl https://pubsub.apache.org:2070/git/commit
~~~

## Using PyPubSub in programming
### Using PyPubSub with Python
You can listen for and react to payloads in Python using the [asfpy](https://pypi.org/project/asfpy/) pip package:
~~~ python
import asfpy.pubsub

def process_event(payload):
   print("Got an event from PyPubSub!")
   ...

def main():
    pubsub = asfpy.pubsub.Listener('http://pubsub.apache.org:2069/')
    pubsub.attach(process_event, raw=True)

~~~

### Using PyPubSub with node.js
This sample snippet lets you use `node.js` for listening for and processing pubsub events:
~~~ javascript
const http = require("http");
const https = require("https");

class PyPubSub {
    constructor(url) {
        this.url = url;
        this.getter = url.match(/^https/i) ? https : http;
    }

    attach(func) {
        this.getter.get(this.url, res => {
            res.setEncoding("utf8");
            res.on("data", data => {
                let payload = JSON.parse(data);
                func(payload);
              });
        });
    }
}


// Payload parser
function process(payload) {
    // ping-back?
    if (payload.stillalive) {
        console.log("Got a ping-back");
    // Actual payload? process it!
    } else {
        console.log("Got a payload from PyPubSub!");
        console.log(payload);
    }
}

const pps = new PyPubSub('http://pubsub.apache.org:2069/');
pps.attach(process);
~~~

## Want to know more? Have questions?
To learn more, or just get some questions answered, please contact us at `users@infra.apache.org`, and we'll try our best to help you out.

## Acknowledgements
PyPubSub is based on [SvnPubSub](https://paul.querna.org/articles/2010/10/22/evolution-of-apaches-websites/)
and [gitpubsub](https://www.apache.org/dev/gitpubsub.html). We wish to thank the Subversion project for building the precursor to this service.
