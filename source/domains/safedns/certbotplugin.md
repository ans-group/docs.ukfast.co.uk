# SafeDNS Authenticator plugin for Certbot

## Prerequisites

To use this Certbot authenticator, you'll need to:

* To have `python3` and `pip` installed on your server
* To have an API key with permissions on the SafeDNS API

You can obtain the API key from your MyUKFast [account page](https://my.ukfast.co.uk/applications/index.php).
See also the [SafeDNS API](https://developers.ukfast.io/documentation/safedns) documentation.

It's also assumed you'll running all commands as the `root` user.

## Setup and configuration

* Make sure we have the latest version of `certbot-dns-safedns` installed.
```bash
pip3 install --upgrade certbot-dns-safedns
```

* Create a Certbot configuration file and a credentials for Certbot to use:
```bash
mkdir ~/.config/letsencrypt/
```

```bash
cat > ~/.config/letsencrypt/dns_safedns-credentials.ini <<EOF
dns_safedns_auth_token = YourAPIKeyGoesHere
EOF
chmod 600 ~/.config/letsencrypt/dns_safedns-credentials.ini
```

```bash
cat > ~/.config/letsencrypt/cli.ini <<EOF
authenticator = dns_safedns
email = admin+certbot-alerts@mydomain.com
no-eff-email = true
agree-tos = true
dns_safedns-credentials = $(realpath ~/.config/letsencrypt/dns_safedns-credentials.ini)
EOF
chmod 600 ~/.config/letsencrypt/cli.ini
```

```eval_rst
.. note::
   You will need to update ``admin+certbot-alerts@mydomain.com`` and ``YourAPIKeyGoesHere`` in the example above (at the least) to values relevant to your environment
```

```eval_rst
.. warning::
   You should protect these API credentials as you would the password to your MyUKFast account. Users who can read this file can use these credentials to issue arbitrary API calls on your behalf. Users who can cause Certbot to run using these credentials can complete a ``dns-01`` challenge to acquire new certificates or revoke existing certificates for associated domains, even if those domains aren't being managed by this server.
```

```eval_rst
.. note::
   Certbot will emit a warning if it detects that the credentials file can be accessed by other users on your system. The warning reads "Unsafe permissions on credentials configuration file", followed by the path to the credentials file. This warning will be emitted each time Certbot uses the credentials file, including for renewal, and cannot be silenced except by addressing the issue (e.g., by using a command like ``chmod 600`` to restrict access to the file).
```

* We should now be able to test it works, using the Lets Encrypt staging environment:

```bash
/usr/local/bin/certbot certonly \
  -d server1.ukfast.co.uk \
  -d *.ukfast.dev \
  -d server3.ukfast.co.uk \
  --test-cert
```

```eval_rst
.. note::
   I have used requested 3 domains on my certificate here, ``server1.ukfast.co.uk``, ``*.ukfast.dev`` and ``server3.ukfast.co.uk``. You'll want to replace these with your choice of domains. You need to have the zone in your SafeDNS account already. In my case this zone name is ``ukfast.co.uk`` for ``server`` and ``server3`` and ``ukfast.dev`` for the other.
```

You'll notice that we didn't need to tell it to any SafeDNS related info as it was read from the `cli.ini` file for us.

* You should now see an output like this:
```none
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator dns_safedns, Installer None
Obtaining a new certificate
Performing the following challenges:
dns-01 challenge for server1.ukfast.co.uk
dns-01 challenge for *.ukfast.dev
dns-01 challenge for server3.ukfast.co.uk
Waiting 30 seconds for DNS changes to propagate
Waiting for verification...
Cleaning up challenges

IMPORTANT NOTES:
- Congratulations! Your certificate and chain have been saved at:
  /etc/letsencrypt/live/server1.ukfast.co.uk/fullchain.pem
  Your key file has been saved at:
  /etc/letsencrypt/live/server1.ukfast.co.uk/privkey.pem
  Your cert will expire on 2020-12-09. To obtain a new or tweaked
  version of this certificate in the future, simply run certbot
  again. To non-interactively renew *all* of your certificates, run
  "certbot renew"
- If you like Certbot, please consider supporting our work by:

  Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
  Donating to EFF:                    https://eff.org/donate-le
```

* This has worked, so we can now switch to use the production Lets Encrypt servers instead. First we delete the staging certificate.

```bash
/usr/local/bin/certbot delete --cert-name server1.ukfast.co.uk
```

* Then request again but excluding the `--test-cert` option

```bash
/usr/local/bin/certbot certonly \
  -d server1.ukfast.co.uk \
  -d *.ukfast.dev \
  -d server3.ukfast.co.uk
```

## Without using the `cli.ini` file

If you prefer to not use the `cli.ini` file, perhaps because you need to use different authenticators side by side, you can be more verbose on the command line and specify the options like this:

```bash
/usr/local/bin/certbot certonly \
  -d server1.ukfast.co.uk \
  -d *.ukfast.dev \
  -d server3.ukfast.co.uk \
  --authenticator dns_safedns \
  --dns_safedns-credentials /root/.config/letsencrypt/dns_safedns.ini \
  --deploy-hook "/usr/bin/systemctl restart httpd"
```

## Known issues

If you get any Python cryptography errors, such as:

```bash
ContextualVersionConflict: ...
```

Try upgrading your version of `pyopenssl`, like this:

```bash
sudo pip install --upgrade pyopenssl
```

You can also check the Certbot log file, available at `/var/log/letsencrypt/letsencrypt.log`

```eval_rst
  .. title:: Certbot SafeDNS Plugin
  .. meta::
    :description: Guidance on using the Certbot SafeDNS to generate certificates.
    :keywords: certbot, safedns, plugin, certificates, https
```
