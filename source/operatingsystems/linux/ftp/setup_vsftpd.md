# VSFTPd

## What is VSFTPd?

VSFTPd stands for Very Secure File Transfer Protocol.

It is a Linux FTP application that is used to transfer files between computers using an FTP client such as FileZilla, and by default, the port used is port 21.

## Adding users for FTP usage

In order to create an account that can use VSFTPd, you will first need to set up a user on the server that you want to transfer files to and from.

The first step is to add a user. This can be done using the `useradd` command, as shown below:

```bash
useradd guest
```

Once you have added a user, you will want to make that account secure by adding a password. Using the `passwd` command and then specifying a user, you will then be prompted to add/change the password for the given user:

```bash
passwd guest
```

## Add attributes to the user

Now that you have added a user, you will want to change the attributes of that user so they have the correct permissions to use VSFTPd. Using the `usermod` command, the below command changes the shell for the user so that they cannot log into the server via SSH:

```bash
usermod -s /sbin/nologin guest
```

Note, this can also be achieved by editing the `/etc/passwd` file.

## VSFTPd configuration

With your FTP user configured, you will want to ensure that the configuration file for VSFTPd is correct.

The configuration file for VSFTPd can be found at `/etc/vsftpd/vsftpd.conf`. You will want to edit this file to contain the configuration displayed below:

```console
pam_service_name=vsftpd
userlist_enable=YES
tcp_wrappers=YES
anonymous_enable=NO
chroot_local_user=YES
rsa_cert_file=/etc/ssl/private/vsftpd.pem
rsa_private_key_file=/etc/ssl/private/vsftpd.pem
ssl_enable=YES
allow_anon_ssl=NO
force_local_data_ssl=YES
force_local_logins_ssl=YES
ssl_tlsv1=YES
ssl_sslv2=NO
ssl_sslv3=NO
require_ssl_reuse=NO
ssl_ciphers=HIGH
pasv_enable=YES
pasv_min_port=8443
pasv_max_port=8443
allow_writeable_chroot=YES
```

Note, this configuration was tested on CentOS 7.

```eval_rst
  .. title:: VSFTPD
  .. meta::
     :title: VSFTPD
     :description: A guide on what vsftpd is and how to set up an account
     :keywords: vsftpd, linux, ftp, users, setup, transfer, file, protocol
```
