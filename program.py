import json 
import requests 

def getdata():
    url="https://myusers.free.beeceptor.com/"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def upload_data():
    answer = getdata()
    return answer