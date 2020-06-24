# Scanning configuration

The Virus Scanning Engine is configured to scan files when they are written to disk during real-time scanning. We disable continuous read scanning to prevent IO Saturation, which would result in performance degradation.

A weekly scan is scheduled to scan all disks apart from any exclusions which have been specified. If you wish to add, remove or modify exclusions on your anti-virus scan, please raise a support request via [MyUKFast](https://my.ukfast.co.uk) detailing your requirements.

Scanning of remote directories is disabled by default, however NFS mounts will be scanned and viewed as a local disk.

Scanning schedules can be customised to your requirements, or they can be managed by you directly. If you want to make any changes to how your schedules are managed, please raise a support request.

Default schedules can be seen [here](schedules).

```eval_rst
   .. title:: McAfee | Scanning Configuration
   .. meta::
      :title: McAfee | Scanning Configuration | UKFast Documentation
      :description: Detail on McAfee scanning configuration
```
