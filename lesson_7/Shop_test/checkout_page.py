
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):
        self.driver.find_element(
            By.ID, "first-name"
        ).send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        self.driver.find_element(
            By.ID, "last-name"
        ).send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code):
        self.driver.find_element(
            By.ID, "postal-code"
        ).send_keys(postal_code)
        return self

    def click_continue(self):
        self.driver.find_element(
            By.ID, "continue"
        ).click()
        return self

    def get_total(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total_element.text
