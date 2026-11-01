from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = Options()


def test_form():
    driver = webdriver.Edge(options=edge_options)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    input_custname = driver.find_element(
        By.NAME, 'first-name')
    input_custname.send_keys("Иван")

    input_custname = driver.find_element(
            By.NAME, 'last-name')
    input_custname.send_keys("Петров")

    input_custname = driver.find_element(
                By.NAME, 'address')
    input_custname.send_keys("Ленина, 55-3")

    input_custname = driver.find_element(
                        By.NAME, 'e-mail')
    input_custname.send_keys("test@skypro.com")

    input_custname = driver.find_element(
            By.NAME, 'phone')
    input_custname.send_keys("+7985899998787")

    input_custname = driver.find_element(
                By.NAME, 'city')
    input_custname.send_keys("Москва")

    input_custname = driver.find_element(By.NAME, 'country')
    input_custname.send_keys("Россия")

    input_custname = driver.find_element(By.NAME, 'job-position')
    input_custname.send_keys("QA")

    input_custname = driver.find_element(By.NAME, 'company')
    input_custname.send_keys("SkyPro")

    click_button = driver.find_element(
        By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3")
    click_button.click()

    wait = WebDriverWait(driver, 5)
    wait.until(
          EC.presence_of_element_located((
              By.CSS_SELECTOR, "#zip-code.alert-danger")))

    zip_code_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

    green_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
        ]

    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class")

    driver.quit()
