import allure
from selenium.webdriver.common.by import By
from selenium import webdriver


class MainPage:
    """
    Этот класс представляет страницу 'Products' с товарами, их описанием и возможностью их выбора
    """
    def __init__(self, driver):
        self.driver = driver
        self.button_sauce_labs_backpack = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self.button_sauce_labs_bolt_t_shirt = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        self.button_sauce_labs_onesie = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        self.button_sauce_labs_backpack_remove = (By.CSS_SELECTOR, "#remove-sauce-labs-onesie")
        self.button_basket = (By.CSS_SELECTOR, "#shopping_cart_container > a")


    @allure.step("Выбрать товары: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie")
    def add_products_in_the_basket(self):
        """
        Эта функция выбирает 3 товара: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
        """
        self.driver.implicitly_wait(15)
        with allure.step("Нажать кнопку 'Add to cart' для товара 'Sauce Labs Backpack'"):
            self.driver.find_element(*self.button_sauce_labs_backpack).click()
        with allure.step("Нажать кнопку 'Add to cart' для товара 'Sauce Labs Bolt T-Shirt'"):
            self.driver.find_element(*self.button_sauce_labs_bolt_t_shirt).click()
        with allure.step("Нажать кнопку 'Add to cart' для товара 'Sauce Labs Onesie'"):
            self.driver.find_element(*self.button_sauce_labs_onesie).click()


    @allure.step("Открыть корзину")
    def opening_the_basket(self):
        """
        Эта функция для открытия корзины со страницы 'Products'
        """
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.button_basket).click()