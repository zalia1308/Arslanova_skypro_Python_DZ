from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.button_sauce_labs_backpack = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self.button_sauce_labs_bolt_t_shirt = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        self.button_sauce_labs_onesie = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        self.button_sauce_labs_backpack_remove = (By.CSS_SELECTOR, "#remove-sauce-labs-onesie")
        self.button_basket = (By.CSS_SELECTOR, "#shopping_cart_container > a")


    def add_products_in_the_basket(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.button_sauce_labs_backpack).click()
        self.driver.find_element(*self.button_sauce_labs_bolt_t_shirt).click()
        self.driver.find_element(*self.button_sauce_labs_onesie).click()


    def opening_the_basket(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.button_basket).click()