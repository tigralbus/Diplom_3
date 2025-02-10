import time
import allure

from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators
from locators.personal_account_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

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

    @allure.step('подождать пока элемент исчезнет')
    def wait_till_modal_form_disappear(self, driver):
        time.sleep(5)
        self.wait_till_element_gone(driver, BasePageLocators.MODAL_FORM)