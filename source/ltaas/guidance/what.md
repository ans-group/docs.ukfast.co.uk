# What to Test

You may already know what you want to test, but ensure you read over this guidance,
as it may help you pick out some additional useful areas to test on your site or
application.

You should sit down with your developers during this process and your developers
should have an open mind for the process. Often developers will write their code to
be functional only and performance is an after thought and this is perfectly
acceptable. This approach can cause performance issues however and you're load testing
to identify bottlenecks, that includes server configuration and most importantly
code performance. Server configuration is more often than not a low hanging fruit on
the fix list, but that is not to say you won't get significant performance boosts
when improving configuration. Some configuration is hard to identify as problematic
without the assistance of developers, since the problem is abstracted away by
code interacting with different systems.

An example of where there could be hidden configuration bottlenecks would be MySQL.
A site may run slow due to queries to the database taking a long time. At initial
glance a sysadmin may say a query is slow or needs better indexing, however the
developer has the best knowledge on those queries and should be able to rule out
that being an issue. It may run fine on the developers machine, but slow on the server.
At that point the developer is responsible for finding out the environment differences.
In that example, it could be that the developer has a small dataset compared to the
live server, in which case a test with more data could rule out the dataset size.

With logs in place, more often than not a sysadmin can identify most straight
forward configuration issues, so work with them also from the start, but have
your developer on hand to help resolve potential issues. You should consider
an APM (Application Performance Monitoring) service to aid your developer. Your
account manager will be able to give a known list of services that other clients
potentially use if you're not able to find one. An APM will give your developer
the quickest way to identify what takes too long in the code to execute. Most can
even detect MySQL queries and external API calls which may be slowing things down.

## Specific Target Recommendations

With the above in mind, we'd recommend you target pages which execute code that
interacts with other services, where possible. Some pages which require
authentication (eg. checkout page) are not possible to test without a custom user
journey written. If that's of interest please speak to your account manager 
regarding a custom user journey. The following pages are good to look for:

- Pages with complex MySQL queries
- Search pages
- Pages with external API calls (Twitter feeds, review feeds)
- Pages lacking cache

## User Journeys

Since load testing is intended to emulate real traffic, it's a good idea to know
how your users move around your site. First how they land on your site and where
they click and subsequently click after that to eventually arrive at their final
destination. This is called a user journey in the industry. You can work out
what your user journeys are by looking at logs and/or your analytics. Your
analytics should also give you an idea of real users as well, since getting that
out of access logs is a little trickier.

User journeys can be difficult to create with realistic timings, that's why we
can build those custom user journeys for you. Please speak to your account manager
about this if you're interested.


```eval_rst
  .. title:: What To Target With Load Testing | UKFast Documentation
  .. meta::
    :title: What To Target With Load Testing | UKFast Documentation
    :description: Advice regarding what to target to get the best results with load testing
    :keywords: load, test, testing, loadtest, load-test, target, what, user, journey, performance
```
