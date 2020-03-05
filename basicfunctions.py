#############################################################
#  Last Revised: 3/4/2020                                   #
#  GitHub: https://github.com/eliminat/ApexCentralAPIClient #
#  Description: API client for the Trend Micro Apex Central #
#  API.                                                     #
#                                                           #
#  Trend Micro's Automation Center:                         #
#  https://automation.trendmicro.com/apex-central/home      #
#############################################################

import json

# Get endpoint name from console
def GetEndpoint(): #TODO Allow multiple endpoints to be entered into an array
    SpecifiedHostname = ''
    while SpecifiedHostname == '':
        print("Provide endpoint name: ")
        SpecifiedHostname = input() #TODO Add input checking/verification
    confirmation = 'The Hostname \"{}\" was provided'
    print('')
    print(confirmation.format(SpecifiedHostname))
    return SpecifiedHostname

# Output endpoint information to console
def BasicOutput(r):
    print('')
    status = "Status Code: {} - {}"
    print(status.format(r.status_code,r.json()['result_description']))
    #print(r.json()['result_content'])  #TODO Break-down results from the JSON output.

    # Format JSON list output then print to console
    json_formatted_str = json.dumps(r.json()['result_content'], indent=2)
    print(json_formatted_str)

    print('')

# Prompt for what type of query should be performed.
def QuerySelection():
    print('')
    print('What would you like to do?')

    choice = ''
    while choice == '':
        print('Press \'1\' to query a specific endpoint, or \'2\' to list all Apex One endpoints.')
        print('')
        choice = input()
        if choice != '1' and choice != '2':
            choice = ''
    if choice == '1':
        return GetEndpointInfo()
    elif choice == '2':
        print('Outputting list of endpoints:')
        print('')
        return GetApexOneEndpoints()


# Retrieve basic endpoint information from endpoint name
def GetEndpointInfo():
    # Get endpoint by name to query
    SpecifiedHostname = GetEndpoint()
    # This Query sends a get request to obtain agent info
    QueryString = "?host_name={}"
    useQueryString = QueryString.format(SpecifiedHostname)
    return useQueryString

# QueryString for requesting a list of all Apex One endpoints
def GetApexOneEndpoints():
    return '?product=SLF_PRODUCT_OFFICESCAN_CE'

# Specify action to be done
#def ActionSelection():
    #TODO implement actions
