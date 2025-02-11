import pytest
from selenium import webdriver

from api_routes.order_routes import OrderRoutes
from api_routes.user_routes import UserRoutes
from helpers import RandomHelper


@pytest.fixture(params=['chrome','firefox'])  #(params=['chrome','firefox']) (params=['firefox','chrome']) (params=['chrome'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser=  webdriver.Chrome()
    else:
        raise ValueError('Unknown browser type')
    yield browser
    browser.quit()

@pytest.fixture(scope='function')
def new_user_parameters():
    # генерируем имя, емейл, пароль
    email = RandomHelper.random_email()
    password = RandomHelper.random_string(6)
    name = RandomHelper.random_name()

    # собираем тело запроса
    parameters = {
        "email": email,
        "password": password,
        "name": name
    }
    return parameters


@pytest.fixture(scope='function')
def disposable_user(new_user_parameters):
    user = UserRoutes()
    # Регистрируем нового юзера и получаем его access_token
    response = user.create_user(new_user_parameters)
    access_token = response.json()['accessToken']
    yield access_token, new_user_parameters, response  # Передаем access_token и параметры ответа в тест
    # Выполняем удаление юзера после завершения теста
    user.delete_user(access_token)

@pytest.fixture(scope='function')
def disposable_order(new_user_parameters):
    user = UserRoutes()
    # Регистрируем нового юзера и получаем его access_token
    access_token = user.create_user(new_user_parameters).json()['accessToken']
    # Получить список ингредиентов
    order = OrderRoutes()
    ingredients_ids_list = order.get_ingredients_list()
    response = order.create_order(access_token, ingredients_ids_list, 3, 5)
    yield access_token, new_user_parameters, ingredients_ids_list, response  # Передаем access_token и параметры ответа в тест
    # Выполняем удаление юзера после завершения теста
    user.delete_user(access_token)

@pytest.fixture(scope='function')
def disposable_login_user(new_user_parameters):
    user = UserRoutes()
    # Регистрируем нового юзера и получаем его access_token
    access_token = user.create_user(new_user_parameters).json()['accessToken']
    # логин юзера
    response = UserRoutes().login_user(new_user_parameters.get("email"),
                                       new_user_parameters.get("password"))
    yield access_token, new_user_parameters, response  # Передаем access_token и параметры ответа в тест
    # Выполняем удаление юзера после завершения теста
    user.delete_user(access_token)