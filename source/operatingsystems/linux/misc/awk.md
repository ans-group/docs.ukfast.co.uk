# The `awk` command

The `awk` command can be used to search through text files by columns. This can be very useful while investigating access logs on the server. A basic use of the `awk` command would be to print the first column of each line in the file. If this was to be done on an access log, this would show the IP the request has been sent from which can potentially help investigate attacks on a server or aid general traffic investigation. An example of this command is below.

```bash
awk '{print $1}' /var/log/nginx/access.log
```

This can be used in conjunction with other commands and more complex commands can be created. The below command will search through the NGINX access logs for today's date and print the IP, the type of request, the page requested and the referrer. This will then sort through the results and order them by amount of unique requests. This will then print the top 20 unique requests from unique IP addresses on the server today and display how many were sent.

```bash
grep "`date +%d/%b/%Y`" /var/log/nginx/access.log | awk '{print $1, $6, $7, $11}' | sort | uniq -c | sort -gr | head -n 20
```

```eval_rst
  .. title:: Using the AWK command in Linux
  .. meta::
     :title: Using the AWK command in Linux | ANS Documentation
     :description: A guide on using the AWK command in Linux
     :keywords: ukfast, awk, command, nginx, search, files, log, cloud, server, virtual
```
