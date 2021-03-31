# Creating eCloud Flex instances using Ansible

Ansible is an open-source software provisioning, configuration management, and application-deployment tool developed by Red Hat. It is generally regarded as one of the leading tools in the DevOps community.

Describing the full scope of Ansible and its usage is clearly out of scope of this article. However, we will attempt to highlight some of the useful ways in which Ansible can be used to automate the creation of your eCloud Flex-based infrastructure.

## The `os_server` module

The brunt of the complicated work here will be carried out by the existing `os_server` module, which is fully documented here:

* <https://docs.ansible.com/ansible/2.9/modules/os_server_module.html>

If you already have Ansible installed then you should already have Python installed too. So there's just one prerequisite package left to install, a `pip` package called `shade`. This will need to be installed on the machine you're running your playbooks from. A simple `pip install shade` should be enough to get you up and running, but to rule out a number of common errors, here's the full set of commands I've had to use in the past to get it installed on a blank system:

```bash
yum install python-pip openssl-devel make gcc python-devel
pip install --upgrade pip
pip install --upgrade setuptools
pip install shade
```

## Creating instances

If you've followed the [Setting Environment Variables for eCloud Flex](/ecloud/flex/general/settingvars) guide, you should already have all the correct environment variables set, so you won't need to specify the otherwise large set of the authentication-based options for the module. You should be able to get away with a fairly lean task that looks like this:

```yaml
  - name: Create 3 VMs
    os_server:
      state: present
      name: ansibletest
      image: CentOS7_2016-01
      flavor: UKF1-io-1x2
      key_name: ansibletest
```

## Working with freshly created instances

By adding `register` to that task, we can capture a lot of information about the freshly created instance. We can then use that information to add the machine to the in-memory inventory, or use them as facts in other tasks. For example, here we see the newly created instance being added to inventory:

```yaml
  - name: Create 3 VMs
    os_server:
      state: present
      name: ansibletest
      image: CentOS7_2016-01
      flavor: UKF1-io-1x2
      key_name: ansibletest
    register: instance

  - name: Add OS instance to inventory
    add_host:
      name: "{{ instance.results.openstack.private_v4 }}"
      groups: openstack
```

The above example shows usage of the `private_v4` fact, but there are many others, which can be shown by using the `debug` module:

```yaml
- name: Show instance variable contents
  debug:
    var: instance
```

## Basic playbook example

The following playbook ties together some of the above functionality to show a relatively trivial example of using a task block to create 3 instances and provision them as web servers. A key pair is created locally for example's sake, but could be generated using the `os_keypair` module if desired. Some relatively pointless / inadvisable actions such as creating a user with password-less sudo access, or adding things to hosts files are carried out so that different elements can be demonstrated.

```yaml
---
- name: Provision 3 web servers
  hosts: localhost
  tasks:
  - name: Install some pre-requisites
    yum:
      name: "{{ item }} "
      state: latest
    with_items:
      - python-pip
      - openssl-devel
      - gcc
      - make
      - git

  - name: Pip install/upgrades for shade
    pip:
      name: "{{ item }} "
      state: latest
    with_items:
      - pip
      - setuptools
      - shade

  - name: Create keypair locally
    shell: ssh-keygen -t rsa -q -N "" -C ansibleexample -b 4096 -f /root/.ssh/ansibleexample
    args:
      creates: /root/.ssh/ansibleexample

  - name: Add new key into OS
    os_keypair:
      state: present
      name: ansibleexample
      public_key_file: /root/.ssh/ansibleexample.pub

  - name: Create 3 VMs
    os_server:
      state: present
      name: "{{ item }}"
      image: CentOS7_2016-01
      flavor: UKF1-io-1x2
      public_ip: no
      key_name: ansibleexample
    with_items:
      - servera
      - serverb
      - serverc
    register: created


  - name: Setup hosts file
    blockinfile:
      dest: /etc/hosts
      marker: "#{mark} ansible managed block for {{ item.openstack.name }}"
      block: |
        {{ item.openstack.private_v4 }} {{ item.openstack.name }} {{ item.openstack.name }}.lab.example.com
    with_items:
      - "{{ created.results }}"

  - name: Add OS servers to inventory
    add_host:
      name: "{{ item.openstack.private_v4 }}"
      groups: openstack
    with_items:
      - "{{ created.results }}"

  - name: Sleep 60 and wait for serverc to get through cloud-init
    wait_for:
      delay: 60
      host: serverc
      port: 22

  - name: Add sysadmin user for engineers to use
    delegate_to: "{{ item }}"
    remote_user: centos
    become: true
    user:
      name: sysadmin
      state: present
    with_items:
      - servera
      - serverb
      - serverc

  - name: Add key to new account
    delegate_to: "{{ item }}"
    authorized_key:
      user: sysadmin
      state: present
      key: "{{ lookup('file', '/root/.ssh/ansibleexample.pub') }}"
      manage_dir: yes
    with_items:
      - servera
      - serverb
      - serverc

  - name: Passwordless sudo for the sysadmin as an example
    delegate_to: "{{ item }}"
    lineinfile:
      dest: /etc/sudoers
      state: present
      line: "sysadmin ALL=(ALL) NOPASSWD: ALL"
    with_items:
      - servera
      - serverb
      - serverc

  - name: Install apache on web servers
    delegate_to: "{{ item }}"
    yum:
      name: httpd
      state: latest
    with_items:
      - servera
      - serverb
      - serverc

  - name: Start and enable web server
    delegate_to: "{{ item }}"
    service:
      name: httpd
      state: started
      enabled: true
    with_items:
      - servera
      - serverb
      - serverc
```

```eval_rst
   .. title:: Using eCloud Flex with Ansible
   .. meta::
      :title: Using eCloud Flex with Ansible | UKFast Documentation
      :description: How to use eCloud Flex with Ansible
      :keywords: ecloud, flex, openstack, ansible, red hat, automation, deployment, configuration, web server
```
