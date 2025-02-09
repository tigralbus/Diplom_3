import allure
from conftest import driver
from constants import Constants
from pages.personal_account_page import PersonalAccountPage


class TestMainPageQuestions:

    @allure.title('Личный кабинет: Проверка перехода по клику на «Личный кабинет».')
    def test_link_to_personal_account_page(self, driver):

    @allure.title('Личный кабинет: Проверка перехода в раздел «История заказов».')
    def test_link_to_orders_history_page(self, driver):

    @allure.title('Личный кабинет: Проверка выходf из аккаунта.')
    def test_logout_possible(self, driver):