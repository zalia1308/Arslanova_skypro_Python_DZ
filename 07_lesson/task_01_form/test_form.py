import pytest
from selenium import webdriver


from MainPage import MainPage


def test_filling_out_the_form():
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
    main_page.green_box()
    driver.quit()