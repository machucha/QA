from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    input_custnumber = driver.find_element(
            By.ID, 'delay')
    input_custnumber.clear()
    input_custnumber.send_keys("45")

    click_button = driver.find_element(
        By.XPATH, "//span[text()='7']")
    click_button.click()

    click_button = driver.find_element(
        By.XPATH, "//span[text()='+']")
    click_button.click()

    click_button = driver.find_element(
        By.XPATH, "//span[text()='8']")
    click_button.click()

    click_button = driver.find_element(
        By.XPATH, "//span[text()='=']")
    click_button.click()

    wait = WebDriverWait(driver, 50)
    wait.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, ".screen"), "15"))

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15"
