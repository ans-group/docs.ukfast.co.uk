# Blacklists

If you think you may be blacklisted, you can confirm this by checking on a blacklist service checker. One example with a range of blacklists is [MultiRBL](http://multirbl.valli.org/). Another less comprehensive blacklist check can be found at [MXtoolbox](https://mxtoolbox.com/). It's quite common to be shown as being blacklisted on some blacklists, for example rbldns.ru has most IPs blacklisted by default. Some blacklists on these checks may also return "Failed", that's normal and it means the request timed out, not that you're on the blacklist.

## What to do if you find yourself on a blacklist

The first step is to see if you can find why you've been blacklisted. Many blacklists allow you to look up the reason they've added you to their lists, which can be a good first step in your investigation. You can also check your mail logs to look for spam or suspicious activity. Please see our other documentation for help on checking logs for [Postfix](/operatingsystems/linux/mail/postfix.html) and [Exim](/operatingsystems/linux/mail/exim.html) mail servers. Services like [Mail-tester](https://www.mail-tester.com/) can also help you find and resolve issues.

Once the issue is found and fixed, you can start getting delisted. As a provider UKFast is not able to get you removed from blacklists, however most blacklists provide an easy delisting process you can use. In most cases you follow the links from the blacklist page and follow the steps provided. A few will expire automatically once the cause is resolved. Some blacklists will ask you to pay money to "expedite" the process of removal. We cannot advise whether this is the best course of action for your individual circumstances. That said, if you feel you have resolved whatever issue caused you to be blacklisted in the first place, it may be worthwhile if you send to mail servers which use those blacklists, since some listings will take up to a month to expire.

Please note that most blacklists use DNS and have a TTL (Time To Live). This is the number of seconds that resolvers will cache the result of the blacklist lookup. Therefore if a blacklist has a very high TTL, it may mean that some mail servers will continue to reject mail for a while after even after you are removed from the blacklist.

## Microsoft, Google and Yahoo

These providers maintain their own private blacklists. You cannot check if you are on these providers' lists. However you have delivery issues to domains like hotmail, outlook, gmail or yahoo, there's a good chance you may be on one of these private blacklists. The best way to check if you may be on these lists is to look in your mail logs for 550 response codes and error messages from these providers. Please see our other documentation on how to check logs for [Postfix](/operatingsystems/linux/mail/postfix.html) and [Exim](/operatingsystems/linux/mail/exim.html) mail servers.

### Microsoft/Hotmail/Office365

Microsoft mail servers are a little different to other providers. Their blacklists are not public so you cannot check if you are blacklisted. You must always get an IP address (or range) whitelisted if you want the mail to end up in the correct mailbox. If you have problems with your mail ending up in spam, of not appearing at all, this is likely the reason.

If you have this issue, we provide a guide in the [Basics of mail](/operatingsystems/linux/mail/mailconfig.html#sending-to-microsoft-hotmail-office365) documentation page which should help you address this. 

```eval_rst
  .. meta::
     :title: Email blacklisting | UKFast Documentation
     :description: How to check if you are blacklisted and steps to take
     :keywords: ukfast, mail, basics, config, dns, spf, mx, blacklist, hotmail, live
