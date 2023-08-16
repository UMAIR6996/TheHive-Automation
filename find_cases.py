# this script helps to find all cases in TheHive

#libraries
import requests
import sys
import json
import time
import uuid
from thehive4py.api import TheHiveApi
from thehive4py.query import *
from thehive4py.models import *
import csv

# connection information/ credentails
thehive_url = 'TheHive-URL' # http://thehive-url:port
thehive_apikey = 'api-key'

# establishing connection
api = TheHiveApi(thehive_url, thehive_apikey)

# requesting all cases data
response = api.find_cases()
# printing all cases data
pretty_json = json.dumps(response.json(), indent=4, sort_keys=True)
print(pretty_json)