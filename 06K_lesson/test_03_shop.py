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

def test_total_sum_basket_of_product(driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    username = driver.find_element(By.CSS_SELECTOR, "#user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    element = WebDriverWait(driver, 15)
    element.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))
    )
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    element.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#remove-sauce-labs-onesie"))
    )
    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a").click()
    element.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
    )
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    element.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue"))
    )
    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys("Залия")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Арсланова")
    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code.send_keys("453050")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    element.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#finish"))
    )
    total = driver.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label").text
    driver.quit()
    total_number = total.split('$')
    assert total_number[1] == "58.29"