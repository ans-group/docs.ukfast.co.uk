# eCloud Flex flavours and configurations

Each instance on eCloud Flex comes in a variety of configurations, known as "flavours" in OpenStack terminology. The resources available for each of these flavours are shown in the table below:

```eval_rst
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| Flavour Type    | Flavour        | Disk Size (GB) | vCPUs | Memory (GB) | IOPS | Network (Mbps) |
+=================+================+================+=======+=============+======+================+
| Small           | UKF2-small-1x0 | 20             | 1     | 0.5         | 500  | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| Small           | UKF2-small-1x1 | 20             | 1     | 1           | 1000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| General Purpose | UKF2-std-2x2   | 60             | 2     | 2           | 1000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| General Purpose | UKF2-std-4x4   | 60             | 4     | 4           | 1000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| General Purpose | UKF2-std-8x8   | 60             | 8     | 8           | 1000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High Memory     | UKF2-mem-1x8   | 60             | 1     | 8           | 2500 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High Memory     | UKF2-mem-2x16  | 60             | 2     | 16          | 2500 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High Memory     | UKF2-mem-4x32  | 60             | 4     | 32          | 2500 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High Memory     | UKF2-mem-8x64  | 60             | 8     | 64          | 2500 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High IO         | UKF2-io-1x2    | 60             | 1     | 2           | 5000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High IO         | UKF2-io-2x4    | 60             | 2     | 4           | 5000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High IO         | UKF2-io-4x8    | 60             | 4     | 8           | 5000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High IO         | UKF2-io-8x16   | 60             | 8     | 16          | 5000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High CPU        | UKF2-cpu-2x12  | 60             | 2*    | 12          | 3000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High CPU        | UKF2-cpu-4x24  | 60             | 4*    | 24          | 3000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High CPU        | UKF2-cpu-6x36  | 60             | 6*    | 36          | 3000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
| High CPU        | UKF2-cpu-8x48  | 60             | 8*    | 48          | 3000 | 10,000         |
+-----------------+----------------+----------------+-------+-------------+------+----------------+
```

 *\* ***High CPU*** flavours have an increased clock speed, providing superior performance over other flavours with comparable numbers of vCPUs.

For more regarding eCloud Flex flavour types please see [this article](/cloud/flex/nova/newinstances.html).


## Block Storage volumes

Additional storage for your eCloud Flex instances is available through attachable Block Storage volumes, based on [OpenStack Cinder](https://docs.openstack.org/cinder/latest/).  Block Storage is available in SATA, SSD and PCIe tiers, with each tier offering increasing IOPS and improved access latency:

* **SATA** volumes offer up to 500 IOPS, and are recommended for storage of large files which are accessed infrequently, or for log files
* **SSD** volumes will perform in excess of 5,000 IOPS, and are recommended for frequently accessed files, databases and web files
* **PCIe** volumes bring performance of over 50,000 IOPS, and are recommended for high performance databases and applications

For pricing information and to quickly calculate your cloud costs, use our [eCloud Flex calculator](https://www.ukfast.co.uk/calculate-ecloud-flex.html).


```eval_rst
.. meta::
    :title: eCloud Flex Flavours | UKFast Documentation
    :description: Detailed guidance on the resources for each eCloud Flex Flavour
    :keywords: ecloud, flex, volume, instance, flavour, flavor, RAM, memory, CPU, clock speed, IOPS, network
```
