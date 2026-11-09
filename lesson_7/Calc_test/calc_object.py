from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorObj:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


def __init__(self, driver):
    self.driver = driver


def open(self):
    self.driver.get(self.URL)
    return self


def set_delay(self, seconds):
    input_field = self.driver.find_element(By.ID, "delay")
    input_field.clear()
    input_field.send_keys(str(seconds))
    return self


def click_button(self, label):
    self.driver.find_element(By.XPATH, f"//span[text()='{label}']").click()
    return self


def wait_for_result(self, expected_text):
    wait = WebDriverWait(self.driver, 60)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), expected_text)
        )
    return self


def get_result(self):
    return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
