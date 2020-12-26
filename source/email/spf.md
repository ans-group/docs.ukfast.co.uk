# Sender Policy Framework (SPF) records

This guide will provide a general overview of Sender Policy Framework records (SPF), what they do, and how to create a suitable record for your purpose.

Once you have a suitable SPF record, please refer to this [guide on how to add your record to SafeDNS](/domains/safedns/spf).

## General overview

Sender Policy Framework records (SPF) are designed to prevent spammers from spoofing email from your domain by providing you with a means of stating which servers are authorised to send email on behalf of your domain.
Most mail servers will check for an SPF record when filtering for spam and typically will choose to reject delivery of a message if the SPF check fails. As such, it's important to note that SPF records will not prevent people from _sending_ spoofed messages but instead provide a mechanism by which receiving mail servers can choose not to deliver them.
SPF records are also valuable in increasing the deliverability of legitimate mail sent from your domain. A message that passes an SPF check is less likely to be labelled as spam by mail servers employing spam filtering technology.

An SPF record consists of a string of text stored in a `TXT` DNS record. While there is also a specific `SPF` record type, the use of this was officially discontinued in 2017 in [RFC 7208](https://tools.ietf.org/html/rfc7208).

An example SPF record looks like this:

```
v=spf1 mx a ~ip4:192.168.1.1/32 a:mail.mybulkmailserver.com -all
```

The first part v=spf1 defines the version of SPF used. This is the same on all records. The next parts: "mx", "a", "ip4" and "all" are "mechanisms", and the "~" and "-" are "qualifiers". Mechanisms are processed in order. We'll explain each one in detail below.

There are eight mechanisms for identifying which servers are allowed to send mail on behalf of your domain. We'll define them all here, but for most purposes, you will only ever need four: all, ip4, mx, and a.

```eval_rst
+-----------+-------------------------------------------------------+-------------------------------------+
| Mechanism | Use                                                   | Example syntax                      |
+===========+=======================================================+=====================================+
| all       | Always match                                          | all                                 |
+-----------+-------------------------------------------------------+-------------------------------------+
| ip4       | Match an IPv4 address or subnet                       | ip4:46.37.163.252/29                |
|           | /32 subnet is the default if not given                |                                     |
+-----------+-------------------------------------------------------+-------------------------------------+
| ip6       | Match an IPv6 address or subnet                       | ip6:2001:db8:85a3::8a2e:370:7334/64 |
|           | /128 subnet is the default if not given               |                                     |
+-----------+-------------------------------------------------------+-------------------------------------+
| a         | Match the A records for example.com                   | a:example.com                       |
|           | Optionally includes a subnet range.                   | a:example.com/29                    |
|           | If no domain is specified, match the current domain   | a                                   |
+-----------+-------------------------------------------------------+-------------------------------------+
| mx        | Match MX records for example.com                      | mx:example.com                      |
|           | Optionally includes a subnet range.                   | mx:example.com/29                   |
|           | If no domain is specified, match the current domain   | mx                                  |
+-----------+-------------------------------------------------------+-------------------------------------+
| ptr       | Match PTR (Also called rDNS) records.                 | ptr:example.com                     |
|           | Not generally used as it results in long DNS lookups  |                                     |
+-----------+-------------------------------------------------------+-------------------------------------+
| exists    | Match if the domain given returns an A record.        | exists:example.com                  |
|           | Only really useful in macros.                         |                                     |
+-----------+-------------------------------------------------------+-------------------------------------+
| include   | Include another domain's SPF record for matches       | include:example.com                 |
|           | Used for managing trust relationships between domains |                                     |
+-----------+-------------------------------------------------------+-------------------------------------+

```

Each mechanism can have a qualifier which defines what action should happen if the mechanism is matched. The default is Pass, so if a mechanism is written without a qualifier, read it as if it has a +.

```eval_rst
+-----------+--------------------+---------------------------------------------------------------------------------------------------------+
| Qualifier | Result on matching | Further notes:                                                                                          |
+===========+====================+=========================================================================================================+
| \+        | Pass               | This is the default action if a mechanism doesn't have a qualifier set.                                 |
|           |                    | If the mechanism matches, it means that host is allowed to send mail and mail should be accepted.       |
+-----------+--------------------+---------------------------------------------------------------------------------------------------------+
| \-        | Fail               | This means the host is not allowed to send, and mail should be rejected                                 |
+-----------+--------------------+---------------------------------------------------------------------------------------------------------+
| ~         | Soft Fail          | This means the host is not allowed to send, but mail should be marked and accepted rather than rejected |
+-----------+--------------------+---------------------------------------------------------------------------------------------------------+
| ?         | Neutral            | This means the mechanism doesn't have any bearing on if mail should be accepted or rejected             |
+-----------+--------------------+---------------------------------------------------------------------------------------------------------+
```

Looking back to our example:

```
v=spf1 mx a ~ip4:192.168.1.1 a:mail.mybulkmailserver.com -all
```

When a remote mail server receives an email claiming to be from your domain, the mail server will read this SPF record and work through the following steps:
- *mx:* Match the MX records for the domain to the origin of the mail and Pass if they match.
- *a:* Match the A records for the domain to the origin of the mail and Pass if they match.
- *~ip4:192.168.1.1:* Match the origin against the subnet ip4:192.168.1.1, and if it matches, mark it with a Soft Fail.
- *a:mail.mybulkmailserver.com:* If the origin matches this domain, return Pass.
- *-all:* If the origin matches anything else, mark it as a Fail.

As you can see this gives you a lot of control over who can send mail on your behalf.

## Real World SPF record examples

You only ever send email from servers you have A or MX records for:

```
v=spf1 a mx -all
```

You send email from servers your have A or MX records for, but your also have another dedicated email server:

```
v=spf1 a mx a:dedicatedmailserver.com -all
```

If you use bulk mail services like Mandrill, Mailchimp or others, please do make sure you consult their documentation on SPF records and include all the services you intend to use:

```
v=spf1 a mx include:spf.mandrillapp.com include:servers.mcsv.net ?all
```

```eval_rst

  .. title:: Email | Sender Policy Framework records

  .. meta::
     :description: Detailed guidance on Sender Policy Framework (SPF) record usage and formats
     :keywords: spf, sender policy framework, dns, dns records, domains, email, spam

```
