from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    input_custname = driver.find_element(
            By.ID, 'user-name')
    input_custname.send_keys("standard_user")

    input_custname = driver.find_element(
            By.ID, 'password')
    input_custname.send_keys("secret_sauce")

    click_button = driver.find_element(
            By.ID, "login-button")
    click_button.click()

    click_button = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack")
    click_button.click()

    click_button = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    click_button.click()

    click_button = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie")
    click_button.click()

    click_button = driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link")
    click_button.click()

    click_button = driver.find_element(
            By.ID, "checkout")
    click_button.click()

    input_custname = driver.find_element(
            By.ID, 'first-name')
    input_custname.send_keys("John")

    input_custname = driver.find_element(
            By.ID, 'last-name')
    input_custname.send_keys("Malkov")

    input_custname = driver.find_element(
            By.ID, 'postal-code')
    input_custname.send_keys("842254")

    click_button = driver.find_element(
            By.ID, "continue")
    click_button.click()

    total_element = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text

    assert "$58.29" in total_text

    driver.quit()
