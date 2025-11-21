title: DMARC filtering on lists that munge messages
date: '2025-11-21T17:12:45+00:00'
permalink: dmarc_filtering_on_lists_that
layout: post

<p>In the battle against spam, it is increasingly common for senders to
attach a DKIM signature to their emails, and instruct recipients to
validate those. This presents a challenge for mailinglists, which often
do some form of message munging, whether it be adding Subject header prefixes,
a Reply-To header, appending message trailers, or removing mime components.</p>

<p>When the sender has set a 'reject policy' on their domain, we now replace
the sender with `John Doe via somelist <somelist@lists.apache.org>`, so that
the sender domain will be apache.org and the original senders' policy does
not come into play.</p>

<p>This replaces an ASF-specific filter that could be configured for ASF lists
since 2014. This previous filter would replace the sender with something like
`John Doe <john@doe.com.INVALID>`. This approach broke deliverability of some
emails when large providers such as GMail and Outlook made their rules around
duplicate `Reply-To` and `Cc` headers more strict, introducing the need to
build this into ezmlm itself rather than in a separate filter.</p>
