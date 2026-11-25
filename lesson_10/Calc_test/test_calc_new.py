import allure
from selenium import webdriver
from calc_object_new import CalculatorObj


@allure.title("Проверка медленного калькулятора: 7 + 8 = 15 с задержкой 45 с")
@allure.description(
    "Тест открывает страницу медленного калькулятора, устанавливает "
    "задержку 45 секунд, выполняет сложение 7 + 8 и проверяет, "
    "что результат равен 15."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator():
    driver = webdriver.Edge()
    page = CalculatorObj(driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay(45)

    with allure.step("Ввести выражение 7 + 8 ="):
        with allure.step("Нажать кнопку '7'"):
            page.click_button("7")
        with allure.step("Нажать кнопку '+'"):
            page.click_button("+")
        with allure.step("Нажать кнопку '8'"):
            page.click_button("8")
        with allure.step("Нажать кнопку '='"):
            page.click_button("=")

    with allure.step("Дождаться результата 15"):
        page.wait_for_result("15")

    with allure.step("Проверить, что результат равен 15"):
        with allure.step("Получить текущий результат с экрана"):
            actual = page.get_result()
        with allure.step(f"Сравнить результат: ожидается '15',"
                         f"получено '{actual}'"
                         ):
            assert actual == "15"

    driver.quit()
