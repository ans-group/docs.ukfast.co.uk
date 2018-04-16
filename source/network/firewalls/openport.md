# Opening ports on your firewall

You can open ports on your shared or dedicated firewall within [MyUKFast](https://www.ukfast.co.uk/myukfast.html). Instructions on viewing your existing firewall configuration are provided in [this guide](viewconfig.html).

## Creating a port group

You may wish to add a Port Group if you don't already have a suitable group set up.  If so, go to the `Port Groups` tab and then create a `New Port Group`.  Select the service you would like to open this port for - either TCP or UDP. Provide a name and description for the port group.

![New Port Group](files/new-port-group.png)

You can add single ports or port ranges that you would like to open.  Once you are happy with the list, click on `Create Group`.

## Adding access rules to open ports

If you already have an existing port group, then you can add the required ports directly to this.  If you have just created a new port group, or the group hasn't previously been used, then you will need to add the actual access list to have the group take effect.

Click `Add Incoming or Outgoing Interface Rule`, select the action as `Permit`, then select the relevant source and destination options. Under `Ports`, select the new Port Group you created.

![Access List SSH Port](files/access-list-ssh-group.png)

Click `Create` and the firewall configuration will be updated.


```eval_rst
  .. meta::
     :title: How to open a port | UKFast Documentation
     :description: How to open a port on your UKFast firewalls
     :keywords: ukfast, firewall, port, ports, open
```
