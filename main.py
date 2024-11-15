import requests
import json
import sys

json_file = sys.argv[1]

with open(json_file) as json_data:
    data = json.load(json_data)
    for ip in data["ips"]:
        api_url = "http://{ipaddr}:8000/stat".format(ipaddr=ip)
        response = requests.get(api_url)
        print(response.json())

