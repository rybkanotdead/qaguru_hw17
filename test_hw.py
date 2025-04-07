import requests
from validate_schemas import validate_json_schema
from schemas import schemas
from data.user_playloads import *

url = 'https://reqres.in'

def test_get_list_of_users():
     response = requests.get(f"{url}/api/users?page=2")
     validate_json_schema(schemas.schema_for_get_list_users, response)
     assert response.status_code == 200

def test_get_single_user():
     response = requests.get(f"{url}/api/users/2")
     validate_json_schema(schemas.schema_for_get_single_user,response)
     assert  response.status_code == 200
     data = response.json()['data']
     assert data['id'] == 2
     assert data['first_name'] == "Janet"
     assert data['last_name'] == "Weaver"

def test_notfound_user():
     response = requests.get(f"{url}/api/users/552")
     assert response.status_code == 404

def test_get_list_resource():
     response = requests.get(f"{url}/api/unknown")
     validate_json_schema(schemas.schema_for_list_resource, response)
     assert response.status_code == 200
     assert response.json()['per_page'] == 6
     assert len(response.json()['support']) > 0


def test_create_user():
     playload = create_user_payload(name="Test",job="QA")
     response = requests.post(f"{url}/api/users", json=playload)

     assert response.status_code == 201
     data = response.json()
     assert data['name'] == "Test"
     assert data['job'] == "QA"

def test_update_user():
     playload = update_user_playload(name="Pupkin", job="Mamkin QA")
     response = requests.put(f"{url}/api/users/2", json=playload)
     assert response.status_code == 200
     data = response.json()
     assert data['name'] == "Pupkin"
     assert data['job'] == "Mamkin QA"

def test_delete_user():
     response = requests.delete(f"{url}/api/users/2")
     assert response.status_code == 204

def test_suc_reg():
     playload = suc_register(email="eve.holt@reqres.in", password="cityslicka")
     response = requests.post(f"{url}/api/register", json=playload)
     assert response.status_code == 200
     data = response.json()
     assert data['token'] == 'QpwL5tke4Pnpja7X4'

def test_unsuc_reg():
     playload = unsuc_register(email="eve.holt@reqres.in")
     response = requests.post(f"{url}/api/register", json=playload)
     assert response.status_code == 400
     data = response.json()
     assert data['error'] == 'Missing password'

def test_unsuc_reg_login():
     playload = suc_register(email="eve123.holt@reqres.in" , password="adjafa")
     response = requests.post(f"{url}/api/login", json=playload)
     assert response.status_code == 400
     data = response.json()
     assert  data['error'] == 'user not found'