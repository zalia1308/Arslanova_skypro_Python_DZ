import allure
from selenium.webdriver.common.by import By
from selenium import webdriver


class Overview:
    """
    Этот класс представляет страницу 'Checkout: Overview' с итоговой информацией по заказу
    """
    def __init__(self, driver):
        self.driver = driver
        self.total = (By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label")


    @allure.step("Проверить отображаемую сумму в поле 'Total:'")
    def check_total(self):
        """
        Эта функция заполнения личной информации (фамилия, имя, код почты).
        И дальнейший переход к следующей странице 'Checkout: Overview'
        """
        total = self.driver.find_element(*self.total).text
        self.driver.quit()
        total_number = total.split('$')
        assert total_number[1] == "58.29"