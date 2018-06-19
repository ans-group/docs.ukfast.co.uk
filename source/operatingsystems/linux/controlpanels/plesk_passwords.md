# Recovering the Plesk admin password

If you ever forget or lose your Plesk admin password, you can always log in and recover access to your Plesk panel by one of the following methods.

## Plesk 10 and older

In these old versions, the password is stored in plaintext in the following location and can be easily viewed by logging into SHH as root and viewing the file:

``#
  cat /etc/psa/.psa.shadow
``

## Plesk 11 - 12.5

In these versions, the psa.shadow file still exists, but it now contains a hash of the password, which is more secure.

To see the password in plaintext, both of the following commands should work:

``#
  /usr/local/psa/bin/admin --show-password
``

``#
plesk bin admin --show-password
``

## Plesk Onyx (17+)

To improve security, Plesk Onyx removed the ability to easily retrieve the admin password in plain text. However, they implemented a couple of new functions to work around a lost password. Firstly you can generate a one-time login link that will let your access your panel without the password:

``#
plesk login
``

That should allow you to log in and manage your panel, although it will not allow you to change the password. If you cannot find your old password, while you cannot retrieve the password you can reset it using another command.

```eval_rst
.. note::
   Bear in mind you are resetting your password using a shell command, so we recommend avoiding using special characters like & or $ which the shell might try to interpret! If you want to have these characters in your password you can always change it again in the Plesk panel once you're able to log in.
```

The command to reset the admin password is as follows:

``#
plesk bin admin --set-admin-password -passwd "**********"
``

If you still have trouble, you can also raise a ticket to our support team and we'll assist you.


```eval_rst
  .. meta::
     :title: Retrieving your Plesk password on Linux | UKFast Documentation
     :description: A guide to retrieving your Plesk password on Linux servers
     :keywords: ukfast, plesk, password, get, retrieve, cloud, server, shadow
