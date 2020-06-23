# Setting up SSH keys

A more secure way of accessing a server via SSH than password authentication is to use SSH keys. Each user on a server can have a public and private key pairing. To gain password-less access to a remote server, simply add your local public key to the authorized_keys file on the remote server you wish to access. This is explained in further detail below.

```eval_rst
.. note::
   The command '~/' is used often here. This is simply a shortcut to the path '/home/user/'
``` 

## Generating Keys

The command `ssh-keygen` will generate a pair of public and private keys for your user. You should see a prompt similar to the below. A passphrase is not necessary, but if entered you will have to enter this passphrase when logging into a remote server using this public key. 

```console
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/dave/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/dave/.ssh/id_rsa.
Your public key has been saved in /home/dave/.ssh/id_rsa.pub.
The key fingerprint is:
ef:69:3b:9e:3b:2d:99:0d:ac:57:4e:b2:92:82:bd:9f dave@hostname
The key's randomart image is:
+--[ RSA 2048]----+
|                 |
|                 |
|                 |
|                 |
|        S.       |
|         .+ o    |
|     o   o.%     |
|    . o +oXo+    |
|      .+E=B*     |
+-----------------+
```

## Copying Key to Remote Server

Once complete, you can either manually add the contents of the `~/.ssh/rsa.pub` file to the file `~/.ssh/authorized_keys` file on the remote server, or use the `ssh-copy-id` command, shown below.

```console
$ ssh-copy-id root@1.2.3.4
/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
root@192.168.0.70's password:

Number of key(s) added: 1
```

Now try logging into the machine, with:   `ssh 'root@1.2.3.4'`
and check to make sure that only the key(s) you wanted were added.


You should now be able to log into the remote server, here `root@1.2.3.4`, without being prompted for a password (unless you added a passphrase to your key).


## Disabling Password Authentication

You may also now wish to disable password authentication on your server. This is done simply by modifying the `/etc/ssh/sshd_config` file, and amending the line below.

```console
PasswordAuthentication no
```
The SSH service will then need restarting using the appropriate command for your distribution. For most systems this can be done with the command `sudo service sshd reload`.

You can also disable password authentication for the root user only, or disable root logins altogether by setting the following in the same file.

This will enable root login with SSH keys only:

```console
PermitRootLogin without-password
```

Disables root login completely

```console
PermitRootLogin no
```


## Revoking a Key

To revoke access for a user, simply remove the relevant public key from the file `~/.ssh/authorized_keys`. Keys are appended with a comment `user@host` by default to help you identify them. Any text following the key and a space is treated as a comment, which can be modified. Comments can also be modified on key creation, see `man ssh-keygen` for more details.

```eval_rst
  .. title:: Using SSH keys with Linux | UKFast Documentation
  .. meta::
     :title: Using SSH keys with Linux | UKFast Documentation
     :description: A guide to using SSH keys with Linux
     :keywords: ukfast, linux, ssh, keys, generation, keys, revoking, security
