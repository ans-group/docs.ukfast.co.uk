# Default Configuration for Linux Servers

## Pre-Launch Questionaire
With every dedicated server on your order form you will receive your Pre-Launch Questionnaire (PLQ). The PLQ give you the ability to verify the configuration for each server, firewall, or other configurable products on your order before we begin the launch process.

Once you are satisfied with your installation settings, please press the "Launch solution" button so that we can get your servers to you as quickly as possible. You will receive your PLQ within 15 minutes of your order form being processed.

To ensure that your order meets its scheduled launch date, the questionnaire will automatically close 24hrs after your order being processed and your server will meet the below default configuration. If you need more time to pre-configure your solution, you may extend the deadline by up to one week online, but please note that this may delay the delivery of your solution.

Please note that some of our more complex solutions may require you to complete additional documentation in order for us to gather as much information as possible to meet your requirements.

If you have a question about your order or our pre-launch process? You can call your Account Management Team on 0161 637 9321.

## Partitions
Please find below the UKFast Default Partitions configured as part of your solution. Default Partitions can be customised using your online Pre-Launch Questionnaire.

```eval_rst
+--------------------------+-----------------------------+--------------------------+
| Partition                | Size or %                   | Example (2x 256GB RAID1) |
+==========================+=============================+==========================+
| Swap                     | 25% of Total Memory         | 4GB                      |
+--------------------------+-----------------------------+--------------------------+
| /boot Partition          | 1GB Minimum                 | 1GB                      |
+--------------------------+-----------------------------+--------------------------+
| /Partition               | Remaining Space             | 230GB                    |
+--------------------------+-----------------------------+--------------------------+
```

## Default Installed Software
Please find below the UKFast Default Software installed as part of your solution. Default Software can be customised using your online Pre-Launch Questionnaire.

### Linux Server (LAMP)

```eval_rst
+--------------------------+---------------------------------+
| Software                 | Default - Yes/No                |
+==========================+=================================+
| Apache                   | Yes                             |
+--------------------------+---------------------------------+
| MySQL / MariaDB          | Yes                             |
+--------------------------+---------------------------------+
| PHP                      | Yes                             |
+--------------------------+---------------------------------+
| UKFast Backup Agent      | If purchased this is compulsory |
+--------------------------+---------------------------------+
| McAfee                   | If purchased this is compulsory |
+--------------------------+---------------------------------+
```

### cPanel or Plesk Server

```eval_rst
+--------------------------+---------------------------------+
| Software                 | Default - Yes/No                |
+==========================+=================================+
| cPanel Pro / Plesk       | If purchased this is compulsory |
+--------------------------+---------------------------------+
| UKFast Backup Agent      | If purchased this is compulsory |
+--------------------------+---------------------------------+
| McAfee                   | If purchased this is compulsory |
+--------------------------+---------------------------------+
```

### Magento Server

```eval_rst
+----------------------+---------------------------------+---------------------------------+
| Software             | Magento 1                       | Magento 2                       |
+======================+=================================+=================================+
| nginx                | Latest                          | Latest                          |
+----------------------+---------------------------------+---------------------------------+
| Percona              | Percona 5.7                     | Percona 5.7                     |
+----------------------+---------------------------------+---------------------------------+
| PHP                  | PHP 5.6                         | PHP 7.2                         |
+----------------------+---------------------------------+---------------------------------+
|McAfee                | Not Installed                   | Not Installed                   |
+----------------------+---------------------------------+---------------------------------+
|UKFast Backup Agent   | If purchased this is compulsory | If purchased this is compulsory |
+----------------------+---------------------------------+---------------------------------+
```

## Monitoring

### Service Monitoring
Service Monitoring can be customised using your online Pre-Launch Questionnaire on a per server basis. The following service monitoring will be added across all servers in the solution by default:

```eval_rst
+--------------------------+---------------------------------+
| Monitoring               | Default                         |
+==========================+=================================+
| Ping                     | Enabled                         |
+--------------------------+---------------------------------+
| SMTP                     | Enabled                         |
+--------------------------+---------------------------------+
| POP                      | Enabled                         |
+--------------------------+---------------------------------+
| HTTP                     | Enabled                         |
+--------------------------+---------------------------------+
| FTP                      | Enabled                         |
+--------------------------+---------------------------------+
```

If additional optional monitoring is required for services not listed above please inform your Account Manager or request via the Priority Support system in the MyUKFast portal after launch to make configuration changes.

#### Example Additional Monitoring Options

```eval_rst
+-------------------------------------+---------------------------------+---------------------------------+
| Hostname                            | Port / Service / URL            | Default                         |
+=====================================+=================================+=================================+
| e.g. http://example.com/status.apsx | e.g. URL                        | Not Enabled                     |
+-------------------------------------+---------------------------------+---------------------------------+
```

### Capacity Threshold Monitoring 
The following CTM alerts will be configured on your Linux servers, where applicable:

