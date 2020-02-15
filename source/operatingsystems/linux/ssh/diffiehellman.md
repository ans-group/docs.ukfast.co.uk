# SSH Diffie-Hellman

### moduli of 2048 bits or greater
Take a copy of /etc/ssh/moduli and /etc/ssh/sshd_config file first

```bash
cp /etc/ssh/moduli /etc/ssh/moduli.backup
cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup
```

Delete lines from /etc/ssh/moduli where the 5th column is less than 2000.

```bash
awk '$5 > 2000' /etc/ssh/moduli > /usr/src/moduli
mv "/usr/src/moduli" /etc/ssh/moduli
```

### Diffie-Hellman
Add the following ‘KexAlgorithms’ in /etc/ssh/sshd_config
```bash
KexAlgorithms ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1,diffie-hellman-group-exchange-sha256
```

### Restart SSH service on the server
```bash
systemctl restart sshd
```

```eval_rst
  .. meta::
     :title: Using SSH Diffie-Hellman | UKFast Documentation
     :description: A guide to using SSH Diffie-Hellman
     :keywords: ukfast, linux, ssh, keys, generation, keys, revoking, security, Diffie-Hellman
