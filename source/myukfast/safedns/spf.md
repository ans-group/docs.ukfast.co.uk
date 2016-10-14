# SPF records

This guide provides the instructions needed to configure an SPF record for your domain.

Sender Policy Framework records (SPF) are designed to prevent spammers from spoofing email from your domain by providing you with a means of stating which servers are authorised to send email on your domains behalf. The large majority of mail servers will check for an SPF record when filtering for spam, preventing people pretending to send mail from your domain when not authorised.

An `SPF` record consists of a string of text stored in a `TXT` or `SPF` record within your DNS setting. This string can be generated using the following wizard:

<http://www.microsoft.com/mscorp/safety/content/technologies/senderid/wizard/>

```eval_rst
.. note::

   If you're looking for a very basic SPF record that fits most situations (mail will only ever send from anything you have an A record or MX record for), the following should suffice:

   v=spf1 a mx -all
```

To add the SPF record, first log into SafeDNS through your MyUKFast client area and choose the relevant domain.

If you already have `TXT` records configured for the domain you will need to add a new record.

![SPF 1](files/spf1.png)

1. Within the `TXT` record section click add record. (This will add a blank record at the end of the record list)
2. Leave hostname blank, under value enter the `SPF` string provided by the wizard
3. Click the Save Records button at the bottom of the page

If you cannot see the `TXT` Records section you will need to add a new record type in order to add the `TXT` record.

![SPF 2](files/spf2.png)

1. Within the Add New Record Type section select `TXT` from the dropdown box. (This should then present you with the fields in the above image)
2. Leave hostname blank, under value enter the `SPF` string provided by the wizard
3. Click Add New Record Type (You should now see the `TXT` Records section listed with your new record present)
4. Click the Save Records button at the bottom of the page

```eval_rst
.. warning::

   Unless your TTL is set to a value other than the default, these records may take up to 24 hours before they have fully propagated.
```
