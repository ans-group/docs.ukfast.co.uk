# Setting up DDoSX, CDN and WAF using ALIAS, ANAME or CNAME

DDoSX<sup>®</sup>, can be setup to protect any domain from DDoS and common Web Application attacks such as SQL Injections, Remote Command Execution and Cross-Site Scripting (XSS). More on how DDoSX<sup>®</sup> works can be found :doc:`/security/ddos/generalinformation`.

CDN and WAF are optional additional DDoSX<sup>®</sup> features, and as a result DDoSX must first be enabled on your domain(s) to allow CDN and WAF to be configured.

To use DDoSX<sup>®</sup>, CDN and WAF, you need to either have your domains' setup on UKFast SafeDNS and ensure it's nameservers pointing to the UKFast nameservers or create a ANAME/ALIAS record with your current DNS provider to point to DDOSx using a provided CNAME. 

To enable DDoSX<sup>®</sup>, CDN and WAF on your domains, follow these steps:

**[1. Connect](#connect-domain)** your domain(s) to DDoSX

**[2. Configure](#configure-domain)** which domain records you'd like to protect

**[3. Test](#test-domain-and-put-live)** your domains will work properly on the DDoSX network before putting them live

**[4. Create CDN Caching Rules](#create-cdn-caching-rules)** for any CDN-enabled domains

**[5. Configure WAF settings](#configure-waf-settings)** for any domains requiring WAF protection

```eval_rst
.. warning::

   DDoSX supports HTTP and HTTPS web traffic on ports 80 and 443 respectively. If you need to route other types of traffic to your UKFast-hosted solution then please contact us before setting up DDoSX.

```

## 1) Prepare your domain

The first step to setting up DDoSX<sup>®</sup> is to preper your domain. Depending if you're going to use SafeDNS or an ANAME/ALIAS, we recoconed complted a few checks first to ensure that DDoSX<sup>®</sup> will work properly.

### SafeDNS:

Before setting up a SafeDNS domain in, double check that your domain is setup correctly and working as expected Documentation onm how to setup SafeDNS can be found at :doc:`/Domains/safedns/index` should you assistance. 

You must move all records associated with the domains (including sub-domains) you wish to protect, including SMTP, MX, mail etc to SafeDNS.

Once you have done this, point your domains to the UKFast nameservers, which are:

   - ns0.ukfast.net
   - ns1.ukfast.net

You'll need to do this through whichever domain registrar you use to manage your domains (which may not be UKFast). If you don't know who your domain registrar is you can do a 'WHOIS' lookup on websites such as https://whois.icann.org/

### ALIAS/ANAME via CNAME

If you don't want to use UKFast SafeDNS, you can route traffic from your domain to DDoSX<sup>®</sup> by creating an ANAME or ALIAS records using a CNAME provided by DDoSX<sup>®</sup>.

Please note, only a handful of DNS providers have the ability to setup ANAME/ALIAS records. Please check that your DNS provider supports root level forwarding via an ANAME or ALIAS records beofre trying to setup a root level domain on DDoSX<sup>®</sup> using a CNAME.

Some DNS providers that do support creating ALIAS/ANAME records include:

* DNS Made Easy
* Cloudflare (Via CNAME Flattening)

If your DNS provider does not support this we cannot protect the root domain.

Non-root level domains such as dashboard.example.com or my.example.com can be setup without using a ANAME/ALIAS by instead creating a basic CNAME record via your DNS provider and pointing it to your DDoSX<sup>®</sup> provided CNAME. 


## 2) Connect your domain to DDoSX<sup>®</sup>

- Login to [MyUKFast](https://my.ukfast.co.uk) and head to `DDoSX Protection` in the navigation menu.
- Click the `GET STARTED` button if this is your first domain, or click 'Add additional domain' in the top right if this is an additional doamin.
- Enter the domain that you want to protect. 
    - If the domain is in SafeDNS, the domain will automatically appear as a part of a selectable dropdown
    - If the domain is not in SafeDNS, you will need to enter the full domain. A blue message box will display with additional information.
- Select any additional features you'd like like to add to this domain such as CDN or WAF.
- Double check your domain and selected additional features and then hit 'Buy Now'..
- Repeat for each domain you want to add to the network.

![connect](files/connect_safedns_external.png)

- Click `Complete Transaction` on the next page to completed payment process. (You won't have to complete this step if you've ordered DDoSX<sup>®</sup>, WAF or CDN via your UKFast account manager -  Any existing credits will be consumed first).

## 3) Verify domain (Non SafeDNS setup only)

## 4) Configure domain

- Click `Configure` next to the domain you wish to setup, and choose which A Records and AAAA Records you specifically want to protect for the domain.
- You can assign any existing SSL certificates at this point. SSL certificates purchased from MyUKFast will appear in the dropdown menu, or click `Add SSL` to add details of other SSL certificates manually. SSL certificates can be managed within the `SSL Certificates` tab.
- Ensure the DDoSX Protection toggle switches are set to "On" for all of the records and sub-domains you wish to protect.

![configuredomain](files/configuredomain.PNG)

- Click `Apply Changes` and your domain will now be connected to the UKFast DDoSX<sup>®</sup> network, and configured appropriately. (You should allow up to 10 minutes for the changes to be fully applied)

## 5) Test domain and put live

- Once you've connected your domain to the DDoSX network and configured your DNS records, you may wish to test that your website or application will work correctly before changing your live DNS routing.  This can be done by modifying your local `hosts` file to look for the DDoSX "Assigned IPv4" address for your domain.

- You will see that initially your DNS Routing is shown as "Server", as per below.

![serverpreview](files/serverpreview.PNG)

- Locate the `hosts` file on your computer.  On Windows you'll find it in **C:\Windows\System32\drivers\etc**.  

- Open the `hosts` file using Notepad or another plain text editor (you may need administrator rights to make changes), and insert a line for each domain you wish to test, that includes the domain and the Assigned IPv4 address from DDoSX; for example:

 ```
 185.156.64.0 mydomain.co.uk
 185.156.64.0 www.mydomain.co.uk
 185.156.64.0 blog.mydomain.co.uk
 ```
- On Linux and MacOS you can open and edit the `hosts` file in a terminal window using a command such as

 ```
 sudo nano /private/etc/hosts
 ```

- [This article](https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/) contains more detailed instructions on modifying the `hosts` file on MacOS, Linux, and different versions of Windows.

- Once you've added all the domains you need to test to your `hosts` file, save the changes. Then open a web browser and try browsing to your domain.  Your local `hosts` file will route the request directly to the DDoSX IP address so you'll be able to see exactly how your site will perform when you change your DNS records.

- If you're happy with how your site performs, you can switch the DNS Routing for your domain to "DDoSX".  Note that it may take [up to 48 hours](/Domains/domains/dnspropagation.html) for DNS changes to propagate across the internet (as with any such changes), and before your domain is fully protected.

## Additional Configuration

If you have added additional features such as CDN or WAF to your DDoSX<sup>®</sup> protected domain, you can configure theese now.

### Create CDN caching rules

For any domains with CDN added, content caching will not be activated until you have [added caching rules to the configuration](/network/cdn/cachingrules.html)

### Configure WAF settings

Navigate to the WAF tab to find the settings for WAF on DDoSX.  There are a number of [different WAF settings](/security/ddos/wafsettings.html) that allow you to manage the level of protection for your domain.

```eval_rst
.. warning::

   Always run your WAF in Detection Only mode for a period of time before switching it on, otherwise you could cause issues that prevent your application from being accessible to you or your customers.  More details available on the :doc:`/security/ddos/wafsettings` page.

```

### Configure webserver logging (optional)

Once your domain is fully enabled on DDoSX, all requests to your webserver will appear to come from the DDoSX IP address rather than the original client. Therefore you may wish to configure your webserver to place the original client IP address into the logs. This is most important if you're using a stats package like Webalizer or AWStats, which rely on analysing your local webserver logs.

Here's how to do this for NGiNX and Apache:

### NGiNX

For NGiNX, insert this code into one of the `http` or `server` blocks in your configuration. This requires the [realip](https://nginx.org/en/docs/http/ngx_http_realip_module.html) module be compiled into nginx. You can confirm if this is already there with `nginx -V 2>&1 | grep -o realip`. If this outputs `realip`, you're good to go.

```
  set_real_ip_from 185.156.64.0/24;
  set_real_ip_from 23.170.128.0/24;
  set_real_ip_from 192.166.44.0/24;
  set_real_ip_from 78.24.88.0/24;
  set_real_ip_from 195.69.102.0/24;
  set_real_ip_from 2a02:21a8:1::/48;
  set_real_ip_from 2a02:21a8:2::/48;
  set_real_ip_from 2a02:21a8::/48;
  set_real_ip_from 2a09:ba00:4::/48;
  set_real_ip_from 2a09:b600:5::/48;
  set_real_ip_from 2a09:b200:6::/48;
  real_ip_header X-Forwarded-For;
  real_ip_recursive on;
```

Once you have added these into your configuration, test and reload your NGiNX configuration (e.g. `nginx -t && systemctl reload nginx`) to make the changes live.

### Apache

For Apache 2.4 and above, you will need to use the [mod_remoteip](https://httpd.apache.org/docs/current/mod/mod_remoteip.html) module. This should be compiled into your Apache installation, but you can confirm this by running `httpd -M 2>&1 | grep remoteip` (use `apache2ctl` instead of `httpd` on Debian/Ubuntu), which should output `remoteip_module (shared)`. As long as you have that, you're good to go. Add the following into your `<VirtualHost>` declaration, and then alter any `CustomLog` directives to use the newly defined `LogFormat`.

```
<IfModule remoteip_module>
    RemoteIPHeader X-Forwarded-For
    RemoteIPTrustedProxy 185.156.64.0/24
    RemoteIPTrustedProxy 23.170.128.0/24
    RemoteIPTrustedProxy 192.166.44.0/24
    RemoteIPTrustedProxy 78.24.88.0/24
    RemoteIPTrustedProxy 195.69.102.0/24
    RemoteIPTrustedProxy 2a02:21a8:1::/48
    RemoteIPTrustedProxy 2a02:21a8:2::/48
    RemoteIPTrustedProxy 2a02:21a8::/48
    RemoteIPTrustedProxy 2a09:ba00:4::/48
    RemoteIPTrustedProxy 2a09:b600:5::/48
   RemoteIPTrustedProxy 2a09:b200:6::/48
</IfModule>
LogFormat "%a %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" ddosx

# You may already have a line like the following in your VirtualHost declaration,
# if so, change the last part (likely the word `combined`) to `ddosx` to use the
# above log format.
CustomLog /var/log/httpd/acmecorp.com/access.log ddosx
```

Test and then reload your Apache configuration (e.g. `httpd -t && systemctl reload httpd`) to make the changes live.

For Apache 2.2 you will need to use [mod_rpaf](https://github.com/gnif/mod_rpaf), the use of which is beyond the scope of this document.

### haproxy

If you have haproxy in front of your webservers, you'll probably want to set the
X-Forwarded-For header on here. The easiest way to do this is to disable the 
`forwardfor` option to prevent haproxy setting the header automatically, and instead
set the header manually in each backend.

First, comment out your forwardfor option, potentially in the `defaults` section, e.g.

```
defaults
    #option forwardfor except 192.168.1.10
...
```

Then, in each backend set the `X-Forwarded-For` header to match the value of the `DDOSX-Connecting-IP` header:

```
backend webservers
    mode http
    http-request set-header X-Forwarded-For %[req.hdr(DDOSX-Connecting-IP)]
    server web1 ...
```

```eval_rst
.. meta::
     :title: Setting up DDoSX, CDN and WAF using ALIAS, ANAME or CNAME | UKFast Documentation
     :description: Guidance to setting up DDoSX, WAF and CDN from UKFast
     :keywords: ddos, ddos protection, anti-ddos, cdn, content delivery, content delivery network, waf, web application firewall
```