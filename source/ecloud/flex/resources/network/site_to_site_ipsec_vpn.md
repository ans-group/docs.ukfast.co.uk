# Site-To-Site VPNs on eCloud Flex

## Site-To-Site VPN To A Cisco ASA Firewall

In this guide we will use `python-neutronclient` and `python-openstackclient` to orchestrate setting up a site-to-site VPN between eCloud Flex and a Cisco ASA firewall.
Prerequisites

* Python 2.7+
* A linux server (ideally, although Windows should work also)
* Your OpenStack credentials
  * Authorisation URL *<https://api.openstack.ecloud.co.uk:5000/v3> by default)*
  * Project Name / ID
  * Username
  * Password
* The following details on the Cisco ASA
  * Public IP address or FQDN
  * VPN Identity (usually the public IP)
  * Subnet(s) on inside interface(s)
  * Pre-Shared Key string
  * IKE Policy
    * Authorisation algorithm `[ SHA1 ]`
    * Encryption algorithm `[ 3des | aes-128 | aes-192 | aes-256 ]`
    * IKE version `[ v1 | v2 ]`
    * IKE key lifetime *(greater than 60, 86400 by default in UKFast)*
    * Perfect Forward Secrecy details `[ group2 | group5 | group14 ]`
    * IKE Phase 1 negotiation mode `[ main ]`
  * IPSec Policy
    * Authorisation algorithm `[ SHA1 ]`
    * Encapsulation mode `[ tunnel | transport ]`
    * Encryption algorithm `[ 3des | aes-128 | aes-192 | aes-256 ]`
    * IKE key lifetime *(greater than 60, 86400 by default in UKFast)*
    * Perfect Forward Secrecy details `[ group2 | group5 | group14 ]`
    * Transform Protocol `[ esp | ah | ah-esp ]`

### Set up the environment

