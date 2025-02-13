from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    PROFILE_BUTTON = [By.XPATH, "//a[text()='Профиль']"]
    EXIT_BUTTON = [By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"]
    ORDERS_HISTORY_BUTTON = [By.XPATH, "//a[text()='История заказов']"]
    ORDERS_HISTORY_LIST = [By.XPATH,
                           "//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']"]
    ORDERS_LIST_HISTORY = [By.XPATH, "//li[@class = 'OrderHistory_listItem__2x95r mb-6']"]
