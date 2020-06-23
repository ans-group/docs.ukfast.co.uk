# Basics of mail

Mail is complicated and requires careful attention during set up to get right. Getting it wrong can mean lots of pain in the future. The aim of this guide is to provide you an overview of how to set up your mail server the right way.

## Requirements

A mail server requires you to setup DNS records for other mail servers to interact with, to verify that your mail server is sending mail legitimately from your domain (otherwise anyone could send mail on your "behalf" by spoofing your email addresses).

A mail server requires the following types of records:

- A
- MX
- rDNS
- SPF (TXT)

## DNS Explained

```eval_rst
+-----------+-----------------------------------------------------------------------------+------------------------------------+
| Type      | Description                                                                 | Example                            |
+===========+=============================================================================+====================================+
| A         | Points a domain to an IP                                                    | mail.ukfast.co.uk -> 37.220.91.195 |
+-----------+-----------------------------------------------------------------------------+------------------------------------+
| MX        | Points mail servers to the correct A record which receives mail              | ukfast.co.uk -> mail.ukfast.co.uk |
+-----------+-----------------------------------------------------------------------------+------------------------------------+
| rDNS      | Points an IP to a corresponding A record                                    | 37.220.91.195 -> mail.ukfast.co.uk |
+-----------+-----------------------------------------------------------------------------+------------------------------------+
| SPF (TXT) | Tells mail servers which IP addresses they should expect mail to arrive from | v=spf1 mx a ~all                  |
+-----------+-----------------------------------------------------------------------------+------------------------------------+

```

In the above examples you would be able to send an email to example@ukfast.co.uk because the MX records is setup for ukfast.co.uk. It points to the A record `mail.ukfast.co.uk` which points to the IP `37.220.91.195`. The IP `37.220.91.195` has a reverse DNS of `mail.ukfast.co.uk` which some mail servers will check as part of their spam checks. On top of this most mail servers will do SPF checks, the example "v=spf1 mx a ~all" specifies that any IP with the A or MX record of ukfast.co.uk is allowed to send mail - Please note we have not set an A record for ukfast.co.uk but `mail.ukfast.co.uk` in the examples, therefore the "a" option is redundant here.

From a mail client you would use the A record you have set up to connect, so in this example you would connect to mail.ukfast.co.uk

If you wanted to use an external service provider to send mail also, you would need to add the IP range of that mail service, usually they will provide a single DNS record or IP range for you to include. It is recommended that you consult your service provider's documentation for this purpose, as it will differ by provider.

You will also need to setup a hostname for the server which matches the reverse DNS. In our example this would be `mail.ukfast.co.uk`. You can learn how to change your hostname [here](../misc/hostname.html).

### Sending mail to Microsoft/Hotmail/Office365

Microsoft mail servers are a little different to other providers. They operate their own private blocklists and greylists, so if you want to send mail to these domains, you should make sure to follow the steps here in order to make sure your IP is allowed by Microsoft. If not, you may find your mail sent to spam. This is described as a "greylist".

In terms of preparing for getting your IP allowed by Microsoft, you must follow the steps outlined above. The two important factors are setting up SPF records and having a hostname on the server resolve to the rDNS for the IP sending mail from that server.

Once done, the first step is to sign up to the JMRP and SNDS services which are provided by Microsoft for email postmasters:

- [SNDS](https://postmaster.live.com/snds/index.aspx)
- [JMRP](https://postmaster.live.com/snds/JMRP.aspx)

You should also submit an outlook.com [sender information form](https://support.live.com/eform.aspx?productKey=edfsmsbl3&ct=eformts&wa=wsignin1.0&scrx=1).

Once you have completed those steps you will need to email Microsoft at **delist@messaging.microsoft.com** requesting they to delist your IP (or range). Office365 also has a delist page [here](https://sender.office.com/).

The process can take up to a week, however it is usually completed in under 24 hours.


```eval_rst

  .. title:: Email | Basics of mail on Linux

  .. meta::
     :description: A guide to the basics of mail on Linux
     :keywords: ukfast, mail, basics, config, dns, spf, mx, blocklist, hotmail, live, microsoft
