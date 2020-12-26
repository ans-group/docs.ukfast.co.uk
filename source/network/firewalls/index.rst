=========
Firewalls
=========

Here you'll find all the guidance relating to UKFast dedicated and shared firewalls, as well as VPNs. UKFast offers two primary types of firewalls, shared and dedicated. Both offer the basic functions you would expect from a firewall such as controlling ports, locking down services by IP, and the ability to blocking IPs.

Our dedicated firewalls allow much finer control, as well as advanced features like VPNs, and the ability to allow ICMP traffic. You can also have more advanced setups, including redundant pairs of firewalls.

-----------------------------------
General UKFast firewall information
-----------------------------------

.. toctree::
   :maxdepth: 1

   viewconfig
   icmp

-----------------------------
UKFast shared firewall guides
-----------------------------
.. toctree::
   :maxdepth: 1

   shared_openport
   shared_lockdown

--------------------------------
UKFast dedicated firewall guides
--------------------------------

.. toctree::
   :maxdepth: 1
   
   dedi_openport
   dedi_lockdown
   schedule_firewall_reboot

----------------------------------
UKFast VPNs on dedicated firewalls
----------------------------------
.. toctree::
   :maxdepth: 1
   
   supportedvpns
   VPNTab
   RA_VPN_Tab
   S2S_VPN_Tab
   VPNUsers
   vpn2fa
   vpncapacity


.. meta::
   :title: UKFast Firewalls | UKFast Documentation
   :description: Guidance and information relating to firewalls when hosting with UKFast
   :keywords: ukfast, firewall, firewalls, VPN, dedicated, shared, cloud, hosting, security
