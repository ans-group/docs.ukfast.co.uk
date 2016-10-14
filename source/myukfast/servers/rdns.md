# Reverse DNS Records

Reverse DNS or reverse DNS resolution (rDNS) is used to associate a domain name with an IP address using Domain Name System (DNS). This can be useful in instances such as mailservers - Quite often mailservers will carry out a check against a sending server to help identify the source of the email.

rDNS records can be updated if you host a server with UKFast. To update these records, start by logging into [MyUKFast](https://my.ukfast.co.uk).

Once logged in, navigate to the server you wish to amend this record on using:

* `Products & Services` > `Dedicated Servers/eCloud/etc..`` > Find the server in question you're looking to apply this change to.
* Click the Server IP Address to open up the device details for this server.
* Part way down the page you should see an option for `rDNS Host` in this section, enter your rDNS record i.e. `mail.mydomain.com`
* Save Changes

This change should propagate immediately and can be confirmed by running the following via command prompt :- `ping -a <server IP address>`
