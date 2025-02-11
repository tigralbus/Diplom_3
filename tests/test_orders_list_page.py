import allure
from conftest import driver
from pages.orders_list_page import OrdersListPage


class TestOrdersListPage:

    @allure.title('Раздел «Лента заказов»: Проверка если кликнуть на заказ, откроется всплывающее окно с деталями.')
    def test_pop_up_window_with_details_opened_for_order(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.go_to_site()
        orders_list_page.click_random_place()
        orders_list_page.wait_till_modal_form_disappear()
        orders_list_page.click_orders_list_link()
        orders_list_page.click_top_order_in_orders_list()

        assert orders_list_page.order_details_modal_window_is_displayed() == True

    @allure.title(
        'Раздел «Лента заказов»: Проверка что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов».')
    def test_orders_from_orders_history_displayed_in_orders_list(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.login_and_create_new_order()
        orders_list_page.click_personal_account_link()
        orders_list_page.click_random_place()
        orders_list_page.wait_till_modal_form_disappear()
        history_ids = orders_list_page.get_history_orders_ids_list()
        orders_list_page.click_orders_list_link()
        orders_list_ids = orders_list_page.orders_ids_on_orders_list_page()

        assert all(item in orders_list_ids for item in history_ids)

    @allure.title(
        'Раздел «Лента заказов»: Проверка что при создании нового заказа счётчик Выполнено за всё время увеличивается.')
    def test_all_time_orders_counter_increasing_with_new_order(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.login_to_account()
        orders_list_page.click_orders_list_link()
        orders_list_page.await_all_time_counter()
        all_orders_count = orders_list_page.get_all_time_orders_counter_value()
        orders_list_page.create_new_order()
        orders_list_page.click_orders_list_link()
        orders_list_page.await_all_time_counter()

        assert int(orders_list_page.get_all_time_orders_counter_value()) == int(all_orders_count) + 1

    @allure.title(
        'Раздел «Лента заказов»: Проверка что при создании нового заказа счётчик Выполнено за сегодня увеличивается.')
    def test_today_orders_counter_increasing_with_new_order(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.login_to_account()
        orders_list_page.click_orders_list_link()
        orders_list_page.await_today_counter()
        today_orders_count = orders_list_page.get_today_orders_counter_value()
        orders_list_page.create_new_order()
        orders_list_page.click_orders_list_link()
        orders_list_page.await_today_counter()

        assert int(orders_list_page.get_today_orders_counter_value()) == int(
            today_orders_count) + 1

    @allure.title(
        'Раздел «Лента заказов»: Проверка что после оформления заказа его номер появляется в разделе В работе.')
    def test_created_order_id_appears_in_processed_orders_list(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.login_to_account()
        orders_list_page.click_orders_list_link()
        order_id = orders_list_page.create_new_order_and_return_order_id()
        orders_list_page.click_orders_list_link()
        orders_list_page.await_in_work_order_list_loading()

        assert orders_list_page.get_in_work_order_id() == f'0{order_id}'
