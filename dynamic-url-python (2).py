#!/usr/bin/python
import sys
DYNAMIC_DNS_URL = "https://ipv4.cloudns.net/api/dynamicURL/?q=NzM4OTk0Njo1MDQ0MTQ5NzY6ZGI5YWZiZTQ0NjI0YjI0NGMxMTJmMGVjMTkzNDAxYzU5ZDBiYzViMzk3YjU4YzMyZjExYjg0MTNiMmRlODg2NQ"
if sys.version_info[0] < 3:
 import urllib
 page = urllib.urlopen(DYNAMIC_DNS_URL);
 page.close();
else:
 import urllib.request
 page = urllib.request.urlopen(DYNAMIC_DNS_URL);
 page.close();