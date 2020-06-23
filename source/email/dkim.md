# DomainKeys Identified Mail (DKIM) on Web Host Manager/cPanel or Plesk

## What is DKIM?

DomainKeys Identified Mail (DKIM) is an email authentication protocol that's designed to transmit email in such a way that it can be verified by email service providers, and hence prevent email address spoofing - often used in spamming and phishing attacks.  However, DKIM can be complicated, and cause more issues than it resolves.

## Do you really need DKIM?

Setting up DKIM records on your Web Host Manager (WHM) / cPanel or Plesk server, where you are using external DNS, is tricky to get right.  Most MTAs (Mail Transfer Agents) recognize the flaws and difficulty in DKIM implementation. An absent DKIM record will not generally be held against you, while an invalid record most certainly will be.

This guide is based around WHM for the most part, but the same principles can apply to Plesk, or any custom built mail server.

It's worth noting that DKIM should have two records to work correctly. The public key record, and the policy record.

The main issue is that when WHM sets up DKIM, it does so with the expectation that WHM will also be acting as the nameserver for the domain. That means WHM can handle the public/private key generation, and add the public key to the DKIM DNS record in a format that it likes, when needed. This presents 2 major issues:

1) In order to get the record to work with other DNS nameservers we need to change the record to match whatever your nameserver provider accepts. Usually this means stripping out " /; and whitespace characters that WHM inserts to separate the long public key into separate records.

2) If the private key on the server is ever re-generated for any reason (For example, if at any point the DKIM option is disabled and then re-enabled in the cPanel account) it will cause problems with your mail delivery, as DKIM validation will fail. Since you're putting put the public key on a DNS server that WHM cannot access, you'll need to manually change this DNS record if this happens.

This is a common issue and there are several discussions on cPanel forums that shed further light on the issue for those interested:
- [DKIM problems with 3rd party / external DNS](https://forums.cpanel.net/threads/dkim-problems-with-3rd-party-external-dns.267001/)
- [How to Enter DKIM record into DNS Zone](https://forums.cpanel.net/threads/how-to-enter-dkim-record-into-dns-zone.528201/)
- [Is DKIM possible if I'm not running DNS locally?](https://forums.cpanel.net/threads/is-dkim-possible-if-im-not-running-dns-locally.595303/)
- [Generate 1024-bit DKIM keys](https://forums.cpanel.net/threads/generate-1024-bit-dkim-keys.542411/)

## I definitely need DKIM!

### For WHM:

With all that said, if DKIM is an absolute requirement, then you can take the public key record from WHM, strip the whitespace, quotes and trailing /; and then test it using an online tool before adding it to your DNS provider as a TXT record.

A tool to test if your record format is valid can be found here: http://dkimcore.org/tools

An example public key record for the domain "example.com" would be:
```
Host field:
default._domainkey
TXT value field:
v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCvc8OvYXyvaiTVTK0vnrPOYhetVgjjAzVMl6GI186o8hCR13/7ZMMhAz3wmADBxW00Xb6S8Z3miqLTBz79ze+N/TvtiupeQHIVH4do+sxWRVfWicWzaVrmKUSOKPk3QhtouRVfpBKOfIQArP07/7/ITC4ZWtHCPq4+l1lPBvvVFQIDAQAB
```
And an example policy record would be:
```
Host field:
_domainkey.example.com
TXT value field:
o=~; r=postmaster@yexample.com
```
This record indicates that not all mail will be signed (o=) and that invalid verifications should be reported to postmaster@yexample.com (r=).
Your DNS provider may have different requirements, so please do check your provider's documentation if you have issues with adding this record.

### For Plesk

Plesk provide their own comprehensive documentation on this, which can be found at [Plesk DKIM documentation](https://docs.plesk.com/en-US/onyx/administrator-guide/mail/antispam-tools/dkim-spf-and-dmarc-protection.59433/#o78133).

## Testing

Ensuring the record is correct is a vital step, as an invalid record is likely to cause mail delivery failures. Once you have added the required records, allow up to 24 hours for DNS propagation and then test it. You can see if the records are present using dig on a Linux server: "dig example.com TXT" will return all the TXT records for example.com. There are [online versions of this tool](https://toolbox.googleapps.com/apps/dig/) if you're not comfortable on the command line.

You can then use other online tools [here](http://dkimcore.org/tools/) or [here](https://www.mail-tester.com/spf-dkim-check) to check the records are valid.

```eval_rst
.. meta::
   :title: DKIM records | UKFast Documentation
   :description: How to set up DKIM on your WHM/cPanel or Plesk server
   :keywords: email, dkim, whm, plesk
