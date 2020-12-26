# Package Management Functions

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

### Extra functions

You can always run a number of checks with yum before either installing or updating an application.

If you wish to check whether a package is available on your system, you can always run a search in yum. This will print out all the packages that match your search:

```console
   yum search $QUERY
```

An example of this, including a snippet of the output, is as follows:

```console
   yum search php

   ...
   =============================== N/S matched: php ===============================
   php.x86_64 : PHP scripting language for creating dynamic web sites
   php-Assetic.noarch : Asset Management for PHP
   php-EasyRdf.noarch : A PHP library designed to make it easy to consume and
                      : produce RDF
   ...
```

If the package exists on your system, you can pull additional information on it, including what version of the package is available to you.

```eval_rst
.. note::

   This will also show you information on an updated version of the package you've got.
   It also highlights the package's name in a different collour based on its status.

   Red: Obsolete
   yellow: Installed from another source
   bold white: Currently installed
   white: Available, but not installed
   blue: Update
```

```console
   yum info $PACKAGE_NAME
```

Here is an example, including a snippet of the output, without colour highlights:

```console
   yum info php70w

   ...
   Installed Packages
   Name        : **php70w**
   Arch        : x86_64
   Version     : 7.0.11
   Release     : 1.w7
   Size        : 9.0 M
   Repo        : installed
   From repo   : webtatic
   ...
   Available Packages
   Name        : **php70w**
   Arch        : x86_64
   Version     : 7.0.12
   Release     : 1.w7
   Size        : 2.8 M
   Repo        : webtatic/x86_64
   ...
```

Yum also has great history features that allow you to examine your previous installations and roll them back if necessary.

To view the history of your yum transactions, run `yum history list`, which will output something like:

```console
[root@7dd0ac475f64 /]# yum history
Loaded plugins: fastestmirror, ovl
ID     | Command line             | Date and time    | Action(s)      | Altered
-------------------------------------------------------------------------------
     4 | groupinstall development | 2017-10-24 09:20 | I, U           |  109 EE
     3 | install vim-enhanced     | 2017-10-24 09:19 | Install        |   33 EE
     2 | -y remove bind-libs bind | 2017-08-01 17:24 | Erase          |   35 E<
     1 |                          | 2017-08-01 17:23 | Install        |  178 >
history list
```

In the above example, if you had finished with the packaged you installed in transaction 4, you could then remove those by running `yum history undo 4`. If you wished to rollback your server to transaction 2, you could run `yum history rollback 2` which would remove packages installed in transactions 3 and 4.

You can get more information about this powerful feature by running `yum help history` or viewing the yum man page (`man yum`).

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
   or
   aptitude update
   aptitude upgrade
```

This will pull in all available updates for your system. Sometimes you may find that packages have been held back (usually Linux kernel updates). These can be pulled in by running a `dist-upgrade`.

```console
   apt-get dist-upgrade
   or
   aptitude full-upgrade
```

If you wish to view which version you're upgrading to and from you can always enable verbosity with the '-V' option

```console
   apt-get -V upgrade|dist-upgrade
   or
   aptitude -V upgrade|full-upgrade
```

```eval_rst
.. warning::

   Take care when updating all packages on a server. This is not something which should be done blindly. Review the packages that are going be updated before accepting the upgrade. If you fail to review the packages you may end up installing a new major version of a package which is not going to be compatible with your code, e.g. MySQL or PHP.
```

### Extra Functions

With apt, there are 2 ways to perform a search for packages, but viewing package info applies the same to both methods.

```console
   apt-cache search $QUERY
```

This will display all packages that have matches based on name, summary, and full description.

If you only want package and summary searches, you can run the following:

```console
   aptitude search $QUERY
```

Here are some examples and their outputs:

```console
   apt-cache search php

   ...
   adminer - Web-based database administration tool
   air-quality-sensor - user space driver for AppliedSensor's Indoor Air Monitor
   ampache - web-based audio file management system
   ampache-common - web-based audio file management system common files
   ampache-themes - Themes for Ampache
   aolserver4-doc - AOL web server version 4 - documentation
   ...

   aptitude search php

   ...
   p   cakephp               - MVC rapid application development framework for PHP
   p   cakephp-instaweb      - Development webserver for CakePHP applications
   p   cakephp-scripts       - MVC rapid application development framework for PHP (scripts)
   p   dh-make-php           - Creates Debian source packages for PHP PEAR and PECL extensions
   p   dh-php5               - debhelper add-on to handle PHP PECL extensions
   ...
```

With aptitude searches, they show information about the installation status of a package.

 - 'p' shows that the package is available, but not installed.
 - 'v' shows that this is a virtual package, i.e. it's provided by another package.
 - 'i' shows that the package is installed.
 - 'c' shows that the package was removed, but the configuration still remains

If an 'A' is visible, it shows that this was automatically installed as a dependency to another package.

After searching for a package you can get more information with the following command:

```console
   apt-cache show $PACKAGE_NAME
   or
   aptitude show $PACKAGE_NAME
```

Here is an example, and a snippet of the output:

```console
   apt-cache show linux-image-amd64
   or
   aptitude show linux-image-amd64

   ...
   Package: linux-image-amd64
   State: installed
   Automatically installed: no
   Version: 3.16+63
   Priority: optional
   Section: kernel
   ...
```

This will tell you additional information, such as what packages it depends on, and which packages it will conflict with, along with a description of what the package does.

```eval_rst
.. meta::
   :title: Package Management Functions | UKFast Documentation
   :description: Examples and information on package management functions on CentOS and Ubuntu from UKFast
   :keywords: servers, centos, ubuntu
```

```eval_rst
  .. title:: Package Management Functions
  .. meta::
     :title: Managing packages in Linux | UKFast Documentation
     :description: A guide to adding and managing packages in Linux
     :keywords: ukfast, linux, packages, adding, managing, yum, install, server, virtual, vm
