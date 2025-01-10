from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.first_name = (By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(1) > label > input")
        self.last_name = (By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(2) > label > input")
        self.address = (By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div.col-md-4.py-2 > label > input")
        self.email = (By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(1) > label > input")
        self.phone_number = (By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(2) > label > input")
        self.city = (By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(3) > label > input")
        self.country = (By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(4) > label > input")
        self.job_position = (By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(1) > label > input")
        self.company = (By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(2) > label > input")
        self.zip_code = (By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div.col-md-2.py-2 > label > input")
        self.button = (By.CSS_SELECTOR, "body > main > div > form > div:nth-child(5) > div > button")


    def filling_out_the_form_first_name(self, input_value):
        self.driver.find_element(*self.first_name).send_keys(input_value)


    def filling_out_the_form_last_name(self, input_value):
        self.driver.find_element(*self.last_name).send_keys(input_value)


    def filling_out_the_form_address(self, input_value):
        self.driver.find_element(*self.address).send_keys(input_value)


    def filling_out_the_form_email(self, input_value):
        self.driver.find_element(*self.email).send_keys(input_value)


    def filling_out_the_form_phone(self, input_value):
        self.driver.find_element(*self.phone_number).send_keys(input_value)


    def filling_out_the_form_city(self, input_value):
        self.driver.find_element(*self.city).send_keys(input_value)


    def filling_out_the_form_country(self, input_value):
        self.driver.find_element(*self.country).send_keys(input_value)


    def filling_out_the_form_job_position(self, input_value):
        self.driver.find_element(*self.job_position).send_keys(input_value)


    def filling_out_the_form_company(self, input_value):
        self.driver.find_element(*self.company).send_keys(input_value)


    def submit(self):
        self.driver.find_element(*self.button).click()
        WebDriverWait(self.driver, 20).until_not(EC.element_to_be_clickable(self.button))


    def red_box(self):
        assert "danger" in self.driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")


    def green_box(self):
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#first-name").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#last-name").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#address").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#city").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#country").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#e-mail").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#phone").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#job-position").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#company").get_attribute("class")