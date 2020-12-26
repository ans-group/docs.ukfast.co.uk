# Plesk SafeDNS Extension

## Extension Interface


### Welcome Page

The welcome page will guide you through checking the settings explained in the “Setup” Page.


### Manage DNS Zones

In The Manage DNS Zones tab, you can control which domains the extension will synchronise to SafeDNS.

```eval_rst
================================ ============================================================================================================================
Column                           Info
================================ ============================================================================================================================
Enabled                                      Domains must be enabled here to work with the extension.

Sync Now                         | This will push an enabled zone to SafeDNS.
                                 |
                                 | If a record already exists, it will be updated to match plesk.
                                 |
                                 | If a record exists on SafeDNS but has been removed, (or didn't exist) on Plesk, it will be deleted

Last Synchronise                 When a domain is Synchronised, this is updated with the date & time

Automatic Sync (on zone change)  When Plesk's internal DNS is updated, the domains that have this enabled, will be automatically Synchronised with SafeDNS.

Delete Zone (From SafeDNS)       Deletes the zone from SafeDNS. Only if the zone is enabled.
================================ ============================================================================================================================
```

### Tasks & Config


In Tasks & Config , you have the following options:

```eval_rst
================ ====================================================================================================================
Button           Function
================ ====================================================================================================================
Set API Key      Open a form for API Key to be inputted. When a Key is saved, It will be tested to confirm it is valid.

Sync All         This will synchronise all enabled zones to SafeDNS.

Sync Domain      | Open a form with a Dropdown to select a Domain.
                 | On Submit,  push only the selected zone to SafeDNS.

Delete All       This will immediately delete all enabled zones from SafeDNS.

Delete Domain    | Open a form with a Dropdown to select a Domain.
                 | On Submit,  delete only the selected zone from SafeDNS.

Clear All Tasks  | Clears out the extension’s task queue.
                 | If a task has errored and you cannot run another one, click this button.
================ ====================================================================================================================
```

```eval_rst
  .. title:: Interface Guide - Plesk SafeDNS Extension
  .. meta::
     :title: Interface Guide - Plesk SafeDNS Extension | UKFast Documentation
     :description: Interface Guide for UKFast SafeDNS Plesk Extension
     :keywords: ukfast, plesk, extension, safedns, dns, domains, integration, interface
```
