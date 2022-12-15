import requests
import json

webhook_url="https://fbed-103-134-162-101.in.ngrok.io/main"

data={'name':'','Channel_URL':''}

r=requests.post(webhook_url,data=json.dumps(data),headers={'Content-Type':'application/json'})