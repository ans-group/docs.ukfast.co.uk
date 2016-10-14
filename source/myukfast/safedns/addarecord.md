# Adding an A record to an existing domain

Before you can add a subdomain or an `A` record to your domain, you must login to the My UKFast client area and access the SafeDNS service, which can be located under the `Services` drop-down menu at the top of the client area.

Once logged in, and in the SafeDNS system, start by selecting the domain you wish to manipulate. In our example, we're using `example.domain`, which isn't a real/valid domain name. Once you've selected the domain, you will want to start by selecting `Add Record` under the `A Records` section:

![No A Records](files/addarecord1.png)

You will presented with a series of fields, as such:

![Blank A Record](files/addarecord2.png)

We need to fill in these fields with the information we want. So in our example, I want `www.example.domain` and I want to point it at `0.0.0.0`. If you want to add more than one record, simply click `Add Record` again and a new set of text fields will appear.

Once you're happy you've added the `A` records you want, just click `Save Records` at the bottom of the page and your DNS zone will be updated. These updates can take upwards of 24 hours to propagate around the world and as such, might be visible to you straight away.
