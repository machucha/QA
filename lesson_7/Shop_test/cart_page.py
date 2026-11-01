from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_items(self, expected_items):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "cart_list")
            )
        )

        actual_items = [
            item.text
            for item in self.driver.find_elements(
                By.CLASS_NAME, "inventory_item_name"
            )
        ]

        return all(
            item in actual_items for item in expected_items
        )

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()
        return self
