
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page Object страницы каталога товаров."""

    def __init__(self, driver) -> None:
        """Сохраняет веб-драйвер и создаёт объект ожидания.

        :param driver: экземпляр веб-драйвера Selenium (WebDriver)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self) -> "InventoryPage":
        """Добавляет в корзину рюкзак Sauce Labs Backpack."""
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()
        return self

    def add_bolt_t_shirt(self) -> "InventoryPage":
        """Добавляет в корзину футболку Sauce Labs Bolt T-Shirt."""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        return self

    def add_onesie(self) -> "InventoryPage":
        """Добавляет в корзину комбинезон Sauce Labs Onesie."""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()
        return self

    def open_cart(self) -> "InventoryPage":
        """Открывает корзину по клику на иконку тележки."""
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
        return self
