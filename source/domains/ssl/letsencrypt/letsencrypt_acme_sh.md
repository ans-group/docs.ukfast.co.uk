# ACME.sh

acme.sh is a simple lets encrypt client written in Unix shell, compared to its counter parts such as the popular Certbot it is much more lightweight on the system and has the ability to be customised, as its shell script the dependencies are minimal any server running bash, sh or zsh is compatible with this script.

More details on the project can be seen on the official repository [here](https://github.com/acmesh-official/acme.sh).

## Installation

One of the benefits of acme.sh is that it can be run and installed as any system user however it is recommended to install it as root, its important to note that acme.sh does not officially work with sudo so the first step would be to either sign in as root or escalate our privileges with.

```bash
sudo -i
```
Most systems come with git pre-installed on them but to ensure it is we can do the following.

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
    Please note this clone the repo to your currenly working directory, you may choose to clone to /tmp so the repo files will automatically be cleared.
```

```bash
git clone https://github.com/acmesh-official/acme.sh.git
cd acme.sh/
```
The next command the following flags can be adjusted to your preference.

- home | This is where acme.sh will be installed including any API plugins.
- config-home | This is where the config files for certificates will be stored (e.g. renewal hooks)
- cert-home | This is where the certificates themselves will be stored.
- accountemail | This will be the address renewal messages will be sent.

```eval_rst
.. note::
    Its important that the email set for accountemail is a valid address as Lets encrypt will sent reminder emails should a certificate not get renewed.
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

The install process will create an alias to the client for you as well as setting up a cron job to automate the renewal of certificates for you, once the install is complete there is two final steps before we can issue certificates, first we need to log out and log back in to apply the command alias then we need to register the Lets encrypt account.

```eval_rst
.. note::
    Its important to ensure that the email used here is the same used to configure acme.sh with.
```

```bash
acme.sh --register-account -m example@example.com
```

## Issuing a certificate

There a couple of different options that acme.sh supports for issuing certificates below we will cover the main three webroot, apache and nginx, acme.sh also supports a number of APIs from many different providors more information on these can be seen [here](https://github.com/acmesh-official/acme.sh/wiki/dnsapi).

### Webroot



##  Additional options

```eval_rst
  .. title:: SSL | How to install and use acme.sh
  .. meta::
     :title: SSL | How to install and use acme.sh | UKFast Documentation
     :description: How to install and use acme.sh
     :keywords: ssl, acme.sh, letsencrypt, let's encrypt, secure, security, linux, server, guide, tutorial
```
