import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Authorization:
    """
    Этот класс представляет страницу авторизации интернет-магазина 'Swag Labs'
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.username = (By.CSS_SELECTOR, "#user-name")
        self.password = (By.CSS_SELECTOR, "#password")
        self.login_button = (By.CSS_SELECTOR, "#login-button")
        self.button_main_page = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")


    @allure.step("Выполнить авторизацию на сайте интернет-магазина 'Swag Labs'")
    def authorization(self, input_value1: str, input_value2: str)  -> None:
        """
        Эта функция выполняет авторизацию в интернет-магазине 'Swag Labs'
        """
        with allure.step("Заполнить поле 'Username'"):
          self.driver.find_element(*self.username).send_keys(input_value1)
        with allure.step("Заполнить поле 'Password'"):
          self.driver.find_element(*self.password).send_keys(input_value2)
        with allure.step("Нажать кнопку 'Login'"):
          self.driver.find_element(*self.login_button).click()
          WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_main_page))
