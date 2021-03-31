# Windows Firewall


## Creating Rules

* Windows firewall can be used alongside your network based hardware firewall to offer an extra layer of security. In order to create rules in windows firewall, please follow the below guide


Select start, then select control panel from the lift of available icons, once the control panel has loaded, please select Windows firewall, you will now be presented with the windows firewall configuration window as below


![Windows Firewall](files/firewall/firewallbasic.png)

Please select "Advanced Settings" from the left hand side of the window, and you will now be presented with the "Windows Firewall with Advanced Security" window as below

![Windows Firewall Advanced](files/firewall/firewalladvanced.png)

Select the Inbound rules item from the available options on the left hand side of the window, now select "New Rule..." from the actions pane on the right hand side of the window.

The "New Inbound Rule Wizard" will now be displayed as below, the first pane of the wizard asks you choose the type of rule which you want to create, please select "Port" and select next

![Rule Type](files/firewall/in1.PNG)

The next pane asks you to choose the protocol and Ports which you wish to configure the rule for as below, please choose from TCP and select "Specific local ports", once you have selected those options, please enter `3399` in the "Specific local ports" field and select next

![Protocol and Ports](files/firewall/in3.PNG)

You will now be asked to specify the action which you wish the rule to carry out, in this instance, please select "Allow the connection" as below and select next.

![Action](files/firewall/in4.PNG)

The next pane is the "Profile" pane, in this pane, you will need to select on which type of connection does the rule apply i.e from a public or private network connection, for this demonstration, please select all 3 options as below

![Profile](files/firewall/in5.PNG)

The Final Pane asks you to provide a name and a description for your rule, please enter an appropriate name, in this case Alt RDP port as below and Select Finish

![Name](files/firewall/in6.PNG)

You will now be returned to the Advanced firewall menu where the list of inbound rules will be displayed, now included in the list is your newly created rule as below

![Created](files/firewall/newinrule.PNG)


* The process for creating an outbound rule is identical to the above guide, you simply select Outbound rules from the left hand menu of the advanced firewall screen.

## Enabling and Disabling rules

The process to enable and disable rules in windows firewall is extremely simple, to do so,

* Select start, and then select control panel, once control panel has launched, select windows firewall
* Now select Advanced settings from the left hand side of the windows firewall pane.
* You will now be presented with the Advanced firewall options, select the Type of rule that you wish to enable or disable (Inbound rule or outbound rule),
* Locate the rule you are looking for in the list, and right click on it
* Select "Disable Rule" or "Enable Rule" as appropriate from the resulting context menu as below

![Enable/Disable](files/firewall/enabledisable.PNG)

## Enabling or Disabling Windows Firewall

In order to enable or disable windows firewall, please follow the simple steps below

 Select start, and then control panel, once control panel has launched, select windows firewall, you will now be presented with the windows firewall pane as below

![Windows Firewall](files/firewall/firewallbasic.png)

Select "Turn Windows Firewall on or off" from the left hand menu (Please note, your user account will need administrator privileges to do so)

You will now be presented with a window titled "Customise settings for each type of network" as below, please select the appropriate setting which suits your needs

![Enable/Disable](files/firewall/firewallenabledisable.PNG)

```eval_rst
  .. title:: Using Windows Firewall
  .. meta::
     :title: Using Windows Firewall | UKFast Documentation
     :description: An in-depth guide to using Windows Firewall
     :keywords: ukfast, windows, firewall, security, rules, virus, scanner, server, cloud
```
