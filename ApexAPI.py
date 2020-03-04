import base64
import jwt
import hashlib
import requests
from Crypto.PublicKey import RSA
import time
import json
import urllib3
from setupapi import create_checksum
from setupapi import create_jwt_token
from basicfunctions import get_endpoint
from basicfunctions import basic_output
from basicfunctions import GetCredentials

# Disable warning from Python that HTTPS is Unverified.
# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SpecifiedHostname = 'WIN10-CLOUD-1'

# Retrieve credential information from credentials.json
credentials = GetCredentials()
use_url_base = credentials["URL"]
use_application_id = credentials["Application ID"]
use_api_key = credentials["APIKey"]


# This is the path for ProductAgents API
productAgentAPIPath = '/WebApp/API/AgentResource/ProductAgents'
# currently Canonical-Request-Headers will always be empty
canonicalRequestHeaders = ''

# Get endpoint by name to query
get_endpoint(SpecifiedHostname)


# This sample sends a get request to obtain agent info
QueryString = "?host_name={}"
useQueryString = QueryString.format(SpecifiedHostname)
useRequestBody = ''
jwt_token = create_jwt_token(use_application_id, use_api_key, 'GET',
                              productAgentAPIPath + useQueryString,
                              canonicalRequestHeaders, useRequestBody, iat=time.time())

# Header information for requests
headers = {'Authorization': 'Bearer ' + jwt_token}

#perform request and store response
r = requests.get(use_url_base + productAgentAPIPath + useQueryString, headers=headers, data=useRequestBody, verify=False)

# Output basic info of endpoint to console.
basic_output(r)
