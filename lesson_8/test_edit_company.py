import requests

base_url = "https://ru.yougile.com"

# Вставьте сюда ваш токен перед запуском тестов
token = "YOUGILE_TOKEN"


headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


def test_project_editing_positive():
    resp_create = requests.post(
        base_url + "/api-v2/projects", headers=headers,
        json={
            "title": "Для редактирования",
            "users": {"73f6bb70-f4be-4b02-a4bf-9bcf669888e5": "admin"}
        }
    )
    assert resp_create.status_code == 201
    project_id = resp_create.json()["id"]

    resp_edit = requests.put(
        base_url + f"/api-v2/projects/{project_id}", headers=headers,
        json={
            "title": "Мой любимый проект"
        }
    )
    assert resp_edit.status_code == 200


def test_project_editing_negative():
    fake_id = "4589-85123-9657-8236"

    resp_edit = requests.put(
        base_url + f"/api-v2/projects/{fake_id}",
        headers=headers,
        json={
            "title": "Мой любимый проект"
        }
    )
    assert resp_edit.status_code == 404
