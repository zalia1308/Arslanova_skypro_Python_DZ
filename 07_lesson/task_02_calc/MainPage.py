from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.seconds = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)")
        self.button_sum = (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)")
        self.button_8 = (By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)")
        self.button_equally = (By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning")
        self.box_result = (By.CSS_SELECTOR, "#calculator > div.top > div")


    def box_seconds(self, input_value):
        seconds = self.driver.find_element(*self.seconds)
        seconds.clear()
        seconds.send_keys(input_value)


    def calculator(self, result_value):
        self.driver.find_element(*self.button_7).click()
        self.driver.find_element(*self.button_sum).click()
        self.driver.find_element(*self.button_8).click()
        self.driver.find_element(*self.button_equally).click()
        WebDriverWait(self.driver, 45).until(EC.text_to_be_present_in_element(self.box_result, result_value))


    def result_calculator(self):
        result = self.driver.find_element(*self.box_result).text
        assert result == "15"