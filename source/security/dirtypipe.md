# CVE-2022-0847 - Dirty Pipe Vulnerability
***Last Updated: 15/03/2022 10:59 AM***

```eval_rst
.. tip::
  Patched kernels are available via the UKFast Public Mirrors.

```

## Overview

On Monday 7th March 2022, a flaw was found in the way the "flags" member of the new pipe buffer structure was lacking proper initialization in copy_page_to_iter_pipe and push_pipe functions in the Linux kernel and could thus contain static values. An unprivileged local user could use this flaw to write to pages in the page cache backed by read only files and as such escalate their privileges on the system.

```eval_rst
+---------------+----------+------------+
| Reference     | Severity | Date       |
+===============+==========+============+
| CVE-2022-0847 | High     | 07/03/2022 |
+---------------+----------+------------+
```

## Impact Assessment

### ANS Response

Patches are currently available for Ubuntu 21.10. ANS is encourages all clients to upgrade thier kernel to the latest version to mitigate this vulnerability.

We have confirmed that we do not deploy Ubuntu 21.10 or any other interim releases for managed services and thus are not impacted by Dirty Cow.

### Vulnerable Versions

```eval_rst
+--------------+--------------------------------+
| Distro       | Comment                        |
+==============+================================+
| CentOS 6.x   | Not vulnerable                 |
+--------------+--------------------------------+
| CentOS 7.x   | Not vulnerable                 |
+--------------+--------------------------------+
| CentOS 8.x   | Not vulnerable                 |
+--------------+--------------------------------+
| Ubuntu 14.04 | Not vulnerable (3.11.0-12.19)  |
+--------------+--------------------------------+
| Ubuntu 16.04 | Not vulnerable (4.4.0-2.16)    |
+--------------+--------------------------------+
| Ubuntu 18.04 | Not vulnerable (4.13.0-16.19)  |
+--------------+--------------------------------+
| Ubuntu 20.04 | Not vulnerable (5.4.0-9.12)    |
+--------------+--------------------------------+
| Ubuntu 21.10 | Vulnerable to CVE-2022-0847    |
+--------------+--------------------------------+
```


## Mitigation

The specific flaw exists in the bionic and focal, but is not currently exploitable due to lack of a flag that was introduced in kernel 5.8. The flaw will be fixed as part of the next round of bionic and focal kernel updates in case some other way of exploiting it is discovered in the future. The hardware enablement kernel for focal, linux-hwe-5.13, was updated to fix this issue in USN-5317-1.

## Fix

### Patched Versions

```eval_rst
.. note::
  A reboot is required to load the new kernel.
```

```eval_rst
+--------------+--------------------------+
| Distro       | Comment                  |
+==============+==========================+
| Ubuntu 21.10 | linux-image-5.13.0.35.40 |
+--------------+--------------------------+
```

## Links

* [Ubuntu Security Report](https://ubuntu.com/security/CVE-2022-0847)

```eval_rst
   .. title:: CVE-2022-0847 - Dirty Pipe Vulnerability
   .. meta::
      :title: CVE-2022-0847 - Dirty Pipe Vulnerability  | UKFast Documentation
      :description: Information for Dirty Pipe Vulnerability ~ CVE-2022-0847
      :keywords: ukfast, linux, security, vulnerability, dirty pipe
```

