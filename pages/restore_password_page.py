import allure
from constants import UserData
from locators.restore_password_locators import RestorePasswordPageLocators
from pages.base_page import BasePage
from pages.navigation_helper import NavigationHelper


class RestorePasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigation = NavigationHelper(driver)

    @allure.step('Подождать прогрузки Заголовки формы восстановления пароля')
    def await_restore_password_header(self):
        self.await_element(RestorePasswordPageLocators.RESTORE_PASSWORD_HEADER)

    @allure.step('кликнуть на ссылку Восстановить пароль')
    def click_restore_link(self):
        self.click_locator(RestorePasswordPageLocators.RESTORE_LINK)

    @allure.step('ввести значение емейла в поле')
    def input_email_value(self):
        self.fill_field(RestorePasswordPageLocators.RESTORE_EMAIL_FIELD, UserData.RESTORE_EMAIL)

    @allure.step('ввести значение в поле Пароль')
    def input_password_value(self):
        self.fill_field(RestorePasswordPageLocators.RESTORE_PASSWORD_FIELD, UserData.RESTORE_PASSWORD)

    @allure.step('кликнуть иконку Показать/скрыть пароль')
    def click_show_hide_password_button(self):
        self.click_locator(RestorePasswordPageLocators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step('кликнуть кнопку Восстановить')
    def click_restore_button(self):
        self.click_locator(RestorePasswordPageLocators.RESTORE_BUTTON)

    @allure.step('Подождать загрузки поля ввода кода из письма')
    def await_loaded_enter_code_field(self):
        self.await_element(RestorePasswordPageLocators.ENTER_CODE_FROM_EMAIL_FIELD)

    @allure.step('Подождать дезактивации поля пароль')
    def await_new_password_field(self):
        self.await_element(RestorePasswordPageLocators.ENTER_NEW_PASSWORD_FIELD)

    @allure.step('Получить значение типа активности поля Пароля')
    def get_type_new_password_field(self):
        value = self.get_element_attribute_value(RestorePasswordPageLocators.ENTER_NEW_PASSWORD_FIELD, "type")
        return value

    @allure.step('кликнуть поле ввода кода из емейла')
    def click_enter_code_field(self):
        self.click_locator(RestorePasswordPageLocators.ENTER_CODE_FROM_EMAIL_FIELD)
