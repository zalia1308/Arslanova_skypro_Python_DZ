import pytest
from selenium import webdriver


from MainPage import MainPage


def test_calculator_sum_7_and_8():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.box_seconds('45')
    main_page.calculator('15')
    main_page.result_calculator()
    driver.quit()