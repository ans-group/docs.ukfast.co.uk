# Add an IP Using Skip as source

If you are having issues with outbound connections coming from the wrong IP after adding an additional IP, this is usually because the IP that was added is lower than the primary IP and was added via the GUI.

This is a known issue with Sage Pay and mail servers, but it will affect most applications.

Remove the Additional IP, then in Command Prompt (as Administrator) use the following::

```console
netsh interface ipv4 add address [network connection name] [ip address] [subnet mask] skipassource=true
```

```console
netsh interface ipv4 add address "Local Area Connection" 172.31.0.0 255.255.255.0 skipassource=true
```

```eval_rst
  .. title:: Adding an IP using SkipAsSource
  .. meta::
     :title: Adding an IP using SkipAsSource | ANS Documentation
     :description: A guide to adding an IP using SkipAsSource in Windows
     :keywords: ukfast, windows, ip, address, information, skip, source, add, skipassource, interface, cloud, server
```
