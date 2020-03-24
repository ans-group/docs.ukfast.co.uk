# Client Veeam Infrastructure

## Core Compenents

### Veeam Backup & Replication Server (VBR Server)

The Veeam Backup & Replication will be the central compenent in your Veeam installation. This holds all of the configuration and manages any jobs that you run. It is run from a Windows Servers and is backed by a SQL, which can on the same Server as SQL Express in small installations or can be split out on to a dedicate Server for large installations. 

### Veeam Proxy Server 

A Proxy Server handles data between your Physical & Virtual infrastructure during Backups to your Veeam repositories. They will also handle the data during a replication to a UKFast Cloud Connect Environment. In very small environments this can be installed on the VBR Server, but it is recommended to split this service out on to its own dedicated Windows Server/s.

### Veeam Backup Repository

A backup repository is used to store local backup files on your site. You will need this set up in advance if you want to use BaaS to perform backup copies to UKFast.

### Network Extension Appliance (NEA Appliance)

An NEA Appliance is a small linux appliance, which is automatically launched by Veeam when you initially connect to a UKFast Cloud Connect environment. This is used to create the Layer 2 connection between sites during a partial failover.

## Environment Sizing 

Veeam have a good document that gives information regarding the sizing of each of the Veeam Components. It's strongly recommended that you pay close attention to this to ensure your jobs optimally. Failure to do so means RPO's will likely be missed and excessive amounts of data could be lost during a DR Scenario. This can be accessed here [Veeam Sizing Summary](https://www.veeambp.com/appendix_a_sizing)

### Concurrent Tasks

One important thing to pay close attention to is the Concurrent tasks that your Veeam Environment can handle. A task is defined as one single VM disk being process; it is often mistaken that a task is the processing of a single VM, which is incorrect.  

The two main compenents that you need to look at concurrency when sizing is Veeam Repositories and Proxies. I will focus on Proxies for this example since that is what will be used for Replications, but the same rules apply for the repositories. It is recommended that you have a CPU Core for each concurrent task.

One large factor of how many concurrent tasks will run at any one time is how you schedule your replication jobs. If you split these out to run at different times, there will be less concurrent tasks than if you were to run them all at once. If you have more jobs running that your environment can handle, VMs will simply queue while they wait for resources to become available.

```eval_rst
.. note::
Proxy Server Sizing Example

If you had a replication job with 5 VMs, all of which had 2 Virtual Disks, you would have a total of 10 tasks that will attempt to run concurrently.

In order to support this you would require at least 10 cores on your Proxy Server/s. This could be split across two smaller proxy servers or one single larger one
```