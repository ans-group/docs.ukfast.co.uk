#Veeam Replication Jobs

There are a number of thoughts and considerations that need to be taken before setting up your replication jobs to UKFast Cloud Connect Infrastructure. This will ensure that jobs will run as reliably as possible, storage is used optimally and your replication jobs stay in compliant with the required RPO's.

## Splitting VMs Between Replication Jobs
The main question when setting up replication jobs is how do you split your VMs in to different replication jobs. Different people will give different answers on this, as there is no one best way, so you need to evaluate what works best for yourselves. You should group VMs based on the following points.

### RPO (Recovery Point Objective) and Retention periods
Your RPO is the last point in time that you will be able to failover to. This is defined per replication job by selecting how often replications occur in the 'Schedule' section. Veeam will allow you to select from 15 minutes up to as high as monthly; we would generally recommend a 1-4 hour RPO for your critical VMs, but needs to be a business decision.

Your retention period is how long restore points are kept for, which you can use to failover to. This is also defined per replication job, but in the 'Job Settings' section by choosing 'Restore Points to Keep'. The max number of replication restore points is 28 due each of them being stored as a VM snapshot on UKFasts infrastructure. Each snapshot will store the changes made since the last restore point and therefore have the potential to use a considerable amount of your storage at UKFast depending on your rate of data change. The retention period is the number of restore points x your schedule frequency. 

```
#### Retention Period Example  
If you have a job that has 7 restore points and runs once an hour, the retention period would be 7 x 1 hour = 7 hour retention.
```

It is important to review each VM individually to decide what RPO they require and only set low RPOs on the VMs that need it. The lower the RPO means more regular snapshots on the VMs, more storage required to meet longer retention periods, potentially more network bandwidth used and more Veeam resources required to meet the higher concurrent tasks (bigger or more proxy servers). Often VMs like webservers can have higher RPO's of a once a day due to them not having a large amount of data change day to day.

### VM Sizes and Data Change
The size of VMs and how much data change that occurs on them is important to take in to consideration when deciding which VMs are grouped together in replication jobs. If you were to group together multiple large VMs with a high amount of data change, they will attempt to run at the same time and could take up all of the Veeam resources; this would likely cause other replications to sit idle potentially missing their RPO. These large VMs should be split out, so they don't all run at once, while many smaller VMs can be put in to the same job due to each replication being able to finish quickly.

## Storage Utilisation 
Running off the back of the rentention periods and data change for VMs is the storage required at UKFast for replication Jobs. The more restore points and the longer retention you have, coupled with the amount of data change, the more storage you will use out of your Cloud Connect quota.

```
#### Storage Utilisation Example  
Continuing with the previous example where there is a VM with 7 restore points and runs once an hour. Lets say this VM is 1000GB in size and has a data change of 10GB per hour. Each restore point on that VM would be saved as a 10GB Snapshot on UKFast's Infrastructure and therefore take 1070GB of your storage quota.  
```

## Summary
Once you are happy with all of the factors above you can start configuring your replication jobs in Veeam. If you have a large VMware estate that needs replicating it is worth noting that you will likely not get the schedule and configuring perfect first time round and that you can tweak/reconfigure jobs as and when needed.

[Configuring Veeam Replication Jobs](configuring_a_replication_job.md)
