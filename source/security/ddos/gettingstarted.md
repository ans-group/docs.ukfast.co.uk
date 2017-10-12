# Getting started

DDoSX<sup>®</sup> and Content Delivery Network (CDN) are two features of our global network that work together to significantly improve your website or web application’s speed and security. DDoSX<sup>®</sup> provides protection against DDoS attacks, and CDN is an **optional** feature that caches your site's content closer to the end user. In order to use CDN, DDoSX must also be enabled on the domain.

```eval_rst
.. seealso::

   To use DDoSX\ :sup:`®` and optional Content Delivery Network from UKFast, you need to have your domains' nameservers pointing to the UKFast nameservers, and you also need to manage your DNS records using SafeDNS.

   Make sure to set up your DNS records correctly in SafeDNS first - see the :doc:`/Domains/safedns/index` guide for assistance.  You must move all records associated with the domains (including sub-domains) you wish to protect, including SMTP, MX, mail etc. to SafeDNS.

   Once you have done this, point your domains to the UKFast nameservers, which are:

   - ns0.ukfast.net
   - ns1.ukfast.net

   You'll need to do this through whichever domain registrar you use to manage your domains (which may not be UKFast).  If you don't know who your domain registrar is you can do a 'WHOIS' lookup on websites such as https://whois.icann.org/

```

To enable DDoSX<sup>®</sup> and CDN on your domains, follow these steps:

**[1. Connect](#connect-domain)** your domain(s) to DDoSX

**[2. Configure](#configure-domain)** which domain records you'd like to protect

**[3. Test](#test-domain-and-put-live)** your domains will work properly on the DDoSX network before putting them live

**[4. Create CDN Caching Rules](#create-cdn-caching-rules)**

## Connect domain

- Login to [MyUKFast](https://my.ukfast.co.uk) and head to `DDoSX & CDN` in the `Products and Services` menu.
- Click `Connect Now`
- On this page you can search for the domains you're managing through SafeDNS. (if you havent added your domains to SafeDNS yet, please refer to the info box at the top of this page)
- Choose the domain you wish to protect and click `Connect`.
- To add CDN to your order, ensure the highlighted toggle switch is set to "On".
- Repeat for each domain you want to add to the network.

![connect](files/connect.PNG)

- Click `Confirm` to go through the payment process. (You won't have to complete this step if you've already ordered DDoSX<sup>®</sup> or CDN via your UKFast account manager).

## Configure domain

- Click `Configure` next to the domain you wish to setup first within the `DDoSX & CDN` control panel and choose which A Records and AAAA Records you specifically want to protect for each domain.
- You can also assign any existing SSL certificates at this point. SSL certificates purchased from MyUKFast will appear in the dropdown menu, or click `Add SSL` to add details of other SSL certificates manually. SSL certificates can be managed within the `SSL Certificates` tab.
- Ensure the highlighted toggle switches are set to "On" for all of the sub-domains you wish to protect with DDoSX<sup>®</sup>.

![configuredomain](files/configuredomain.PNG)

- Click `Apply Changes` and your domain will now be connected to the UKFast DDoSX<sup>®</sup> network, and configured appropriately. (You should allow up to 10 minutes for the changes to be fully applied)

## Test domain and put live

- Once you've connected your domain to the DDoSX network and configured your DNS records, you may wish to test that your website or application will work correctly before changing your live DNS routing.  This can be done by modifying your local `hosts` file to look for the DDoSX "Assigned IPv4" address for your domain.

- You will see that initially your DNS Routing is shown as "Server", as per below.

![serverpreview](files/serverpreview.PNG)

- Locate the `hosts` file on your computer.  On Windows you'll find it in **C:\Windows\System32\drivers\etc**.  

- Open the `hosts` file using Notepad or another plain text editor (you may need administrator rights to make changes), and insert a line for each domain you wish to test, that includes the domain and the Assigned IPv4 address from DDoSX; for example:

 ```
 189.192.54.168 mydomain.co.uk
 189.192.54.168 www.mydomain.co.uk
 189.192.54.168 blog.mydomain.co.uk
 ```
- On Linux and MacOS you can open and edit the `hosts` file in a terminal window using a command such as

 ```sudo nano /private/etc/hosts```

- [This article](https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/) contains more detailed instructions on modifying the `hosts` file on MacOS, Linux, and different versions of Windows.

- Once you've added all the domains you need to test to your `hosts` file, save the changes. Then open a web browser and try browsing to your domain.  Your local `hosts` file will route the request directly to the DDoSX IP address so you'll be able to see exactly how your site will perform when you change your DNS records.

- If you're happy with how your site performs, you can switch the DNS Routing for your domain to "DDoSX".  Note that it may take [up to 48 hours](/Domains/domains/dnspropagation.html) for DNS changes to propogate across the internet (as with any such changes), and before your domain is fully protected.

## Create CDN caching rules

For any domains with CDN added, content caching will not be activated until rules have been added to the configuration.

[Follow this link to the CDN 'caching rules' setup guide](/network/cdn/cachingrules.html)

```eval_rst
.. meta::
     :title: Getting started with DDoSX and CDN | UKFast Documentation
     :description: Guidance to setting up DDoSX and CDN from UKFast
     :keywords: ddos, ddos protection, anti-ddos, cdn, content delivery, content delivery network
```
