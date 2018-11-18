# Phyton Script: Enter Sub Questions
# Written By: Stephen Lam
# Date: 23-Dec-2015
# Screen resolution Specification: (1680,1050)

# Import GUI Intyerface
import urllib.parse
import requests
import json


main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = input('Address: ')
	
	if address == 'quit':
		break
	
	url = main_api + urllib.parse.urlencode({'address':address})
	print (url)
	
	json.data = requests.get(url).json()
	print(json.data)
	json_status = json.data['status']
	print('API Status: ' + json_status)
	
	if json_status == 'OK':
		for each in json.data['results'][0]['address_components']:
			print(each)
			formatted_address = json.data['results'][0]['formatted_address']
			print()
			print(formatted_address)


