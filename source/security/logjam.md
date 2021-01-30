# The Logjam attack

The Logjam attack is based on a weakness found in the [Diffie-Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) (DH) key exchange method. By using Logjam, an attacker can force an otherwise secure connection to be downgraded to a vulnerable one, which they can easily break.

Fortunately, there are a few ways we can mitigate against this attack.

## General guidance

Firstly, you should disable ["export"](https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States#PC_era) ciphers. Most browsers don't use these any more, as they're known to be vulnerable. The attack relies on these weak ciphers being available, so if they're disabled, the attack fails. While changing your available cipher suites to exclude export ciphers, consider looking at [moving to a modern configuration](https://mozilla.github.io/server-side-tls/ssl-config-generator/).

Without going into the maths, DH is based on the exchange of large prime numbers. The larger the number, the harder the encryption is to break. Currently, numbers larger than 1028 bits are considered safe. If you make sure to use only numbers of 2048 bit or higher, the attack should fail.

## Plesk 12.5+
Plesk 12.5 and higher provide a [single script](https://docs.plesk.com/en-US/12.5/advanced-administration-guide-linux/pci-dss-compliance/tune-plesk-to-meet-pci-dss-on-linux.65871/) to manage encryption, server-wide. To ensure you're using the encryption settings recommended by Plesk, run following command:
```console
   plesk sbin pci_compliance_resolver --enable
```

Alternatively, if you wish to address the Logjam attack only without changing other settings:
```console
   plesk sbin sslmng --strong-dh
```

## Generating new Strong DH groups on with OpenSSL

To generate a new set of prime numbers for DH to use, run the following command. Please note that generating large prime numbers is a fairly intensive task, so where possible avoid running this on a live server already under high load:
```console
openssl dhparam -out dhparams.pem 2048
```

## Apache

The parameters to change are:
```console
SSLCipherSuite At least add :!EXPORT, if possible use a modern configuration.
SSLHonorCipherOrder on
```

## NGINX

The parameters to change are:
```console
ssl_ciphers At least add :!EXPORT, if possible use a modern configuration.
ssl_prefer_server_ciphers on;
ssl_dhparam /path/to/dhparams.pem;
```

## OpenSSH

Add KexAlgorithms to `sshd_config` to avoid algorithms that use DH key exchange with weak keys:
```console
KexAlgorithms curve25519-sha256@libssh.org, diffie-hellman-group-exchange-sha256
```

Change the existing moduli so 1024 bit keys are not available:
Remove all DH moduli < 2048
```console
awk '$5 > 2000' /etc/ssh/moduli > ~/moduli
```

Check new file looks OK, and doesn't have any 1024 bit keys, then if it's good, copy it into place:
```console
mv ~/moduli" /etc/ssh/moduli
```

Or generate new ones from scratch. This is more computationally expensive, but gives you all new keys:
```console
ssh-keygen -G moduli.candidates -b 2048 (or 4096 if you're paranoid)
ssh-keygen -T moduli.safe -f moduli.candidates
mv moduli.safe /etc/ssh/moduli
```

## Testing

There are external web-based testers such as [this one from KeyCDN.com](https://tools.keycdn.com/logjam).

```eval_rst
.. warning::
    UKFast is not responsible for the performance of 3rd party software or testing tools.
```

## Further external reading

[Imperfect Forward Secrecy: How Diffie-Hellman Fails in Practice](https://weakdh.org/imperfect-forward-secrecy-ccs15.pdf)

[Weak Diffie-Hellman and the Logjam Attack](https://weakdh.org/)

[The Logjam Attack: What You Need to Know](https://blog.malwarebytes.com/101/2015/05/the-logjam-attack-what-you-need-to-know/)


```eval_rst
   .. title:: Logjam attack
   .. meta::
      :title: Logjam attack | UKFast Documentation
      :description: How to prevent Logjam attacks based on weak Diffie-Hellman key exchange
      :keywords:  logjam, SSL, TLS, attack, attacks, log, jam, deffie hellman
```
