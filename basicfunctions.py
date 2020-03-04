import json

# Get endpoint name from console
def get_endpoint(SpecifiedHostname): #TODO Allow multiple endpoints to be entered into an array
    print("Provide endpoint name: ")
    SpecifiedHostname = input() #TODO Add input checking/verification
    confirmation = 'The Hostname {} was provided'
    print('')
    print(confirmation.format(SpecifiedHostname))
    return SpecifiedHostname

# Output endpoint information to console
def basic_output(r):
    print('')
    status = "Status Code: {} - {}"
    print(status.format(r.status_code,r.json()['result_description']))
    #print(r.status_code)
    #print(r.json()['result_code'])
    #print(r.json()['result_description'])
    print(r.json()['result_content'])  #TODO Break-down results from the JSON output.
    print('')

# Retrieve credential information from credentials.json
# TODO Allow specification of JSON file instead of hard-code?
def GetCredentials():
    with open('credentials.json', 'r') as f:
        credentials = json.load(f)
    return credentials