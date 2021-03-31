# The Security Scan

Your first encounter with TLS/SSL may come when a security scan or PCI-DSS compliance scan is run against one of your websites. These scans can help reveal security issues to be addressed and are considered good practice, and even almost mandatory for Internet facing services. A security scan can very quickly analyse a website or server against known vulnerabilities and list these vulnerabilities in the form of a report. This report can then be used to make the site or server more secure.


## How do you tackle this?

First, you should determine the severity of the vulnerability.

Second, you must determine if the vulnerability can be safely patched without disrupting the functionality of the site or service.

Critical vulnerabilities should always be patched, however, sometimes there is a real business case to leave very minor vulnerabilities untouched (this is fairly common on private networks). An example of this would be a legacy application that requires the use of a certain TLS protocol or cipher in order to connect to a site or service. If you cannot upgrade or re-code the application, then removing these protocols will cause the application to fail TLS negotiation, causing the handshake to be aborted.

However, when it comes to Internet-facing web servers, security is paramount. When your website or application can be accessed from anywhere in the world, you must remain up to date with the latest security advisories and vulnerabilities in order to keep your application and your visitor's data safe.

Additionally, if the service handles payments or credit card information then you will want to make sure that you use security protocols and cipher suites that are at least PCI-DSS compliant. This will include ensuring that your application and database can support secure protocols.

We recommend keeping up-to-date with the PCI Security Standards for any upcoming changes to the PCI-DSS specification. The most recent revisions and news regarding payment card industry standards can be found from the PCI Security Standards website. An link to the external site is provided [here](https://www.pcisecuritystandards.org)

Next, we will look at some [TLS and Schannel settings relating to Windows Web Servers](/operatingsystems/windows/tlsandschannel/webserverrecommendations)

```eval_rst
   .. title:: Windows | The Security Scan
   .. meta::
      :title: Windows | The Security Scan | UKFast Documentation
      :description: Information and guidance on Windows security scans
```
