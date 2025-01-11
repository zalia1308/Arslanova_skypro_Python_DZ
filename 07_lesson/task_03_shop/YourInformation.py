from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YourInformation:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.CSS_SELECTOR, "#first-name")
        self.last_name = (By.CSS_SELECTOR, "#last-name")
        self.postal_code = (By.CSS_SELECTOR, "#postal-code")
        self.button_continue = (By.CSS_SELECTOR, "#continue")
        self.button_next_page = (By.CSS_SELECTOR, "#finish")


    def filling_information(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.button_continue).click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_next_page))