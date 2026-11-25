
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object страницы оформления заказа."""

    def __init__(self, driver) -> None:
        """Сохраняет веб-драйвер и создаёт объект ожидания.

        :param driver: экземпляр веб-драйвера Selenium (WebDriver)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name: str) -> "CheckoutPage":
        """Вводит имя покупателя.

        :param first_name: имя (строка)
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        return self

    def enter_last_name(self, last_name: str) -> "CheckoutPage":
        """Вводит фамилию покупателя.

        :param last_name: фамилия (строка)
        """
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code: str) -> "CheckoutPage":
        """Вводит почтовый индекс покупателя.

        :param postal_code: почтовый индекс (строка)
        """
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        return self

    def click_continue(self) -> "CheckoutPage":
        """Нажимает кнопку Continue для перехода к сводке заказа."""
        self.driver.find_element(By.ID, "continue").click()
        return self

    def get_total(self) -> str:
        """Возвращает текст итоговой суммы заказа со страницы сводки."""
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total_element.text
