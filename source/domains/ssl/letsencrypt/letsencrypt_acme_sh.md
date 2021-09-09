# ACME.sh

acme.sh is a simple lets encrypt client written in Unix shell, compared to its counter parts such as the popular Certbot it is much more lightweight on the system and has the ability to be customised, as its shell script the dependencies are minimal any server running bash, sh or zsh is compatible with this script.

More details on the project can be seen on the offcial repository [here](https://github.com/acmesh-official/acme.sh).

## Installation

One of the benifits of acme.sh is that it can be run and installed as any system user however it is recomended to install it as root, its important to note that acme.sh does not offically work with sudo so the first step to su up to the servers root account.

```bash
sudo -i
```
Most systems come with git pre-installed on them but to ensure it is we can do the following.

For RHEL based systems (e.g. centOS, Alma)

```bash
yum install git
```
For Debian based systems (e.g. ubuntu)

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

- home | This is where acme.sh will be installed includeing any api plugins.
- config-home | This is where the configs for certificates will be store (e.g. renewal hooks)
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


## Issuing a certificate

##  Additional options

```eval_rst
  .. title:: SSL | How to install and use acme.sh
  .. meta::
     :title: SSL | How to install and use acme.sh | UKFast Documentation
     :description: How to install and use acme.sh
     :keywords: ssl, acme.sh, letsencrypt, let's encrypt, secure, security, linux, server, guide, tutorial
```
