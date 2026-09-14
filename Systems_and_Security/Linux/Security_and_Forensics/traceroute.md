---
tags:
  - networking
  - routeur
---
Permet de voir tout les routeurs par lequel passe le réseau avant d'aller sur un site.
```bash
traceroute <site>
```
>[!example] google.com
>```bash
>traceroute google.com
>```
>traceroute to google.com (172.217.22.78), 30 hops max, 60 byte packets  
1  _gateway (172.26.179.254)  4.837 ms  4.821 ms  4.812 ms  
2  192.168.114.9 (192.168.114.9)  5.134 ms  5.126 ms  5.118 ms  
3  192.168.45.153 (192.168.45.153)  4.781 ms  4.773 ms  4.765 ms  
4  * * *  
5  * * *  
6  * * *  
7  * * *  
8  * * *  
9  * * *  
10  * * *  
11  * * *  
12  * * *  
13  * * *  
14  * * *  
15  * * *  
16  * * *  
17  * * *  
18  * * *  
19  * * *  
20  * * *  
21  * * *  
22  * * *  
23  * * *  
24  * * *  
25  * * *  
26  * * *  
27  * * *  
28  * * *  
29  * * *  
30  * * *

