import requests

apiKey = 'RW_API_KEY'

url = "https://rest.logentries.com/management/logs/"
headers = {'x-api-key': apiKey, 'content-type': 'application/json'}

def make_request():
	response = requests.get(url, headers=headers)
	return response

def handle_request(response):
	log_sets = {}
	logs = {}
	resp = eval(response.text.replace('null', 'None'))
	for log in resp['logs']:
		logs.setdefault(log['logsets_info'][0]['name'], {}).setdefault(log['name'], log['id'])
		log_sets.setdefault(log['logsets_info'][0]['name'], log['logsets_info'][0]['id'])
	return logs, log_sets

if __name__ == '__main__':
	response = make_request()
	logs, log_sets = handle_request(response)
	print "Log keys:"
	print json.dumps(logs, sort_keys=True, indent=4, separators=(',', ': ')) + '\n'
	print "Log Set keys:"
	print json.dumps(log_sets, sort_keys=True, indent=4, separators=(',', ': '))
