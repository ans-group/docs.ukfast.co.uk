# Default Configuration of UKFast Appliances

Where UKFast appliances are deployed as virtual machines and configured in an active/ passive configuration, one appliance is hosted on your solution’s resources and the other on an appliances hypervisor.

This document provides information about the default configuration - please use the Priority Support System in the MyUKFast portal after launch to make advanced configuration changes (e.g. to get SSL offloading set up).

## Load Balancers
Your UKFast load balancers are configured with a single virtual IP on port 80 load balancing your web servers in a round robin fashion, for example WEB-01 and WEB-02 with an equal weighting of 1:1. 

More information around load balancing can be found [here](https://docs.ukfast.co.uk/network/loadbalancing/index.html)

## Web Application Firewalls

UKFast offers both hardware based WAF and Network based WAF, running on our global DDOSX® network.

Information on how to configure WAF on DDoSX® can be found [here](https://docs.ukfast.co.uk/security/ddos/wafsettings.html)

Your [hardware based WAFs](https://docs.ukfast.co.uk/security/webapplicationfirewall/whatisawaf.html) are configured with a single virtual IP on port 80 pointing to the load balancer virtual IP. 

## Webcelerators

Your UKFast Webcelerators are configured with a single virtual IP on port 80 pointing to the Web Application virtual IP, if you do not have Web Application firewalls this will point to your or your load balancer IP.

The full Webcelerator configuration guide is available [here](https://docs.ukfast.co.uk/webcel/)

```eval_rst
  .. title:: Default Configuration for UKFast Appliances
  .. meta::
      :title: Default Configuration for UKFast Appliances | UKFast Documentation
      :description: Default Configuration for UKFast Appliances.
      :keywords: ukfast, hosting, load balancing, load, web acceleration, webceleration, webcelerator, waf, web application firewall, layer7 firewall
