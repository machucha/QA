from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#start button")
        )
    )
    start_btn.click()

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish > h4"))
    )

    driver.save_screenshot("lesson_6/screen_page.png")

    actual_text = driver.find_element(By.CSS_SELECTOR, "#finish > h4").text
    assert actual_text == "Hello World!"
