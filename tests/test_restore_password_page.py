import allure
from conftest import driver
from constants import Constants
from pages.restore_password_page import RestorePasswordPage


class TestMainPageQuestions:

    @allure.title(
        'Восстановление пароля: Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль».')
    def test_restore_link_redirect_to_restore_form(self, driver):
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.go_to_site()
        restore_password_page.navigation.click_personal_account_link()
        restore_password_page.click_restore_link()

        assert restore_password_page.get_current_url() == Constants.FORGOT_PASSWORD_URL

    @allure.title('Восстановление пароля: Проверка ввода почты и клика по кнопке «Восстановить».')
    def test_enter_email_click_restore_button(self, driver):
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.go_to_site()
        restore_password_page.navigation.click_personal_account_link()
        restore_password_page.click_restore_link()
        restore_password_page.await_restore_password_header()
        restore_password_page.input_email_value()
        restore_password_page.click_restore_button()
        restore_password_page.await_loaded_enter_code_field()

        assert restore_password_page.get_current_url() == Constants.RESTORE_PASSWORD_URL

    @allure.title(
        'Восстановление пароля: Проверка клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_hide_show_button_activates_password_field(self, driver):
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.go_to_site()
        restore_password_page.navigation.click_personal_account_link()
        restore_password_page.click_restore_link()
        restore_password_page.await_restore_password_header()
        restore_password_page.input_email_value()
        restore_password_page.click_restore_button()
        restore_password_page.await_loaded_enter_code_field()

        restore_password_page.await_loaded_enter_code_field()
        restore_password_page.input_password_value()

        restore_password_page.click_show_hide_password_button()
        restore_password_page.await_new_password_field()

        assert restore_password_page.get_type_new_password_field() == 'text'

        restore_password_page.click_enter_code_field()

        assert restore_password_page.get_type_new_password_field() == 'password'
