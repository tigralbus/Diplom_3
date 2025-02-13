import allure
from locators.orders_list_locators import OrdersListPageLocators
from pages.base_page import BasePage
from pages.navigation_helper import NavigationHelper


class OrdersListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigation = NavigationHelper(driver)

    @allure.step('кликнуть на заказ из ленты заказов')
    def click_top_order_in_orders_list(self):
        self.click_locator(OrdersListPageLocators.TOP_ORDER_IN_LIST)

    @allure.step('подождать появление модального окна с деталями заказа')
    def await_order_details_modal_window_appears(self):
        self.wait_till_element_gone(OrdersListPageLocators.ORDER_DETAILS_MODAL_POP_UP)

    @allure.step('проверить видимость модального окна с деталями заказа')
    def order_details_modal_window_is_displayed(self):
        return self.element_is_displayed(OrdersListPageLocators.ORDER_DETAILS_MODAL_POP_UP)

    @allure.step('подождать исчезновение модального окна с деталями заказа')
    def await_order_details_modal_window_is_gone(self):
        self.await_element(OrdersListPageLocators.ORDER_DETAILS_MODAL_POP_UP)

    @allure.step('получить список id заказов страницы Лента Заказов')
    def orders_ids_on_orders_list_page(self):
        return self.navigation.create_list_of_orders_ids(OrdersListPageLocators.ORDERS_LIST)

    @allure.step('подождать загрузку значения счетчика заказов за сегодня страницы Лента Заказов')
    def await_today_counter(self):
        self.await_element(OrdersListPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step('получить значение счетчика заказов за сегодня страницы Лента Заказов')
    def get_today_orders_counter_value(self):
        return self.get_element_text(OrdersListPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step('подождать загрузку значения счетчика заказов за все время страницы Лента Заказов')
    def await_all_time_counter(self):
        self.await_element(OrdersListPageLocators.ALL_ORDERS_COUNTER)

    @allure.step('получить значение счетчика заказов за все время страницы Лента Заказов')
    def get_all_time_orders_counter_value(self):
        return self.get_element_text(OrdersListPageLocators.ALL_ORDERS_COUNTER)

    @allure.step('подождать загрузку списка заказов в работе страницы Лента Заказов')
    def await_in_work_order_list_loading(self):
        self.await_element(OrdersListPageLocators.IN_WORK_ORDERS_LIST)

    @allure.step('получить id заказа в работе на странице Лента Заказов')
    def get_in_work_order_id(self):
        return self.get_element_text(OrdersListPageLocators.IN_WORK_ORDERS_LIST)
