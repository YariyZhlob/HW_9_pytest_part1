import requests


def test_list_resource_total():
    total = 12

    response = requests.get('https://reqres.in/api/unknown')
    assert response.json()['total'] == 12


def test_name_id_1():
    check_name = 'cerulean'

    response = requests.get('https://reqres.in/api/unknown')
    data = response.json()
    name = None
    for items in data['data']:
        if items['id'] == 1:
            name = items['name']
            break

    assert check_name == name


def test_status_code_single_resource_not_found():
    code = 404

    response = requests.get('https://reqres.in/api/unknown/23')
    status_code = response.status_code
    assert code == status_code


def test_register_successful():
    email = 'eve.holt@reqres.in'
    password = 'pistol123'

    response = requests.post(
        url='https://reqres.in/api/register',
        json={
            "email": email,
            "password": password}
    )
    assert response.json()['id'] == 4

def test_update_user_put_method():
    name = 'any_name'
    job = 'any_company'

    response = requests.put(
        url = 'https://reqres.in/api/users/2',
        json = {
            'name': name,
         'job' : job}
    )

    assert response.json()['name'] == 'any_name'

def test_update_user_patch_method():
    name = 'superuser'
    job = 'any_company'

    response = requests.patch(
        url = 'https://reqres.in/api/users/2',
        json = {
            'name': name,
         'job' : job}
    )

    assert response.json()['name'] == 'superuser'


def test_delete_user():
    response = requests.delete(
        url = 'https://reqres.in/api/users/2'
    )

    assert response.status_code == 204

def test_unsuccessful_register():
    response = requests.post(
        url = 'https://reqres.in/api/register',
        json = {
            "email": "sydney@fife"
        }
    )

    assert response.status_code == 400

def test_successful_login():
    response = requests.post(
        url = 'https://reqres.in/api/login',
        json = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )

    assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'


def test_delayed_response_id_1_first_name():
    response = requests.get('https://reqres.in/api/users?delay=3')
    data = response.json()['data']
    name = None
    for items in data:
        if id == 1:
            name = 'first_name'
        return name
        brake

    assert name == 'George'
