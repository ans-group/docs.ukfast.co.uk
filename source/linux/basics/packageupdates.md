# Package Installs and Updates

As most UKFast servers are either CentOS/RedHat or Ubuntu/Debian, this article will only cover two of the most popular Linux package managers, `yum` and `apt`.

## yum

### Installing Packages

To install a package in yum, the following syntax can be used:

```console
   yum install $PACKAGE_NAME
```

This will search the currently installed repositories for a package with that name and install it if it's found.

If the package you're looking for isn't found, then you may have to install an additional repository that does provide it.

A common additional repository is `epel` (Extra Packages for Enterprise Linux).

On CentOS, this can itself be installed using yum:

```console
   yum install epel-release
```

If you're using official RedHat Enterprise Linux, you will need to download the RPM from the EPEL site and install it manually, as well as enabling packages in the 'optional' RHEL repo. More instructions can be found [here](https://fedoraproject.org/wiki/EPEL)

With this installed, we can then install additional utilities on our server that were previously unavailable:

```console
   yum install htop
```

### Updating Packages

```eval_rst
.. note::
   In all these examples, the update command will be used rather than upgrade.
   Both commands look to perform the same function, but upgrade will remove packages that it classifies as obsolete as part of the upgrade process.
   If you're confident in what you're removing or drive space is at a premium then this option can be used instead.
```

The update syntax for yum is similar to the install syntax:

```console
   yum update $PACKAGE_NAME
```   

If it's just one package that needs to be updated then the above syntax is fine, for example:

```console
   yum update httpd
```

If you're looking to update all the packages on your server, simply run the command without a package name:

```console
   yum update
```

```eval_rst
.. warning::

   Take care when updating all the packages on a server, this isn't something that should be done blindly.
   Review the packages that are going to update before accepting it.
   Failure to review package updates could result in you running a higher version of something critical (such as PHP) than your code supports.
```

## apt


### Installing Packages

To install a package with `apt` you should first update the apt cache, then install your desired package:

```console
   apt-get update
   apt-get install $PACKAGE_NAME
```

Updating the cache first is important as this will ensure you get the latest available packages and security updates.

### Updating Packages

As with installing, you should ensure your apt cache is up to date so you get the latest software updates and security patches.

```console
   apt-get update
   apt-get upgrade
```

This will pull in all available updates for your system. Sometimes you may find that packages have been held back (usually Linux kernel updates). These can be pulled in by running a `dist-upgrade`.

```console
   apt-get dist-upgrade
```

```eval_rst
.. warning::

   Take care when updating all packages on a server. This is not something which should be done blindly. Review the packages that are going be updated before accepting the upgrade. If you fail to review the packages you may end up installing, e.g., a new major version of MySQL or PHP which is not going to be compatible with your code.
```
