```eval_rst
:orphan:
```

# Web Server Default Configuration

## IIS

Internet Information Services (IIS) is a Microsoft developed web server that runs .NET. IIS is a built in feature of the Windows Operating System and below are the default settings/components installed at point of deployment:

```eval_rst
+---------------------------+----------------------------------------------------------------+
| Web Setting               | Default                                                        |
+===========================+================================================================+
| Installed Version:        | Latest Version                                                 |
+---------------------------+----------------------------------------------------------------+
| Installed Components:     |                                                                |
+---------------------------+------------------+------------------+--------------------------+
| Web-Server                | Web-Basic-Auth   | Web-ISAPI-Ext    | Web-Scripting-Tools      |
+---------------------------+------------------+------------------+--------------------------+
| Web-Http-Redirect         | Web-Windows-Auth | Web-ISAPI-Filter | Web-DAV-Publishing       |
+---------------------------+------------------+------------------+--------------------------+
| Web-CGI                   | Web-Net-Ext      | Web-Mgmt-Console | Web-Custom-Logging       |
+---------------------------+------------------+------------------+--------------------------+
| Web-Http-Logging          | Web-Includes     | Web-Mgmt-Tools   | Web-Stat-Compression     |
+---------------------------+------------------+------------------+--------------------------+
| Web-Filtering             | Web-ASP          | Web-Asp-Net      | Web-Asp-Net4 [2012 only] |
+---------------------------+------------------+------------------+--------------------------+
| Web-Net-Ext45 [2012 only] |                  |                  |                          |
+---------------------------+------------------+------------------+--------------------------+
```

## NGINX

NGINX is an open source application which is mainly deployed on Linux based operating systems that has a plethora of uses, however in this context we are focusing on the web server aspect, below are the default settings/components installed at point of deployment:

```eval_rst
+----------------------+------------------------------------------------------------------------------+
| Web Setting          | Default                                                                      |
+======================+==============================================================================+
| NGINX Version:       | Latest version from EPEL repository                                          |
+----------------------+------------------------------------------------------------------------------+
| Mount Point:         | /var/www/vhosts                                                              |
+----------------------+------------------------------------------------------------------------------+
| Additional Features: | N/A                                                                          |
+----------------------+------------------------------------------------------------------------------+
| Configuration:       | VirtualHosts will be set up under the mount point for the domain example.com |
+----------------------+------------------------------------------------------------------------------+
```

### APACHE

Apache HTTP Server is an open source web server which is mainly deployed on Linux based operating systems, below are the default settings/components installed at point of deployment:

```eval_rst
+----------------------+------------------------------------------------------------------------------+
| Web Setting          | Default                                                                      |
+======================+==============================================================================+
| APACHE Version:      | Latest version from default repository                                       |
+----------------------+------------------------------------------------------------------------------+
| Mount Point:         | /var/www/vhosts                                                              |
+----------------------+------------------------------------------------------------------------------+
| Additional Features: | N/A                                                                          |
+----------------------+------------------------------------------------------------------------------+
| Configuration:       | VirtualHosts will be set up under the mount point for the domain example.com |
+----------------------+------------------------------------------------------------------------------+
```

## PHP

PHP: Hypertext Preprocessor (PHP) is one of most popular open source scripting languages that is used to develop websites or web applications, below are the default settings/components installed at point of deployment:

```eval_rst
+----------------------------+-----------------------------------------------------------------+
| Web Setting                | Default                                                         |
+============================+=================================================================+
| PHP Version:               | Latest version from default repositories                        |
+----------------------------+-----------------------------------------------------------------+
| Mount Point:               | /var/www/vhosts                                                 |
+----------------------------+-----------------------------------------------------------------+
| Specific Modules Required: | N/A                                                             |
+----------------------------+-----------------------------------------------------------------+
| Configuration:             | Separate PHP-FPM processes should be run for each VirtualHost.  |
|                            |                                                                 |
|                            | Service should listen on the server's primary IP address.       |
+----------------------------+-----------------------------------------------------------------+
| Specific php.ini configs:  | display errors: On                                              |
|                            |                                                                 |
|                            | date.timezone: Europe/London                                    |
+----------------------------+-----------------------------------------------------------------+
```

```eval_rst
   .. title:: UKFast web build documentation
   .. meta::
      :description: Build documentation for web servers
      :keywords: ukfast, hosting, web, server, virtual
```
