import allure
from locators.base_page_locators import BasePageLocators
from locators.heades_page_locators import HeadersPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.personal_account_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class NavigationHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('совершить логин в аккаунт')
    def login_to_account_create_user_api(self, new_user_parameters):
        navigation_helper = NavigationHelper(self.driver)
        navigation_helper.go_to_login_page()
        navigation_helper.fill_field(LoginPageLocators.EMAIL_FIELD, new_user_parameters["email"])
        navigation_helper.fill_field(LoginPageLocators.PASSWORD_FIELD, new_user_parameters["password"])
        navigation_helper.click_locator(LoginPageLocators.ENTER_BUTTON)

    @allure.step('получить список id заказов на странице')
    def create_list_of_orders_ids(self, list_elements_locator):
        list_ids = []
        list_elements_count = self.count_elements(list_elements_locator)
        for i in range(1, list_elements_count):
            locator = BasePageLocators().get_order_locator_by_index(i)
            order_id = self.get_element_text(locator)
            list_ids.append(order_id)
        return list_ids

    @allure.step('получить список id заказов на странице')
    def create_list_of_orders_ids(self, list_elements_locator):
        list_ids = []
        list_elements_count = self.count_elements(list_elements_locator)
        for i in range(1, list_elements_count):
            locator = BasePageLocators().get_order_locator_by_index(i)
            order_id = self.get_element_text(locator)
            list_ids.append(order_id)
        return list_ids

    @allure.step('получить список id заказов на странице истории заказов')
    def get_history_orders_ids_list(self):
        return self.create_list_of_orders_ids(PersonalAccountPageLocators.ORDERS_LIST_HISTORY)

    @allure.step('кликнуть на Конструктор')
    def click_constructor_link(self):
        self.click_locator(HeadersPageLocators.CONSTRUCTOR_LINK)

    @allure.step('кликнуть на Ленту Заказов')
    def click_orders_list_link(self):
        self.click_locator(HeadersPageLocators.ORDERS_LIST_LINK)

    @allure.step('кликнуть на Личный Кабинет')
    def click_personal_account_link(self):
        self.click_locator(HeadersPageLocators.PERSONAL_ACCOUNT_LINK)
