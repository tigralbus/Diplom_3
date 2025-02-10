import allure
from conftest import driver
from constants import Constants
from pages.orders_list_page import OrdersListPage


class TestOrdersListPage:

    @allure.title('Раздел «Лента заказов»: Проверка если кликнуть на заказ, откроется всплывающее окно с деталями.')
    def test_pop_up_window_with_details_opened_for_order(self, driver):
       orders_list_page = OrdersListPage(driver)

    @allure.title('Раздел «Лента заказов»: Проверка что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов».')
    def test_orders_from_orders_history_displayed_in_orders_list(self, driver):
       orders_list_page = OrdersListPage(driver)


    @allure.title('Раздел «Лента заказов»: Проверка что при создании нового заказа счётчик Выполнено за всё время увеличивается.')
    def test_all_time_orders_counter_increasing_with_new_order(self, driver):
        orders_list_page = OrdersListPage(driver)

    @allure.title('Раздел «Лента заказов»: Проверка что при создании нового заказа счётчик Выполнено за сегодня увеличивается.')
    def test_today_orders_counter_increasing_with_new_order(self):
        orders_list_page = OrdersListPage()

    @allure.title('Раздел «Лента заказов»: Проверка что после оформления заказа его номер появляется в разделе В работе.')
    def test_creared_order_id_appears_in_processed_orders_list(self):
        orders_list_page = OrdersListPage()