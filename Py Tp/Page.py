from urllib import request
import requests
import json
page=requests.get(" https://21e0-103-134-162-102.in.ngrok.io")
print(type(page))
print(page.text[:10000])
print(page.url)
page.json()
print(json.dumps(indent=2))