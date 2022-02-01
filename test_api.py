import pytest 
import requests
import json 

actual = {
  "data": {
    "id": 2,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver",
    "avatar": "https://reqres.in/img/faces/2-image.jpg"
  },
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
url="https://myusers.free.beeceptor.com/"
    

def test_api():
    response = requests.get(url)
    data = json.loads(response.text)
    assert data == actual
    assert response.status_code == 200
