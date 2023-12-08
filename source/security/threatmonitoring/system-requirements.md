# System Requirements

To ensure the best possible experience, Threat Monitoring may only be installed on systems that meet or exceed the below system requirements. These requirements may be subject to change as Threat Monitoring improves.

If you have any questions regarding the below or would like further information regarding a custom installation, please [contact UKFast support](https://portal.ans.co.uk/pss/create).

### Hardware requirements

Please refer to the below compatibility matrix before installing threat monitoring onto a server to understand what hardware is required.

```eval_rst
+---------------------+-----------------------+
|       Hardware      |      Requirement      |
+=====================+=======================+
| System Architecture | x86                   |
+---------------------+-----------------------+
| CPU Cores           | 2 (Dual-core) or more |
+---------------------+-----------------------+
| CPU Speed           | 1Ghz or more          |
+---------------------+-----------------------+
| Memory (RAM)        | 2GB or more           |
+---------------------+-----------------------+
| Free disk space     | 8GB or more           |
+---------------------+-----------------------+
| Disk Speed          | 600 IOPS or more      |
+---------------------+-----------------------+
```

### Virtual Servers

Threat Monitoring may also be installed onto virtual servers.

OS container-based servers and applications containers (such as `Docker`) are not currently supported.

Please refer to the below compatibility matrix before installing threat monitoring onto a virtual server to understand what virtualisation types are supported. Any virtualisation not mentioned below are not supported.

If you don't know your virtual server's virtualisation type, please contact your hosting provider for more information. Additionally, the below commands may be able to show you your system's virtualisation type on a Linux system.

```bash
hostnamectl status
```

```bash
dmidecode -s system-product-name
```

```eval_rst
+---------------------+-----------+
| virtualisation Type | Supported |
+=====================+===========+
| KVM                 | Yes       |
+---------------------+-----------+
| vmware              | Yes       |
+---------------------+-----------+
| hyperv              | Yes       |
+---------------------+-----------+
| xen                 | No        |
+---------------------+-----------+
| openvz              | No        |
+---------------------+-----------+
| LXC/LXD             | No        |
+---------------------+-----------+
| AWS                 | No        |
+---------------------+-----------+
```

Please note Threat Monitoring does **not** support cloud services such as Amazon AWS, Microsoft Azure or Google Cloud.

### Operating System compatibility matrix

Please refer to the below compatibility matrix before installing threat monitoring onto a server to understand which Threat Monitoring modules may be installed onto a target server.

Threat Monitoring Core is required, any other modules are optional but highly recommended for full protection.

```eval_rst
+---------------------+---------------+-------------------+--+------+-------------+
|   Operating System  | UKFast Hosted | Non-UKFast Hosted |  | Core | NIDS Module |
+=====================+===============+===================+==+======+=============+
| CentOS 7            | Yes           | Yes               |  | Yes  | Yes         |
+---------------------+---------------+-------------------+--+------+-------------+
| CentOS 8            | Yes           | Yes               |  | Yes  | Yes         |
+---------------------+---------------+-------------------+--+------+-------------+
| RHEL 7              | Yes           | Yes               |  | Yes  | Yes         |
+---------------------+---------------+-------------------+--+------+-------------+
| RHEL 8              | Yes           | Yes               |  | Yes  | Yes         |
+---------------------+---------------+-------------------+--+------+-------------+
| Ubuntu 18.04        | Yes           | Yes               |  | Yes  | Yes         |
+---------------------+---------------+-------------------+--+------+-------------+
| Ubuntu 20.04        | Yes           | Yes               |  | Yes  | Yes         |
+---------------------+---------------+-------------------+--+------+-------------+
| Debian 8            | Yes           | Yes               |  | Yes  | Yes         |
+---------------------+---------------+-------------------+--+------+-------------+
| Debian 9            | Yes           | Yes               |  | Yes  | Yes         |
+---------------------+---------------+-------------------+--+------+-------------+
| Windows Server 2012 | Yes           | No                |  | Yes  | No          |
+---------------------+---------------+-------------------+--+------+-------------+
| Windows Server 2016 | Yes           | No                |  | Yes  | No          |
+---------------------+---------------+-------------------+--+------+-------------+
| Windows Server 2019 | Yes           | No                |  | Yes  | No          |
+---------------------+---------------+-------------------+--+------+-------------+
```

**Any operating systems not mentioned above are not supported.**


```eval_rst
   .. title:: Threat Monitoring system requirements
   .. meta::
        :title: Threat Monitoring system requirements | ANS Documentation
        :description: UKFast Threat Monitoring system requirements
        :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up
```
