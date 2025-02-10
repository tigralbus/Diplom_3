from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    PROFILE_BUTTON = [By.XPATH, "//div/main/div/nav/ul//a[text()='Профиль']"]
    EXIT_BUTTON = [By.XPATH, "//div/main/div/nav/ul//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"]
    ORDERS_HISTORY_BUTTON = [By.XPATH, "//div/main/div/nav/ul//a[text()='История заказов']"]
    ORDERS_HISTORY_LIST = [By.XPATH, "//div/main/div/div/div/ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']"] #это когда заказы есть, когда нет хз

