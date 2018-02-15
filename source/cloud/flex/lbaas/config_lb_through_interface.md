# Creating an eCloud Flex Load Balancer

## Creating a HTTP Load Balancer
First of all, log in to your [eCloud Flex Horizon Dashboard](<https://api.openstack.ecloud.co.uk/project/ngloadbalancersv2/>) and navigate to the **Network** tab, then **Load Balancers** in the menu. If you have no existing Load Balancers, the table presented should be empty.

To proceed, click the **Create Load Balancer** button found to the top right of the interface, which will create a pop-up wizard as shown below.

![createlb](../files/17.png)

![lbwizard](../files/18.png)

Within the Load Balancer Details screen, you will create information on the name you would like to give the Load Balancer, an optional description, an optional IP address to assign to this (one will be generated for you if left blank) and which subnet you would like this load balancer created on. Once this information has been filled in, proceed to the next screen by clicking "Next".

The following screen will then prompt you for the Listener details. A Listener is the interface over which to receive incoming traffic to be distributed amongst the load-balanced pool of members. For example, the following would be an example of incoming HTTP traffic listener.

![lblistenerwizard](../files/19.png)

Additional options with which to configure listeners on are **TCP** and **Terminated HTTPS** (HTTPS Offloading). More listeners can be added later in the process, and existing ones may be modified as required after setting the Load Balancer up for the first time.

Further to this page will be the **Pool Details** in which you must created your first member pool. A member pool is the term used to describe backend servers which will receive the load-balanced traffic from the Listener you specified earlier. For this section of the wizard, you must assign a name to the pool, an optional description and the load balancing method. The three current load balancing methods are described below:

-   `LEAST_CONNECTIONS` will always use the server with the least volume of existing connections to it at present between the load balancer and the instance. This may mean that between requests, clients may use different backends.
-   `ROUND_ROBIN` will use each backend in order and rotate between them on each request, regardless of the current volume of open connections to that backend or the client making the request.
-   `SOURCE_IP` is a way of ensuring clients connecting will always use the same backend between visits or requests so long as the source IP remains identical.

On the next screen you will be required to set up the pool members, which are the backends receiving the traffic from the listener. You will be able to add the instances to the pool with the "Add" button to the right of the instance shown.

![lbmemberpoolwizard](../files/20.png)

For each  of the instances, you will also be able to select the port and weight of these individual backends should you wish to shape the traffic distribution between the instances. The weight value may be set between 1 and 256. The greater the weight set, the greater the share of traffic will be directed to the instance.

On the final screen of the wizard shall be the pool monitor, which determines which members of the pool are active and which are not. Instances which fail this health check are removed from the pool until it can pass the monitor check again. The three type of health monitor types are:

-   `HTTP` which will generate a HTTP request similar to that of a client visit. This method can monitor for the status code returned and the HTTP method used, as well as the URI to test.
-   `PING` will generate an ICMP request on the frequency set to the server. This test is useful to determine the server is online and responsive to network requests, but does not make any checks on the application layer.
-   `TCP` performs a check on the port stipulated in the wizard. For example, if a TCP health check on port 3306 is created, pool members will be suspended from the pool until a TCP handshake can successfully occur.

To finish the wizard, you should now be able to press **Create Load Balancer** which will then provision the load balancer and show in the dashboard for you shortly! If the button remains faded out and unable to be pressed, revisit your previous pages to ensure all fields marked as required (displaying an asterisk next to their field) have been completed.

## Assocating a Floating IP with a Load Balancer

To enable IPv4 access to your Load Balancer from public networks, a Floating IP address must be added. To check if you have a Floating IP address already associated, or what that address is, open the [Load Balancer dashboard](<https://api.openstack.ecloud.co.uk/project/ngloadbalancersv2/>) and click on the Load Balancer you are investigating. On the page you are taken to, a **Floating IP Address** field will become visible with the Floating IP attached to the Load Balancer if one is available, or show "None" if this has not yet set up.

![lbfip](../files/21.png)

Notably, the IP address displayed to the top-left of the interface is the internal IPv4 address of the Load Balancer, but this IP will not be publicly accessible by others outside of your eCloud Flex network.

To attach a Floating IP, use the drop-down icon next to **Edit** to the top right of the interface, and select **Associate Floating IP**.

![lbfipassociate](../files/22.png)

Depending on your existing network configuration, one or two options may be provided. If two categories are presented, the first will be **Floating IP Addresses** where you may directly select the reserved Floating IPs in your account to attach to the Load Balancer. The second, which shall also be visible if one one category is shown, will be **Floating IP Pools**. Selecting this option will ask your network IP pool to automatically reserve a floating IP address for your account, and then continue to associated this address with your Load Balancer for you.

Regardless of which method is chosen to select a Floating IP, clicking the blue **Associate** button will continue to add this to the load balancer, and this should be usable immediately to connect to. To find this Floating IP address, follow the steps outlined in the first part of this section to see the **Floating IP Address Field** found on the Load Balancer page.

```eval_rst
.. meta::
    :title: Creating an eCloud Flex Load Balancer | UKFast Documentation
    :description: Detailed guidance on establishing a load balancing instance on eCloud Flex using the Flex dashboard
```
