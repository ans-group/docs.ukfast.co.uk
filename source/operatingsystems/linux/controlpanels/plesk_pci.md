# PCI compliance and Plesk

Starting with Plesk 12.5, Plesk created a one line command to apply a set of defaults which comply to common PCI standards. While it's not a 100% catch-all solution, it's a great starting point if you need to prepare for PCI compliance scans.

The command to run is as follows:

```bash
plesk sbin pci_compliance_resolver {--enable|--disable}
```

Alternatively, if you have more specific requirements and don't wish to apply Plesk's defaults to your entire server you can build your own using the `plesk sbin sslmng` command. A common use of this would be to address the [Logjam vulnerability](/security/logjam).

```bash
plesk sbin sslmng --strong-dh
```

For further reading and to see exactly what the current recommendations from Plesk are, please do check out the official Plesk pages for your version:

- [Plesk 12.5](https://docs.plesk.com/en-US/12.5/advanced-administration-guide-linux/pci-dss-compliance/tune-plesk-to-meet-pci-dss-on-linux.65871/)
- [Plesk Onyx](https://docs.plesk.com/en-US/onyx/administrator-guide/plesk-administration/securing-plesk/pci-dss-compliance/tune-plesk-to-meet-pci-dss-on-linux.78899/)
- [Plesk Obsidian](https://docs.plesk.com/en-US/obsidian/administrator-guide/plesk-administration/securing-plesk/pci-dss-compliance/tune-plesk-to-meet-pci-dss-on-linux.78899/)

If you need any assistance meeting the requirements of a PCI report, please do contact your account manager and they'll be able to book in one of our experienced PCI team to assist you.

```eval_rst
   .. title:: Plesk | PCI Compliance
   .. meta::
      :title: Plesk | PCI Compliance | UKFast Documentation
      :description: Guidance on achieving PCI compliance with Plesk and cPanel servers
      :keywords: ukfast, plesk, cpanel, whm, panel
```
