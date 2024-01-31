import allure
from utils.api_client import APIClient


class OrderPage:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    @allure.step('Отправка запроса на создание заказа')
    def create_order(self, data):
        return self.api_client.post('/api/v1/orders', data=data)

    @allure.step('Отправка запроса на получение заказа')
    def get_orders(self, courierId=None):
        params = {'courierId': courierId} if courierId is not None else {}
        return self.api_client.get('/api/v1/orders', params=params)

