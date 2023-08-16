# this script helps to count all alerts in TheHive

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

# find and print all alerts in TheHive
response = api.find_alerts()

data = json.loads(response.json())

# counting the total number of alerts from the json we got
if isinstance(data, list):
    num_alerts = len(data)
elif isinstance(data, dict):
    # In case the JSON data is a dictionary with an 'alerts' key containing a list of alerts
    num_alerts = len(data.get('alerts', []))
else:
    # Handle the case where the data is not in the expected format
    num_alerts = 0

print("Number of alerts:", num_alerts)