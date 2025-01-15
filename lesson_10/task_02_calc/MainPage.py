import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
    Этот класс представляет страницу "Hands-On Selenium WebDriver with Java" с калькулятором "Slow calculator", где также можно указывать секунды для ожидания результатов вычислений
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.seconds = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)")
        self.button_sum = (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)")
        self.button_8 = (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)")
        self.button_equally = (By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning")
        self.box_result = (By.CSS_SELECTOR, "#calculator > div.top > div")


    @allure.step("Заполнить поле с секундами ожидания результатов")
    def box_seconds(self, input_value: str) -> None:
        """
        Эта функция очищает поле с секундами ожиданий и заполняет его цифрой, т.е. результат вычислений отобразится лишь например через 45 секунд, если в поле с секундами указано значение '45'
        """
        with allure.step("Очистить поле с секундами"):
          seconds = self.driver.find_element(*self.seconds)
          seconds.clear()
        with allure.step("Заполнить поле с секундами"):
          seconds.send_keys(input_value)


    @allure.step("Выполнить вычисления")
    def calculator(self, expected_result: str) -> None:
        """
        Эта функция для вычислений на калькуляторе.
        Такой порядок действий:
        1. Нажимается кнопка с цифрой '7'
        2. Нажимается кнопка со знаком '+'
        2. Нажимается кнопка с цифрой '8'
        2. Нажимается кнопка со знаком '='
        """
        with allure.step("Нажать кнопку с цифрой '7'"):
          self.driver.find_element(*self.button_7).click()
        with allure.step("Нажать кнопку со знаком '+'"):
          self.driver.find_element(*self.button_sum).click()
        with allure.step("Нажать кнопку с цифрой '8'"):
          self.driver.find_element(*self.button_8).click()
        with allure.step("Нажать кнопку со знаком '='"):
          self.driver.find_element(*self.button_equally).click()
          WebDriverWait(self.driver, 45).until(EC.text_to_be_present_in_element(self.box_result, expected_result))


    @allure.step("Проверить, что в результате вычислений отображена цифра '15'")
    def result_calculator(self):
        """
        Эта функция для проверки результата вычислений суммы чисел 7 и 8
        """
        result = self.driver.find_element(*self.box_result).text
        assert result == "15"