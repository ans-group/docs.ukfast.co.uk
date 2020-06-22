# Reverse DNS Records

Reverse DNS or reverse DNS resolution (rDNS) is used to associate a domain name with an IP address using Domain Name System (DNS). This can be useful in instances such as mailservers - quite often mailservers will carry out a check against a sending server to help identify the source of the email.

rDNS records can be updated if you host a server with UKFast. To update these records, start by logging into [MyUKFast](https://my.ukfast.co.uk).

Once logged in, navigate to the server you wish to amend with these steps:

* Go to `Products & Services` then `Dedicated Servers` or `eCloud Public` etc. Find the server you're looking to apply the change to.
* Click the server's IP Address to open the details page.
* Scroll down to the option for `rDNS Host`.  In this section, enter your rDNS record i.e. `mail.mydomain.com`
* Save Changes

This change should propagate immediately and can be confirmed by running the following via command prompt :- `ping -a <server IP address>`
