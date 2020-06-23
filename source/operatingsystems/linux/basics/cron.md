# Setting up cron jobs

Cron is a time-based job scheduler found in most Linux based operating systems, it is used to execute jobs at regular intervals.

The easiest way to add Cronjobs to your server is to use the `crontab` utility. The manual page for the tool can tell you all you need to know however you will likely
be using `-u {username}` to designate a user and `-e` to edit the jobs.

For example `crontab -u {username} -e` opens {username}'s crontab for editing. Using the user 'bob' as a demonstration, we could use the following command:

```bash
  crontab -u bob -e
```

A typical cronjob is comprised of two parts:
* The schedule
* The action

## The Schedule

The schedule denotes the times that the job should be exectuted, unfortunately this is a little more complicated than just typing 'every tuesday' but it doesn't take too
long to get used to. The schedule takes five arguments; minute/hour/day of month/month/day of week, for example

`1 0 * * *`

tells `cron` to run the job at one minute past midnight every day of every month no matter which day of the week it is.

`1 0 * * 1`

Is very similar to our first example however this tells `cron` to run the job at one minute past midnight on Monday.

### The Action

The second part of the cronjob denotes the command to be executed at the given time. Using our examples from above

`1 0 * * *     /path/to/script.sh`

Would run the script at one minute past midnight.

There are [several](http://crontab.guru/) [online](http://www.openjs.com/scripts/jslibrary/demos/crontab.php) [utilites](http://www.cronmaker.com/) that will generate the cronjob for you and most control panels will also have a user friendly interface for the system.

```eval_rst
  .. title:: Setting cron jobs on Linux | UKFast Documentation
  .. meta::
     :title: Setting cron jobs on Linux | UKFast Documentation
     :description:  A guide on how to set up cron jobs on Linux
     :keywords: ukfast, linux, server, cron, jobs, schedule, virtual, vm, cronjob
