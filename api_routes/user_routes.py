import allure
import requests
from constants import Constants


class UserRoutes:
    @allure.step('API: Создать юзера')
    def create_user(self, new_user_parameters):
        response = requests.post(f"{Constants.API_URL}/auth/register", data=new_user_parameters)
        return response

    @allure.step('API: Создать юзера для получения accessToken')
    def create_user_return_access_token(self, new_user_parameters):
        response = requests.post(f"{Constants.API_URL}/auth/register", data=new_user_parameters)
        return response.json()['accessToken']

    @allure.step('API: Логин юзера')
    def login_user(self, email, password):
        login_payload = {
            "email": email,
            "password": password,
        }
        response_login = requests.post(f"{Constants.API_URL}/auth/login",
                                       data=login_payload)
        return response_login

    @allure.step('API: Логин юзера для получения accessToken')
    def login_user_return_access_token(self, email, password):
        login_payload = {
            "email": email,
            "password": password,
        }
        response_login = requests.post(f"{Constants.API_URL}/auth/login", data=login_payload)
        return response_login.json()['accessToken']

    @allure.step('API: Удалить юзера')
    def delete_user(self, access_token):
        headers = {
            "Authorization": f"{access_token}"
        }
        response_delete = requests.delete(f"{Constants.API_URL}/auth/user", headers=headers)
        return response_delete
