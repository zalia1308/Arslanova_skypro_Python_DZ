import allure
import pytest
from selenium import webdriver


from lesson_10.task_02_calc.MainPage import MainPage

@allure.id("lesson_10-2")
@allure.story("Сумма в калькуляторе с ожиданием")
@allure.feature("SUMMA")
@allure.epic("Калькулятор")
@allure.title("Проверка суммы 7 и 8")
@allure.description("Проверка суммы 7 и 8 при ожидании 45 секунд")
@allure.severity("critical")
def test_calculator_sum_7_and_8():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.box_seconds('45')
    main_page.calculator('15')
    main_page.result_calculator()
    driver.quit()