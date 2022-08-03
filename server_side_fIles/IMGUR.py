import requests
import base64
import json

from base64 import b64encode

from requests.api import request

#auth/client info
client_id = 'e2822da1a215a8e'

headers = {"Authorization": "Client-ID " + client_id}

api_key = '5eeae49394cd929e299785c8805bd168fc675280'

url = "https://api.imgur.com/3/upload"

def url_call():
    #make a post requerst
    j1 = requests.post(
        url,
        headers = headers,
        data = {
            'key' : api_key,
            'image':b64encode(open('recent_trend.png','rb').read()),
            'type' : 'base64',
            'name' : 'recent_trend.png',
            'title' : 'pic 1'
        }
    )
    #saving the j1 to access JSON
    response = j1
    if response.status_code == 200: # Status: OK
            #collect json
            data = response.json()
            #collect data(url)
            info = data['data']
            pic_link = info['link']
            #return link
            return pic_link