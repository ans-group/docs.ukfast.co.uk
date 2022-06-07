# Failover costs
There are two different types of DRaaS solutions, Public and Private. This will give you a summary of how the DRaaS costs are calculated.

## DRaaS Public Solutions
DRaaS Public solutions replicate in to an eCloud Public environment in the given DRaaS region. This means that when you failover, your VMs will run on shared hypervisors.

In this scenario, there a few parts to the failover costings.

### Recurring costs
You will pay static monthly costs for:
- Per VM
- Per GB storage, at the 600 IOPs tier

### Failover Costs
When you failover, you will pay based on our eCloud Public billing model, pro rata'd hourly.

**Costs do occassionally change, so please get in touch with your Account Manager to receive the latest pricing.**

#### Compute costs
You will pay an hourly fee based on your VM specifications. This is per:
- 1 x vCPU
- 1GB RAM

#### Storage Costs
All customers pay a static monthly charge per GB for the storage they require in DRaaS. This price is based on the 600 IOPs tier.

If a client decides to increase the IOPs tier to 1200 or 2500 on a VM, they will pay the difference in cost pro rata'd hourly when they failover.

```eval_rst
**Costs used in example may not be correct**
For example, if the static storage cost paid is 20p per GB a month and the 1200 IOPs tier costs 30p per GB a month.

The storage failover cost for VMs set to 1200 IOPs would be 10p per GB a month, pro rata'd down to hourly.
```

## DRaaS Private Solutions

DRaaS Private Solutions have a dedicated eCloud solution in the DRaaS region, which will be paid for by the client. Due to this, in most cases failover will not cost anything.

Every DRaaS private solution is different, so this should be confirmed with your Account Manager or Service Manager.



```eval_rst
   .. title:: Veeam Failover Costs
   .. meta::
      :title: Veeam Failover Costs | UKFast Documentation
      :description: Summary of DRaaS failover costs
      :keywords: ukfast,cloud,ecloud,public,hosting,infrastructure,vmware,draas,veeam,connect,dr,replication,backup,failover
```
