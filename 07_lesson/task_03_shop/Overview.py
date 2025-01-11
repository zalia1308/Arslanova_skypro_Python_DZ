from selenium.webdriver.common.by import By
from selenium import webdriver


class Overview:
    def __init__(self, driver):
        self.driver = driver
        self.total = (By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label")


    def check_total(self):
        total = self.driver.find_element(*self.total).text
        self.driver.quit()
        total_number = total.split('$')
        assert total_number[1] == "58.29"