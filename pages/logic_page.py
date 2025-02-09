import allure
import time

from constants import UserData
from locators.base_page_locators import BasePageLocators
from locators.restore_password_locators import RestorePasswordPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)