# Spam Confidence Level

Spam confidence level (SCL) is a numerical value indicating the likelihood that an incoming email message is spam. SCL is a part of the Microsoft Exchange spam filter.

1 is definitely not spam

10 is definitely spam

You can set the SCL on your Exchange server mailboxes using the below command

```powershell
Get-Mailbox -OrganisationalUnit contoso.com | Set-Mailbox -SCLJunkEnabled $true -SCLJunkThreshold 5 -SCLRejectEnabled $true -SCLRejectThreshold 9
```

* The `-SCLJunkThreshold 5` parameter denotes the SCL rating at which mail is marked as spam
* The `-SCLRejectThreshold 9` parameter denotes the SCL rating at which mail is outright rejected by the mail server.

These values should be adjusted to your preference before running the command although the values using in our demonstration are a good starting point.

```eval_rst
  .. title:: Spam Confidence Level
  .. meta::
     :title: Spam Confidence Level | ANS Documentation
     :description: Information on Spam Confidence Level (SCL) for Microsoft Exchange
     :keywords: ukfast, windows, exchange, spam, confidence, level, scl, microsoft, block, junk, cloud, server, virtual
```
