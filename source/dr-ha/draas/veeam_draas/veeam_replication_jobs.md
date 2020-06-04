# Veeam Replication Jobs

There are a number of thoughts and considerations that need to be taken before setting up your replication jobs to UKFast Cloud Connect Infrastructure. Pre-planning ensures that jobs run as reliably as possible, storage is used optimally and your replication jobs remain compliant with the required RPOs (recovery point objectives)

## Splitting VMs Between Replication Jobs
The main question when setting up replication jobs is how to split VMs into different replication jobs. There are different schools of thought on the best way to set these up, so evaluate what works best for your organisation. You should group VMs based on the following points.

### RPO (Recovery Point Objective) and Retention periods
Your RPO is the last point in time that you will be able to failover to. This is defined per replication job by selecting how often replications occur in the 'Schedule' section. Veeam allows you to select from every 15 minutes to once a month; UKFast would generally recommend an RPO of one to four hours for your critical VMs, but needs to be a business decision.

Your retention period is how long restore points are kept for, which you can use to failover to. This is also defined per replication job, but in the 'Job Settings' section by choosing 'Restore Points to Keep'. The max number of replication restore points is 28, due to each of them being stored as a VM snapshot on UKFast’s infrastructure. Each snapshot stores the changes made since the last restore point and therefore has the potential to use a considerable amount of your storage at UKFast, depending on your rate of data change. The retention period is `[number of restore points] x [your schedule frequency]`.

```eval_rst
.. note::

    Retention Period Example

    If you have a job that has 7 restore points and runs once an hour, the retention period would be: 
    
    7 x 1 hour = 7 hour retention.
```

It is important to review each VM individually to decide what RPO they require, and to only set low RPOs on the VMs that need it. A lower RPO means more regular snapshots on the VMs and more storage required to meet longer retention periods, as well as potentially more network bandwidth used and more Veeam resources required to meet the higher concurrent tasks (bigger or more proxy servers). Often VMs such as webservers can afford to have higher RPOs of once a day, as they tend to have fewer data changes.

### VM Sizes and Data Change
The size of VMs and how much data change occurs on them is important to take into consideration when deciding which VMs are grouped together in replication jobs. If you were to group together multiple large VMs with a high amount of data change, they will attempt to run simultaneously and could utilise all of your Veeam resources. This would likely cause other replications to sit idle, potentially missing their RPO. These large VMs should be split out so they don't all run at once, while many smaller VMs can be put into the same job due to each replication finishing quickly.

## Storage Utilisation 
Running off the back of the retention periods and data change for VMs is the storage required at UKFast for replication jobs. The more restore points and the longer retention you have, coupled with the amount of data change, the more storage you will use out of your UKFast Cloud Connect quota.

```eval_rst
.. note::
    Storage Utilisation Example 

    Continuing with the previous example where there is a VM with 7 restore points and runs once an hour. Let's say this VM is 1000GB in size and has a data change of 10GB per hour. Each restore point on that VM would be saved as a ~10GB Snapshot on UKFast's Infrastructure and therefore take ~1070GB of your storage quota (this figure could be higher if there has been a lot of additional data written rather than just changes).  
```

## Summary
Once you are happy with all of the factors above you can start configuring your replication jobs in Veeam. If you have a large VMware estate that needs replicating it is worth noting that you will likely not get the schedule and configuration of jobs perfect first time round and will need to tweak them as time goes on.

[Configuring Veeam Replication Jobs](configuring_a_replication_job.md)


```eval_rst
   .. meta::
      :title: Veeam Replication Jobs | UKFast Documentation
      :description: A guide to setting up Veeam replication jobs
      :keywords: ukfast, cloud, ecloud, public, hosting, infrastructure, vmware, draas, veeam, connect, dr, replication, backup, failover