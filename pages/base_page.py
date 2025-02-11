import time
from time import sleep

from selenium.common import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants, UserData
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL

    @allure.step('перейти на стартовую страницу Stellar Burgers')
    def go_to_site(self):
        self.driver.get(Constants.URL)

    @allure.step('перейти на страницу логина')
    def go_to_login_page(self):
        self.driver.get(Constants.LOGIN_URL)

    @allure.step('подождать пока появится локатор')
    def await_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located(locator), message=f'Not find element {locator}')

    @allure.step('кликнуть на элемент')
    def click_locator(self, locator):
        element = (self.await_element(locator, 10))
        try:
            element.click()
        except ElementClickInterceptedException:
            # в Firefox оверлей может перехватывать клики несмотря на успешное ожидание
            # wait_till_element_gone(BasePageLocators.MODAL_FORM)
            sleep(1)
            element.click()

    @allure.step('кликнуть на Конструктор')
    def click_constructor_link(self):
        self.click_locator(BasePageLocators.CONSTRUCTOR_LINK)

    @allure.step('кликнуть на Ленту Заказов')
    def click_orders_list_link(self):
        self.click_locator(BasePageLocators.ORDERS_LIST_LINK)

    @allure.step('кликнуть на Личный Кабинет')
    def click_personal_account_link(self):
        self.click_locator(BasePageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step('подождать загрузку урла {url}')
    def await_url(self, url, time=10):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.url_to_be(url), message=f"URL did not match exactly: {url}")

    @allure.step('проскроллить страницу вниз до конца')
    def scroll_till_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('переместить один элемент в другой')
    def move_one_element_to_another_one(self, source_element_locator, target_element_locator):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(self.driver.find_element(*source_element_locator),
                              self.driver.find_element(*target_element_locator)).perform()

    @allure.step('вернуть количество элементов соответствующих локатору')
    def count_elements(self, locator):
        return len(self.driver.find_elements(*locator))

    @allure.step('проскроллить страницу к элементу')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('получить текст элемента')
    def get_element_text(self, locator):
        text = self.driver.find_element(*locator).text
        return text

    @allure.step('заполнить текстовое поле')
    def fill_field(self, field_name, field_value):
        element = self.driver.find_element(*field_name)
        element.send_keys(field_value)

    @allure.step('получить значение аттрибута элемента')
    def get_element_attribute_value(self, element_name, attribute):
        element = self.driver.find_element(*element_name)
        attribute_value = element.get_attribute(attribute)
        return attribute_value

    @allure.step('получить урл текущей табы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('кликнуть на случайное место экрана')
    def click_random_place(self):
        ActionChains(self.driver).move_by_offset(10, 10).click().perform()

    @allure.step('подождать пока элемент исчезнет')
    def wait_till_element_gone(self, element_name, time=10):  # 10 секунд ожидания
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.invisibility_of_element_located(element_name))

    @allure.step('подождать пока модальное окно на весь экран исчезнет')
    def wait_till_modal_form_disappear(self):
        self.wait_till_element_gone(BasePageLocators.MODAL_FORM, 10)
        time.sleep(1)  # в фаерфоксе часто зависает (не visible, но перехватывает клики)

    @allure.step('проверить является ли элемент видимым')
    def element_is_displayed(self, locator):
        try:
            modal = self.driver.find_element(*locator)
            return modal.is_displayed()
        except NoSuchElementException:
            return False

    @allure.step('дождаться видимости элемента')
    def await_element_is_displayed(self, locator):
        try:
            modal = self.await_element(locator)
            return modal.is_displayed()
        except TimeoutException:
            return False

    @allure.step('кликнуть на кнопку Войти')
    def click_enter_button(self):
        self.click_locator(LoginPageLocators.ENTER_BUTTON)

    @allure.step('совершить логин в аккаунт')
    def login_to_account(self):
        base_page = BasePage(self.driver)
        base_page.go_to_login_page()
        base_page.fill_field(LoginPageLocators.EMAIL_FIELD, UserData.EMAIL)
        base_page.fill_field(LoginPageLocators.PASSWORD_FIELD, UserData.PASSWORD)
        # base_page.click_random_place()
        # time.sleep(5)
        # base_page.wait_till_element_gone(BasePageLocators.MODAL_FORM)
        base_page.click_enter_button()
        base_page.click_random_place()
        base_page.wait_till_element_gone(BasePageLocators.MODAL_FORM)

    @allure.step('совершить логин в аккаунт')
    def login_to_account_create_user_api(self, new_user_parameters):
        base_page = BasePage(self.driver)
        base_page.go_to_login_page()
        base_page.fill_field(LoginPageLocators.EMAIL_FIELD, new_user_parameters["email"])
        base_page.fill_field(LoginPageLocators.PASSWORD_FIELD, new_user_parameters["password"])
        base_page.click_random_place()
        time.sleep(5)
        base_page.wait_till_element_gone(BasePageLocators.MODAL_FORM)
        base_page.click_enter_button()
        base_page.click_random_place()
        base_page.wait_till_element_gone(BasePageLocators.MODAL_FORM)

    @allure.step('совершить логин и оформить заказ')
    def login_and_create_new_order(self):
        base_page = BasePage(self.driver)
        base_page.login_to_account()
        base_page.move_one_element_to_another_one(MainPageLocators.INGREDIENT_BUN,
                                                  MainPageLocators.BURGER_CONSTRUCTOR_TOP)
        base_page.await_element(MainPageLocators.MAKE_ORDER_BUTTON)
        base_page.click_locator(MainPageLocators.MAKE_ORDER_BUTTON)
        base_page.await_element(MainPageLocators.CLOSE_BUTTON_CREATED_MODAL_POP_UP)
        base_page.wait_till_element_gone(MainPageLocators.PREORDER_ID)
        base_page.click_locator(MainPageLocators.CLOSE_BUTTON_CREATED_MODAL_POP_UP)

    @allure.step('совершить логин и оформить заказ')
    def create_new_order(self):
        base_page = BasePage(self.driver)
        base_page.click_constructor_link()
        base_page.move_one_element_to_another_one(MainPageLocators.INGREDIENT_BUN,
                                                  MainPageLocators.BURGER_CONSTRUCTOR_TOP)
        base_page.await_element(MainPageLocators.MAKE_ORDER_BUTTON)
        base_page.click_locator(MainPageLocators.MAKE_ORDER_BUTTON)
        base_page.await_element(MainPageLocators.CLOSE_BUTTON_CREATED_MODAL_POP_UP)
        base_page.wait_till_element_gone(MainPageLocators.PREORDER_ID)
        base_page.click_locator(MainPageLocators.CLOSE_BUTTON_CREATED_MODAL_POP_UP)

    @allure.step('совершить логин и оформить заказ')
    def create_new_order_and_return_order_id(self):
        base_page = BasePage(self.driver)
        base_page.click_constructor_link()
        base_page.move_one_element_to_another_one(MainPageLocators.INGREDIENT_BUN,
                                                  MainPageLocators.BURGER_CONSTRUCTOR_TOP)
        base_page.await_element(MainPageLocators.MAKE_ORDER_BUTTON)
        base_page.click_locator(MainPageLocators.MAKE_ORDER_BUTTON)
        base_page.await_element(MainPageLocators.CLOSE_BUTTON_CREATED_MODAL_POP_UP)
        base_page.wait_till_element_gone(MainPageLocators.PREORDER_ID)
        order_id = base_page.get_element_text(MainPageLocators.ORDER_ID_MODAL_POP_UP)
        base_page.click_locator(MainPageLocators.CLOSE_BUTTON_CREATED_MODAL_POP_UP)
        return order_id

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
