# Updates

To make sure your solution is patched and updated to the latest version, UKFast will configure the following update policy:

```eval_rst
.. seealso::
   Please note that updates can be customised using your online Pre-Launch Questionnaire.
```
## Windows Updates

By default single role Windows Servers will have the following Group Policy Configuration:

- Automatically download and install all updates
- This will be scheduled for Friday at 8am.

You are also able to configure Windows Updates with the following options:

- Automatically download all updates, but allow me to manually install the update
- Notify me when there is an update before downloading, and allow me to manually install the update
- Never check for updates
- Install Preferences (Day and Time)
```eval_rst
.. seealso::
   Please keep in mind that updates may reboot your server automatically, so you should pick an appropriate time to install the updates.
```
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

If you wish, you are able to update this to:

- Yes, I want this server to automatically apply updates.

```eval_rst
  .. title:: UKFast Updates Default Configuration
  .. meta::
      :title: UKFast Updates Default Configuration | UKFast Documentation
      :description: Default Configuration for UKFast Updates
      :keywords: ukfast, hosting, updates, server, virtual
