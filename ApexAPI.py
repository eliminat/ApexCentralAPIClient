import jwt
import hashlib
import requests
import time
import json
import urllib3
from setupapi import *
from basicfunctions import *

# Get Credentials from the credentials.json file
CREDENTIALS = GetCredentials()
# This is the path for ProductAgents API
PRODUCTAGENTAPIPATH = '/WebApp/API/AgentResource/ProductAgents'

# Disable warning from Python that HTTPS is Unverified.
# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Get endpoint by name to query
SpecifiedHostname = GetEndpoint()


# This Query sends a get request to obtain agent info
QueryString = "?host_name={}"
useQueryString = QueryString.format(SpecifiedHostname)
useRequestBody = ''


# Header information for requests
#headers = {'Authorization': 'Bearer ' + jwt_token}

headers = GenerateHeaders(useQueryString, useRequestBody, CREDENTIALS)

#perform request and store response
response = requests.get(CREDENTIALS["URL"] + PRODUCTAGENTAPIPATH + useQueryString, headers=headers, data=useRequestBody, verify=False)

# Output basic info of endpoint to console.
BasicOutput(response)