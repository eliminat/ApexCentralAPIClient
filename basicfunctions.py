#############################################################
#  Last Revised: 4/8/2020                                   #
#  GitHub: https://github.com/eliminat/ApexCentralAPIClient #
#  Description: API client for the Trend Micro Apex Central #
#  API.                                                     #
#                                                           #
#  Trend Micro's Automation Center:                         #
#  https://automation.trendmicro.com/apex-central/home      #
#############################################################

import json
import sys

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

# Get new location from console
#TODO Need to clarify what to specify for the location
def GetLocation():
    SpecifiedLocation = ''
    while SpecifiedLocation == '':
        print("Provide new location path: ")
        SpecifiedLocation = input() #TODO Add input checking/verification
    confirmation = 'The location \"{}\" was provided'
    print('') 
    print(confirmation.format(SpecifiedLocation))
    return SpecifiedLocation

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
def ActionSelection():
    print('')
    print('What would you like to do?')


    choice = ''
    while choice == '':
        print('1) Isolate an endpoint')
        print('2) Restore an isolated endpoint')
        print("3) Relocate an endpoint")
        print('4) Uninstall the Security Agent from an Endpoint')
        print('5) Quit')
        print('')
        
        choice = input()
        try:
            if int(choice) < 0 or int(choice) > 5:
                choice = ''
                break
        except:
            choice = ''
    
    
    
    # Choice options are temporary filler for validation
    # Choice 1 - Isolate Endpoint
    
    if choice == '1':
        SpecifiedEndpoint = GetEndpoint()
        print('')
        payload = {
            "host_name":SpecifiedEndpoint,
            "act":"cmd_isolate_agent",
            "allow_multiple_match":False
        }
        return json.dumps(payload)

    # Choice 2 - Restore an isolated endpoint
    elif choice == '2':
        SpecifiedEndpoint = GetEndpoint()
        print('')
        payload = {
            "host_name":SpecifiedEndpoint,
            "act":"cmd_restore_isolated_agent",
            "allow_multiple_match":False
        }
        return json.dumps(payload)

    # Choice 3 - Relocate an endpoint
    elif choice == '3':
        SpecifiedEndpoint = GetEndpoint()
        SpecifiedLocation = GetLocation()
        print('')
        payload = {
            "host_name":SpecifiedEndpoint,
            "act":"cmd_relocate_agent",
            "allow_multiple_match":False,
            "relocate_to_folder_path":SpecifiedLocation
        }
        return json.dumps(payload)

    # Choice 4 - Uninstall an agent on an endpoint
    elif choice == '4':
        SpecifiedEndpoint = GetEndpoint()
        payload = {
            "host_name":SpecifiedEndpoint,
            "allow_multiple_match":False,
            "act":"cmd_uninstall_agent"
        }
        command_sent = 'Command to uninstall \"{}\" has been sent.'
        print('') 
        print(command_sent.format(SpecifiedEndpoint))
        return json.dumps(payload)

    # Choice 5 - Exit
    elif choice == '5':
        print('Choice is 5')
        sys.exit()