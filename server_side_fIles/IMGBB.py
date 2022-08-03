import base64
import requests

IMGBB_API_KEY = 'd343a394534eeb067389939d0ecb3a53'

def url_call():
    #open recent_trend.png as a file    
    with open("recent_trend.png", "rb") as file:
        #api url to upload
        url = "https://api.imgbb.com/1/upload"
        #parameters for the api
        payload = {
            "key": IMGBB_API_KEY,
            "image": base64.b64encode(file.read()),
            #we can add a "name" - optional
        }
        #request
        res = requests.post(url, payload)
        #saving the res to access JSON
        response = res
        #if the code was successful
        if response.status_code == 200: # Status: OK
            #collect json
            data = response.json()
            #enter data key
            info = data["data"]
            #obtain URL for image
            url = info["url_viewer"]
            #print the url 
            return url #this needs to be changed to return the server response