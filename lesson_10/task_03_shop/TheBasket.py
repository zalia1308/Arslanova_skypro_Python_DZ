import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TheBasket:
    """
    Этот класс представляет страницу 'Your Cart' со списком выбранных товаров, их описанием, их количеством в корзине и возможностью их удаления из корзины.
    """
    def __init__(self, driver):
        self.driver = driver
        self.button_checkout = (By.CSS_SELECTOR, "#checkout")
        self.button_next_page = (By.CSS_SELECTOR, "#continue")


    @allure.step("Нажать кнопку 'Checkout'")
    def checkout_in_the_basket(self):
        """
        Эта функция для нажимания кнопки "Checkout"
        """
        self.driver.find_element(*self.button_checkout).click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_next_page))