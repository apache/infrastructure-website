Title: Subscribe to Apache Software Foundation infrastructure events

license: https://www.apache.org/licenses/LICENSE-2.0

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
To subscribe to multiple topic batches in an OR'ed way, you may use a comma to separate your batches of topics.

Some examples:

* To subscribe to all svn commits; `http://pubsub.apache.org:2069/svn/commit`
* To subscribe to all git commits; `http://pubsub.apache.org:2069/git/commit`
* To subscribe to all git events (push+commit) for whimsy.git; `http://pubsub.apache.org:2069/git/whimsy`
* To subscribe to all `netbeans.apache.org` emails: `http://pubsub.apache.org:2069/email/netbeans.apache.org`
* To subscribe to PRs opened against `beam-foo.git`: `http://pubsub.apache.org:2069/github/beam-foo.git/pr`
* To subscribe to all commits, both Subversion and git: `http://pubsub.apache.org:2069/commit`
* To subscribe to all JIRA events for the HADOOP JIRA instance: `http://pubsub.apache.org:2069/jira/HADOOP`
* To subscribe to *both* JIRA and email streams for tomcat in one go: `http://pubsub.apache.org:2069/jira/TOMCAT,email/tomcat.apache.org`

Public SVN repo topics consist of 'svn', the first one or two path segments after the /repos/ in the URL, and 'commit'.
For example, changes to the repository `https://dist.apache.org/repos/dist/release/` have the topics `svn/dist/release/commit`.
A commit that involves changes to both `dist/release` and `dist/dev` has the topics `svn/dist/commit`.
Note that `svn/dist/release/commit` will not match, because the topics in the response do not include `release`.

Private SVN repos topics are constructed in the same way, but have an additional 'private' topic.
For example `https://pubsub.apache.org:2070/private/svn/private/committers/commit` returns commits for
`https://svn.apache.org/repos/private/committers/board/`


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
		"committed": "Wed Mar 11 19:25:06 2020 -0500",
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

A secure version also exists on port 2070, for use with authenticated event streams:
~~~ bash
curl https://pubsub.apache.org:2070/git/commit
~~~
Please note that due to limitations in our TLS terminator, payloads larger than 64kb are split into 64kb chunks on
port 2070. If you are using port 2070, you should ensure that the data you receive is terminated with a newline (\n),
or continue fetching data till you hit a chunk terminated with a newline.

N.B. the following curl switches may be added:

* -N - non-buffered output; used when piping into another command (e.g. tail)
* -sS - silent mode (-s) but still shows error messages (-S)


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
            let body = '';
            res.on("data", data => {
	        // Be mindful of proxies that split pubsub chunks into smaller ones,
		// only load the JSON blob once we hit a newline (\n)
                body += data;
                if (data.endsWith("\n")) {
                    let payload = JSON.parse(body);
                    body = '';
                    func(payload);
                }
              });
        });
    }
}


// Test
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

### Using PyPubSub with Ruby
This sample lets you connect to our pubsub service via Ruby:

~~~ruby
require 'net/http'
require 'json'
require 'thread'

pubsub_URL = 'https://pubsub.apache.org:2070/'

def do_stuff_with(event)
  print("Got a pubsub event!:\n")
  print(event)
  print("\n")
end

def listen(url)
  ps_thread = Thread.new do
    begin
      uri = URI.parse(url)
      Net::HTTP.start(uri.host, uri.port, :use_ssl => url.match(/^https:/) ? true : false) do |http|
        request = Net::HTTP::Get.new uri.request_uri
        http.request request do |response|
          body = ''
          response.read_body do |chunk|
            body += chunk
	    # All chunks are terminated with \n. Since 2070 can split events into 64kb sub-chunks
	    # we wait till we have gotten a newline, before trying to parse the JSON.
            if chunk.end_with? "\n"
              event = JSON.parse(body.chomp)
              body = ''
              if event['stillalive']  # pingback
                print("ping? PONG!\n")
              else
                do_stuff_with(event)
              end
            end
          end
        end
      end
    rescue Errno::ECONNREFUSED => e
      restartable = true
      STDERR.puts e
      sleep 3
    rescue Exception => e
      STDERR.puts e
      STDERR.puts e.backtrace
    end
  end
  return ps_thread
end

begin
  ps_thread = listen(pubsub_URL)
  print("Pubsub thread started, waiting for results...\n")
  while ps_thread.alive?
    sleep 10
  end
end
~~~

## Want to know more? Have questions?
To learn more, or just get some questions answered, please contact us at `users@infra.apache.org`, and we'll try our best to help you out.

## Acknowledgements
PyPubSub is based on [SvnPubSub](https://paul.querna.org/articles/2010/10/22/evolution-of-apaches-websites/)
and [gitpubsub](/gitpubsub.html). We wish to thank the Subversion project for building the precursor to this service.
