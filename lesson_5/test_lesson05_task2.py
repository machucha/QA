from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    
    input_custname = driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Customer name"]')
    input_custname.send_keys("Anatoly_sky")

    click_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    click_button.click()
    assert driver.current_url == "https://httpbin.qa-territory.online/post"

    driver.quit()
