#!/usr/bin/env python

import os
import requests

SERVER_HTTP = 'http://0.0.0.0:5000'

try:
    os.environ['IP_ADDR']
    os.environ['PORT']
    IP_ADDR=os.environ.get('IP_ADDR')
    PORT=os.environ.get('PORT')
    SERVER_HTTP = "http://" + IP_ADDR + ":" + PORT
except:
    print("Did not find exported IP_ADDR and PORT. Using 'http://0.0.0.0:5000'.")

DEPLOYMENTS_URL = SERVER_HTTP + "/v1/deployments"

header = {'Content-Type':'application/json'}
r = requests.get(DEPLOYMENTS_URL, headers=header)

print(str(r.text))
