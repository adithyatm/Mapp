import requests

#URL = "https://tenmilesadithya.happyfox.com/api/1.1/json/ticket/26/staff_update"
#PAYLOAD = "{'text': 'This is a staff update from API' 'staff': 1}"
AUTH = ('43d5e36d980541cc88ce838b54365207', '9bb36ea082ce4c15839c934218c6bc4c')
HEADERS = {'content-type': 'application/json'}


def request_hf(url):
    return requests.get(url, auth=AUTH)
    return

def post_hf(url, payload):

    ticket_response = requests.post(url, auth=AUTH, data=payload)
    print ticket_response.text
    print payload
    return