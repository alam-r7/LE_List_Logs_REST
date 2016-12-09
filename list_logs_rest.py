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
		logset_name = log['logsets_info'][0]['name']
		log_name = log['name']
		logs[logset_name] = {}
		log_sets[logset_name] = {}
		log_sets[logset_name] = log['logsets_info'][0]['id']
	for log in resp['logs']:
		logset_name = log['logsets_info'][0]['name']
		log_name = log['name']
		logs[logset_name][log_name] = {}
		logs[logset_name][log_name] = log['id']
	return logs, log_sets

if __name__ == '__main__':
	response = make_request()
	logs, log_sets = handle_request(response)
	print "log keys"
	print str(logs) + '\n'
	print "log set keys"
	print str(log_sets) + '\n'