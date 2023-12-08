# Plesk FAQs and top tips

While addressing every possible issue with Plesk is outside the scope of this page, we do see some frequently asked questions!

For more full and in depth guides, we recommend checking out the official user guides which are maintained by Plesk:

* <https://docs.plesk.com/>
* <https://support.plesk.com/>

## Why do I keep getting emails about "green" "yellow" and "red" warnings from my Plesk server?

Those emails are from the Plesk Server Health Monitor, which is a built in service to provide basic monitoring of your server's health. It's generally a great idea to use this service, but the default values are often set too low and trigger a lot of false positives.

Plesk provide a full guide on how to set these values to something more suitable for your server [here](https://docs.plesk.com/en-US/12.5/administrator-guide/statistics-and-monitoring/server-health-monitor.68886/).

## The statistics on Server Health Monitor seem wrong, can I fix it?

Yes, you can reset the statistics by following [this guide](https://support.plesk.com/hc/en-us/articles/360011108979-No-data-is-shown-in-the-charts-of-Advanced-Monitoring).

## The statistics for traffic and disk space on a domain seem wrong, can I fix it?

Yes, you can recalculate the domain statistics using the following command:

```bash
plesk sbin statistics --calculate-one --domain-name=example.com
```

There is a [full guide here](https://docs.plesk.com/en-US/onyx/cli-linux/using-command-line-utilities/statistics-calculating-statistics.78387/).

## How do I check my users have strong passwords?

If you host a lot of accounts on your Plesk server, it's a good idea to ensure your users have strong passwords. Weak passwords are a choice attack vector for spammers who will use your server to send out spam and cause you headaches.

Newer versions of Plesk can enforce strong password use, [for full details see here](https://docs.plesk.com/en-US/12.5/administrator-guide/plesk-administration/securing-plesk/setting-up-the-minimum-password-strength.71081/).

However all versions will let your check your email users passwords manually to look for vulnerable accounts:

```bash
/usr/local/psa/admin/sbin/mail_auth_view
```

```eval_rst
  .. title:: Plesk FAQs
  .. meta::
     :title: Plesk FAQs | ANS Documentation
     :description: Plesk control panel FAQs and tips on Linux servers
     :keywords: ukfast, plesk, control, panel, tutorial, cloud, server, guide, virtual
```