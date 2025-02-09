from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    PROFILE_HEADER = [By.XPATH, "//div/main/div/nav/ul//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"]
    EXIT_BUTTON = [By.XPATH, "//div/main/div/nav/ul//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"]
    ORDERS_HISTORY_BUTTON = [By.XPATH, "//div/main/div/nav/ul//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"]
    ORDERS_HISTORY_LIST = [By.XPATH, "//div/main/div/div/div/ul/li[@class='OrderHistory_listItem__2x95r mb-6']"] #это когда заказы есть, когда нет хз

