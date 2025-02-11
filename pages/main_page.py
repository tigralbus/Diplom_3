import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('кликнуть на ингредиент')
    def click_ingredient(self):
        self.click_locator(MainPageLocators.INGREDIENT_BUN)

    @allure.step('кликнуть на x кнопку деталей ингредиента')
    def click_close_icon_ingredient_details(self):
        self.click_locator(MainPageLocators.INGREDIENT_DETAILS_MODAL_CLOSE_ICON)

    @allure.step('проверить видимость модального окна с деталями ингридиента')
    def ingredient_modal_window_is_displayed(self):
        return self.element_is_displayed(MainPageLocators.INGREDIENT_DETAILS_MODAL_HEADER)

    @allure.step('подождать исчезновение модального окна с деталями ингридиента')
    def await_ingredient_modal_window_is_gone(self):
        self.wait_till_element_gone(MainPageLocators.INGREDIENT_DETAILS_MODAL_HEADER)

    @allure.step('подождать исчезновения дефолтного 9999 с модального окна с деталями нового заказа')
    def await_new_order_modal_window_default_id_gone(self):
        self.wait_till_element_gone(MainPageLocators.PREORDER_ID)

    # @allure.step('подождать появление модального окна с новым заказом')
    # def await_new_order_modal_window_appears(self):
    #     self.wait_till_element_gone(MainPageLocators.MODAL_WINDOW_NEW_ORDER)

    @allure.step('посчитать количество ингредиента')
    def count_ingredients(self):
        return self.count_elements(MainPageLocators.BUNS_IN_ORDER_FOR_COUNT)

    @allure.step('перетащить ингредиент в заказ')
    def add_ingredient_to_order(self):
        self.move_one_element_to_another_one(MainPageLocators.INGREDIENT_BUN, MainPageLocators.BURGER_CONSTRUCTOR_TOP)

    @allure.step('кликнуть на кнопку Оформить заказ')
    def click_make_order_button(self):
        self.click_locator(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('проверить что хедер модального окна отображается')
    def await_new_order_modal_header_displayed(self):
        return self.await_element_is_displayed(MainPageLocators.MODAL_WINDOW_NEW_ORDER)
