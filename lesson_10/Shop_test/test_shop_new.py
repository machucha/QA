import allure
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.title("Покупка трёх товаров в SauceDemo с проверкой итоговой суммы")
@allure.description(
    "Тест авторизуется на saucedemo.com, добавляет в корзину рюкзак, "
    "футболку и комбинезон, проверяет состав корзины, оформляет заказ "
    "и проверяет итоговую сумму: Total: $58.29."
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Edge()

    with allure.step("Авторизоваться на saucedemo.com"):
        login_page = LoginPage(driver)
        with allure.step("Открыть страницу авторизации"):
            login_page.open()
        with allure.step("Ввести имя пользователя 'standard_user'"):
            login_page.enter_username("standard_user")
        with allure.step("Ввести пароль 'secret_sauce'"):
            login_page.enter_password("secret_sauce")
        with allure.step("Нажать кнопку Login"):
            login_page.click_login()

    with allure.step("Добавить товары в корзину"):
        inventory_page = InventoryPage(driver)
        with allure.step("Добавить Sauce Labs Backpack"):
            inventory_page.add_backpack()
        with allure.step("Добавить Sauce Labs Bolt T-Shirt"):
            inventory_page.add_bolt_t_shirt()
        with allure.step("Добавить Sauce Labs Onesie"):
            inventory_page.add_onesie()
        with allure.step("Открыть корзину"):
            inventory_page.open_cart()

    with allure.step("Проверить состав корзины"):
        cart_page = CartPage(driver)
        expected_items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]
        with allure.step("Убедиться, что в корзине все ожидаемые товары"):
            assert cart_page.check_items(expected_items)
        with allure.step("Нажать кнопку Checkout"):
            cart_page.click_checkout()

    with allure.step("Оформить заказ"):
        checkout_page = CheckoutPage(driver)
        with allure.step("Ввести имя 'John'"):
            checkout_page.enter_first_name("John")
        with allure.step("Ввести фамилию 'Malkov'"):
            checkout_page.enter_last_name("Malkov")
        with allure.step("Ввести почтовый индекс '842254'"):
            checkout_page.enter_postal_code("842254")
        with allure.step("Нажать кнопку Continue"):
            checkout_page.click_continue()

    with allure.step("Проверить итоговую сумму заказа"):
        with allure.step("Получить итоговую сумму со страницы"):
            total = checkout_page.get_total()
        with allure.step(
            f"Сравнить итоговую сумму: 'Total: $58.29', получено '{total}'"
        ):
            assert total == "Total: $58.29"

    driver.quit()
