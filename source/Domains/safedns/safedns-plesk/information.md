## Info

The UKFast SafeDNS Plesk extension provides the ability to manage the SafeDNS Zone for any of the domains on your Plesk Server.

It will synchronise the DNS Zones from Plesk with SafeDNS.
It does not replace or modify Plesk’s internal DNS , so if you have specific domains which use an external DNS Service, you’re free to continue using that service.

Logs are stored in : /var/log/plesk/ext-plesk-safedns/

At present, this extension is **only compatible with linux systems**.
Usage on windows will result in synchronise tasks erroring & no logs being written by the extension.
