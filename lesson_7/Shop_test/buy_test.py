from selenium import webdriver

from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Chrome()

    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack()
    inventory_page.add_bolt_t_shirt()
    inventory_page.add_onesie()
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    expected_items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    assert cart_page.check_items(expected_items)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_first_name("John")
    checkout_page.enter_last_name("Malkov")
    checkout_page.enter_postal_code("842254")
    checkout_page.click_continue()

    total = checkout_page.get_total()
    assert total == "Total: $58.29"

    driver.quit()
