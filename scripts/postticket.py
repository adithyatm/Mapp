import json
import requests	

def test():
	url = "https://tenmilesadithya.happyfox.com/api/1.1/json/ticket/26/staff_update"
	payload = '{"text": "This is a sample update  made via API - - 3", "staff": 1}'
	auth = ('43d5e36d980541cc88ce838b54365207', '9bb36ea082ce4c15839c934218c6bc4c')
	headers = {'content-type': 'application/json'}
	res = requests.post(url,auth=auth,data=payload, headers=headers)
	return (res.text, res.status_code, res.headers.items())


if __name__ == '__main__':
	app.debug = True
	app.run()