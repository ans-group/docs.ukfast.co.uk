# Schedule a task with `at`

There are multiple ways to schedule a task on your server. This guide will explain how to create a one time task to run using the `at` command. An example of a use of this would be when you would like to schedule a reboot to take place at a certain time. To schedule a job you will need to type the `at` command. You can follow this with the desired time you want the task to execute at. You will then be prompted for the task that you wish to run at this time. Once you have finished, you will need to press `ctrl + d` together. An example is shown below which schedules a reboot to take place at 1pm.

```console
at 13:00
warning: commands will be executed using /bin/sh
at> reboot
at> <EOT>
```

You can then view the list of at jobs by using the `atq` command. An example output of this is shown below.

```console
atq
2       Fri Aug 12 13:00:00 2016 a root
1       Thu Aug 11 21:30:00 2016 a root
```

To cancel a scheduled at job you can use the `atrm` command followed by the ID of the scheduled job that you wish to cancel. The ID can be taken from the output of `atq`. An example to delete a scheduled task with the ID 2 is below.

```bash
atrm 2
```

```eval_rst
  .. title:: Using the AT command in Linux
  .. meta::
     :title: Using the AT command in Linux | UKFast Documentation
     :description: Information and guidance on using the AT command in Linux
     :keywords: ukfast, linux, at, command, time, console, atq, job, schedule, server, cloud
```
