# Common Changes

## Adding a new server behind the load balancer

## Replacing an expired SSL certificate

## Temporarily remove a target server from behind the load balancer

You may want to remove a target server from the load balancer to stop traffic going to it temporarily. For instance
to run updates or to be able to restart the server.

This will immediately take the target server out of load. If you're using "Source" as a load balancing method to send 
users to the same target server each time, this could disrupt their session. You should first drain the server 

Navigate to the load balancer you want to edit in [MyUKFast](https://my.ukfast.co.uk/load-balancers) then click on `Target Groups` at the top of the load balancer screen

[![Target Group Tab](files/inactive_target_1_small.png)](files/inactive_target_1.png)

Click the target group which contains the target server which you want to temporarily remove

[![Target Group Listview](files/inactive_target_2_small.png)](files/inactive_target_2.png)

Click the `Targets` tab at the top of the screen

[![Target Group Overview](files/inactive_target_3_small.png)](files/inactive_target_3.png)

Click `Edit` next to the target server you want to remove from load, notice how it currently says `Active` next to
the target.

[![Targets Listview](files/inactive_target_4_small.png)](files/inactive_target_4.png)

Uncheck the "Target is Active" box near the bottom of the form, then press save

[![Target Edit Screen](files/inactive_target_5_small.png)](files/inactive_target_5.png)

Notice that the tag in the target server you have just edited has changed to `Inactive` and you now have a message about
pending configuration updates to the load balancer. Click the `deployments screen` link

[![Targets Listview](files/inactive_target_6_small.png)](files/inactive_target_6.png)

As long as the rest of your configuration is valid, you will see a `Deploy Now` button. Press this and wait for the screen to reload. Your changes have now been deployed to the load balancer and the target server you have edited will
no longer be recieving traffic.

[![Deployment Screen](files/inactive_target_7_small.png)](files/inactive_target_7.png)

To allow traffic to be sent to the server again, repeat the above steps but check the "Target is Active" box instead.

```eval_rst
   .. title:: Load Balancers | Common Changes
   .. meta::
      :title: Load Balancers | Common Changes | UKFast Documentation
      :description: Making common changes to UKFast load balancers
```