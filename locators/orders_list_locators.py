from selenium.webdriver.common.by import By


class OrdersListPageLocators:
    ALL_ORDERS_COUNTER = [By.XPATH,
                          "//p[text() = 'Выполнено за все время:']/../p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']"]
    TODAY_ORDERS_COUNTER = [By.XPATH,
                            "//p[text() = 'Выполнено за сегодня:']/../p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']"]

    ORDERS_LIST_HEADER = [By.XPATH, "//h1[text()='Лента заказов']"]
    ORDER_DETAILS_MODAL_POP_UP = [By.XPATH,
                                  "//div[@class = 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"]
    TOP_ORDER_IN_LIST = [By.XPATH, "//li[1]//h2[@class = 'text text_type_main-medium mb-2']"]
    ORDERS_LIST = [By.XPATH, "//li[@class = 'OrderHistory_listItem__2x95r mb-6']"]
    IN_WORK_ORDERS_LIST = [By.XPATH,
                           "//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class = 'text text_type_digits-default mb-2']"]
