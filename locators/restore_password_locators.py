from selenium.webdriver.common.by import By


class RestorePasswordPageLocators:
    RESTORE_LINK = [By.XPATH, "//a[@class='Auth_link__1fOlj'][@href='/forgot-password']"]
    RESTORE_PASSWORD_HEADER = [By.XPATH, "//h2[text() = 'Восстановление пароля']"]
    RESTORE_EMAIL_FIELD = [By.XPATH, "//input[@class='text input__textfield text_type_main-default'][@name = 'name']"]
    RESTORE_PASSWORD_FIELD = [By.XPATH,
                              "//input[@class='text input__textfield text_type_main-default'][@type='password']"]
    RESTORE_BUTTON = [By.XPATH,
                      "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]
    ENTER_CODE_FROM_EMAIL_FIELD = [By.XPATH,
                                   "//label[@class='input__placeholder text noselect text_type_main-default'][text() = 'Введите код из письма']"]
    SHOW_HIDE_PASSWORD_BUTTON = [By.XPATH, "//div[@class='input__icon input__icon-action']"]
    ENTER_NEW_PASSWORD_FIELD = [By.XPATH,
                                "//input[@class='text input__textfield text_type_main-default'][@name='Введите новый пароль']"]
