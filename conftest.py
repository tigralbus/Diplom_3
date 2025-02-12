import pytest
from selenium import webdriver

from api_routes.order_routes import OrderRoutes
from api_routes.user_routes import UserRoutes
from helpers import RandomHelper


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
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
    response = user.create_user(new_user_parameters)
    access_token = response.json()['accessToken']
    yield access_token, new_user_parameters, response
    user.delete_user(access_token)


@pytest.fixture(scope='function')
def disposable_order(new_user_parameters):
    user = UserRoutes()
    response_create_user = user.create_user(new_user_parameters)
    access_token = response_create_user.json()['accessToken']
    order = OrderRoutes()
    ingredients_ids_list = order.get_ingredients_list()
    response_create_order = order.create_order(access_token, ingredients_ids_list, 3, 5)
    order_id = response_create_order.json()['order']['number']
    yield new_user_parameters, order_id, ingredients_ids_list, access_token
    user.delete_user(access_token)
