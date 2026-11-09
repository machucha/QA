from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")
    sleep(3)

    click_button = driver.find_element(
        By.CSS_SELECTOR, "a[href='/forms/post']")
    click_button.click()
    sleep(4)

    assert driver.current_url == (
        "https://httpbin.qa-territory.online/forms/post"
    )

    driver.back()
    sleep(4)

    assert driver.current_url == (
        "https://httpbin.qa-territory.online/"
    )

    driver.quit()
