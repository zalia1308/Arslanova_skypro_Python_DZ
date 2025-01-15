import allure
import pytest
from selenium import webdriver

from lesson_10.task_01_form.MainPage import MainPage


@allure.id("lesson_10-1")
@allure.story("Заполнение формы")
@allure.feature("CREATE")
@allure.epic("Форма")
@allure.title("Проверка цветовой индикации незаполненных полей")
@allure.description("Проверка выделения красным цветом поля 'Zip code' при его незаполнении")
@allure.severity("blocker")
def test_filling_out_the_form_1():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.filling_out_the_form_first_name('Иван')
    main_page.filling_out_the_form_last_name('Петров')
    main_page.filling_out_the_form_address('Ленина, 55-3')
    main_page.filling_out_the_form_email('test@skypro.com')
    main_page.filling_out_the_form_phone('+7985899998787')
    main_page.filling_out_the_form_city('Москва')
    main_page.filling_out_the_form_country('Россия')
    main_page.filling_out_the_form_job_position('QA')
    main_page.filling_out_the_form_company('SkyPro')
    main_page.submit()
    main_page.red_box()
    driver.quit()


@allure.id("lesson_10-4")
@allure.story("Заполнение формы")
@allure.feature("CREATE")
@allure.epic("Форма")
@allure.title("Проверка цветовой индикации заполненных полей")
@allure.description("Проверка выделения зеленым цветом всех полей кроме поля 'Zip code' при их заполнении")
@allure.severity("critical")
def test_filling_out_the_form_2():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.filling_out_the_form_first_name('Иван')
    main_page.filling_out_the_form_last_name('Петров')
    main_page.filling_out_the_form_address('Ленина, 55-3')
    main_page.filling_out_the_form_email('test@skypro.com')
    main_page.filling_out_the_form_phone('+7985899998787')
    main_page.filling_out_the_form_city('Москва')
    main_page.filling_out_the_form_country('Россия')
    main_page.filling_out_the_form_job_position('QA')
    main_page.filling_out_the_form_company('SkyPro')
    main_page.submit()
    main_page.green_box()
    driver.quit()