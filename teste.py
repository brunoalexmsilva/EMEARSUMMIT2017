import urllib.parse
import requests

url = 'http://maps.googleapis.com/maps/api/geocode/json?address=athens'
json_data = requests.get(url).json()
county = json_data['results'][0]['address_components'][1]['long_name']
print(county)
