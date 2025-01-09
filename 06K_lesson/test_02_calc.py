import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    seconds = driver.find_element(By.CSS_SELECTOR, "#delay")
    seconds.clear()
    seconds.send_keys("45")
    driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)").click()
    driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click()
    element = WebDriverWait(driver, 45)
    element.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#calculator > div.top > div"), "15")
    )


def test_result_calculator(driver):
    calculator(driver)
    result = driver.find_element(By.CSS_SELECTOR, "#calculator > div.top > div").text
    assert result == "15"