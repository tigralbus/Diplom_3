import allure
from conftest import driver
from constants import Constants
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Основной функционал: Проверка перехода по клику на «Конструктор».')
    def test_constructor_link_redirect(self, driver):
       main_page = MainPage(driver)

    @allure.title('Основной функционал: Проверка перехода по клику на «Лента заказов».')
    def test_orders_list_redirect(self, driver):
       main_page = MainPage(driver)


    @allure.title('Основной функционал: Проверка если кликнуть на ингредиент, появится всплывающее окно с деталями.')
    def test_pop_up_window_appears_by_ingredient_click(self, driver):
        main_page = MainPage(driver)

    @allure.title('Основной функционал: Проверка что всплывающее окно закрывается кликом по крестику.')
    def test_pop_up_window_closed_by_x_icon(self, driver):
        main_page = MainPage(driver)

    @allure.title('Основной функционал: Проверка что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента.')
    def test_ingredients_counter_increasing_by_adding_new_ingredient(self, driver):
        main_page = MainPage(driver)

    @allure.title('Основной функционал: Проверка что залогиненный пользователь может оформить заказ.')
    def test_logined_user_can_create_order(self, driver):
        main_page = MainPage(driver)