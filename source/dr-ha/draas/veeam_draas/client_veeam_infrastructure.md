# Client Veeam Infrastructure

## Core Components

### Veeam Backup & Replication Server (VBR Server)

The Veeam Backup & Replication Server is the central component in your Veeam installation. This holds all of the configuration data and manages any jobs that you run. It is run from a Windows server and backed by SQL, which can run on the same server as a SQL Express instance in small installations or can be split out on to a dedicated server for larger installations. 


### Veeam Proxy Server 

A proxy server handles data between your physical & virtual infrastructure during backups to your Veeam repositories. The proxy servers will also handle the data during a replication to a UKFast Cloud Connect Environment. In very small environments this can be installed on the VBR Server, but it is recommended to split this service out on to its own dedicated Windows Server/s.


### Network Extension Appliance (NEA Appliance)

An NEA Appliance is a small Linux appliance, which is automatically launched by Veeam when you initially connect to a UKFast Cloud Connect environment. This is used to create the Layer 2 connection between sites during a partial failover. You will have one NEA Appliance for every internal Network/VLAN that you replicate to UKFast.


## Environment Sizing 

Veeam has a good document that gives information regarding the sizing of each of the Veeam components and it's strongly recommended that you pay close attention to this to ensure your jobs run optimally. Failure to do so means RPOs will likely be missed and data could be lost during a DR Scenario. This document can be accessed here:  [Veeam Sizing Summary](https://www.veeambp.com/appendix_a_sizing)


### Concurrent Tasks

One important thing to pay close attention to is the concurrent tasks that your Veeam environment can handle. A task is defined as one single VM disk being processed. It is often assumed that a task is the processing of a single VM, which is incorrect.

The two main components that you need to look at concurrency when sizing is Veeam repositories and proxies. This example focuses on proxies, since these are used for replications, but the same rules apply for repositories. It is recommended that you have a CPU core for each concurrent task; you can set the limit for concurrent tasks in the properties of your proxy server in the Veeam console (this should match the number of vCPUs, if you set a higher value you risk replications not performing optimally).

One large factor of how many concurrent tasks will run at any one time is how you schedule your replication jobs. If you split these out to run at different times there will be fewer concurrent tasks than if you were to run them all at once. If you have more jobs running than your environment can handle, VMs will simply queue while they wait for resources to become available.


```eval_rst
.. note::

   Proxy server sizing example

   If you had a replication job with five VMs, all of which had two virtual disks, you would have a total of 10 tasks attempting to replicate concurrently.

   In order to support this you would require at least 10 cores on your proxy server/s. This could be split across two smaller proxy servers or one single larger one.
```

```eval_rst
   .. meta::
      :title: Client Veeam Infrastructure | UKFast Documentation
      :description: Client infrastructure required to connect to UKFast Veeam Cloud Connect
      :keywords: ukfast, cloud, ecloud, public, hosting, infrastructure, vmware, draas, veeam, connect, dr, replication, backup
```
