# cPanel/WHM FAQs and top tips

While addressing every possible issue with cPanel/WHM is outside the scope of this page, we do see some frequently asked questions!

For more full and in depth guides, we recommend checking out the official user guides which are maintained by cPanel:

<https://documentation.cpanel.net/>

## I can't connect to FTP?

Please do refer to our [guide on setting up FTP](..ftp/passive_mode.html) and to the [official cPanel guide](https://documentation.cpanel.net/display/CKB/How+to+Enable+FTP+Passive+Mode). If you still have trouble after following those steps, please do [submit a support request](https://my.ukfast.co.uk/pss/add.php) and be sure to include any changes made so far, and any error logs from your FTP client.

## My mailboxes aren't showing properly/Mail isn't sending

WHM includes a mailbox repair script which is a good first step. You can run this from WHM under the section Email >> Repair Mailbox Permissions. Alternatively it's possible to call this script as a root user via SSH:
``#
/scripts/mailperm
``

If that doesn't resolve the issue please do refer to our [mail guides](../mail) for further steps to ensure your mail is set up optimally.

## cPanel statistics seem to be wrong

cPanel stats are not live, so they only update a few times a day. This is to reduce the load on your server and leave more resources free for hosting your applications. If they are clearly wrong and do not update after a day, you can try to manually update them with the following scripts:
``#
/scripts/fixwebalizer
/scripts/runlogsnow
``

## I'm trying to update WHM but it keeps failing

For a few reasons, running the update process from the WHM web GUI can fail. It's possible to run the update via SSH:
``#
/scripts/upcp --force
``
The --force flag causes WHM to update all components regardless of any previous updates. This will make sure all WHM components are updated.

```eval_rst
  .. meta::
     :title: cPanel/WHM FAQs | UKFast Documentation
     :description: cPanel/WHM control panel FAQs and tips on Linux servers
     :keywords: ukfast, cpanel, whm, control, panel, tutorial, cloud, server, guide, virtual
