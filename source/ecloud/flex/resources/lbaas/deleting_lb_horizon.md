# Deleting Load Balancers in the Horizon interface

Unfortunately the process for deleting a load balancer using the Horizon dashboard isn't as simple as we would like, however this guide should detail all the necessary steps to remove the load balancer from your project.

The order for removal is as follows:

1. Health Monitors
2. Pool Members
3. Pools
4. Listeners
5. Load Balancer

You must remove every instance of the previous resource before removing the next. For example, you would have to remove all pool members before removing the pool, or you would have to remove all listeners before removing the load balancer etc.

1. Health Monitors

    From the main Load Balancers menu (Project / Network / Load Balancers) you need to click on the Load Balancer that you'd like to remove. From here, you can see a list of the listeners attached to that Load Balancer. If you click on the name of each Listener, it'll take you to a details page, and in here it'll tell you the `Default Pool ID`. If you click on this, it'll give you the pool details. Finally, in here you can see the `Health Monitor ID`, and if you follow this link, you can remove the Health Monitor by clicking the drop-down menu in the top right corner, and selecting `Delete Health Monitor`.

2. Pool Members

    Once you've deleted the Health Monitor in Step 1, it'll drop you back into the `Pool Details` screen. Look for a button called `Add/Remove Pool Members`, and in here, you will need to remove all the Allocated Members. Once you do this, you will see that there are `No items to display` on the `Pool Details` screen.

3. Pools

    When they are no members left in the Pool, you will be able to remove the Pool using the drop-down menu and selecting `Delete Pool`. This should then drop you back into the `Listener Details` page.

4. Listeners

    Provided that you have removed the pool, and the `Default Pool ID` now has a value of `None`, you will be able to remove the listener using the drop-down menu in the right corner, and selecting `Delete Listener`.

5. Load Balancer

    Steps 1-4 will need to be repeated until all listeners in the load balancer have been removed, and you see `No items to display` in the listener list. At this point, you will be able to remove the Load Balancer using the top right corner drop-down menu and selecting `Delete Load Balancer`.

If you are still having problems removing your Load Balancer after following this guide, please contact our UKFast Support team by [raising a ticket](https://my.ukfast.co.uk/pss/create) or by calling the [dedicated support line](https://www.ukfast.co.uk/contact.html).

```eval_rst
   .. title:: Deleting a Load Balancer in the Horizon Dashboard
   .. meta::
      :title: Deleting a Load Balancer in the Horizon Dashboard
      :description: A guide detailing how to remove load balancers using the Horizon dashboard
      :keywords: ecloud, flex, cloud, load balancers, lbaas, neutron, horizon, guide, delete, load, balancer
```
