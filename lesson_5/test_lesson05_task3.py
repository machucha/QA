from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    

    links = driver.find_elements(By.TAG_NAME, "a")

    assert len(links) == 9, f"Ожидалось 9 ссылок, найдено {len(links)}"

    for i, link in enumerate(links):
        assert link.is_displayed(), (
             f"Ссылка #{i} ('{link.text}') не отображается"
        )

    assert "1" in links[0].text, (
         f"Первая ссылка не содержит '1': '{links[0].text}'"
    )

    driver.quit()
