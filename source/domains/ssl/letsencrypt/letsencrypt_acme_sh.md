# ACME.sh

acme.sh is a simple lets encrypt client written in Unix shell, compared to its counter parts such as the popular Certbot it is much more lightweight on the system and has the ability to be customised, as its a shell script the dependencies are minimal any server running bash, sh or zsh is compatible with this client.

More details on the project can be seen on the official repository [here](https://github.com/acmesh-official/acme.sh).

## Installation

One of the benefits of acme.sh is that it can be run and installed as any system user however it is recommended to install it as root, its important to note that acme.sh does not officially work with sudo (there is a work around for this, but it is not recommended so the first step would be to either sign in as root or escalate privileges with.

```bash
sudo -i
```
Most systems come with git pre-installed but to ensure it is installed we can do the following.

For RHEL based systems (e.g. CentOS, Alma)

```bash
yum install git
```
For Debian based systems (e.g. Ubuntu)

```bash
apt-get install git
```
Now we need to clone the acme.sh repository locally and move into the directory.
```eval_rst
.. note::
    Please note this will clone the repo to your current working directory, you may choose to clone to /tmp so the repo files will automatically be cleared.
```

```bash
git clone https://github.com/acmesh-official/acme.sh.git
cd acme.sh/
```
For next command the following flags can be adjusted to your preference.

- home | This is where acme.sh will be installed including any API plugins.
- config-home | This is where the config files for certificates will be stored (e.g. renewal hooks)
- cert-home | This is where the certificates themselves will be stored.
- accountemail | This will be the address renewal messages will be sent to.

```eval_rst
.. note::
    Its important that the email set for accountemail is a valid address as Lets encrypt will send reminder emails should a certificate not get renewed which is usually an indication of a problem.
```
An example of a install command would look something like this.

```bash
./acme.sh --install --home /etc/acmesh --config-home /etc/ssl/data --cert-home /etc/ssl/certs --accountemail "example@example.com"
```
You will likely see this warning when installing the client.

```
It is recommended to install socat first.
We use socat for standalone server if you use standalone mode.
If you don't use standalone mode, just ignore this warning.
```

This warning only applies if the server you are installing the client on **does not** have a web server (such as NGINX) installed.

The install process will create a bash alias for client for you as well as setting up a cron job to automate the renewal of certificates, once the install is complete there is two final steps before we can issue certificates, first we need to log out and log back in to apply the bash alias then we need to register the Lets encrypt account.

```eval_rst
.. note::
    Its important to ensure that the email used here is the same used to configure acme.sh with.
```

```bash
acme.sh --register-account -m example@example.com
```

## Issuing a certificate

There a couple of different options that acme.sh supports for issuing certificates below we will cover the main three webroot, Apache and NGINX, acme.sh also supports a number of APIs from many different providers more information on these can be seen [here](https://github.com/acmesh-official/acme.sh/wiki/dnsapi).

## Webroot

Webroot verification involves placing a verification file in the document root of the site, this it then polled by the CA to verify your control over the domain and issue the certificate, normally with paid certificates this is a manual process however acme.sh takes care of this all automatically.

For webroot verification you will need to know the document root of your site, you can usually find this information from your webserver config files, although commonly they found in the /var/www directory.

Once we know where the document root is we can begin with issuing certificates.

For securing a standard website with www. and non-www.

```eval_rst
.. note::
    Replace <webserver> with the webserver you are using this will likely be NGINX or Apache this ensures the service is restarted when the certificate is renewed.
    apache's service name also changes depending on the OS it is installed on for Debian (e.g. Ubuntu) systems this is apache2, for RHEL (e.g. Alma) this is httpd.
```

```bash
acme.sh --issue -d example.com -d www.example.com -w /path/to/doc/root --reloadcmd "systemctl reload <webserver>"
```

For a single subdomain you can use the following example.

```bash
acme.sh --issue -d test.example.com -w /path/to/doc/root --reloadcmd "systemctl reload <webserver>"
```
## NGINX

acme.sh also has a NGINX mode this will only work if you are **currently** running NGINX on port 80

For securing a standard website with www. and non-www.

```bash
acme.sh --issue -d example.com -d www.example.com --nginx --reloadcmd "systemctl reload nginx"
```
For a single subdomain you can use the following example.

```bash
acme.sh --issue -d test.example.com --nginx --reloadcmd "systemctl reload nginx"
```

## Apache
acme.sh also has a Apache mode this will only work if you are **currently** running Apache on port 80

For securing a standard website with www. and non-www.

On RHEL based systems (e.g. CentOS, Alma)

```bash
acme.sh --issue -d example.com -d www.example.com --apache --reloadcmd "systemctl reload httpd"
```
On Debian based systems (e.g. Ubuntu)

```bash
acme.sh --issue -d example.com -d www.example.com --apache --reloadcmd "systemctl reload apache2"
```
For a single subdomain you can use the following example.

On RHEL based systems (e.g. CentOS, Alma)

```bash
acme.sh --issue -d test.example.com --apache --reloadcmd "systemctl reload httpd"
```

On Debian based systems (e.g. Ubuntu)

```bash
acme.sh --issue -d test.example.com --apache --reloadcmd "systemctl reload apache2"
```

```eval_rst
  .. title:: SSL | How to install and use acme.sh
  .. meta::
     :title: SSL | How to install and use acme.sh | UKFast Documentation
     :description: How to install and use acme.sh
     :keywords: ssl, acme.sh, letsencrypt, let's encrypt, secure, security, linux, server, guide, tutorial
```
