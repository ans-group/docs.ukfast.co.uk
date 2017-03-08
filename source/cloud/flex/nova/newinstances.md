
# UKF2 eCloud Flex instances replace UKF1

As of March 2017, a new range of eCloud Flex instance flavours, called UKF2, has replaced the previous UKF1 range.  Full details of the new flavour configurations can be found in [MyUKFast](https://my.ukfast.co.uk/ecloud-flex/16029/pricing.php) (along with pricing) and in the [OpenStack control panel](https://api.openstack.ecloud.co.uk/project/instances/).  You can continue to run existing UKF1 instances, but will not be able to create new ones.

There are a couple of reasons behind this change:

- we wanted to standardise the storage volume size attached to instances, to make it easier for customers to scale up and down between instance sizes as necessary.  All UKF2 instances, with the exception of the Small type, have a 60GB attached volume.  You can scale up and down between General Purpose, High CPU, High Memory and High I/O instances as necessary.  (Please note you won't be able to scale down to a Small instance from one of the other types, as they have a 20GB attached volume).  If you need more storage attached to your instances you can create block storage volumes, choosing from SATA, SSD and PCIe.

- we also wanted to introduce a couple of new flavour types to better cater for the different compute workloads customers need to run.  You can now choose from the following flavour types:

```eval_rst
+-----------------+---------------+---------------+-------------------------+------------------------------------------------------------------------------+
| Flavour type    | Available CPU | Available RAM | Attached storage volume | Ideal workloads                                                              |
+=================+===============+===============+=========================+==============================================================================+
| Small           | 1             | 0.5GB to 1GB  | 20GB                    | small workloads, test and development                                        |
+-----------------+---------------+---------------+-------------------------+------------------------------------------------------------------------------+
| General Purpose | 2 to 8        | 2GB to 8GB    | 60GB                    | a balance of CPU, RAM and storage, good for all-round compute requirements  |
+-----------------+---------------+---------------+-------------------------+------------------------------------------------------------------------------+
| High Memory     | 1 to 8        | 8GB to 64GB   | 60GB                    | a higher RAM to CPU allocation, designed for memory-intensive workloads      |
+-----------------+---------------+---------------+-------------------------+------------------------------------------------------------------------------+
|  High I/O       | 1 to 8        | 2GB to 16GB   | 60GB                    | designed for running databases that need higher I/O performance              |
+-----------------+---------------+---------------+-------------------------+------------------------------------------------------------------------------+
|  High CPU       | 2 to 8        | 12GB to 48GB  | 60GB                    | a higher frequency CPU for workloads that need greater CPU performance      |
+-----------------+---------------+---------------+-------------------------+------------------------------------------------------------------------------+
```

Existing UKF1 instances will continue to operate as normal - we have no plans to end-of-life these any time soon.  However when you want to create new instances, you'll need to choose a UKF2 type.
