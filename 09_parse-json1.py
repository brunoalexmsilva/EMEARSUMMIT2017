import urllib.parse
import requests

main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
address = 'san jose'
key = 'AIzaSyAwP_WJSMYC73kgFTo4oJHMl1hI4JZXTUo'

"""
urlencode convert spaces into %20 to be accepted in the address
"""
url = main_api + urllib.parse.urlencode({'address': address}) + '&key=' + key

json_data = requests.get(url).json()
"""
print(json_data)
"""
"""
print(url)
json_status = json_data['status']
print('API Status: ' + json_status)
"""

formatted_address = json_data['results'][0]['formatted_address']
print['formatted_address']

