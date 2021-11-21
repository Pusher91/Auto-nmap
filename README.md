# Auto-nmap

Automatically runs nmap scans against a target ip address.

### Automatic scans:
+ nmap <target> -p- -oN tcp_ping_scan
+ nmap <target> -sV -sC -oN -p \<open ports from previous scan\> -oN tcp_script_scan
+ nmap <target> -p- -sU -sV -oN ping_udp_scan
+ nmap <target> -sU -sV -sC -p \<open ports from previous scan\> -oN udp_script_scan



### Script output:

Scanning for open tcp ports...
+ Finished scanning for open ports. 'tcp_ping_scan' created.
Running nmap scripts against open tcp ports...
+ Finished tcp script scan. 'tcp_script_scan' created.
Scanning for open udp ports...
+ Finished udp ping scan. 'udp_ping_scan' created.
Running nmap scripts against open udp ports...
+ Finished udp script scan. 'udp_script_scan' created.
