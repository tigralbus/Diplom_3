from selenium.webdriver.common.by import By


class OrdersListPageLocators:
    ALL_ORDERS_COUNTER = [By.CLASS_NAME, 'Home_Header__iJKdX']
    TODAY_ORDERS_COUNTER = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text() = 'Заказать']"]
    WORKING_ORDERS_ID = []
    ORDERS_LIST_IDs = []
    ORDERS_LIST_HEADER = [By.XPATH, "//div/main/div/h1[text()='Лента заказов']"]
