# What to do if your emails get blacklisted

If you think your eamils are blacklisted, you can confirm this by checking on a blacklist service checker. One example with a range of blacklists is [MultiRBL](http://multirbl.valli.org/). Another (less comprehensive) blacklist check can be found at [MXtoolbox](https://mxtoolbox.com/). It's quite common to be shown as being blacklisted on some blacklists, for example rbldns.ru has most IPs blacklisted by default. Some blacklists may also return "Failed" - that's common and may simply mean the request timed out, rather than you being on the blacklist.

## What to do if you find yourself on a blacklist

The first step is to try and find why you've been blacklisted. Many blacklists allow you to look up the reason they've added you to their lists, which can be a good first step in your investigation. You can also check your mail logs to look for spam or suspicious activity. Please see our guidance on checking logs for [Postfix](/operatingsystems/linux/mail/postfix.html) and [Exim](/operatingsystems/linux/mail/exim.html) mail servers. Services like [Mail-tester](https://www.mail-tester.com/) can also help you find and resolve issues.

Once you've found the issue and fixed it, you can start getting delisted. As a hosting provider UKFast is not able to get you removed from blacklists, however most blacklists provide an easy delisting process you can use. In most cases you should follow the steps provided on the blacklist provider's website. A few will expire automatically once the cause is resolved. Some blacklists will ask you to pay money to "expedite" the process of removal - UKFast cannot advise whether this is the best course of action for your individual circumstances. That said, if you feel you have resolved whatever issue caused you to be blacklisted in the first place, it may be worthwhile if you send to mail servers which use those blacklists, since some listings will take up to a month to expire.

Please note that most blacklists use DNS and have a TTL (Time To Live). This is the number of seconds that resolvers will cache the result of the blacklist lookup. Therefore if a blacklist has a very high TTL, it may mean that some mail servers will continue to reject mail for a while even after you are removed from the blacklist.

## Microsoft, Google and Yahoo

These providers maintain their own private blacklists, and you cannot check if you are on these lists. However, if you have delivery issues to domains like hotmail, outlook, gmail or yahoo, there's a good chance you may be on one of these private blacklists. The best way to check is to look in your mail logs for 550 response codes and error messages from these providers. Again, please see our guides on checking logs for [Postfix](/operatingsystems/linux/mail/postfix.html) and [Exim](/operatingsystems/linux/mail/exim.html) mail servers.

### Microsoft/Hotmail/Office365

Microsoft mail servers are a little different to other providers. Their blacklists are not public so you cannot check if you are blacklisted. You must always get an IP address (or range) whitelisted if you want the mail to end up in the correct mailbox. If you have problems with your mail ending up in spam, or not appearing at all, this is likely the reason.

If you have this issue, read our guide in the [basics of mail](/operatingsystems/linux/mail/mailconfig.html#sending-to-microsoft-hotmail-office365) section, which should help you address this. 

### Google / Gmail

Google provides [some useful guidance on mail](https://support.google.com/mail/answer/81126?hl=en) which is also worth reading.


```eval_rst
  .. meta::
     :title: Email blacklisting | UKFast Documentation
     :description: How to check if you are blacklisted and steps to take
     :keywords: ukfast, mail, basics, config, dns, spf, mx, blacklist, hotmail, live, google, gmail
