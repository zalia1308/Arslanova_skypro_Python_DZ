import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YourInformation:
    """
    Этот класс представляет страницу 'Checkout: Your Information' для заполнения личной информации (фамилия, имя, код почты)
    """
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.CSS_SELECTOR, "#first-name")
        self.last_name = (By.CSS_SELECTOR, "#last-name")
        self.postal_code = (By.CSS_SELECTOR, "#postal-code")
        self.button_continue = (By.CSS_SELECTOR, "#continue")
        self.button_next_page = (By.CSS_SELECTOR, "#finish")


    @allure.step("Заполнить поля и нажать кнопку 'Continue'")
    def filling_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Эта функция заполнения личной информации (фамилия, имя, код почты).
        И дальнейший переход к следующей странице 'Checkout: Overview'
        """
        with allure.step("Заполнить поле 'First Name'"):
            self.driver.find_element(*self.first_name).send_keys(first_name)
        with allure.step("Заполнить поле 'Last Name'"):
            self.driver.find_element(*self.last_name).send_keys(last_name)
        with allure.step("Заполнить поле 'Zip/Postal Code'"):
            self.driver.find_element(*self.postal_code).send_keys(postal_code)
        with allure.step("Нажать кнопку 'Continue'"):
            self.driver.find_element(*self.button_continue).click()
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_next_page))