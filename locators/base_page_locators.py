from selenium.webdriver.common.by import By


class BasePageLocators:
    CONSTRUCTOR_LINK = [By.XPATH, "//div//p[@class='AppHeader_header__linkText__3q_va ml-2'][text() = 'Конструктор']"]
    ORDERS_LIST_LINK = [By.XPATH, "//div//p[@class='AppHeader_header__linkText__3q_va ml-2'][text() = 'Лента Заказов']"]
    PERSONAL_ACCOUNT_LINK = [By.XPATH, "//div/header/nav/a/p[@class='AppHeader_header__linkText__3q_va ml-2']"]

    MODAL_FORM = [By.XPATH, "//div/section/div[@class='Modal_modal_overlay__x2ZCr']"]

    def get_order_locator_by_index(self, index):
        return [By.XPATH, f"//li[{index}]//p[@class = 'text text_type_digits-default']"]
