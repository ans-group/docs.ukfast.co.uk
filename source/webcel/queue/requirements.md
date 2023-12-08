# Implementation requirements

In order to be able to use the Webcelerator queue system, you need to have a live Webcelerator as part of your solution.

You must be using **SSL Offloading or Secure Origin Pull** to be able to make use of the queue system, assuming your site uses HTTPS.

Further to this, your domain should be pointed at the Webcelerator and working in testing before the queue is activated.

## Exceptions to queuing

Naturally, there will be some requests that you will not want to enter the queue, such as:

* Requests from GoogleBot and other key spiders
* Requests to your API endpoints
* Requests from your payment processors to inform of completed transactions
* Requests to administrative areas of your site
* Requests from certain IP addresses

You will need to detail to UKFast what should be excluded from being queued, to ensure that your site continues to work normally once this is implemented.

As such, we generally recommend making a test purchase through your site using the "Skip Queue" feature of the admin panel to ensure all is working as expected.

## Issues with the queue system

As this is still a beta addition to the Webcelerator, you may encounter other issues. Where possible, we will attempt to resolve these, however it may be the case that the queue needs to be disabled if it is causing more problems than help in your situation.


```eval_rst
.. meta::
   :title: Webcelerator queue system requirements | ANS Documentation
   :description: Detailed requirements to get started with the Webcelerator queue system.
   :keywords: ukfast, webcel, webcelerator, queue, webcelerate queue requirements
```

