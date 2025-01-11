import requests
import pytest
import json


base_url = "https://yougile.com/api-v2/"


# Создание ключа
@pytest.fixture
def my_token():
     creds = {
        'login': '14yellow@tohru.org',
        'password': '0W.D~%{1"*',
        'name': 'Курс_автоматизация'
     }

     # 1 Получить ID компании
     resp = requests.post(base_url + 'auth/companies', json=creds)
     # 1.1 Сохранить companyId из ответа шага 1
     my_companyId = resp.json()["content"][0]["id"]

     body = {
         'login': '14yellow@tohru.org',
         'password': '0W.D~%{1"*',
         'companyId': my_companyId
     }

     # 2 Получить ключ API
     resp = requests.post(base_url + 'auth/keys', json=body)
     my_token = resp.json()["key"]
     return my_token


# Получить ID проекта для тестов
@pytest.fixture
def id_my_projects(my_token):
    my_headers = {
         'Authorization': 'Bearer ' + my_token,
         'Content-Type': 'application/json'
    }
    body = {
        'title': 'PyCharm для получения ID проекта для тестов'
    }
    resp = requests.post(base_url + 'projects', json=body, headers=my_headers)
    with open('id_my_projects.txt', 'w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)
    id_my_projects = resp.json()["id"]
    return id_my_projects


# ПОЗИТИВНЫЕ ТЕСТЫ
# Получить список проектов [GET]  --позитивные
def test_get_a_list_projects(my_token):
    my_headers = {
         'Authorization': 'Bearer ' + my_token,
         'Content-Type': 'application/json'
    }
    body = {
        'includeDeleted': True,
        'limit': 10
    }
    resp = requests.get(base_url + 'projects', json=body, headers=my_headers)
    assert resp.status_code == 200
    with open('positive/result_test_get_a_list_projects.txt', 'w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)


# Создать проект [POST]  --позитивные
def test_create_projects(my_token):
    my_headers = {
         'Authorization': 'Bearer ' + my_token,
         'Content-Type': 'application/json'
    }
    body = {
        'title': 'Тест через PyCharm'
    }
    resp = requests.post(base_url + 'projects', json=body, headers=my_headers)
    assert resp.status_code == 201
    with open('positive/result_test_create_projects.txt', 'w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)


# Получить по ID описание проекта [GET]  --позитивные
def test_get_by_project_id(my_token, id_my_projects):
    my_headers = {
         'Authorization': 'Bearer ' + my_token,
         'Content-Type': 'application/json'
    }

    resp = requests.get(base_url + 'projects/' + id_my_projects, headers=my_headers)
    assert resp.status_code == 200
    with open('positive/result_test_get_by_project_id.txt', 'w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)


# Изменить проект по ID [PUT]  --позитивные
def test_change_the_project_by_id(my_token, id_my_projects):
    my_headers = {
         'Authorization': 'Bearer ' + my_token,
         'Content-Type': 'application/json'
    }
    body = {
        'title': 'PyCharm для получения ID проекта для тестов_БЫЛО ИЗМЕНЕНО ЧЕРЕЗ ТЕСТ'
    }

    resp = requests.put(base_url + 'projects/' + id_my_projects, json=body, headers=my_headers)
    assert resp.status_code == 200
    with open('positive/result_test_change_the_project_by_id.txt', 'w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)

    # Для проверки описания изменного проекта, изменение названия можно увидеть в файле
    id_change_projects = resp.json()["id"]
    resp_change = requests.get(base_url + 'projects/' + id_change_projects, headers=my_headers)
    with open('checking_the_changed _project_name.txt', 'w', encoding='utf-8') as f:
        json.dump(resp_change.json(), f, ensure_ascii=False, indent=4)


# НЕГАТИВНЫЕ ТЕСТЫ
# Получить список проектов без авторизации[GET]  --негативные
def test_get_a_list_projects_negative():
    body = {
        'includeDeleted': True,
        'limit': 10
    }

    resp = requests.get(base_url + 'projects', json=body)
    message = resp.json()["message"]
    assert resp.status_code == 401
    assert message == "Unauthorized"
    with open('negative/result_test_get_a_list_projects_negative.txt', 'w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)


# Создать проект без обязательного поля [POST]  --негативные
def test_create_projects_negative_1(my_token):
    my_headers = {
         'Authorization': 'Bearer ' + my_token,
         'Content-Type': 'application/json'
    }
    body = {
        'users': 'admin'
    }
    resp = requests.post(base_url + 'projects', json=body, headers=my_headers)
    message = resp.json()["message"]
    assert resp.status_code == 400
    assert message[0] == "title should not be empty"
    with open('negative/result_test_create_projects_negative_1.txt', 'w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)


# Создать проект с некорректным значением в поле [POST]  --негативные
def test_create_projects_negative_2(my_token):
    my_headers = {
         'Authorization': 'Bearer ' + my_token,
         'Content-Type': 'application/json'
    }
    body = {
        'title': True
    }
    resp = requests.post(base_url + 'projects', json=body, headers=my_headers)
    message = resp.json()["message"]
    assert resp.status_code == 400
    assert message[0] == "title must be a string"
    with open('negative/result_test_create_projects_negative_2.txt', 'w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)


# Получить по несуществующему ID описание проекта [GET]  ---негативные
def test_get_by_project_id_negative(my_token):
    my_headers = {
         'Authorization': 'Bearer ' + my_token,
         'Content-Type': 'application/json'
    }

    resp = requests.get(base_url + 'projects/15485', headers=my_headers)
    message = resp.json()["message"]
    assert resp.status_code == 404
    assert message == "Проект не найден"
    with open('negative/result_test_get_by_project_id_negative.txt', 'w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)


# Изменить проект по несуществующему ID [PUT]  ---негативные
def test_change_the_project_by_id_negative(my_token):
    my_headers = {
         'Authorization': 'Bearer ' + my_token,
         'Content-Type': 'application/json'
    }
    body = {
        'title': 'PyCharm для получения ID проекта для тестов_БЫЛО ИЗМЕНЕНО ЧЕРЕЗ ТЕСТ'
    }

    resp = requests.put(base_url + 'projects/15485', json=body, headers=my_headers)
    message = resp.json()["message"]
    assert resp.status_code == 404
    assert message == "Проект не найден"
    with open('negative/result_test_change_the_project_by_id_negative.txt', 'w', encoding='utf-8') as f:
        json.dump(resp.json(), f, ensure_ascii=False, indent=4)