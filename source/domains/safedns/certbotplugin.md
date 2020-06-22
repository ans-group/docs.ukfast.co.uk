# SafeDNS Authenticator plugin for Certbot

```eval_rst

   .. meta::
      :title: SafeDNS | Authenticator plugin for Certbot | UKFast Documentation
      :description: SafeDNS Authenticator plugin for Certbot

```

## Setup

```bash
apt install certbot python3-pip
pip3 install certbot-dns-safedns
```

## Execution

```bash
certbot certonly --authenticator certbot-dns-safedns:dns_safedns
```

> **Warning**: certbot might tell you that it doesn't have permissions to write to its log file. However, if you run certbot as sudo, you won't have access to the safedns plugin if you didn't install the plugin as sudo.

This will result in the following error from certbot:

```bash
Could not choose appropriate plugin: The requested dns_safedns plugin does not appear to be installed
```

To get around this just do:

```bash
sudo pip3 install certbot-dns-safedns
sudo certbot certonly --authenticator certbot-dns-safedns:dns_safedns
```

If you get any python cryptography errors, such as:

```bash
ContextualVersionConflict: ...
```

just make sure to upgrade your pyopenssl.

```bash
sudo pip install --upgrade pyopenssl
```

### Credentials and Config Options

Use of this plugin requires a configuration file containing SafeDNS API credentials, obtained from your MyUKFast [account page](https://my.ukfast.co.uk/applications/index.php). See also the [SafeDNS API](https://developers.ukfast.io/documentation/safedns) documentation.

An example ``credentials.ini`` file:

```ini
certbot_dns_safedns:dns_safedns_auth_token = 0123456789abcdef0123456789abcdef01234567
certbot_dns_safedns:dns_safedns_propagation_seconds = 20
```

The path to this file can be provided interactively or using the `--certbot-dns-safedns:dns_safedns-credentials` command-line argument. Certbot records the path to this file for use during renewal, but does not store the file's contents.

> **CAUTION:** You should protect these API credentials as you would the password to your MyUKFast account. Users who can read this file can use these credentials to issue arbitrary API calls on your behalf. Users who can cause Certbot to run using these credentials can complete a ``dns-01`` challenge to acquire new certificates or revoke existing certificates for associated domains, even if those domains aren't being managed by this server.

Certbot will emit a warning if it detects that the credentials file can be accessed by other users on your system. The warning reads "Unsafe permissions on credentials configuration file", followed by the path to the credentials file. This warning will be emitted each time Certbot uses the credentials file, including for renewal, and cannot be silenced except by addressing the issue (e.g., by using a command like `chmod 600` to restrict access to the file).

### Examples

To acquire a single certificate for both `example.com` and `*.example.com`, waiting 900 seconds for DNS propagation:

```bash
certbot certonly \
  --authenticator certbot-dns-safedns:dns_safedns \
  --certbot-dns-safedns:dns_safedns-credentials ~/.secrets/certbot/safedns.ini \
  --certbot-dns-safedns:dns_safedns-propagation-seconds 900 \
  --server https://acme-v02.api.letsencrypt.org/directory \
  -d 'example.com' \
  -d '*.example.com'
```

```eval_rst
.. meta::
   :title: Certbot SafeDNS Plugin
   :description: Guidance on using the Certbot SafeDNS to generate certificates.
   :keywords: certbot, safedns, plugin, certificates, https
```
