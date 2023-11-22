# Brute Force Attacks

### What is a brute force attack?

Brute forcing is when an attacker submits lots of password attempts in quick succession with the aim of guessing a password correctly and gaining access. This can be either random words or using "dictionaries" that contain passwords that are commonly used.

It's very common, and not typically a very effective type of attack, but the sheer number of these requests can sometimes contribute to load issues.

### Types of brute forcing

It's possible for brute forces to occur over any protocol that allows a login and is open over the internet, for example, WordPress sites, any other sites with an admin page, SSH, cPanel/Plesk, and FTP.

### WordPress

WordPress is a common target of these attacks due to it's popularity. On WordPress, there are two files that are typically targeted for brute forcing:

- `wp-login.php` - The default WordPress login page
- `xmlrpc.php` - A protocol used historically with WordPress to enable communication between WordPress and other systems. It's enabled by default, but has largely been superseded by REST API, so in most cases it can be disabled without harm.

WordPress have a [great guide](https://wordpress.org/support/article/brute-force-attacks/) on how to mitigate these attacks specifically for this platform.

### How to spot a brute force attack

A brute force attack will leave behind lots of log entries of failed attempts. For example, with `xmlrpc.php` as mentioned above, in the web server access logs you'll see a large number of requests such as the below:

```console
X.X.X.X - - [25/Jul/2021:01:48:21 +0100] "POST //xmlrpc.php HTTP/1.1" 200 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
```

Alternatively, in the server authorisation logs (`/var/log/secure` or `/var/log/auth.log`), you may see lots of entries such as:

```console
Jul 28 18:48:22 78 sshd[19900]: Failed password for root from X.X.X.X port 47894 ssh2
```

Both of the above indicate that login attempts are being made, so if there are high quantities it's likely this is brute forcing.

### Protecting against attacks

You can block the IP addresses sending these requests, but this isn't an effective solution in the long-term as the requests are usually automated and will originate from various different IPs.

We recommend:

- Using strong and unique passwords for accounts

- Using a [Web Application Firewall](/security/webapplicationfirewall/index) or security plugin such as [Wordfence](https://www.wordfence.com/)

- Using our [Threat Vision](https://www.ukfast.co.uk/intrusion-detection-response.html) service

- For server-level services such as SSH and FTP, we'd recommend locking down the ports in your [firewall](/docs/network/firewalls/index.html) so that only you can access them. This removes the attack vector entirely as they can no longer attempt to login.

- For WordPress or site-level attacks, we'd recommend locking down `wp-login` [to select IPs](https://wordpress.org/support/article/brute-force-attacks/#limit-access-to-wp-login-php-by-ip), and disabling `xmlrpc.php`:

Apache:

```console
<Files xmlrpc.php>
  Order Allow,Deny
  Deny from all
</Files>
```

NGINX:

```console
location ~* ^/xmlrpc.php$ {
  return 403;
}
```

```eval_rst
   .. title:: Brute Force Attacks
   .. meta::
      :description: Basic overview on what brute force attacks are, how to identify and mitigate them
      :keywords: ukfast, linux, security, WordPress, brute, force, password, login
```
