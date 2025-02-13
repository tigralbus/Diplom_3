import allure
from locators.login_page_locators import LoginPageLocators
from locators.personal_account_locators import PersonalAccountPageLocators
from pages.base_page import BasePage
from pages.navigation_helper import NavigationHelper


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigation = NavigationHelper(driver)

    @allure.step('кликнуть на История заказов')
    def click_orders_history_link(self):
        self.click_locator(PersonalAccountPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('кликнуть на Выход')
    def click_exit_link(self):
        self.click_locator(PersonalAccountPageLocators.EXIT_BUTTON)

    @allure.step('Подождать загрузки Профиля')
    def await_loaded_profile(self):
        self.await_element(PersonalAccountPageLocators.PROFILE_BUTTON)

    @allure.step('Подождать загрузки Истории заказов')
    def await_loaded_orders(self):
        self.await_element(PersonalAccountPageLocators.ORDERS_HISTORY_LIST)

    @allure.step('Подождать загрузки Профиля')
    def await_loaded_login_page_header(self):
        self.await_element(LoginPageLocators.LOGIN_FORM_HEADER)

    @allure.step('получить список id заказов на странице истории заказов')
    def get_history_orders_ids_list(self):
        return self.navigation.create_list_of_orders_ids(PersonalAccountPageLocators.ORDERS_LIST_HISTORY)
