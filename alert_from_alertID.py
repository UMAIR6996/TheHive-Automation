# this script helps to find alerts on the basis of alertID

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

# query alerts on basis of alertID
ALERT_ID = 'Enter alertID'
response = api.get_alert(ALERT_ID)

# receiving the alert data
alert_data = response.json()

# filter one attribute from the alert data
print(alert_data.get('title'))
print(alert_data.get('date'))

# printing the alert data we found by quering for ALERT_ID
pretty_json = json.dumps(alert_data, indent=4)
print(pretty_json)