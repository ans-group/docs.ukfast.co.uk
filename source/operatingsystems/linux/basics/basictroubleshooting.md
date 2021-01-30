# Basic Troubleshooting

## How to raise a good ticket

When raising a ticket the most important aspect to keep in mind is to be informative and comprehensive whilst remaining concise.

Engineers need to know:

* A short description of the issue.
* Any error messages produced when encountering the issue
* When did the issue start? Has this happened before?

When raising tickets you may also select a priority for the issue. Whilst we understand that the issue is important to you, we politely ask that you refrain from marking all tickets as Critical. This should be reserved for instances where the server is offline or completely inoperable, your account manager will be able to further advise on this.

## Finding error messages

When issues occur on a Linux system a (sometimes but not exclusively) helpful message is printed to the application's error log. Commonly these are found in the location `/var/log/{application}/error.log`. For example `/var/log/nginx/error.log`. If you are using a control panel such as cPanel or Plesk then your logs may be in different locations.

Knowing the time that the issue occurred is important to reading logs as every entry will have a timestamp. Knowing the time of the issue means that you can locate the relevant information to the issue quickly.

## Checking system performance

The most common cause of server slow down is one or more processes consuming a large amount of the system resources. The easiest way to view the current usage of resources is to use the utility `top`. `top` allows you to view CPU utilisation, Memory usage, Disk activity, Tasks and Load Average. Many of these are quite self explanatory and percentages to show usage. Load Average is representative of the queue of instructions on the CPU, this should ideally remain below 1.

There are several variations on the `top` utility however those are not covered in this section.

```eval_rst
  .. title:: Basic troubleshooting for Linux
  .. meta::
     :title: Basic troubleshooting for Linux | UKFast Documentation
     :description:  A guide to troubleshooting basic issues for Linux
     :keywords: ukfast, linux, troubleshooting, system, server, virtual, vm, performance, errors, tickets, ticket
```
