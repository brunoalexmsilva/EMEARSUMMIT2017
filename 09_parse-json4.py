import urllib.parse
import requests

main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
address = 'san jose'
key = 'AIzaSyAwP_WJSMYC73kgFTo4oJHMl1hI4JZXTUo'

while True:
    address = input('Address: ')
    if address == 'quit' or address == 'q':
        break

    url = main_api + urllib.parse.urlencode({'address': address}) + '&key=' + key
    print(url)

    json_data = requests.get(url).json()
    json_status = json_data['status']
    print('API Status: ' + json_status)

    if json_status == 'OK': 
        formatted_address = json_data['results'][0]['formatted_address']
        print(formatted_address)

