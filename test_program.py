import program 
import pytest 


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

@pytest.fixture
def initialization(mocker):
  mocker.patch('program.upload_data', return_value = actual)
  

def test_upload_data(initialization):
    assert program.upload_data() == actual
    