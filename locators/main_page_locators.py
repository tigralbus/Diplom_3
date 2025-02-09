from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_HEADER = [By.CLASS_NAME, 'Home_Header__iJKdX']
    LOWER_ORDER_BUTTON = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text() = 'Заказать']"]

    COST_QUESTION = [By.ID, 'accordion__heading-0']
    SEVERAL_SCOOTERS_QUESTION = [By.ID, 'accordion__heading-1']
    RENT_TIME_QUESTION = [By.ID, 'accordion__heading-2']
    ORDER_TODAY_QUESTION = [By.ID, 'accordion__heading-3']
    CHANGE_RENT_TIME_QUESTION = [By.ID, 'accordion__heading-4']
    CHARGE_SCOOTER_QUESTION = [By.ID, 'accordion__heading-5']
    DECLINE_ORDER_QUESTION = [By.ID, 'accordion__heading-6']
    COUNTRYSIDE_DELIVERY_QUESTION = [By.ID, 'accordion__heading-7']

    COST_QUESTION_ANSWER = [By.ID, 'accordion__panel-0']
    SEVERAL_SCOOTERS_QUESTION_ANSWER = [By.ID, 'accordion__panel-1']
    RENT_TIME_QUESTION_ANSWER = [By.ID, 'accordion__panel-2']
    ORDER_TODAY_QUESTION_ANSWER = [By.ID, 'accordion__panel-3']
    CHANGE_RENT_TIME_QUESTION_ANSWER = [By.ID, 'accordion__panel-4']
    CHARGE_SCOOTER_QUESTION_ANSWER = [By.ID, 'accordion__panel-5']
    DECLINE_ORDER_QUESTION_ANSWER = [By.ID, 'accordion__panel-6']
    COUNTRYSIDE_DELIVERY_QUESTION_ANSWER = [By.ID, 'accordion__panel-7']