```eval_rst
+--------------------------+-----------------------------+--------------------------+--------------------------+
| Name                     | Acceptable Range            | Alert Triggered When     | Default                  |
+==========================+=============================+==========================+==========================+
| CPU Usage                | 0% - 80%                    | CPU usage hits 81%       | Enabled                  |
+--------------------------+-----------------------------+--------------------------+--------------------------+
| / Space (free)           | 15% - 100%                  | Free space hits 14%      | Enabled                  |
+--------------------------+-----------------------------+--------------------------+--------------------------+
| /var Space (free)        | 15% - 100%                  | Free space hits 14%      | Enabled                  |
+--------------------------+-----------------------------+--------------------------+--------------------------+
| /home Space (free)       | 15% - 100%                  | Free space hits 14%      | Enabled                  |
+--------------------------+-----------------------------+--------------------------+--------------------------+
| Swap Usage               | 0% - 80%                    | Swap usage hits 81%      | Enabled                  |
+--------------------------+-----------------------------+--------------------------+--------------------------+
```

## Anti-Virus
All Physical and Virtual Machines as part of your solution will come with McAfee Anti-Virus installed, this comes as part of your PROprotection package.
Below you will find a list of common questions related to Anti-Virus:

#### Is this installed on all servers in my solution?
> This will be included on all servers if you have purchased PROprotection, both Windows and Linux server. The only devices this does not apply to are UKFast Appliances and Magento Servers.

#### Are all files scanned by the av software?
> Yes, on-access scanning is enabled by default.

#### At what frequency are files scanned?
> On-access scanning and weekly full scan.

#### At what frequency is the av software updated?
> Daily DAT Updates and Agent updates when available.

#### What are dat files?
> Virus definition or DAT files contain virus signatures and other information that McAfee anti-virus products use to protect your computer against existing and new potential threats. DAT files are released on a daily basis.

#### Are any other av based tools or activates used? (e.g. local firewall)
> No, by default local firewalls are disabled and no other AV tools are installed or used by UKFast.

## Updates

By default single role Linux Servers will have the following, please note that updates can be customised using your online Pre-Launch Questionnaire:
- No, I do not wish for this server to automatically apply updates 

If you wish, you are able to update this to: 
- Yes, I want this server to automatically apply updates

## Application Specific Default Configuration

### MySQL / Percona / MariaDB Database Configuration

```eval_rst
+-------------------------------+----------------------------+
| DB Setup                      | Default                    |
+===============================+============================+
| Installed Version             | Latest Stable Release      |
+-------------------------------+----------------------------+
| Mount Point                   | /var/lib/mysql             |
+-------------------------------+----------------------------+
| Collation                     | utf8mb4_general_ci         |
+-------------------------------+----------------------------+
| Additional Features / Modules | N/A                        |
+-------------------------------+----------------------------+
```

### NGINX Web Configuration

```eval_rst
+----------------------+-------------------------------------------------------------------------------+
|       Web Setup      |                                    Default                                    |
+======================+===============================================================================+
|  NGiNX Version       | Latest version from EPEL repository                                           |
+----------------------+-------------------------------------------------------------------------------+
|  Mount Point         | /var/www/vhosts                                                               |
+----------------------+-------------------------------------------------------------------------------+
|  Additional Features | N/A                                                                           |
+----------------------+-------------------------------------------------------------------------------+
|  Configuration       | VirtualHosts will be set up under the mount point for the domain example.com  |
+----------------------+-------------------------------------------------------------------------------+
```

### APACHE Web Configuration

```eval_rst
+----------------------+------------------------------------------------------------------------------+
|       Web Setup      |                                   Default                                    |
+======================+==============================================================================+
|  Apache Version      | Latest version from default repositories                                     |
+----------------------+------------------------------------------------------------------------------+
|  Mount Point         | /var/www/vhosts                                                              |
+----------------------+------------------------------------------------------------------------------+
|  Additional Features | N/A                                                                          |
+----------------------+------------------------------------------------------------------------------+
|  Configuration       | VirtualHosts will be set up under the mount point for the domain example.com |
+----------------------+------------------------------------------------------------------------------+
```

### PHP Web Configuration

```eval_rst
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
|         Web Setup          |                                                          Default                                                          |
+============================+===========================================================================================================================+
| PHP Version                |  Latest version from default repositories                                                                                 |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Mount Point                |  /var/www/vhosts                                                                                                          |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Specific Modules Required  |  N/A                                                                                                                      |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Configuration              |  Separate PHP-FPM processes should be run for each VirtualHost. Service should listen on the server’s primary IP address. |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Specific php.ini configs   |  display errors: On                                                                                                       |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
| date.timezone              |  Europe/London                                                                                                            |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------+
```

### NFS File Configuration

+----------------------------+-----------------------+
|         NFS Setup          |        Default        |
+============================+=======================+
| Installed Version          | Latest version of NFS |
+----------------------------+-----------------------+
| Mount on following servers | WEB-01 , WEB-02       |
+----------------------------+-----------------------+
| Mount Point                | /var/www/             |
+----------------------------+-----------------------+

```eval_rst
  .. meta::
      :title: UKFast Default Configuration Of A Linux Server | UKFast Documentation
      :description: Default Configuration for Linux Servers at deployment. 
      :keywords: ukfast, hosting, linux, server, virtual

