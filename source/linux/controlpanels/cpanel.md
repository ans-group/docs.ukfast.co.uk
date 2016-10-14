# cPanel

## Overview

If a server is said to have cPanel installed on it, there are two distinct parts:

* WHM
* cPanel

WHM is the top level control panel that allows you to create user accounts (domains) and manage server level options.

cPanel is for site management and controls things such as mailboxes and site specific variables.

## Connecting

If cPanel/WHM is installed, you can access the various parts in the following locations:

* WHM

```console
  https://ip.ip.ip.ip:2087
```

* cPanel

```console
  https://ip.ip.ip.ip:2083
```

WHM will require you to use your server's root credentials for access.

Logging into cPanel will require a set of account credentials that you created through WHM.

```eval_rst
.. note::
   The first time you access this, it will likely show a certificate warning that varies depending on which browser you're using.

   This is nothing to be worried about, it's just that cPanel uses a self-signed certificate to encrypt traffic.
```

It is also possible to use WHM to connect directly to any accounts cPanel without need for their credentials using the following method:

![cPanel Login](cPanellogin.png)

1. Find the 'List Accounts' page in the navigation pane on the left
2. Press the 'cP' logo next to the domain you want to access

## Further Documentation

Describing individual cPanel issues is beyond the scope of a page such as this due to the constant changes brought to cPanel.

cPanel maintain exhaustive usage and troubleshooting guides here:

<https://documentation.cpanel.net>
