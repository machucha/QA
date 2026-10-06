from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(3)
    input_custname = driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Customer name"]')
    input_custname.send_keys("Anatoly_sky")

    click_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    click_button.click()
    assert driver.current_url == "https://httpbin.qa-territory.online/post"
