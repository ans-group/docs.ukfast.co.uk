# Understanding Results

The results screen contains two sections: `Latency vs Virtual Users`,
`Failed Requests vs Virtual Users`.

# Latency vs Virtual Users

Latency vs Virtual Users is used to show the relationship
between the amount of virtual users visiting the site or application, against
the latency of the request. `Latency` refers to the round trip time of when the
request is sent, to when the content is returned back. The TTFB (Time To First Byte)
is a metric used by search engines to calculate how high to put you up on their
results pages, so having a low latency is good *but* it is **not** the be all
and end all.

This document isn't intended to go over SEO in depth or be up to date with current
SEO practice, however it's pretty well understood that a low latency will rank you
well, but that must also be consistent. Search providers usually slow down their
crawling if they detect they're having a detrimental affect on a site. It can be
inferred from that action that they understand they've hit your capacity and are
toning things back. This is a bad thing for you if you want to rank high, since
only sites with high capacity can rank highly on important keywords.

The main thing to take from this is that a low latency is good, but consistency
in latency should take priority first. Low latency tends to require hardware
upgrades and performance fixes for the application, whereas consistency requires
a thorough review of all the systems, that is why search engines will rank that
high. Don't neglect the TTFB however, since that is directly connected to capacity
and search engines such as goole make it very clear they expect quick responses.
You can review specific user experience issues with
[Google PageSpeed](https://developers.google.com/speed/pagespeed/insights/), which
will provide you with useful information in a few different areas.

# Failed Requests vs Virtual Users

Failed Requests vs Virtual Users is the most simple out of the two to understand.
If you have failed requests, something has gone wrong somewhere and you've hit
your current capacity maximum, something will need fixing before that can increase.
If for example you had only a couple of failed requests and this correlated with a
large increase of users, then it's likely to be a configuration issue, rather
than an application performance issue or constrained resources. Servers tend to
take the approach of "pools" to interact with services. When you make a request to
the web-server, you're hitting a pool of workers. When that web-server makes a
request to PHP, it's usually to a pool of workers. When that PHP request needs
to run a query, it will be connecting to a pool of MySQL connections. Those pools
usually need tweaking to make sure they can cope with a sudden increase in requests.
In IT this is referred to as bursts. Being ready for bursts is important and should
be something you test for. Make sure you run some tests which fluctuate virtual
user counts quickly to forcefully test these things.


```eval_rst
  .. title:: Understanding Load Testing Results
  .. meta::
    :title: Understanding Load Testing Results | UKFast Documentation
    :description: What do the results mean in the load testing results screen
    :keywords: load, test, testing, loadtest, load-test, results, graph
```
