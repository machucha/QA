from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def enter_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        return self

    def enter_password(self, password):
        self.driver.find_element(
            By.ID, "password"
        ).send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(
            By.ID, "login-button"
        ).click()
        return self
