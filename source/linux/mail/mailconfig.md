# Basics of mail

Mail is complicated and requires lots of setup to get right. Getting it wrong can mean lots of pain in the future. The aim of this guide is to provide you an overview of how to set up your mail server the right way.

## Requirements

A mail server requires you to setup DNS records for other mail servers to interact with it and to verify your mail server should be sending mail for your domain, otherwise anyone could send mail on your behalf.

It requires the following types of records:

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
| MX        | Points mailservers to the correct A record which receives mail              | ukfast.co.uk -> mail.ukfast.co.uk  |
+-----------+-----------------------------------------------------------------------------+------------------------------------+
| rDNS      | Points an IP to a corresponding A record                                    | 37.220.91.195 -> mail.ukfast.co.uk |
+-----------+-----------------------------------------------------------------------------+------------------------------------+
| SPF (TXT) | Tells mailservers which IP addresses they should expect mail to arrive from | v=spf1 mx a ~all                   |
+-----------+-----------------------------------------------------------------------------+------------------------------------+

```

In the above examples you would be able to send an email to example@ukfast.co.uk because the MX records is setup for ukfast.co.uk. It points to the A record mail.ukfast.co.uk which points to the IP 37.220.91.195. The IP 37.220.91.195 has a reverse DNS of mail.ukfast.co.uk which some mail servers will check as part of their spam checks. On top of this most mail servers will do SPF checks, the example "v=spf1 mx a ~all" specifies that any IP which the A or MX record of ukfast.co.uk is allowed to send mail - Please note we have not set an A record for ukfast.co.uk but mail.ukfast.co.uk in the examples, therefore the "a" option is redundent here.

From a mail client you would use the A record you have set up to connect, so in this example you would connect to mail.ukfast.co.uk

If you wanted to use an external service to send mail also, you would need to add the IP range of that mail service, usually they will provide a single DNS records or IP range for you to include. It is recommended that you consult their documentation for this purpose as it will be specialised for their service.

You will also need to setup a hostname for the server which matches the reverse DNS. In our example this would be mail.ukfast.co.uk. You can learn how to change your hostname [here](../misc/hostname.html).
 
## Misc Issues
### Blacklists

If you think you may be blacklisted, you can confirm this by checking on a blacklist service checker. One example with a range of blacklists is [MultiRBL](http://multirbl.valli.org/). It's quite common to be shown as being blacklisted on some blacklists, for example rbldns.ru has most IP's blacklisted by default. Some will also not work.

Unfortunately as a provider UKFast is not able to get you removed from blacklists. Luckily most blacklists are easy to get removed from, just follow the links from the blacklist page and follow the steps. Some blacklists will ask you to pay money to "expedite" the process of removal. Unfortunately we cannot advise whether this would be the best cause of action in individual circumstances, however if you feel you have resolved whatever issue caused you to be blacklisted in the first place then it may be worthwhile if you send to mailservers which use those blacklists since some will take up to a month to expire.

Please note that most blacklists use DNS and have a TTL. This is the number of seconds that resolvers will cache the result of the blacklist lookup. Therefore if a blacklist has a very high TTL, it may mean that some mail servers will continue to reject mail for a while after even after the blacklist is removed.

### Microsoft/Hotmail/Office365

Microsoft mail servers are a little different to other providers. Their blacklists are not public so you cannot check if you are blacklisted and you must always get an IP address (or range) whitelisted if you want the mail to end up in the correct mailbox, if it is not it will always be sent to spam. This is described as a "greylist".

In terms of preparing for getting whitelisted by Microsoft, you must follow the steps previously in this documentation page. The two important factors are setting up SPF records and having a hostname on the server resolve to what the rDNS is for the IP sending the mail from that server.

The first step is to sign up to the JMRP and SNDS services which are provided by Microsoft for email postmasters:

- [SNDS](https://postmaster.live.com/snds/index.aspx)
- [JMRP](https://postmaster.live.com/snds/JMRP.aspx)

You should also submit an outlook.com sender information form [here](https://support.live.com/eform.aspx?productKey=edfsmsbl3&ct=eformts&wa=wsignin1.0&scrx=1).

Once you have completed those steps you will need to email microsoft to greylist your IP (or range) at delist@messaging.microsoft.com. Office365 also has a delist page [here](https://sender.office.com/).

The process can take up to a week, however it usually is done in under 24 hours.
