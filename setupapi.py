#############################################################
#  Last Revised: 3/4/2020                                   #
#  GitHub: https://github.com/eliminat/ApexCentralAPIClient #
#  Description: API client for the Trend Micro Apex Central #
#  API.                                                     #
#                                                           #
#  Trend Micro's Automation Center:                         #
#  https://automation.trendmicro.com/apex-central/home      #
#############################################################

import base64
import jwt
import hashlib
import requests
from Crypto.PublicKey import RSA
import time
import json
import os
import sys

# Create Checksum
def create_checksum(http_method, raw_url, headers, request_body):
        string_to_hash = http_method.upper() + '|' + raw_url.lower() + '|' + headers + '|' + request_body    
        base64_string = base64.b64encode(hashlib.sha256(str.encode(string_to_hash)).digest()).decode('utf-8')
        return base64_string   

# Create security token
def create_jwt_token(appication_id, api_key, http_method, raw_url, headers, request_body,
                     iat=time.time(), algorithm='HS256', version='V1'):
    checksum = create_checksum(http_method, raw_url, headers, request_body)
    payload = {'appid': appication_id,
               'iat': iat,
               'version': version,
               'checksum': checksum}
    token = jwt.encode(payload, api_key, algorithm=algorithm).decode('utf-8')
    return token

# Retrieve credential information from credentials.json
# TODO Allow specification of JSON file instead of hard-code?
def GetCredentials():
    # Verify file exists
    if os.path.exists ('credentials.json'):
        with open('credentials.json', 'r') as f:
            credentials = json.load(f)
        return credentials
    else:
        print('Unable to retrieve credentials. credentials.json does not exist.')
        sys.exit()

# Generate Headers for Query
def GenerateQueryHeaders(useQueryString, useRequestBody, credentials, productAgentAPIPath):

        # currently Canonical-Request-Headers will always be empty
        canonicalRequestHeaders = ''


        jwt_token = create_jwt_token(credentials["Application ID"], credentials["APIKey"], 'GET',
                              productAgentAPIPath + useQueryString,
                              canonicalRequestHeaders, useRequestBody, iat=time.time())
        return {'Authorization': 'Bearer ' + jwt_token, 'Content-Type': 'application/json;charset=utf-8'}


# Generate Headers for Action
def GenerateActionHeaders(useQueryString, useRequestBody, credentials, productAgentAPIPath):

        # currently Canonical-Request-Headers will always be empty
        canonicalRequestHeaders = ''


        jwt_token = create_jwt_token(credentials["Application ID"], credentials["APIKey"], 'POST',
                              productAgentAPIPath + useQueryString,
                              canonicalRequestHeaders, useRequestBody, iat=time.time())
        return {'Authorization': 'Bearer ' + jwt_token, 'Content-Type': 'application/json;charset=utf-8'}