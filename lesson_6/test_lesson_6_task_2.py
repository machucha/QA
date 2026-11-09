from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "MDZjZDY0OTItNTI4ZS00MDUzLWE3MzUtMjYyZTA4NTIwZjdk"
    })
    driver.refresh()

    driver.get("https://gitflic.ru/user/student_sky")
    wait.until(EC.url_contains("/user/student_sky"))
    user1_url = driver.current_url

    driver.delete_all_cookies()
    driver.refresh()

    driver.add_cookie({
        "name": "SESSION",
        "value": "MzUyNzVkNjMtNmU1OS00MjFlLWExN2UtZGRiMmRhMWExMWIx"
    })
    driver.refresh()

    driver.get("https://gitflic.ru/user/anatoly_sky")
    wait.until(EC.url_contains("/user/anatoly_sky"))
    user2_url = driver.current_url

    assert user1_url != user2_url

    driver.quit()
