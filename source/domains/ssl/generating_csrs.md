# How to Generate a CSR File

```eval_rst
   .. title:: SSL | Generating a CSR
   .. meta::
      :title: SSL | Generating a CSR | ANS Documentation
      :description: Generating a CSR
```
This guide will help you generate a Certificate Signing Request (CSR) on different operating systems.

## Pre-requisite reading

On SSL certificates that protect a single hostname/domain, your primary hostname is the hostname/domain you have chosen.

For multi-domain SSL certificates, the primary hostname is the first hostname that
is listed on your SSL certificate inside [ANS Glass](https://portal.ans.co.uk/ssl/index.php).

You should also ensure to make sure your key and CSR are in a safe folder, as you'll need the the key
to install the SSL certificate and the CSR to generate your SSL Certificate.

## Generate a CSR on Linux

First, check if OpenSSL is installed:

```shell
openssl version
```

If OpenSSL is not installed, you will see an error message. In that case, install OpenSSL:

#### Ubuntu

```shell
sudo apt install openssl
```

#### RHEL/AlmaLinux

```shell
sudo yum install openssl
```

Now you can generate the CSR. You need to replace `yourhostname` with your primary hostname (Common Name)
that the SSL will protect.

```shell
openssl req -new -newkey rsa:2048 -nodes -keyout /path/to/yourhostname.key -out /path/to/yourhostname.csr
```

## Generate a CSR on Windows

1. Open `IIS Manager`.
1. Select the server in the `Connections` pane.
1. Double-click the `Server Certificates` icon.
1. Click the `Create Certificate Request` link in the Actions pane.
1. Fill out the `Distinguished Name Properties` form with the required information (`Common Name` (primary hostname), `Organization`, `City/locality`, `State/province`, `Country/region`).
1. Set the `Cryptographic Service Provider Properties` (Microsoft RSA SChannel Cryptographic Provider and a bit length of 2048).
1. Create a file name for your CSR and click the Finish button.
