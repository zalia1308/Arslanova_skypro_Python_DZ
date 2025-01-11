import pytest
from selenium import webdriver


from Authorization import Authorization
from MainPage import MainPage
from TheBasket import TheBasket
from YourInformation import YourInformation
from Overview import Overview


def test_shop_in_the_online_store():
    driver = webdriver.Chrome()
    authorization = Authorization(driver)
    authorization.authorization('standard_user', 'secret_sauce')
    main_page = MainPage(driver)
    main_page.add_products_in_the_basket()
    main_page.opening_the_basket()
    the_basket = TheBasket(driver)
    the_basket.checkout_in_the_basket()
    your_information = YourInformation(driver)
    your_information.filling_information('Залия', 'Арсланова', '453050')
    overview = Overview(driver)
    overview.check_total()