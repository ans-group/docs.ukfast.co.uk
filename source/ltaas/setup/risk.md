# Understanding Risk

Load Testing, as described by Wikipedia "is the process of putting demand on
a system and measuring its response". It's likely you've decided to load test
because you already understand there's risk with putting demand on systems and
have seen that the response may have been slow or non-existent. Most people experience
an outage and then decide to perform a load-test to stop future outages. This is
an excellent decision, however you must not forget, you will be replicating these
same conditions in a more controlled environment and as such, **the potential
to cause an outage is quite high**.

If management are reluctant to cause an outage, it's important to convey why
it's important to perform testing:

- Testing is controlled
  - Can be cancelled
  - Can be modified
  - At a time suited for you
- Testing catches issues before they become a problem for your business
- It's an industry standard for anything which must be available at all times (Including
once a year events, such as black friday)

It's the equivalent of a fire drill, which all businesses must perform regularly.
It may cause a little disruption to your day, but you're allowed to choose the terms
of when.

If there's still reluctance, you should consider a proposal of a testing environment.
An additional environment may be more expensive, but it does allow you to test
code and infrastructure decisions outside of your live environment. If you've already
considered a UAT/Staging/Dev environment, then this may be a good argument for it.


```eval_rst
  .. title:: Understand The Risks With Load Testing | UKFast Documentation
  .. meta::
    :title: Understand The Risks With Load Testing | UKFast Documentation
    :description: Load testing involves risk. This document goes over that in detail.
    :keywords: load, test, testing, loadtest, load-test, risk
```
