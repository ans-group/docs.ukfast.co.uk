# Default Configuration of UKFast Appliances

UKFast has a wide range of bespoke appliances designed to cater for performance, high-availability or security requirements. Where UKFast appliances are deployed as virtual machines and configured in an active/ passive configuration, one appliance is hosted on your solution’s resources and the other on an appliances hypervisor.

This page provides information about the default configuration - please use the Priority Support System in the MyUKFast portal after launch to make advanced configuration changes (e.g. to get SSL offloading set up).

## Load Balancers
Increasing capacity and reliability of your applications, UKFast load balancers are configured with a single virtual IP on port 80/443 load balancing your web servers in a round robin fashion, for example WEB-01 and WEB-02 with an equal weighting of 1:1. 

More information around load balancing can be found [here](/network/loadbalancing/index)

## Web Application Firewalls

A web application firewall (WAF) is designed to ensure your data and applications are protected by blocking suspicious activity, providing comprehensive security for critical applications. UKFast offers both hardware based WAF and Network based WAF, running on our global DDOSX® network. 

Information on how to configure WAF on DDoSX® can be found [here](/security/ddos/wafsettings)

Your [hardware based WAFs](/security/webapplicationfirewall/whatisawaf) are configured with a single virtual IP on port 80/443 pointing to the load balancer virtual IP. 

## Webcelerators

With UKFast's Webcelerator your website visitors can enjoy an unaffected visit, even when traffic is reaching new record highs. Retain every conversion with a purpose-built solution which prevents sluggish online experiences. 

Your UKFast Webcelerators are configured with a single virtual IP on port 80/443 pointing to the Web Application Firewall's virtual IP, if you do not have a Web Application firewall this will point to your load balancer VIP or primary server IP.

The full Webcelerator configuration guide is available [here](/webcel/index)

```eval_rst
   .. title:: Default Configuration for UKFast Appliances
   .. meta::
      :title: Default Configuration for UKFast Appliances | UKFast Documentation
      :description: Default Configuration for UKFast Appliances.
      :keywords: ukfast, hosting, load balancing, load, web acceleration, webceleration, webcelerator, waf, web application firewall, layer7 firewall
```
