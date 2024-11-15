import requests
api_url = "http://10.0.0.82:8000/countries"
response = requests.get(api_url)
print(response.json())

