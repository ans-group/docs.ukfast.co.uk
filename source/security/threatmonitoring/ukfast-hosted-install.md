# Installing Threat Monitoring on a UKFast hosted server

```eval_rst
.. warning::
   This documentation is for setting on a UKFast hosted server with Threat Monitoring. Instructions on how install Threat Monitoring and Response on a non-UKFast hosted server can be found in our [Installing Threat Monitoring on a non-UKFast server](/security/threat-monitoring/non-ukfast-install) documentation.
```

Threat Monitoring and Threat Response can be installed on servers that are hosted with UKFast, allowing you to secure and protect all parts of your UKfast hosted IT infrastructue via one centrilised threat defence platform.

To begin, log into MyUKFast and visit the Threat Monitoring new agent configuration page https://my.ukfast.co.uk/threat-monitoring/configuration then select `UKFast` from the `Hosting Type` drop-down option.

![setup-type](files/setup-ukfast-select-type.png)


To install UKFast Threat Monitoring on a UKFast hosted server, follow these steps:

**[1. Select a server](#add-api-token)** to install Threat Monitoring

**[3. Configure and install](#configure-and-install)** threat monitoring onto your server.


```eval_rst
.. warning::

   Threat Monitoring only supports a specific set of operating systems and configurations. Please make sure your server meets the minimum required specification and required requirements as defined in our [System Requirements](/security/threat-monitoring/system-requirements) documentation.

```

## 1) Select a server

Firstly, using the list shown on the configuration page, select the server you want to install with Threat Monitoring by pressing the blue `Add Threat Monitoring` button, aas shown below.

![setup-type](files/setup-ukfast-select-server.png)

You may filter the list of shown server by the IP Address, Name or hostname of the server. Simply select the search type using the `Search By` drop down and enter your search criteria ion the next box provided, as shown below.

![setup-type](files/setup-ukfast-search-server.png)

Adding Threat Monitoring to a server will consume a Threat Monitoring credit. Your remaining Threat Monitroing and Threat Response credits is shown at the top of the configuration page.


## 2) Configure and install

Once your chosen server(s) have been selected, they will appear towards the bottom of the page in an `Install On` section. 

You can remove a server from the `Install On` list via the red bin icon.

If you would also like to install Threat Response into any of these selected servers, simply select the `THREAT RESPONSE` check mark next to the server. This will consule a Threat Response credit, as shown below.

![setup-type](files/setup-ukfast-add-response.png)

Once you are happy with your selectiob, press the `Install Agent ` button to launch the automated installation process.

When the servers have been queued for automation, you will see a green success message like the below.

![setup-type](files/setup-ukfast-success.png)

The automated installation process normally takes 5 minutes per server. Once the installation process has completed you will start to see data for the server in your Threat Monitoring dashboard, view alerts and run vulnerability scans.

If you do encounter any issues during installation, please get in contact with UKFast support.


```eval_rst
.. meta::
     :title: Installing Threat Monitoring on a non-UKFast server | UKFast Documentation
     :description: Guidance on installing UKFast's Threat Monitoring on a non-UKFast server
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up

```eval_rst
