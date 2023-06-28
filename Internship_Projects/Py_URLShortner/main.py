import requests

def shorten_link(full_link, link_name):
    API_KEY='8d417892be571df42145eb9f9a61f3cec3b97'
    BASE_URL=' https://cutt.ly/api/api.php'

    payload = {'key':API_KEY, 'short':full_link, 'name':link_name}
    request = requests.get(BASE_URL,params=payload)
    data = request.json()
    short_link = data['url']['shortlink']
    print('Short Link:', short_link)
    
link = input("Enter the Link:")
title= input("Enter the Title:")

shorten_link(link,title)
    

