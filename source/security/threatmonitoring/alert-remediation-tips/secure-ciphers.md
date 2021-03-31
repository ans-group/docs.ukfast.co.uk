# Setting Secure Ciphers

Ciphers and Key Exchange Algorithms are used by many applications to ensure that the connection between the server and the user is adequately secured. As computers become faster and more equipped, they are more capable of breaking older ciphers and encryption algorithms, and as such those ciphers become obsolete. This is why it's important to ensure that we're using that latest and greatest ciphers, where possible.

A great list of up-to-date strong ciphers can be found here: <https://syslink.pl/cipherlist/>

Follow the below steps to set secure ciphers for web servers like Apache, NGINX and other services like SSH.

## Web Servers

### Apache

**RHEL/CentOS**

Make a backup of the Apache config file `/etc/httpd/conf.d/ssl.conf`

```bash
cp /etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/ssl.conf.backup
```

Edit the Apache config file in `/etc/httpd/conf.d/ssl.conf` with your preferred editor.

```bash
vi /etc/httpd/conf.d/ssl.conf
```

Comment any lines that start with any of the following. This will disable your old insecure ciphers:

* `SSLCipherSuite`
* `SSLProtocol`
* `SSLHonorCipherOrder`
* `Header`
* `SSLCompression`
* `SSLUseStapling`
* `SSLStaplingCache`
* `SSLSessionTickets`

Next, append the latest ciphers from <https://syslink.pl/cipherlist/> to the bottom of the file. This will enable the more secure ciphers. For example:

```nginx
SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH
SSLProtocol All -SSLv2 -SSLv3 -TLSv1 -TLSv1.1
SSLHonorCipherOrder On
Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"
Header always set X-Frame-Options DENY
Header always set X-Content-Type-Options nosniff
# Requires Apache >= 2.4
SSLCompression off
SSLUseStapling on
SSLStaplingCache "shmcb:logs/stapling-cache(150000)"
# Requires Apache >= 2.4.11
SSLSessionTickets Off
```

Save the file

Restart the Apache webserver.

```bash
service httpd restart
```

---

**Debian/Ubuntu**

The process is exactly the same as for RHEL/CentOS except that the path to the config file is different. So, follow the steps above but change the path `/etc/httpd/conf.d/ssl.conf` to be `/etc/apache2/mods-available/ssl.conf` instead.

To restart the Apache webserver, use this command:

```bash
service apache2 restart
```

### NGINX

In NGINX, we need can specify ciphers to the virtual host you wish to secure. These are commonly `.conf` files found in the directory `/etc/nginx/conf.d`, with one for each of your websites.

To specify secure ciphers for these virtual hosts, we can add the latest ciphers from <https://syslink.pl/cipherlist/> to our host, as shown below:

```nginx
server {

    server_name my.website.com;
    listen 443 ssl http2;

        ssl_protocols TLSv1.3;# Requires nginx >= 1.13.0 else use TLSv1.2
        ssl_prefer_server_ciphers on;
        ssl_dhparam /etc/nginx/dhparam.pem; # openssl dhparam -out /etc/nginx/dhparam.pem 4096
        ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384;
        ssl_ecdh_curve secp384r1; # Requires nginx >= 1.1.0
        ssl_session_timeout  10m;
        ssl_session_cache shared:SSL:10m;
        ssl_session_tickets off; # Requires nginx >= 1.5.9
        ssl_stapling on; # Requires nginx >= 1.3.7
        ssl_stapling_verify on; # Requires nginx => 1.3.7
        resolver $DNS-IP-1 $DNS-IP-2 valid=300s;
        resolver_timeout 5s;
        add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;
        add_header X-XSS-Protection "1; mode=block";

}
```

## SSH

We can also set secure ciphers for SSH sessions. This will ensure a secure connection is made whenever a server administrator connects to the server via SSH.

Follow the below commands to set secure ciphers for SSH.

Edit the SSH config file `/etc/sshd/sshd_config` with your preferred editor.

```bash
vi /etc/sshd/sshd_config
```

Next, append the latest ciphers from <https://syslink.pl/cipherlist/> to the bottom of the file, like shown

```nginx
# Example of overriding settings on a per-user basis
#Match User anoncvs
#       X11Forwarding no
#       AllowTcpForwarding no
#       PermitTTY no
#       ForceCommand cvs server

Protocol 2
HostKey /etc/ssh/ssh_host_ed25519_key
HostKey /etc/ssh/ssh_host_rsa_key
KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-exchange-sha256
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com
```

Save the file.

Restart the SSH Server service.

```bash
service sshd restart
```

```eval_rst
   .. title:: Setting Secure Ciphers
   .. meta::
      :title: Setting Secure Ciphers | UKFast Documentation
      :description: Useful threat remediation and prevention tips
      :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up
```
