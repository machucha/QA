import requests

base_url = "https://ru.yougile.com"

# Вставьте сюда ваш токен перед запуском тестов
token = "YOUGILE_TOKEN"


headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


def test_get_project_positive():
    resp_create = requests.post(
        base_url + "/api-v2/projects",
        headers=headers,
        json={
            "title": "Проект для чтения",
            "users": {"73f6bb70-f4be-4b02-a4bf-9bcf669888e5": "admin"}
        }
    )
    assert resp_create.status_code == 201
    project_id = resp_create.json()["id"]

    resp_get = requests.get(
        base_url + f"/api-v2/projects/{project_id}",
        headers=headers
    )
    assert resp_get.status_code == 200
    assert resp_get.json()["title"] == "Проект для чтения"


def test_get_project_negative():
    fake_id = "4588-4584-52155-878"
    resp_get = requests.get(
        base_url + f"/api-v2/projects/{fake_id}",
        headers=headers
    )
    assert resp_get.status_code == 404
