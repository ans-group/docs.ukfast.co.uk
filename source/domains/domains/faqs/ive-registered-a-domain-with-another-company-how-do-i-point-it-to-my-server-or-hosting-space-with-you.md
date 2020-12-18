# I've registered a domain with another company, how do I point it to my server or hosting space with you?

```eval_rst
   .. title::Domain Name FAQ I've registered a domain with another company, how do I point it to my server or hosting space with you?"
   .. meta::
       :description: Domain Name FAQ I've registered a domain with another company, how do I point it to my server or hosting space with you?"
```


To connect your domain to your UKFast server, you need to edit the DNS zone for the domain. This can be done in one of two ways:


1. You can use your domain registrar's control panel to edit the DNS records and configure it to point at your solution


2. You can use our SafeDNS system to manage the DNS records.


If you decide on the first option, then your registrar's control panel should provide guidance on the below. Their service is going to look different to our SafeDNS interface, so things might be done in a slightly different manner. However, the theory is the same and so are the details you need to key into their system.


If you want to us our SafeDNS system, then you must first point your domain at our name servers:


1. ns0.ukfast.net


2. ns1.ukfast.net


How this is done depends entirely on the control panel offered by your registrar. Please consult their documentation on the matter as it should contain everything you need to get this done. Once the name servers are in place, please allow at least 24 hours for the DNS change to take effect.


Once the name servers are in place and the information has been transmitted, it's time to add the relevant records to your DNS zone. Depending on what services you offer you will need different records, but in our example below we're going to assume simple web services and e-mail.


Let's start with the web services. First we need to create an 'A' record for out domain, and also the 'www' sub-domain. We've already written a handy guide on :doc:`how to add sub-domains and 'A' records to your domain</domains/safedns/addarecord>`, so please consult this guide and when you're done, then pop back here to read on. Now that you're an expert on adding 'A' records to your domain, let's list the information you need and the records you need to create:


1. The IP address of your server. This can be found under the Services > Dedicated Servers tab in MyUKFast. (If you don't have a dedicated server, select the relevant solution; for example, 'Cloud')


2. An ""empty"" 'A' record for your domain 3. A 'www' record for your domain


First, add the two 'A' records to your domain, remembering the first one is blank, so the 'Hostname' is left empty. This enables people to type 'example.domain' and get your website. The second is the 'www' record, which allows people to visit you via 'www.example.domain'. You should have something like this:   Please allow upwards of 24 hours for these new records to propagate.


Next you need to add the e-mail services. This will require three things:


1. The IP address of your server again


2. An 'A' record pointing at the above IP


3. An 'MX' record which tells other e-mail services how-to get in touch with your server when trying to deliver mail


To add an 'A' record just repeat the steps above, but now we're adding something new: an 'MX' record. We've got[ a guide for that ](https://my.ukfast.co.uk/faq/view/1054.html)too, and it also shows you how-to add the 'A' record part!


Once you've completed the last stage, your domain is ready to go and will be serving up the basic services of web-sites and e-mail.

