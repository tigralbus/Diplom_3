import allure
import requests
from constants import Constants


class OrderRoutes:
    @allure.step('API: Создать заказ с 2 ингредиентами по индексу')
    def create_order(self, access_token, ingredients_ids_list, index1, index2):
        ingredients_load = {
            "ingredients": [ingredients_ids_list[index1], ingredients_ids_list[index2]]
        }
        headers = {
            "Authorization": f"{access_token}"
        }
        response = requests.post(f"{Constants.API_URL}/orders", data=ingredients_load, headers=headers)
        return response


    @allure.step('Получить список ингредиентов')
    def get_ingredients_list(self):
        response = requests.get(f"{Constants.API_URL}/ingredients")
        ingredients_ids_list = []
        for i in range(len(response.json()["data"])):
            ingredients_ids_list.append(response.json()["data"][i]["_id"])
        return ingredients_ids_list