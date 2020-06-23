# Updates
```eval_rst
.. seealso::
   Please note that updates can be customised using your Enterprise Launch Questionnaire.
```
## Windows Updates

Any File or SQL Clusters in the solution will have the following Group Policy configuration:
- Auto Download and notify for install.

These updates will be then coordinated with yourselves to fail-over services and install/reboot (if required). 

All other single role Windows Servers will have the following Group Policy Configuration:
- Auto download and schedule the install.

These will be applied in one of the following 2 groups with times and days stipulated by UKFast to take in account redundancy of roles across VMs. 

### Example Updates Schedule
```eval_rst
+------------------------+--------------------------+
| Group 1 – Friday @ 8am | Group 2 – Saturday @ 9am |
+========================+==========================+
| DC-01                  | DC-02                    |
+------------------------+--------------------------+
| WEB-01                 | WEB-02                   |
+------------------------+--------------------------+
| SQL-01                 | SQL-02                   |
+------------------------+--------------------------+
```

## Linux Updates

By default single role Linux Servers will have the following updates configured:

- No, I do not wish for this server to automatically apply updates.

```eval_rst
  .. title:: UKFast Enterprise Updates Default Configuration | UKFast Documentation
  .. meta::
      :title: UKFast Enterprise Updates Default Configuration | UKFast Documentation
      :description: Default Configuration for UKFast Enterprise Updates
      :keywords: ukfast, hosting, updates, server, virtual, enterprise

