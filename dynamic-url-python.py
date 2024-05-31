#!/usr/bin/python
import sys
DYNAMIC_DNS_URL = "https://ipv4.cloudns.net/api/dynamicURL/?q=NzM4OTk0Njo0OTczNjA5NDY6MTNmOThjNjMwMWVhNDYwY2RmYzA4ODFlOGUzZjk4NGM5OTNmYWM1MjgxZTI4MDIyMWFlYTNjNDVhNzY4NDU1MA"
if sys.version_info[0] < 3:
 import urllib
 page = urllib.urlopen(DYNAMIC_DNS_URL);
 page.close();
else:
 import urllib.request
 page = urllib.request.urlopen(DYNAMIC_DNS_URL);
 page.close();