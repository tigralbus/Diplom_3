import allure
from conftest import driver, disposable_user, new_user_parameters
from constants import Constants
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Основной функционал: Проверка перехода по клику на «Конструктор».')
    def test_constructor_redirect_by_constructor_link(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_random_place()
        main_page.wait_till_modal_form_disappear()
        main_page.click_orders_list_link()
        main_page.click_constructor_link()

        assert main_page.get_current_url() == Constants.URL

    @allure.title('Основной функционал: Проверка перехода по клику на «Лента заказов».')
    def test_redirect_by_orders_list(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_random_place()
        main_page.wait_till_modal_form_disappear()
        main_page.click_orders_list_link()

        assert main_page.get_current_url() == Constants.ORDERS_LIST_URL

    @allure.title('Основной функционал: Проверка если кликнуть на ингредиент, появится всплывающее окно с деталями.')
    def test_pop_up_window_appears_by_ingredient_click(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_random_place()
        main_page.wait_till_modal_form_disappear()
        main_page.click_ingredient()

        assert main_page.get_current_url() == Constants.INGREDIENT_BUN_DETAILS_URL

    @allure.title('Основной функционал: Проверка что всплывающее окно закрывается кликом по крестику.')
    def test_pop_up_window_closed_by_x_icon(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_random_place()
        main_page.wait_till_modal_form_disappear()
        main_page.click_ingredient()
        main_page.click_close_icon_ingredient_details()
        main_page.await_ingredient_modal_window_is_gone()

        assert main_page.ingredient_modal_window_is_displayed() == False

    @allure.title(
        'Основной функционал: Проверка что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента.')
    def test_ingredients_counter_increasing_by_adding_new_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_random_place()
        main_page.wait_till_modal_form_disappear()
        main_page.add_ingredient_to_order()
        main_page.count_ingredients()

        assert main_page.count_ingredients() == 2

    @allure.title('Основной функционал: Проверка что залогиненный пользователь может оформить заказ.')
    def test_authorized_user_can_create_order(self, driver, new_user_parameters, disposable_user):
        main_page = MainPage(driver)
        main_page.login_to_account()
        #access_token, new_user_parameters, response = disposable_user #постоянно падает
        #main_page.login_to_account_create_user_api(new_user_parameters)
        main_page.count_ingredients()
        main_page.click_make_order_button()
        #main_page.await_new_order_modal_window_default_id_gone()

        success = main_page.check_new_order_modal_header_displayed()
        if not success:
            print("ololo")
        assert main_page.check_new_order_modal_header_displayed() == True
