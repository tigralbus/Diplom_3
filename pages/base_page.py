from selenium.webdriver.support import expected_conditions as EC

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL

    def await_loaded(self):
        self.wait_element(self.page_locator())

    def page_locator(self):
        return None

    @allure.step('перейти на стартовую страницу Stellar Burgers')
    def go_to_site(self):
        self.driver.get(Constants.URL)

    @allure.step('подождать пока появится локатор')
    def wait_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located(locator), message=f'Not find element {locator}')

    @allure.step('кликнуть на элемент')
    def click_locator(self, locator):
        self.wait_element(locator, 10).click()

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
        attribute_value= element.get_attribute(attribute)
        return attribute_value

    @allure.step('получить урл текущей табы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('кликнуть на случайное место экрана')
    def click_random_place(self, driver):
        ActionChains(driver).move_by_offset(10, 10).click().perform()

    @allure.step('подождать пока элемент исчезнет')
    def wait_till_element_gone(self, driver, element_name):
        wait = WebDriverWait(driver, 10)  # 10 секунд ожидания
        wait.until(EC.invisibility_of_element_located(element_name))

    #
    # @allure.step('выбрать значение чекбокса')
    # def select_checkbox_by_value(self, value):
    #     checkbox = [By.ID, value]
    #     self.click_locator(checkbox)
    #
    # @allure.step('получить список открытых табов')
    # def get_tabs_list(self):
    #     return self.driver.window_handles
    #
    # @allure.step('переключиться на табу {tab_number}')
    # def switch_to_tab(self, tab_number):
    #     self.driver.switch_to.window(self.get_tabs_list()[tab_number])


    #

