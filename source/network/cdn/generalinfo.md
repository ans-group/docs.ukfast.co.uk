# Introduction to CDN

## What is CDN?

A Content Delivery Network (or CDN) is a network of highly-distributed servers that are specifically designed to deliver static content or streaming media. The servers are spread over a number of physical locations in order to bring the content as close as possible to the user requesting it.

## How does CDN work?

The CDN sits between the client and the origin server and caches content to reduce the number of requests to the origin server.  In doing so it lowers latency to the end user (speeding up page load time) and eases the amount of traffic sent to the origin server. This is achieved by making use of Anycast routing, where each of the servers share the same IP address so that a request for content is sent to one of many IP addresses. The IP address is announced through BGP (Border Gateway Protocol), so the client's request should hit the closest server to the client, based on the geographical location.

For example, an end user based in the USA streaming video from a server hosted in the UK could typically experience latency of 75ms or higher. However the same request for a video to a CDN server based in the USA can be as little as 10ms.
