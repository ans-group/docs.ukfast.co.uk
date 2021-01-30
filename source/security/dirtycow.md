# Dirty COW

Dirty COW, or CVE-2016-5195 to use it's less sensationalist name, is a privilege escalation vulnerability in Linux from October 2016.

The obligatory branded vulnerability website can be found [here](https://dirtycow.ninja/), replete with logo, proof of concept and more detail on the underlying issue.

Describing what the vulnerability is, what it does and how it came about is better left to the above link, this page is aimed at people wanting to patch their way to safety.

The good news is that by the time you're reading this, all the major linux distributions will have patches available for their various kernels, so it's simply a matter or running an update through your package manager and restarting your server.

First things first though, let's check if you're actually vulnerable.

## Checking vulnerability

### CentOS/Red Hat

Red Hat have provided a handy script for checking if you're vulnerable or not. Carry out the following steps which logged into your server over SSH to check.

First, download the script from Red Hat using `wget`:

```bash
 wget https://access.redhat.com/sites/default/files/rh-cve-2016-5195_1.sh
```

Then run the script and see what it returns:

```bash
 bash rh-cve-2016-5195_1.sh
```

The output should be fairly self explanatory, but if you're vulnerable it'll look something like this:

```console
 Your kernel is 3.10.0-327.10.1.el7.x86_64 which IS vulnerable.
 Red Hat recommends that you update your kernel. Alternatively, you can apply partial
 mitigation described at https://access.redhat.com/security/vulnerabilities/2706661 .
```

If vulnerable, you should follow the next section to patch and fix the vulnerability.

### Debian/Ubuntu

If you're on a Debian or Ubuntu based distribution, the Red Hat script won't work, but you can find your kernel version with the following version:


```bash
 uname -a
```

This will return something like:

```console
 root@dev:~# uname -a
 Linux dev 3.13.0-76-generic #120-Ubuntu SMP Mon Jan 18 15:59:10 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
```

If your kernel version is earlier (lower) than the following list, you're vulnerable and should follow the next section to update your kernel to safe version.


* **4.8.0-26.28** for Ubuntu 16.10
* **4.4.0-45.66** for Ubuntu 16.04 LTS
* **3.13.0-100.147** for Ubuntu 14.04 LTS
* **3.2.0-113.155** for Ubuntu 12.04 LTS
* **3.16.36-1+deb8u2** for Debian 8
* **3.2.82-1** for Debian 7
* **4.7.8-1** for Debian unstable

## Patching the vulnerability

### UKFast clients

If you're one of our linux clients, you can still follow the non-UKFast section if you'd like, but we've implemented an easier patching process through your MyUKFast client area, [located here](https://my.ukfast.co.uk/server/package-update.php).

Once you've followed that link and logged in, you should be confronted with something like this:

![Patching page](files/dirtycow1.jpg)

Select all the servers you want to patch, select `Update selected packages` from the dropdown menu underneath and then press `GO` to start the update process.

This process should take a few minutes, but we're not out of the woods yet. Refresh the page in a few minutes time and you should now see the following section has appeared, showing that there are severs that need rebooting to utilise the patch you just applied:

![Pending reboot](files/dirtycow2.jpg)

Again, select the servers you want to restart, and select either `Reboot selected now` or `Reboot selected at set time` from the dropdown. If you're doing it at a set time, enter a time, then hit `Schedule Reboot` to get it all under way.

Once your servers are back online, you're good to go.


### Non-UKFast clients

As mentioned previously, there should be a patch available for your kernel version through your standard package manager now.

#### CentOS/Red Hat

`yum` is the package manager at play here, so you can update the kernel with the following command:

```bash
yum update kernel
```

Alternatively, if you'd like to update all packages on your server, you can use:

```bash
yum update
```

After this has completed, you'll need to reboot your server to load the new kernel:

```bash
reboot
```

#### Ubuntu/Debian

With Debian based systems, your package manager is `aptitude`, but we'll use `apt-get` here. Run the following to upgrade your packages:

```bash
apt-get update && apt-get dist-upgrade
```

As with CentOS, a reboot is needed to use this new kernel:

```bash
reboot
```

```eval_rst
   .. title:: Patching the DirtyCOW vulnerability
   .. meta::
      :title: Patching the DirtyCOW vulnerability | UKFast Documentation
      :description: Guidance on patching the DirtyCOW vulnerability
      :keywords: vulnerability, dirtycow, patching, security, dss, pci, security
```
