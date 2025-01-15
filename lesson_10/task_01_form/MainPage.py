import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
    Этот класс представляет страницу "Hands-On Selenium WebDriver with Java" с заполнением полей "Data types"
    """
    def __init__(self, driver):
        self.driver = driver
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


    @allure.step("Заполнить поле 'First name'")
    def filling_out_the_form_first_name(self, input_value: str) -> None:
        """
        Эта функция находит поле "First name" и заполняет его именем
        """
        self.driver.find_element(*self.first_name).send_keys(input_value)


    @allure.step("Заполнить поле 'Last name'")
    def filling_out_the_form_last_name(self, input_value: str) -> None:
        """
        Эта функция находит поле "Last name" и заполняет его фамилией
        """
        self.driver.find_element(*self.last_name).send_keys(input_value)


    @allure.step("Заполнить поле 'Address'")
    def filling_out_the_form_address(self, input_value: str) -> None:
        """
        Эта функция находит поле "Address" и заполняет его адресом.
        Адрес может быть составным из улицы и дома.
        Например, "Ленина, 55-3"
        """
        self.driver.find_element(*self.address).send_keys(input_value)


    @allure.step("Заполнить поле 'E-mail'")
    def filling_out_the_form_email(self, input_value: str) -> None:
        """
        Эта функция находит поле "E-mail" и заполняет его значением из "input_value".
        Электронная почта должна содержать имя пользователя и доменное окончание, например, .ru.
        Пример полной электронной почты "test@skypro.com"
        """
        self.driver.find_element(*self.email).send_keys(input_value)


    @allure.step("Заполнить поле 'Phone number'")
    def filling_out_the_form_phone(self, input_value: str) -> None:
        """
        Эта функция находит поле "Phone number" и заполняет его значением из "input_value".
        Телефонный номер должен содержать "+" и дальше числовую часть номера.
        Например, "+7985899998787"
        """
        self.driver.find_element(*self.phone_number).send_keys(input_value)


    @allure.step("Заполнить поле 'City'")
    def filling_out_the_form_city(self, input_value: str) -> None:
        """
        Эта функция находит поле "City" и заполняет его городом
        """
        self.driver.find_element(*self.city).send_keys(input_value)


    @allure.step("Заполнить поле 'Country'")
    def filling_out_the_form_country(self, input_value: str) -> None:
        """
        Эта функция находит поле "Country" и заполняет его страной
        """
        self.driver.find_element(*self.country).send_keys(input_value)


    @allure.step("Заполнить поле 'Job position'")
    def filling_out_the_form_job_position(self, input_value: str) -> None:
        """
        Эта функция находит поле "Job position" и заполняет его должностью в компании
        Например, "QA"
        """
        self.driver.find_element(*self.job_position).send_keys(input_value)


    @allure.step("Заполнить поле 'Company'")
    def filling_out_the_form_company(self, input_value: str) -> None:
        """
        Эта функция находит поле "Company" и заполняет его названием компании
        Например, "SkyPro"
        """
        self.driver.find_element(*self.company).send_keys(input_value)


    @allure.step("Нажать кнопку 'Submit'")
    def submit(self) -> None:
        """
        Эта функция для нажимания кнопки "Submit"
        """
        self.driver.find_element(*self.button).click()
        WebDriverWait(self.driver, 20).until_not(EC.element_to_be_clickable(self.button))


    @allure.step("Проверить, что поле 'Zip code' подсвечено красным цветом")
    def red_box(self) -> None:
        """
        Эта функция для проверки цветовой индикации незаполненного поля "Zip code", а именно в красный цвет
        """
        assert "danger" in self.driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")


    @allure.step("Проверить, что все поля кроме поля 'Zip code' подсвечены зеленым цветом цветом")
    def green_box(self) -> None:
        """
        Эта функция для проверки цветовой индикации заполненных полей, а именно в зеленый цвет:
        - First name
        - Last name
        - Address
        - City
        - Country
        - E-mail
        - Phone number
        - Job position
        - Company
        """
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#first-name").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#last-name").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#address").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#city").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#country").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#e-mail").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#phone").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#job-position").get_attribute("class")
        assert "success" in self.driver.find_element(By.CSS_SELECTOR, "#company").get_attribute("class")