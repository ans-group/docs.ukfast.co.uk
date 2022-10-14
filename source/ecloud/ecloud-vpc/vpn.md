# VPC

In eCloud VPC you have the ability to set up Site-to-site IPSec VPN's. These can be used to enable connectivity from external devices or between different eCloud VPC Routers.


### How to setup a VPN

Select the region you want to create the VPN in using the dropdown on the left hand menu and navigate to the VPNs section.

![VPN View](files/vpn-vpnview.png)

#### Services

A VPN Service has a one-to-one mapping with a Routers in eCloud VPC. This means if you want to have a VPN to two different Routers, you will need to create a separate VPN Service for each of them.

Select "Create Service", choose a name, select the relevant VPN and Router, then select "Create Service".

![VPN Service](files/vpn-vpnservice.png)

#### Endpoints

A VPN Endpoint is where the IPSec VPN will terminate at the eCloud VPC side. A VPN Endpoint has a One-to-One mapping with a VPN Service, but you can have multiple Endpoints mapped to the same Service.

Select "Create Endpoint", choose a name and select the VPN Service you would like this Endpoint to be mapped to. You then have the option to choose either an existing Floating IP (external IP) or request a new one. Finally, select "Create Endpoint" to create the VPN Endpoint (this could take a few minutes to complete).

![VPN Endpoint](files/vpn-vpnendpoint.png)

#### Sessions

A VPN Session will link to the a VPN Service and Endpoint you have created and contain all of the configuration required to set up the VPN tunnel on the eCloud VPC side.

Select "Create Session", choose a name and then select the VPN Service and Endpoint you would like this Session to use.

The Profile Group defines what encryption settings are applied, such as the Ciphers. It is critical that the profile used in eCloud VPC matches the configuration of the remote device or the tunnel will not come up. We have a range of generic profiles which are detailed [here](vpn.md#profiles).

The Local IP will automatically be selected, as it is defined in the Endpoint you will have already created.

The "Remote IP" will be the external IP of the device you are setting up a VPN connection to. This will either an external device or the external IP of another eCloud VPC Endpoint.

The "Local Networks" are the local eCloud VPC internal IPs and/or Subnets, which you would like to be part of this VPN Tunnel. These can only include IPs or Subnets, which are defined on networks associated with the Router the Service is linked to. It is critical that these match the configuration on the remote device.

The "Remote Networks" are the internal IPs and/or Subnets from the remote site, which you would like to be part of this VPN Tunnel. It is critical that these match the configuration on the remote device.

A "Pre-Shared Key (PSK)" needs to be defined, which will need to match the PSK on the remote device.

![VPN Session](files/vpn-session.png)


##### Profiles

| Profile Name    | Phase 1 - Encryption | Phase 1 - Integrity | Phase 1 - DH Group | Phase 1 - PRF | Phase 1 - SA Lifetime | Phase 2 - Encryption | Phase 2 - Integrity | Phase 2 - SA Lifetime | Phase 2 - PFS |
|-----------------|----------------------|---------------------|--------------------|---------------|-----------------------|----------------------|---------------------|-----------------------|---------------|
| IKEv1 Weak      | AES-128              | SHA-1               | 2                  | -             | 86400                 | AES-128              | SHA-1               | 28800                 | No            |
| IKEv1 Medium    | AES-256              | SHA-256             | 5                  | -             | 28800                 | AES-256              | SHA-1               | 3600                  | 5             |
| IKEv2 Medium    | AES-256              | SHA-256             | 14                 | SHA-256       | 86400                 | AES-256              | SHA-256             | 28800                 | 14            |
| IKEv2 Strong    | AES-256              | SHA-256             | 19                 | SHA-256       | 28800                 | AES-256              | SHA-256             | 3600                  | 19            |
| IKEv2 Strongest | AES-256-GCM          | -                   | 21                 | SHA-512       | 28800                 | AES-256-GCM          | -                   | 3600                  | 21            |



```eval_rst
   .. title:: Virtual Private Cloud (VPC)
   .. meta::
      :title: Virtual Private Cloud (VPC) | UKFast Documentation
      :description: Virtual Private Cloud (VPC)
      :keywords: ecloud, ecloud VPC, MyUKFast, VPC, Virtual Private Cloud
```
