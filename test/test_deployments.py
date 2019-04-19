#!/usr/bin/env python

import os
import requests
import sys

try:
    os.environ['IP_ADDR']
    os.environ['PORT']
except:
    print("Please export IP_ADDR and PORT of modify this file with the vars")
    sys.exit(1)

IP_ADDR=os.environ.get('IP_ADDR')
PORT=os.environ.get('PORT')


DEPLOYMENTS_URL = "http://" + IP_ADDR + ":" + PORT + "/v1/deployments"
header = {'Content-Type':'application/json'}
r = requests.get(DEPLOYMENTS_URL, headers=header)

print(str(r.text))
