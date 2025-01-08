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


def filling_out_the_form_and_submit(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    # Заполнить форму данными
    first_name = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(1) > label > input")
    first_name.send_keys("Иван")
    last_name = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(2) > label > input")
    last_name.send_keys("Петров")
    address = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div.col-md-4.py-2 > label > input")
    address.send_keys("Ленина, 55-3")
    email = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(1) > label > input")
    email.send_keys("test@skypro.com")
    phone_number = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(2) > label > input")
    phone_number.send_keys("+7985899998787")
    city = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(3) > label > input")
    city.send_keys("Москва")
    country = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(4) > label > input")
    country.send_keys("Россия")
    job_position = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(1) > label > input")
    job_position.send_keys("QA")
    company = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(2) > label > input")
    company.send_keys("SkyPro")
    # Нажать кнопку
    driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(5) > div > button").click()
    element = WebDriverWait(driver, 40)
    element.until_not(
        EC.element_located_to_be_selected((By.CSS_SELECTOR, "body > main > div > form > div:nth-child(5) > div > button"))
    )


def test_red_box(driver):
    filling_out_the_form_and_submit(driver)
    assert "danger" in driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")


def test_green_box(driver):
    filling_out_the_form_and_submit(driver)
    assert "success" in driver.find_element(By.CSS_SELECTOR, "#first-name").get_attribute("class")
    assert "success" in driver.find_element(By.CSS_SELECTOR, "#last-name").get_attribute("class")
    assert "success" in driver.find_element(By.CSS_SELECTOR, "#address").get_attribute("class")
    assert "success" in driver.find_element(By.CSS_SELECTOR, "#city").get_attribute("class")
    assert "success" in driver.find_element(By.CSS_SELECTOR, "#country").get_attribute("class")
    assert "success" in driver.find_element(By.CSS_SELECTOR, "#e-mail").get_attribute("class")
    assert "success" in driver.find_element(By.CSS_SELECTOR, "#phone").get_attribute("class")
    assert "success" in driver.find_element(By.CSS_SELECTOR, "#job-position").get_attribute("class")
    assert "success" in driver.find_element(By.CSS_SELECTOR, "#company").get_attribute("class")