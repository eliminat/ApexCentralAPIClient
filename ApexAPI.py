#############################################################
#  Last Revised: 3/4/2020                                   #
#  GitHub: https://github.com/eliminat/ApexCentralAPIClient #
#  Description: API client for the Trend Micro Apex Central #
#  API.                                                     #
#                                                           #
#  Trend Micro's Automation Center:                         #
#  https://automation.trendmicro.com/apex-central/home      #
#############################################################



import jwt
import hashlib
import requests
import time
import json
import urllib3
import sys
from setupapi import *
from basicfunctions import *

# Get Credentials from the credentials.json file
CREDENTIALS = GetCredentials()
# This is the path for ProductAgents API
PRODUCTAGENTAPIPATH = '/WebApp/API/AgentResource/ProductAgents'

useQueryString = ''
useRequestBody = ''

# Disable warning from Python that HTTPS is Unverified.
# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print('')

choice = ''
while choice == '':
    print('Do you want to perform a (Q)uery or an (A)ction? ')
    print('')
    choice = input()
#    print(choice)
    if (choice.lower() != 'q') and (choice.lower() != 'a'):
        choice = ''

if choice.lower() == 'q':
    # Determine which Query to Run
    useQueryString = QuerySelection()

    # Header information for requests
    # headers = {'Authorization': 'Bearer ' + jwt_token}
    headers = GenerateQueryHeaders(useQueryString, useRequestBody, CREDENTIALS, PRODUCTAGENTAPIPATH)
    
    # Perform request and store response
    response = requests.get(CREDENTIALS["URL"] + PRODUCTAGENTAPIPATH + useQueryString, headers=headers, data=useRequestBody, verify=False)
    # Output to console.
    BasicOutput(response)

elif choice.lower() == 'a':
    # Determine which Action to Run
    useRequestBody = ActionSelection()

    # Header information for requests
    # headers = {'Authorization': 'Bearer ' + jwt_token, 'Content-Type': 'application/json;charset=utf-8')}
    headers = GenerateActionHeaders(useQueryString, useRequestBody, CREDENTIALS, PRODUCTAGENTAPIPATH)
    
    # Perform request and store response
    response = requests.post(CREDENTIALS["URL"] + PRODUCTAGENTAPIPATH + useQueryString, headers=headers, data=useRequestBody, verify=False)
    # Output to console.
    BasicOutput(response)




