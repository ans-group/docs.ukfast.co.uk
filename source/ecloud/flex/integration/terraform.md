# Using eCloud Flex as a Terraform Provider

Terraform is an open-source tool that allows you to code and provision your infrastructure. Terraform have created extensive documentation about their product, and you can learn all about it below:

<https://www.terraform.io/>  

<https://www.terraform.io/docs/index.html>

## Connecting your Openstack project

A provider in Terraform manages API interactions with external resources (eg. eCloud Flex) and exposes all the relevant data sources available for you to use.

In order to define a provider, you need to create a `provider block`.

```yaml
provider "openstack" {
  user_name   = "<username>"
  tenant_name = "<tenant-name>"
  password    = "<password>"
  auth_url    = "https://api.openstack.ecloud.co.uk:5000/v3"
}
```

The username and password are the same credentials that you would use to authenticate with the [Horizon dashboard](https://api.openstack.ecloud.co.uk/auth/login/). The tenant name variable is the name of your project within Openstack. The easiest way to find this, would be to download your [Openstack RC file](https://api.openstack.ecloud.co.uk/project/api_access/openrc/) and view the enviroment variables required to authenticate with Openstack. We already have some [documentation](/ecloud/flex/general/settingvars.html) that details how to go through this. You'll need to use the value of the `OS_PROJECT_NAME` variable for your tenant name.

After you've added eCloud Flex as a provider, you can then use resource blocks to perform tasks in your project. The below example spins up a simple instance in your project.

```yaml
resource "openstack_compute_instance_v2" "test-instance" {
  name            = "test-instance"
  image_id        = "6f526ede-0b07-4e7f-be83-84f474ebcd2e"
  flavor_id       = "24bd8e8c-5575-439a-8f51-289c79e5175a"
  key_pair        = "key-pair"
  security_groups = ["default"]

  network {
    name = "my_network"
  }
}
```

```eval_rst
.. warning::
  Warning: We do not support the use of third-party applications such as Terraform, and we will not be able to diagnose errors within your code.
```

You can find the full configuration reference, resource types and further details [here](https://www.terraform.io/docs/providers/openstack/).

```eval_rst
.. meta::
   :title: Using eCloud Flex as a Terraform Provider
   :description: How to use eCloud Flex as a terraform provider
   :keywords: ecloud, flex, terraform, openstack, IaC, provider, integration
```
