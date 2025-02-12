import allure
import requests
from constants import Constants


class UserRoutes:
    @allure.step('API: Создать юзера')
    def create_user(self, new_user_parameters):
        response = requests.post(f"{Constants.API_URL}/auth/register", data=new_user_parameters)
        return response

    @allure.step('API: Удалить юзера')
    def delete_user(self, access_token):
        headers = {
            "Authorization": f"{access_token}"
        }
        response_delete = requests.delete(f"{Constants.API_URL}/auth/user", headers=headers)
        return response_delete
