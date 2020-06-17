# Container Orchestration Engines in eCloud Flex

[Magnum](https://wiki.openstack.org/wiki/Magnum) is an OpenStack API service developed by the OpenStack Containers Team making container orchestration engines such as Docker Swarm, Kubernetes, and Apache Mesos available as first class resources in OpenStack. Magnum uses Heat to orchestrate an OS image which contains Docker and Kubernetes and runs that image in either virtual machines or bare metal in a cluster configuration.

```eval_rst
.. note::
  At present, you will need to contact UKFast Support via. the priority support system to have the relevent Heat permission applied to your user / project.
```

## Installation

You can install the magnumclient package on your system by running the following:

```bash
sudo yum install python-magnumclient
sudo apt-get install python-magnumclient
```

We have a full page of documentation about installing the openstack clients [here](/cloud/flex/general/openstackcli.html).

### Creating a Kubernetes cluster with Magnum

Our Magnum deployment supports all of the engines that Magnum supports (Docker Swarm, Kubernetes and Apache Mesos) however this article details how to create a cluster using the Kubernetes engine.

1. Create an image

   Presuming you have already configured the [relevent environment variables](/cloud/flex/general/settingvars.html) to authenticate with your project, we now need to download an image to upload as our base image for the template. In this example, we found a Fedora [CoreOS](https://getfedora.org/en/coreos/download/) cloud image (qcow2 format) and uploaded it to our project using the `openstack image` command.

   ```bash
   openstack image create --disk-format=qcow2 \
                          --container-format=bare \
                          --file=fedora-coreos.qcow2.xz \
                          --property os_distro='coreos' \
                          coreos
   ```

   Be sure to make a note of your image ID, as we'll be using this in the next step. We must specify the os_distro property in order for the cluster to build correctly. If you're using Fedora Atomic, the os_distro would be `fedora-atomic`.

   Please refer to our other documentation for more information about [managing images](/cloud/flex/resources/storage/managing-images.html).

2. Create the cluster template

    The cluster template does what it says on the tin, it contains a collection of parameters to describe how a cluster can be constructed. We can use the `openstack coe` command to control all-things Magnum.

    ```bash
    openstack coe cluster template create \
            --image 3320c598-e8c0-438b-a1da-d0edf45da362 \
            --keypair development \
            --external-network 544c39f7-7bc7-4abc-b195-68b56d80c8ac \
            --dns-nameserver 8.8.8.8 \
            --flavor 9803b4b8-59a2-4eb8-97ee-9236ef64e987 \
            --master-flavor 5a32c71e-80d5-47ad-9427-d94694f472f9 \
            --docker-volume-size 20 \
            --network-driver flannel \
            --coe kubernetes \
            k8s-template
    ```

    `--image` parameter is the same image that we created in step 1.  

    `--keypair` parameter is the keypair that will be used to spin up the instances in your project.  

    `--external-network` asks for the ID for the external network, and in the case of eCloud Flex, this will be the `vlan2803` network.  

    `--flavor` and `--master-flavor` requires the flavor ID for your `minion` and `master` instances.  

    `--docker-volume-size` asks for the size (in GB) to create the volume which will be attached to your instances. 20GB is sufficient for testing.  

    The remaining flags just specify details about the engine and network drivers, followed by the name of the new template.

3. Create the cluster

    Now that we have the template, we're able to spin up a cluster based on the parameters we established within the template.

    ```bash
    openstack coe cluster create --cluster-template k8s-template\
                                 --node-count 3 \
                                 --master-count 1 \
                                 test-cluster
    ```

    `--cluster-template` needs the name / ID of the template that we created in the previous step.  
    `--node-count` and `--master-count` is the number of master / minion instances that you'd like to create.  
    The final argument is the name of the cluster.

4. Watch the deployment

    You can see the status of the cluster deployment(s) by running the following commands:

    ```bash
    openstack coe cluster list
    openstack coe cluster show <id>
    ```

    The `status` field in the `cluster show` command will detail what the cluster is up to, and will also tell you if anything has gone wrong with the deployment. The error codes are generally quite helpful and will point you in the right direction of resolving the issue. You can also view the status of the Heat template in the [Horizon dashboard](https://api.openstack.ecloud.co.uk/project/stacks/). When the deployment is completed, you'll be greeted by the floating IP addresses for your nodes. You can login to these via. SSH (Port 22) and using the private key that was specified earlier.

5. (Optional) Deleting your cluster

    It's easy to remove a cluster, by running the following command:

    ```bash
    openstack coe cluster delete <id>
    ```

You can find lots of information and further user guides over at the [Openstack documentation for Magnum](https://docs.openstack.org/magnum/latest/user/).

If you need any further assistance, you can contact our UKFast Support team by [raising a ticket](https://my.ukfast.co.uk/pss/create) or by calling the [dedicated support line](https://www.ukfast.co.uk/contact.html).

```eval_rst
.. meta::
   :title: Deploying a Kubernetes cluster using Magnum
   :description: How to use eCloud Flex Magnum to deploy a kubernetes cluster
   :keywords: ecloud, flex, kubernetes, magnum, docker, containers, deployment, cluster, templates
```
