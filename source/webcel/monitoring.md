# Monitoring

Webcelerators have the ability to monitor your backend servers to ensure they're responding correctly before sending traffic to them. By default, it will monitor the page returned when you visit the IP address of your server (e.g. `http://198.51.100.10/`). We can configure this to monitor an arbitrary script, including one that isn't on the default site by sending a Host header with the monitoring request.

The Webcelerator considers a backend to be online if the page it's monitoring returns a 200 OK HTTP status code. It can also accept 3xx status codes as 'good', but we would advise against returning anything other than 200 OK as a 'good' status. 4xx and 5xx status codes will mark that backend as offline and remove it from the load balancing rotation.

Having a monitoring script you can control allows you to take a backend out of the load balancer rotation for maintenance or upgrades without affecting the live site, as traffic will automatically be directed to your other servers. If all web servers are unavailable, a maintenance page could be served from the Webcelerator.

Your monitoring script could also connect to your database and run a basic query (`SELECT NOW()` for example) and return an appropriate status code based on whether that connection and request succeeded or not. If you do this, the query you use should return quickly and not put excessive load on the database, as the script will be called every few seconds.

```eval_rst
   .. title:: Webcels | Monitoring Backends
   .. meta::
      :title: Webcels | Monitoring Backends | ANS Documentation
      :description: Useful information on monitoring backends for Webcelerators
      :keywords: monitoring, webcels, webcelerator, ukfast, backend
```
