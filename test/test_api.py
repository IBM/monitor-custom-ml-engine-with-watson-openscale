# import the necessary packages
import ast
import json
import os
import pprint
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

pp = pprint.PrettyPrinter(indent=4)

# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = "http://" + IP_ADDR + ":" + PORT + "/v1/deployments/resnet50_non_compliant/online"
IMAGE_PATH = "dog.jpg"

# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

# submit the request
r = requests.post(KERAS_REST_API_URL, files=payload).json()

b = ast.literal_eval(json.dumps(r))
pp.pprint(b)