First of all, log into the [eCloud Flex Horizon Dashboard](<https://api.openstack.ecloud.co.uk/project/api_access/>), navigate to **API Access** and download your bash shell configuration file by clicking **Download OpenStack RC File v3**

Put that onto your Linux server in your home directory and import it into your session using `source`. For example, in my case:

```console
source 6150-openrc.sh
```

Check the version of python you have installed

```console
[root@ukfastserver ~]# python --version
Python 2.7.5
```

Now install the required Python packages using `pip`

```console
[root@ukfastserver ~]# pip install python-openstackclient python-neutronclient
```

Check what versions we have installed on the server Now

```console
[root@ukfastserver ~]# openstack module list
+-----------------+--------+
| Field           | Value  |
+-----------------+--------+
| cinderclient    | 3.1.0  |
| keystoneclient  | 3.13.0 |
| novaclient      | 9.0.1  |
| openstack       | 0.9.17 |
| openstackclient | 3.12.0 |
+-----------------+--------+
```

### Create the IKE Policy

Create our **VPN IKE Policy**. You can see here that I've used `sha1`, `aes-256`, `v1`, etc. in my settings, which match what I have set on the Cisco side of the VPN. I've also called my policy **Test VPN IKE Policy 1**

```bash
neutron vpn-ikepolicy-create --description "Test VPN IKE policy" \
                             --auth-algorithm sha1 \
                             --encryption-algorithm aes-256 \
                             --ike-version v1 \
                             --lifetime units=seconds,value=86400 \
                             --pfs group2 \
                             --phase1-negotiation-mode main \
                             'Test VPN IKE Policy 1'
```

Something similar to this will be output to screen:

```console
Created a new ikepolicy:
+-------------------------+--------------------------------------+
| Field                   | Value                                |
+-------------------------+--------------------------------------+
| auth_algorithm          | sha1                                 |
| description             | Test VPN IKE policy                  |
| encryption_algorithm    | aes-256                              |
| id                      | b250861a-4e42-4c9b-b807-120f1fefbc4c |
| ike_version             | v1                                   |
| lifetime                | {"units": "seconds", "value": 86400} |
| name                    | Test VPN IKE Policy 1                |
| pfs                     | group2                               |
| phase1_negotiation_mode | main                                 |
| project_id              | aa9c0db4ac974d2d8feb71f145e22160     |
| tenant_id               | aa9c0db4ac974d2d8feb71f145e22160     |
+-------------------------+--------------------------------------+
```

We can then see a list using `neutron vpn-ikepolicy-list` if need be

### Create the IPSec Policy

Now create the **VPN IPSec Policy**. I've set `sha1`, `aes-256`, `group2`, etc., very similar to the IKE policy above.

```bash
neutron vpn-ipsecpolicy-create --description "Test VPN IPSEC policy" \
                               --auth-algorithm sha1 \
                               --encapsulation-mode tunnel \
                               --encryption-algorithm aes-256 \
                               --lifetime units=seconds,value=86400 \
                               --pfs group2 \
                               --transform-protocol esp \
                               "Test VPN IPSEC Policy 1"
```

As before, something like this should be output if the command was successful

```console
Created a new ipsecpolicy:
+----------------------+--------------------------------------+
| Field                | Value                                |
+----------------------+--------------------------------------+
| auth_algorithm       | sha1                                 |
| description          | Test VPN IPSEC policy                |
| encapsulation_mode   | tunnel                               |
| encryption_algorithm | aes-256                              |
| id                   | 88435b95-8cb7-4bd6-8cdc-3ba2c70e8476 |
| lifetime             | {"units": "seconds", "value": 86400} |
| name                 | Test VPN IPSEC Policy 1              |
| pfs                  | group2                               |
| project_id           | aa9c0db4ac974d2d8feb71f145e22160     |
| tenant_id            | aa9c0db4ac974d2d8feb71f145e22160     |
| transform_protocol   | esp                                  |
+----------------------+--------------------------------------+
```

These can be viewed again using `neutron vpn-ipsecpolicy-list`

### Get our Router ID and Subnet IDs

Using the `openstack` commandset we can now get the IDs for the router and subnet as follows:

```console
[root@ukfastserver ~]# openstack router list
+--------------------------------------+------+--------+-------+-------------+-------+----------------------------------+
| ID                                   | Name | Status | State | Distributed | HA    | Project                          |
+--------------------------------------+------+--------+-------+-------------+-------+----------------------------------+
| 1399c7d5-da8e-4f7a-8d62-c9544a161b6d | rtr1 | ACTIVE | UP    | False       | False | aa9c0db4ac974d2d8feb71f145e22160 |
+--------------------------------------+------+--------+-------+-------------+-------+----------------------------------+
```

```console
[root@ukfastserver ~]# openstack subnet list
+--------------------------------------+--------------------+--------------------------------------+--------------------+
| ID                                   | Name               | Network                              | Subnet             |
+--------------------------------------+--------------------+--------------------------------------+--------------------+
| 17cc8ea4-7a77-4b72-8b1b-db1bf1ad9991 | 192.168.3.0/24     | 57f6e2c9-0e5a-43a8-b62b-dd725114fa41 | 192.168.3.0/24     |
| 8b2510c8-ece2-4e8d-aac3-a0f36b3ae80c | 2a02:22d0:9:f::/64 | 57f6e2c9-0e5a-43a8-b62b-dd725114fa41 | 2a02:22d0:9:f::/64 |
+--------------------------------------+--------------------+--------------------------------------+--------------------+
```

### Create the VPN Service

Now we create the **VPN Service**, using those details from the above two commands. Here I'm using the `192.168.3.0/24` subnet on the OpenStack side, and my one and only router. Adjust these to your command outputs

```bash
neutron vpn-service-create --description "Test VPN Service" \
                           1399c7d5-da8e-4f7a-8d62-c9544a161b6d \
                           17cc8ea4-7a77-4b72-8b1b-db1bf1ad9991 \
                           --name "Test VPN Service 1"
```

Something the following should be echoed to screen:

```console
+----------------+--------------------------------------+
| Field          | Value                                |
+----------------+--------------------------------------+
| admin_state_up | True                                 |
| description    | Test VPN Service                     |
| external_v4_ip | 46.37.188.191                        |
| external_v6_ip | 2a02:22d0:8::40                      |
| id             | 9194fb3e-fba9-4b2a-9ba5-c6cbd03c848e |
| name           | Test VPN Service 1                   |
| project_id     | aa9c0db4ac974d2d8feb71f145e22160     |
| router_id      | 1399c7d5-da8e-4f7a-8d62-c9544a161b6d |
| status         | PENDING_CREATE                       |
| subnet_id      | 17cc8ea4-7a77-4b72-8b1b-db1bf1ad9991 |
| tenant_id      | aa9c0db4ac974d2d8feb71f145e22160     |
+----------------+--------------------------------------+
```

As before, we can see the list of VPN services using `neutron vpn-service-list`

### Create the Site-To-Site connection

Now it's time to tie all these policies together in what OpenStack refers to as a **IPSec Site Connection**. I've used the `id` output of the previous commands in place of the `ikepolicy-id`, `ipsecpolicy-id` and `vpnservice-id` values. I've also used the Cisco ASA VPN policy details listed in the prerequisites at the top of this article. Here is how they translate:

* `peer-address` is the **Public IP address or FQDN**
* `peer-id` is the **VPN Identity**
* `peer-cidr` is the **Subnet on inside interface**
* `psk` is the **Pre-Shared Key**

The rest should be pretty self-explanatory...

```bash
neutron ipsec-site-connection-create --name "VPN-to-CiscoASA-1" \
                                     --description "VPN between OpenStack router and Cisco ASA firewall" \
                                     --vpnservice-id 9194fb3e-fba9-4b2a-9ba5-c6cbd03c848e \
                                     --ikepolicy-id b250861a-4e42-4c9b-b807-120f1fefbc4c \
                                     --ipsecpolicy-id 88435b95-8cb7-4bd6-8cdc-3ba2c70e8476 \
                                     --peer-address "185.160.252.4" \
                                     --peer-id "185.160.252.4" \
                                     --peer-cidr "172.24.27.0/25" \
                                     --psk "67BD88KpA9bY0Mu2"
```

As before, the output to screen should reflect our command entered:

```console
Created a new ipsec_site_connection:
+-------------------+-----------------------------------------------------+
| Field             | Value                                               |
+-------------------+-----------------------------------------------------+
| admin_state_up    | True                                                |
| auth_mode         | psk                                                 |
| description       | VPN between OpenStack router and Cisco ASA firewall |
| dpd               | {"action": "hold", "interval": 30, "timeout": 120}  |
| id                | 598e981b-6b3b-4521-aaa4-8273de804402                |
| ikepolicy_id      | b250861a-4e42-4c9b-b807-120f1fefbc4c                |
| initiator         | bi-directional                                      |
| ipsecpolicy_id    | 88435b95-8cb7-4bd6-8cdc-3ba2c70e8476                |
| local_ep_group_id |                                                     |
| local_id          |                                                     |
| mtu               | 1500                                                |
| name              | VPN-to-CiscoASA-1                                   |
| peer_address      | 185.160.252.4                                       |
| peer_cidrs        | 172.24.27.0/25                                      |
| peer_ep_group_id  |                                                     |
| peer_id           | 185.160.252.4                                       |
| project_id        | aa9c0db4ac974d2d8feb71f145e22160                    |
| psk               | 67BDRYKpA9bYRMu2                                    |
| route_mode        | static                                              |
| status            | PENDING_CREATE                                      |
| tenant_id         | aa9c0db4ac974d2d8feb71f145e22160                    |
| vpnservice_id     | 9194fb3e-fba9-4b2a-9ba5-c6cbd03c848e                |
+-------------------+-----------------------------------------------------+
```

And you can see those IPSec Site Connections using `neutron ipsec-site-connection-list`

### Checking the connection came up

If all is well you should be able to see the connection has come up, and on the OpenStack side you should see something like this:

```console
[root@ukfastserver ~]# neutron ipsec-site-connection-list
+--------------------------------------+-------------------+-----------------+-----------+--------+
| id                                   | name              | peer_address    | auth_mode | status |
+--------------------------------------+-------------------+-----------------+-----------+--------+
| 598e981b-6b3b-4521-aaa4-8273de804402 | VPN-to-CiscoASA-1 | 185.160.252.4   | psk       | ACTIVE |
+--------------------------------------+-------------------+-----------------+-----------+--------+
```

On the Cisco ASA logs you should see something like the following:

```console
ukfast-fw-1# show logging
Aug 24 2017 16:58:42: %ASA-6-113009: AAA retrieved default group policy (DfltGrpPolicy) for user = 46.37.188.24
Aug 24 2017 16:58:42: %ASA-5-713119: Group = 46.37.188.24, IP = 46.37.188.24, PHASE 1 COMPLETED
Aug 24 2017 16:58:42: %ASA-5-713076: Group = 46.37.188.24, IP = 46.37.188.24, Overriding Initiator's IPSec rekeying duration from 0 to 4608000 Kbs
Aug 24 2017 16:58:43: %ASA-5-713049: Group = 46.37.188.24, IP = 46.37.188.24, Security negotiation complete for LAN-to-LAN Group (46.37.188.24)  Responder, Inbound SPI = 0x2b4a1133, Outbound SPI = 0xce8c73ac
Aug 24 2017 16:58:43: %ASA-6-602303: IPSEC: An outbound LAN-to-LAN SA (SPI= 0xCE8C73AC) between 185.160.252.4 and 46.37.188.24 (user= 46.37.188.24) has been created.
Aug 24 2017 16:58:43: %ASA-6-602303: IPSEC: An inbound LAN-to-LAN SA (SPI= 0x2B4A1133) between 185.160.252.4 and 46.37.188.24 (user= 46.37.188.24) has been created.
Aug 24 2017 16:58:43: %ASA-5-713120: Group = 46.37.188.24, IP = 46.37.188.24, PHASE 2 COMPLETED (msgid=033c8971)
```

### Example "running-config" on the Cisco ASA side

```console
object-group network ukfastserver-vpn.local
 network-object 172.24.27.0 255.255.255.128
object-group network ukfastserver-vpn.remote
 network-object 192.168.3.0 255.255.255.0
!
access-list acl_out extended permit ip object-group ukfastserver-vpn.remote object-group ukfastserver-vpn.local
access-list acl_in extended permit ip object-group ukfastserver-vpn.local object-group ukfastserver-vpn.remote
access-list ukfastserver-split-vpn extended permit ip object-group ukfastserver-vpn.local object-group ukfastserver-vpn.remote
!
nat (inside,any) source static ukfastserver-vpn.local ukfastserver-vpn.local destination static ukfastserver-vpn.remote ukfastserver-vpn.remote no-proxy-arp route-lookup
!
crypto ipsec ikev1 transform-set esp-aes256-sha esp-aes-256 esp-sha-hmac
crypto ipsec security-association pmtu-aging infinite
crypto map vpnmap 10 match address site-to-site
crypto map vpnmap 10 set pfs
crypto map vpnmap 10 set peer 46.37.188.24
crypto map vpnmap 10 set ikev1 transform-set esp-aes256-sha
crypto map vpnmap interface outside
crypto isakmp identity address
!
crypto ikev1 enable outside
crypto ikev1 policy 10
 authentication pre-share
 encryption aes-256
 hash sha
 group 2
 lifetime 86400
!
tunnel-group 46.37.188.24 type ipsec-l2l
tunnel-group 46.37.188.24 ipsec-attributes
 ikev1 pre-shared-key 67BD88KpA9bY0Mu2
```

```eval_rst
.. title: Site-To-Site VPN In eCloud Flex
.. meta::
    :title: Site-To-Site VPN In eCloud Flex | UKFast Documentation
    :description: Detailed guidance on setting up a site-to-site VPN between eCloud Flex and various endpoints
```
