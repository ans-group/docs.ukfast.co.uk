# Brute Force Attacks

### What is a brute force attack?

Brute forcing is when an attacker submits lots of password attempts in quick succession with the aim of guessing a password correctly and gaining access. This can be either random words or using "dictionaries" that contain passwords that are commonly used. 

It's very common, and not typically a very effective type of attack, but the sheer number of these requests can sometimes contribute to load issues. Moreover, much of the time these requests will be automatically sent by numerous bots, so blocking the origin IPs is only a short-term resolution.

### Wordpress 

On wordpress, there are two files that are targeted commonly for brute forcing:

- wp-login.php - The default wordpress login page
- xmlrpc.php - A protocol used historically with wordpress to enable communication between wordpress and other systems. It's enabled by default, but has largely been superseded by REST API, so in most cases it can be disabled without harm. 

 We recommend:

- Using strong and unique passwords for accounts 

- Using a [Web Application Firewall](/security/webapplicationfirewall/index) or security plugin such as [Wordfence](https://www.wordfence.com/) 

- Using our [Threat Vision](https://www.ukfast.co.uk/intrusion-detection-response.html) service.
- 
- Locking down wp-login [to select IPs](https://wordpress.org/support/article/brute-force-attacks/#limit-access-to-wp-login-php-by-ip)

- Disabling xmlrpc.php:

Apache:

```console
<Files xmlrpc.php>
Order Allow,Deny
Deny from all
</Files>
```

Nginx:

```console
location ~* ^/xmlrpc.php$ {
return 403;
}
```

Wordpress also have a [great guide](https://wordpress.org/support/article/brute-force-attacks/) on how to mitigate these attacks.

### Other types of brute forcing

It's also possible for brute forces to occur over any protocol that allows a login and is open over the internet, for example, SSH, cPanel/Plesk, FTP.

As such, for any services that require a login we'd recommend locking down the ports in your [firewall](https://docs.ukfast.co.uk/network/firewalls/index.html) so that only you can access them.

