# `logrotate`

`logrotate` is a service that allows log files to be rotated and compressed depending on when they meet a specified criteria. It's an important tool to use to ensure that growing log files do not fill a filesystem.

`logrotate` is called via a scheduled task, normally located within `/etc/cron.daily`.

The configuration files can be found within `/etc/logrotate.d` and you'll generally find each service has its own configuration file to handle its specific log files.

Common options you may see used in a configuration file include:

* `compress` - this indicates the log files should be compressed once rotated. `gzip` is used by default.

* `daily` / `weekly` / `monthly` / `yearly` - this specifies that the log file should be rotated every day, week, or month.

* `ifempty` / `notifempty` - these specify whether to either rotate the log file even if it's empty, or to not rotate the log file if it's empty, respectively.

* `missingok` / `notmissingok` - these options will either not generate an error, or will generate an error if the log file does not exist. `notmissingok` is the default.

* `rotate` - this is supplied with a number argument, which specifies how many times the log files are rotated before being removed.

* `size` - this specifies the size a log file has to reach before it is rotated.

Most services will generate a standard `logrotate` file in `/etc/logrotate.d` when installed, however you may wish to implement custom ones such as the following examples:

Magento log files:

```console
/var/www/vhosts/example.com/var/log/*log {
    rotate 7
    daily
    compress
    missingok
    notifempty
}
```

```eval_rst
  .. title:: Using logrotate in Linux
  .. meta::
     :title: Using logrotate in Linux | ANS Documentation
     :description: How to use logrotate to manage rotating log files in Linux
     :keywords: ukfast, log, rotate, linux, size, magent, cron, schedule, cloud, virtual
```
