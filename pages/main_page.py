import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def page_locator(self):
        return MainPageLocators.MAIN_PAGE_HEADER

    @allure.step('кликнуть на нижнюю кнопку Заказать')
    def click_lower_order_button(self):
        button = self.await_element(MainPageLocators.LOWER_ORDER_BUTTON)
        # при дефолтном скролле закрыто с подтверждением куки
        self.scroll_to_element(button)
        button.click()

    @allure.step('раскрыть ответ на вопрос')
    def get_answer(self, question_locator, answer_locator):
        self.await_element(question_locator)
        self.click_locator(question_locator)
        self.await_element(answer_locator)
        return self.get_element_text(answer_locator)

    @allure.step('нажать кнопку Заказать')
    def make_order(self, use_top_button):
        if use_top_button:
            self.click_order_button()
        else:
            self.click_lower_order_button()