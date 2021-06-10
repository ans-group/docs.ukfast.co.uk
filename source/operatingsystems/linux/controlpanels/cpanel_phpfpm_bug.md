# PHP-FPM is Disabled after EasyApache Update

## Why was PHP-FPM disabled for all my domains?

As of **June 9th 2021**, an `EasyApache` update to `ea-apache24-config-1.0-171` has inadvertently disabled `PHP-FPM` on `cPanel/WHM` servers. The following components of `WHM` have been identified to have been affected.

```console
ea-apache24-config-runtime-1.0-171.172.2.cpanel.noarch
ea-apache24-config-1.0-171.172.2.cpanel.noarch
```

This has also caused custom `PHP-FPM` configurations to be removed.

## When will this be resolved?

As of yet, no automatic fix has been pushed out by `cPanel`. However `UKFast` have successfully tested an interim fix that restores functionality to websites on affected `cPanel` servers.

## How to re-enable PHP-FPM for a single domain

* Log into `WHM`.
* Navigate to `MultiPHP Manager`..
* In the bottom section, under `Set PHP Version per Domain`, use the search bar to search for your domain.
* To the far right of your domain, click the toggle icon to enable `PHP-FPM`.

## How to re-enable PHP-FPM for all domains

* Log into `WHM`.
* Navigate to `MultiPHP Manager`.
* In the bottom section, under `Set PHP Version per Domain`, scroll through your list of domains and click the checkbox to the left of each domain you want to enable `PHP-FPM` on.
* Click the drop-down menu to the far right of the search bar and next to `PHP-FPM`, then select On.
* Click Apply to enable PHP-FPM on the selected domains.

## How to re-enable PHP-FPM & restore custom configurations

```eval_rst
.. note::
   This section requires you to connect to your server over `SSH`. Please see our guide on `connecting to your server via SSH`_ for further assistance.

.. _connecting to your server via SSH: /operatingsystems/linux/basics/connecting.html
```

To reinstate all domains that were previously using `PHP-FPM` along with any custom configuration, please see the following steps;

* Connect to your server via SSH as the `root` user
* Create a file named `fix.pl` with your preferred text editor (`vi`, `vim` or `nano`, for example) and populate it with the following contents:

```console
#!/usr/local/cpanel/3rdparty/bin/perl
use strict;
use warnings;
use Cpanel::JSON;
use Data::Dumper;
use File::Slurp;
use YAML::Syck;
my $file = "@ARGV";
my $json = File::Slurp::slurp ($file);
my $hr = Cpanel::JSON::Load ($json);
my $yaml = YAML::Syck::Dump ($hr);
print $yaml . "\n";
```

* Make sure the file is executable by running:

```console
chmod +x fix.pl
```

* Run the following loop:

```console
find /var/cpanel/userdata -type f -iname '*fpm.cache' | while read file; do ./fix.pl ${file} > $(echo ${file} | sed 's/cache/yaml/'); done
```

* Finally, rebuild all of the `PHP-FPM` configurations:

```console
for i in $(cat /etc/userdomains | awk '{print $2}'); do echo "$i"; /scripts/php_fpm_config --rebuild $i; done
```

```eval_rst
.. note::
   Please contact UKFast support via a Priority Support Ticket for any further assistance with this.
```

```eval_rst
  .. title:: cPanel | PHP-FPM is Disabled after EasyApache Update
  .. meta::
     :title: PHP-FPM is Disabled after EasyApache Update | UKFast Documentation
     :description: PHP-FPM is Disabled after EasyApache Update
     :keywords: ukfast, cpanel, whm, bug, control, panel, tutorial, cloud, server, guide, virtual
```
