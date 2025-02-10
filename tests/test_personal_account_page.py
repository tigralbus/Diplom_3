import allure
from conftest import driver
from constants import Constants
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccountPage:

    @allure.title('Личный кабинет: Проверка перехода по клику на «Личный кабинет».')
    def test_link_to_personal_account_page(self, driver):
        personal_page = PersonalAccountPage(driver)
        personal_page.login_to_account(driver)
        personal_page.wait_till_modal_form_disappear(driver)
        personal_page.click_personal_account_link()

        assert personal_page.get_current_url() == Constants.PERSONAL_ACCOUNT_URL

    @allure.title('Личный кабинет: Проверка перехода в раздел «История заказов».')
    def test_link_to_orders_history_page(self, driver):
        personal_page = PersonalAccountPage(driver)
        personal_page.login_to_account(driver)
        personal_page.wait_till_modal_form_disappear(driver)
        personal_page.click_personal_account_link()
        personal_page.await_loaded_profile()
        personal_page.click_orders_history_link()
        personal_page.await_loaded_orders()

        assert personal_page.get_current_url() == Constants.ORDERS_HISTORY_URL

    @allure.title('Личный кабинет: Проверка выход из аккаунта.')
    def test_logout_possible(self, driver):
        personal_page = PersonalAccountPage(driver)
        personal_page.login_to_account(driver)
        personal_page.wait_till_modal_form_disappear(driver)
        personal_page.click_personal_account_link()
        personal_page.click_exit_link()
        personal_page.await_loaded_login_page_header()

        assert personal_page.get_current_url() == Constants.LOGIN_URL
