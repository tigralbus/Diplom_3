from selenium.webdriver.common.by import By


class BasePageLocators:
    def get_order_locator_by_index(self, index):
        return [By.XPATH, f"//li[{index}]//p[@class = 'text text_type_digits-default']"] #шаблон локатора актуален для 2 страниц Лента Заказов и История Заказов
