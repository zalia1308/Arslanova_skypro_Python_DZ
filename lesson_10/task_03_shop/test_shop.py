import allure
import pytest
from selenium import webdriver


from lesson_10.task_03_shop.Authorization import Authorization
from lesson_10.task_03_shop.MainPage import MainPage
from lesson_10.task_03_shop.TheBasket import TheBasket
from lesson_10.task_03_shop.YourInformation import YourInformation
from lesson_10.task_03_shop.Overview import Overview


@allure.id("lesson_10-3")
@allure.story("Покупка товаров в магазине")
@allure.feature("SHOPPING")
@allure.epic("Интернет-магазин")
@allure.title("Проверка соответствия итоговой суммы с выбранными товарами")
@allure.description("Проверяется, что итоговая сумма в интернет-магазине вычисляется корректно при выборе товара")
@allure.severity("blocker")
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