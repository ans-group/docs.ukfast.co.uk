# Site To Site VPN Dashboard

On the VPN tab of the editor, click the "Details" button on the "Site To Site" Section.

![Site To Site Dashboard](files/editor2_s2s_dash.PNG)

This screen displays information about the currently configured site-to-site VPNs on your firewall.  There is also the option to create a site-to-site VPN by clicking the "Add New" button
at the top of the page.

## Existing Connections

You can see the peer IP and connection status for VPNs configured on the firewall.  If the VPN is connected you can force a termination of the tunnel by clicking the "Rekey Connection" button.  If you click
the "Edit" button you are then given the option to change the Peer IP and/or Pre-shared key in use on the tunnel.

![Edit Peer IP](files/editor2_change_peer_ip.PNG)

Enter the peer IP and PSK into the boxes provided and click "update". If you would like to keep using the same pre-shared key for the new peer then leave the PSK box blank. 

Please note, the change is not made to the firewall until you click "Apply Changes".

## Creating a New Site To Site VPN

If you click the "Add New" button at the top of the page you can configure a new site-to-site VPN on your firewall.

![New S2S VPN](files/editor2_config_new_s2s.PNG)

### Required Elements:

#### Name

Each VPN needs to have a unique name.  This name is administrative and will be used to reference the VPN.

#### Peer IP

This is the public IP or the remote IPSec device where the VPN will be terminating

#### PSK

This is the pre-shared key that will be used on both ends of the VPN to authenticate the tunnel at establishment

#### Zones To Be Accessed

Please select which zones on your firewall you would like to be able to access over the VPN.  This can be further restricted to individual servers by editing the access lists later

#### Remote Subnets

Please enter the remote subnets (encryption domains) that will be accessed over the VPN.

#### IKE Version (IKEv2 is recommended)

Select the IKE version to be used on the VPN.  This setting needs to match at both ends of the VPN as the version are not interoperable.

When these fields are completed please click "Next"

### IKEv1 Options

#### Phase 1

![New S2S VPN v1P1](files/editor2_ikev1_p1.png)

Select the required encryption, dh group and hashing for phase 1.  This will need to match the settings on the remote end.

#### Phase 2

![New S2S VPN v1P2](files/editor2_ikev1_p2.png)

Select the required encryption, dh group and hashing for phase 2.  This will need to match the settings on the remote end.

### IKEv2 Options

#### Phase 1

![New S2S VPN v2P1](files/editor2_ikev2_p1.png)

Select the required encryption, dh group and hashing and prf value for phase 1.  This will need to match the settings on the remote end.

#### Phase 2

![New S2S VPN v2P2](files/editor2_ikev2_p2.png)

Select the required encryption, dh group and hashing for phase 2.  This will need to match the settings on the remote end.


```eval_rst
  .. meta::
     :title: Remote Access VPN Administration | UKFast Documentation
     :description: Remote Access VPN Dashboard
     :keywords: ukfast, firewall, vpn, setup, remove access, AnyConnect, users
```
