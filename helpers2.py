import requests

URL = "https://api.pipedrive.com/v1/persons?start=0&api_token=cd7e7856f5dc0ae6d5327826438a4729d12fe466"
#PAYLOAD = "{'text': 'This is a staff update from API' 'staff': 1}"
HEADERS = {'content-type': 'application/json'}

def build_contact_info(email):
	open_deals_count = fetch_deal_info(email)
	payload = 

def fetch_deal_info(email):
	res = request_hf(url)
	a = res.json()
	for item in a['data']:
    	if item['email'][0]['value'] == email: 
        	open_deals_count =  item['open_deals_count']
        	break
    return open_deals_count

def request_hf(url, auth = None):
    return requests.get(url, auth=AUTH)


def post_hf(url, payload):
    ticket_response = requests.post(url, auth=AUTH, data=payload)
    print ticket_response.text
    print payload
    return