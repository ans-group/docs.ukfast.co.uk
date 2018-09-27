# DDoS Policy

We have an anti-DDoS monitoring service deployed across our entire network. The threshold is currently set to 200,000 packets per second (200k pps) or 3072Mbps of traffic. If the traffic patten for any one IP address is exceeding those thresholds, the IP address will be automatically black-holed. If after 30 minutes the attack is still ongoing, the IP address will remain black-holed until a further check 30 minutes after that, and so on.

If one of your IPs is under attack but isn't tripping the threshold, you can always phone or raise a ticket requesting that we black-hole the IP manually. This can be useful if traffic to one particular IP is affecting the rest of your solution.

If you're repeatedly affected by DDoS attacks, we do offer a DDoS mitigation platform. Your account manager will have more information on this service.
