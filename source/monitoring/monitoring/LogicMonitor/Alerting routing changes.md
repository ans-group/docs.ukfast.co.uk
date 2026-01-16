# Changes to How Alerting routing Works in LogicMonitor Compared to the Current Monitoring in the Portal

When a device is onboarded into LogicMonitor, the alerting behaviour differs slightly from the existing system used in the portal. Below is a breakdown of how the process works and what to expect.

## Default Case Contact

When a new device—such as "WebServer-01" is deployed in VPC and subsequently onboarded into LogicMonitor, it is automatically assigned to the Default Case Contact.
This means that whoever is set as the Default Case Contact at the moment of onboarding will receive all alert notifications for that device.

## Updating the Default Case Contact

If the Default Case Contact is later updated in Glass, the change does not automatically apply to devices that have already been onboarded.
Existing devices retain the contact details they were initially assigned.

If you need the alert contact updated for previously onboarded devices, this requires raising a support ticket so the correct contacts can be manually applied.
Using Distribution Groups for Multiple Recipients

If your team requires multiple people to receive the “new ticket” alert emails, the best approach is to use a distribution group (shared mailbox or group email address).
You can then set this distribution group as the alert contact in LogicMonitor.

This ensures that alerts reach all relevant team members without needing to modify LogicMonitor each time personnel changes occur.