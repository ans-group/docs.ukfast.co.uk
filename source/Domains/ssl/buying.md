# Purchasing and renewing SSL certificates

This guide covers how to purchase and renew SSL certificates.

:doc:`/Domains/ssl/types` may also be a useful read.

## Purchasing

SSL certificates are available to purchase via [MyUKFast](https://my.ukfast.co.uk/ssl/buy.php)

Select the SSL certificate and click `Buy Now`. You'll then be asked to provide some information regarding the organisation responsible for the domain in question.

After this, you'll need to go through one of the validation processes outlined below, to confirm you're entitled to purchase an SSL certificate for the domain:

* **File Upload** - This is typically the fastest form of validation but requires that you have access to the webserver currently hosting the domain's site. You will need to upload a .txt file to your website which must be publicly accessible via the `Protocol` specified, either HTTP or HTTPS. If you already have an SSL secured site that is available via HTTPS, you should typically choose this option when purchasing the certificate, otherwise, leave this on HTTP.
  
  The file will need to be accessible at `http(s)://example.com/.well-known/pki-validation/<MD5 Hash>.txt` - specific instructions are provided via MyUKFast at the point of purchase.
  
  This file will need to be present throughout validation but can be safely removed once the certificate has been issued.

* **DNS Lookup** -  You will need to create a new CNAME DNS record for your domain. This will be in the format:

  `_<MD5 Hash>.example.com CNAME <SHA-256 hash (part 1)>.<SHA-256 hash (part 2)>.<uniqueValue>.comodoca.com`

   Full details are provided at point of purchase and, as before, this record can be safely deleted once validation is complete.

* **Email** - An email will be sent to an administrative contact registered for the domain (e.g., `admin@example.com`) and you'll see a list of possible email addresses to choose from in MyUKFast. 

  The email will contain a unique validation code and link that are only valid for 30 days. The email can be resent in the event that validation is not completed within this time frame.

Once validation is complete, a UKFast support engineer will be in touch if you've selected the option for UKFast to install the certificate for you.  If you've chosen to install the SSL certificate yourself, you'll find a link to the certificate in [MyUKFast](https://my.ukfast.co.uk/ssl/index.php)

## Renewing

We will send you a number of email alerts in the run up to your SSL certificate expiring.  Simply click the link in one of these emails and follow the process to renew your certificate within MyUKFast.  Alternatively you can login to [MyUKFast](https://my.ukfast.co.uk/ssl/index.php) and go to `Products and Services` then `SSL Certificates` to check when your certificates are due to expire and manage their renewal.
