# this script helps to find case observables by CaseID

#libraries
import requests
import sys
import json
import time
import uuid
from thehive4py.api import TheHiveApi
from thehive4py.query import *
from thehive4py.models import *


# connection information/ credentails
thehive_url = 'TheHive-URL' # http://thehive-url:port
thehive_apikey = 'api-key'

# establishing connection
api = TheHiveApi(thehive_url, thehive_apikey)

case_id = 'Enter Case ID'
response = api.get_case_observables(case_id)
#printing the ovservables
pretty_json = json.dumps(response.json(), indent=4, sort_keys=True)
print(pretty_json)