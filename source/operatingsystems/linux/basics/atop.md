# Monitoring performance with atop

A handy utility to monitor performance on a server is `atop`. Generally speaking this is a more detailed and interactive alternative to the `top` utility.

## Installation

You will need to install atop through the `yum` utility. You can use the below command to install atop.

```bash
  yum install atop
```

You may receive an error if the enabled repositories do not contain the atop package. This is explained in detail in the repository guide.

You will need to ensure that the service is started and that is set to start on boot. If the service is not started then there will be no historic logging available. To do this you can use the below commands which will start the service and also set it to start on boot.

```bash
  service atop start
```

```bash
  chkconfig atop on
```

## Basic live activity monitoring

To use the atop utility you will need to enter `atop` while connected to the server over SSH. You will then be presented with a screen that contains information on all system resources such as CPU usage, memory usage and disk activity.

By default this will auto refresh the information every 10 seconds. You can manually refresh using the `t` command. By default the process list is ordered by CPU usage. You can change the ordering to use a variety of different values. For example, you can type `m` which will order the process list by memory.

There atop utility is very versatile and allows for a large variety of different monitoring such as grouping processes together using `p` or viewing the command that is running using `c`. An exhaustive list of options can be found by looking at the man page for the atop package.

## Basic historic monitoring

The atop utility also allows historic server monitoring. To do this you will need to use the below command.

```bash
  atop -r
```

This will look the same as the live monitoring but will start from the start of the current log, which is generally midnight of the current day. To step ahead in the log you will need to type `t` which will take you one step ahead in the configured logging period. To take a step backwards, you will need to type `T`. You can also specify a specific time by typing `b` followed by the desired time.


```eval_rst
  .. title:: Monitoring performance with atop | UKFast Documentation
  .. meta::
     :title: Monitoring performance with atop | UKFast Documentation
     :description:  A guide on how to monitor server performance with atop 
     :keywords: ukfast, server, atop, linux, performance, virtual, vm, activity, historic, monitoring
