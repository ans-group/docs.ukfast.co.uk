# Getting Started

## Load Balancer Overview

Once your new load balancer has been launched, it will appear in the [load balancers section](https://my.ukfast.co.uk/load-balancers) of your MyUKFast account. Any load balancers which haven't had their initial deployment will be marked with "Initial Setup Required".

Clicking on the load balancer will take you to the screens which you use to configure and deploy your new load balancer.

![Initial Setup Required](files/getting_started_1_small.png)

From the load balancer overview screen, you can work your way through the onboarding wizard. If you already know how to set up a UKFast load balancer, you can skip this wizard and work your way through the screens yourself by clicking "Skip Onboarding Wizard".

You can also rename a load balancer to help you remember which load balancer is which if you have multiple in your account. This is done by clicking the pencil icon highlighted in blue on the screenshot below, typing in the new name and clicking the save icon.

```eval_rst
.. warning::

   The primary IP on this page is not a VIP for you to use, it is the IP of the actual load balancer device. You should set up your virtual IPs when configuring your listeners.

```

![Renaming a load balancer](files/getting_started_2_small.png)

A load balancer needs configuring with three aspects as a minimum:
- At least one target group
- At least one target within that target group
- At least one listener

There are also optional aspects that can be configured within a load balancer, for example:
- Access IP controls
- SSL certificates
- Access control rules

For more information on these terms, check out the [key terms page](key-terms.html).

## Target Groups

The first step of configuring a load balancer is to add a target group. You can do this by clicking "Add Target Group" in the onboarding wizard or by going to the "Target Groups" tab and clicking "Create Target Group".

![Add Target Group](files/getting_started_3_small.png)

Fill the form in and then press "Create Target Group" at the bottom right of the form.



#### Load Balancing Methods

There are 3 ways to balance traffic between the target servers, know as the load balancing method:
* **Round Robin:** Sends traffic first to server A, then to server B, then to server A and so on. This has a slightly lower overhead but can lead to hot-spots developing if sticky sessions are in use.
* **Least Connections:** Intelligently sends traffic to the target server that has the least connections at any one time.
* **Source:** The source IP address of the request is hashed and then this is used to determine which target server should be used. It ensures that the IP will always end up on the same target server providing no servers are added or removed.

### Monitoring

By default the load balancer will check the default site for each target server to see if it responds with a status code between 200 and 399. If the target server doesn't respond (or responds with a status code outside this range) the target server will be marked as unhealthy and no traffic will be sent to it until it recovers.

You can use the target group configuration screen to manage which URL to hit on a target server as either a HEAD, OPTIONS or GET request if you don't want to use the default site. For example if you have a health check URL which performs additional checks before returning a 200 you could put the host, port and path of this URL into the form.

If you've got a Lumen or Laravel PHP application and want to create a health check URL for your application, why not take a look at our [Health Check Package](https://github.com/ukfast/laravel-health-check)?

### Advanced Settings

The other settings on this page are for more advanced control over your load balancer. We've set them to sensible defaults and most people won't need to change them.

## Targets

Once you've created a target group, you can start adding targets to it. Targets are the servers that the load balancer will share requests between, you can add as few or as many as you would like. You can do this by clicking "Add Target" in the onboarding wizard or by going to the "Targets" tab and clicking "Create Target".

![Add Target](files/getting_started_4_small.png)

Fill the form in and then press "Create Target" at the bottom right of the form.

### Basic Configuration

In this section of the form you are able to give an optional name to the target server to help you recognise it easily in the future. The IP and port fields are both required and tell the load balancer which server and port to send any requests to. If the server is hosted by UKFast you are able to search for the server by  partial name or IP in the IP box and then choose the correct IP. Otherwise copy and paste the IP in from your server provider.

The Weight field is used to specify how much traffic each target will receive from the load balancer. For instance if you have two targets both with a weight of `1` then they will receive equal traffic. If target A has a weight of `1` and target B has a weight of `2` then target B will receive twice as much traffic as target A.

You can set Weight to 0 to "drain" the target. This means that any existing connections will remain open till they close but no new connections will be sent to that target. This is a way to gradually remove a target server from load without disrupting existing users.

### Availability

You can set a target server to only ever receive requests if all the other targets in that target group are failing their health checks. To do this, change the backup option to `Target only available if all other targets are failing health checks`.

If you need to temporarily stop a server from receiving requests (for instance to install updates) you can uncheck the "Target is Active" box and deploy changes. This will stop this target from receiving any requests from the load balancer.

### Advanced Settings

The more advanced settings have already had sensible defaults applied to them so most people won't need to make any changes. If you do need to make changes to the HTTP version, SSL certificate health checks or how many failed health checks it takes for a target server to be classed as unhealthy, you can change these by pressing "Show Advanced Options" at the bottom left of the form.

## Listeners

Once you've created a target group and at least one target, you can add a listener. You can do this by clicking "Add Listener" in the onboarding wizard or by going to the "Listeners" tab from the load balancer overview and clicking "Create Listener".

![Add Listener](files/getting_started_5_small.png)

Fill the form in and then press "Create Listener" at the bottom right of the form.

### Basic Configuration

When creating a new listener you will first need to give it a unique name. The default target group is where traffic from the listeners binds (see next section) will be sent to by default unless you override this behaviour with an access control rule.

### Binds

These are the combinations of Virtual IP and port that this listener will respond to, you can add multiple binds per listener. If you only have one Virtual IP assigned to a load balancer then this will automatically be filled in to the VIP field, otherwise you will get a search box allowing you to select the correct VIP for that bind.

Each listener needs to have at least one bind and can have as many as needed. Click the "Add Bind" button to add a new VIP / Port combination and the red X to delete a bind.

![Binds Input](files/getting_started_6_small.png)

### Additional SSL Settings

You can set this listener to enable HSTS for visitors, this means that the website will always need to have a valid SSL for users to access the website. If your SSL certificate is ever removed or expires, the users browser remembers that there should be an SSL certificate and stops the user accessing the website. **If you are going to enable this setting make sure you have an SSL certificate ready to use.**

You can also enable "Redirect to HTTPS" which similar to HSTS will redirect non HTTPS traffic to HTTPS ensuring the users data is encrypted between their computer and the server. However unlike HSTS this isn't enforced and you can disable this setting if needed in the future.

## First Deployment

Once you have finished configuring your load balancer, it is time to [deploy your changes](deploying-changes.html).

```eval_rst
   .. title:: Load Balancers | Getting Started
   .. meta::
      :title: Load Balancers | Getting Started | UKFast Documentation
      :description: Getting started with UKFast load balancers
```
