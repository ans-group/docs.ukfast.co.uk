# Connecting to MySQL via SSH Tunnelling

MySQL is a popular target to a wide-range of attacks worldwide. While by default, it is configured to only listen on `localhost`, which means that it can only be accessed by processes running on the same server. A lot of developers connect to MySQL remotely, so MySQL is then opened publically, which introduces security risks.

In this guide we'll discuss how you can create an SSH tunnel to connect to MySQL remotely without the need to open MySQL to the public.

## What is SSH Tunnelling

SSH tunnelling allows a remote user to redirect traffic from one network port to another. It creates a tunnel between a client computer and a server over the encrypted channel SSH, allowing remote users to pass traffic to the server as though the traffic originated locally to the server. This becomes extremely useful when connecting to services such as `MySQL`, as it's best practice to keep the MySQL port closed and MySQL bound to localhost only.

## SSH Tunnelling with MySQL Workbench

### Creating a new connection
- Start by opening MySQL Workbench
-  Next to MySQL Connection, click the `+` button.

Below are the Parameters you will need to fill in:

| Parameters | Description |
|-|-|
| Connection Name | A name for the connection that uniquely identifies the connection you're making.  |
| SSH Hostname | The IP address of the server you're connecting to, followed by the port. With UKFast installations, the default SSH port is `2020`. For example, `1.2.3.4:2020`. |
| SSH Username | The username you use to SSH onto the server. |
| SSH Password / SSH Key File | This is the SSH password or the SSH key for your server. |
| MySQL Hostname | As we're connecting via an SSH Tunnel, this will likely be `127.0.0.1`. |
| MySQL Server Port | The default for this is `3306` |
| Username | The MySQL user that you're connecting as. As we're connecting locally, it will need to be a user which has the host set to `localhost`.  |
| Password | The MySQL password for the MySQL user.  |

```eval_rst
.. seealso::
   Note:
     When entering passwords, MySQL Workbench offers users the ability to store passwords in a Vault, which is encrypted on your machine. See `MySQL - The Password Storage Vault <https://dev.mysql.com/doc/workbench/en/wb-mysql-connections-vault.html>`_ for more information.
```

### Testing the connection
- Once you've entered all the above parameters, click `Test Connection`.
- You may receive a prompt about the fingerprint not being recognised. If this is the first time connecting to the server and you're confident that the details you've entered are correct, click **Yes**.

This should return **Successfully made the MySQL connection**. Click **OK**, and then **OK** again to save the configuration. If this is unsucessful due to incorrect MySQL credentials, check that the user you're connecting with is set with the host `localhost`.

## SSH Tunnelling with Other Clients (Windows)
While most MySQL clients support SSH tunnelling, some clients do not. Using PuTTY, we can create an SSH Tunnel systemwide, so that you can connect to MySQL on `localhost:3306`, which will route the traffic to the server. To do this, follow the following steps:

- If you don't already have PuTTY, you can download it [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html). Download the 32/64-bit MSI (most modern operating systems are 64-bit, so if unsure, try this first). Open the downloaded `.exe` and go through the installation steps.
 - Once installed, open PuTTY. Below are the values to enter, along with their description.

 ### Configuring PuTTY with SSH Tunnelling

 #### Session
 On PuTTY, on the left side, you can see the different categories for values. Start off by selecting Session, and fill in the values below:

 | Value | Description |
|-|-|
| SSH Hostname | Your SSH username followed by the IP address of the server you're connecting to. For example, `root@1.2.3.4` |
| SSH Port | The default SSH port for UKFast servers is `2020`, otherwise, try `22`. |
| Saved Sessions | Enter a name to uniquely identify this connection.  |

 #### Tunnels
 On the left menu, scroll down and select Tunnels (under `Connection` > `SSH` > `Tunnels`). This is where we will configure the SSH tunnel.

 | Value | Description |
|-|-|
| Source Port | `3306` is the default MySQL port. |
| Destination | `localhost:3306` |
| Radio Button: Local | `Local` forwards a local port to a remote server. |
| Radio Button: Auto | Keep this on `Auto`  |

Click `Add`.

#### Optional: Key Based Authentication
If you're using SSH Keys to authenticate, go to `Connections` > `SSH` > `Auth`. Here you can browse for your SSH private key.

### Saving and testing your configuration
- Once you've done the above steps, go back to Session and click `Save`. This saves your configuration under the name you specified under Saved Sessions.
- Whenever you now open putting, you will be able to load your configuration by selecting the Saved Sessions name and clicking `Load`.

Click `Open` to open your SSH session and Tunnel!

You'll now be able to connect to MySQL with your client by specifying the host as localhost and the port as `3306`. The traffic will then be tunnelled through SSH to the server.

## Conclusion
We've covered a couple of different ways of connecting to MySQL using SSH tunnels. While we cannot cover every MySQL client, this provides you with all the values and information you'll need to get connected to a MySQL instance through an encrypted SSH tunnel, allowing you to lock down your MySQL port and create users with the host set as localhost.

```eval_rst
  .. title:: Connecting to MySQL via SSH Tunnelling
  .. meta::
     :title: Connecting to MySQL via SSH Tunnelling| UKFast Documentation
     :description: A guide on how to connect to a MySQL instance through an SSH tunnel.
     :keywords: ukfast, linux, mysql, ssh, database, security, cloud, server, virtual
```
