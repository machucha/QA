import requests

base_url = "https://ru.yougile.com"

# Вставьте сюда ваш токен перед запуском тестов
token = "YOUGILE_TOKEN"


headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


def test_create_project_positive():
    resp = requests.post(
        base_url + "/api-v2/projects",
        headers=headers,
        json={
            "title": "Тестовый проект",
            "users": {"73f6bb70-f4be-4b02-a4bf-9bcf669888e5": "admin"}
              }
    )
    assert resp.status_code == 201
    assert "id" in resp.json()


def test_create_project_negative():
    resp = requests.post(
        base_url + "/api-v2/projects",
        json={
            "title": "Тестовый проект",
            "users": {"73f6bb70-f4be-4b02-a4bf-9bcf669888e5": "admin"}
              }
    )
    assert resp.status_code == 401
