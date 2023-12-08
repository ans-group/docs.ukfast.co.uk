# How Let's Encrypt works

`Let's Encrypt` uses a 2 step process to issue a certificate:

* **Domain Validation**, to prove you own the domain
* The ability to issue, renew or revoke certificates thereafter

There a few distinct types of domain validation available, so you will need to first assess which method best suits your needs.

```eval_rst
.. warning::
  If your sites or services use our DDoSX/Webcel/WAF services you will not be able to use Let's Encrypt certificates currently.
```

## Types of challenges

### HTTP-01

`HTTP-01` validation is the most common type of SSL challenge method. This involves using an `ACME` client to communicate with `Let's Encrypt` by placing a file containing a unique token in the following directory on your website

```none
<docroot>/.well-known/acme-challenge/<youruniquetoken>
```

This needs to be accessible over port **80** and cannot include a redirect to an IP address. This can validate up to 10 redirects deep, and does not care about *HTTPS validation*, so will allow for self-signed certificates along the way.

It is also easy to automate, which is why tools like `certbot` and `AutoSSL` among others are available to make use of this technology.

A limitation of this challenge is you cannot request [**wildcard certificates**](/domains/ssl/types).

If you have multiple web servers, you have to make sure the file is available on all of them.

```eval_rst
.. note::
  You will need to ensure that your server has either port 80 open inbound/outbound, on both your firewall and your software firewall (eg. IPTables, firewalld, Plesk firewall, CSF). If having any issues, please do contact our support team.

```

### DNS-01

The `DNS-01` challenge method requires you to add a [**TXT**](https://en.wikipedia.org/wiki/TXT_record) record to prove domain ownership.

This can be useful if your service is not accessible over port **80**, or if you have multiple web servers to cover. This challenge method also allows for you to issue [**wildcard certificates**](/domains/ssl/types), along with [**CNAME challenge delegation**](https://www.eff.org/deeplinks/2018/02/technical-deep-dive-securing-automation-acme-dns-challenge-validation)

If using an API, such as our [SafeDNS API](https://developers.ukfast.io/documentation/safedns), this is quick and easy to add and to automate.

```eval_rst
.. note::
  You should always factor in **DNS propagation** when using this challenge method,
```

### TLS-ALPN-01

`TLS-ALPN-01` challenges are currently **not** supported by `certbot`. This type of challenge uses `HTTPS` validation via `TLS`, but requires for the server to be using the `ALPN` protocol. As this is not very common currently, we would recommend you use `HTTP-01` or `DNS-01` as your challenge method.

## Rate Limits

Let's Encrypt has rate limits in-built to prevent abuse of the system. This may affect how and when you issue your certificates.

More information on these limits are at the following link: [Let's Encrypt Rate Limits](https://letsencrypt.org/docs/rate-limits/)

```eval_rst
  .. title:: SSL | How Let's Encrypt Works
  .. meta::
     :title: SSL | How Let's Encrypt Works | ANS Documentation
     :description: How Let's Encrypt Works
     :keywords: ssl, letsencrypt, let's encrypt, secure, security, server, howto, guide, tutorial
```
