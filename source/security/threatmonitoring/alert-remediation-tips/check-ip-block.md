# Checking if an IP has been blocked

Threat Monitoring can detect incoming attacks in real-time and proactively block them, minimising the risk of compromise. This is achieved through the use of iptables and hosts.deny on Linux, and Windows firewall on Windows systems

### Linux

To check whether an IP address has been blocked (either intentionally due to attacks or unintentionally), use our verification script. Run the following command, replacing $IP_ADDRESS with the actual IP address you want to check.

```
curl -sSf https://repo.thmon.ukfast.co.uk/check-block-status.sh | sudo bash -s -- $IP_ADDRESS
```

If you would like to automatically remove the IP from the block list, specify `--remove-found` when using the script, like below:

```
curl -sSf https://repo.thmon.ukfast.co.uk/check-block-status.sh | sudo bash -s -- $IP_ADDRESS --remove-found
```

For additional security, you may wish to download and inspect the script before execution:

```
curl -sSfO https://repo.thmon.ukfast.co.uk/check-block-status.sh
nano check-block-status.sh
chmod +x check-block-status.sh
./check-block-status.sh $IP_ADDRESS --remove-found
```

### Windows

To check if an Ip has been blocked in windows, follow the below steps.

Open up the windows firewall configuration utility. This can be found by searching for "Windows Firewall with Advanced Security"

Click "Inbound rules" on the left pane

You should now be able to see all the incoming firewall rules.

Look for any rules with the name "WAZUH ACTIVE RESPONSE BLOCKED IP", check the 'Remote Address' column to see if the IP in question has been blocked.

If you'd like to remove an IP from the blocklist, you can right-click the rule that is enforcing the block, and click delete, confirming by pressing Yes.

```eval_rst
    .. title:: Threat Monitoring | Check if an IP is blocked | ANS Documentation
    .. meta::
        :title: Check if an IP is blocked | ANS Documentation
        :description: Useful threat remediation and prevention tips
        :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up
```