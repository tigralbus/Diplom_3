import allure
from constants import Constants
from pages.personal_account_page import PersonalAccountPage
from conftest import driver, disposable_user, new_user_parameters, disposable_order


class TestPersonalAccountPage:

    @allure.title('Личный кабинет: Проверка перехода по клику на «Личный кабинет».')
    def test_link_to_personal_account_page(self, driver, new_user_parameters, disposable_user):
        personal_page = PersonalAccountPage(driver)
        access_token, new_user_parameters, response = disposable_user
        personal_page.navigation.login_to_account_create_user_api(new_user_parameters)
        personal_page.navigation.click_personal_account_link()
        personal_page.await_loaded_profile()

        assert personal_page.get_current_url() == Constants.PERSONAL_ACCOUNT_URL

    @allure.title('Личный кабинет: Проверка перехода в раздел «История заказов».')
    def test_link_to_orders_history_page(self, driver, new_user_parameters, disposable_order):
        personal_page = PersonalAccountPage(driver)
        new_user_parameters, order_id, ingredients_ids_list, access_token = disposable_order
        personal_page.navigation.login_to_account_create_user_api(new_user_parameters)
        personal_page.navigation.click_personal_account_link()
        personal_page.await_loaded_profile()
        personal_page.click_orders_history_link()
        personal_page.await_loaded_orders()

        assert personal_page.get_current_url() == Constants.ORDERS_HISTORY_URL

    @allure.title('Личный кабинет: Проверка выход из аккаунта.')
    def test_logout_possible(self, driver, new_user_parameters, disposable_user):
        personal_page = PersonalAccountPage(driver)
        access_token, new_user_parameters, response = disposable_user
        personal_page.navigation.login_to_account_create_user_api(new_user_parameters)
        personal_page.navigation.click_personal_account_link()
        personal_page.click_exit_link()
        personal_page.await_loaded_login_page_header()

        assert personal_page.get_current_url() == Constants.LOGIN_URL
