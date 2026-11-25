
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object страницы авторизации saucedemo.com."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver) -> None:
        """Сохраняет веб-драйвер и создаёт объект ожидания.

        :param driver: экземпляр веб-драйвера Selenium (WebDriver)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> "LoginPage":
        """Открывает страницу авторизации по адресу URL."""
        self.driver.get(self.URL)
        return self

    def enter_username(self, username: str) -> "LoginPage":
        """Вводит имя пользователя в поле логина.

        :param username: имя пользователя (строка)
        """
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        """Вводит пароль в поле пароля.

        :param password: пароль пользователя (строка)
        """
        self.driver.find_element(By.ID, "password").send_keys(password)
        return self

    def click_login(self) -> "LoginPage":
        """Нажимает кнопку входа."""
        self.driver.find_element(By.ID, "login-button").click()
        return self
