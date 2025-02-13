from time import sleep
from selenium.common import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants


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

    @allure.step('переместить один элемент в другой')
    def move_one_element_to_another_one(self, source_element_locator, target_element_locator):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(self.driver.find_element(*source_element_locator),
                              self.driver.find_element(*target_element_locator)).perform()

    @allure.step('вернуть количество элементов соответствующих локатору')
    def count_elements(self, locator):
        return len(self.driver.find_elements(*locator))

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

    @allure.step('подождать пока элемент исчезнет')
    def wait_till_element_gone(self, element_name, time=10):  # 10 секунд ожидания
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.invisibility_of_element_located(element_name))

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
