# Going Live

```eval_rst
   .. title:: Webcelerator | Going Live
   .. meta::
      :title: Webcelerator | Going Live | UKFast Documentation
      :description: Guide to going live with Webcelerator from UKFast
```

When you've completed your testing and feel confident using the Webcelerator, you should change the DNS for the domains to point to the Webcelerator VIP(s). We would change the DNS 'A' records for example.com and www.example.com to your Webcelerator's VIP(s). Once DNS has finished propagating, you should find your site is now active through the Webcelerator. Remember to remove your local hosts file entry so you can see your public domain.

With regards to DNS itself, most DNS changes can take up to [24 hours](/domains/domains/dnspropagation) to propagate globally (and sometimes longer). You can reduce this time by changing your domain's TTL value to 30 minutes at least 24-48 hours before you plan on changing your DNS 'A' records. This should reduce the amount of time it takes to propagate the DNS changes. If you host your DNS through SafeDNS, you should speak with your account manager to get SOA controls enabled for your domains.

We've stressed the importance of testing because of the amount of time it takes to propagate a DNS change. **It's not possible to roll back instantly if you notice a problem with the way your site and Webcelerator interact.**
