import time
import allure


class CourierApi:
    def __init__(self, api_client):
        self.api_client = api_client
        self.courier_id = None

    @allure.step('Создание курьера')
    def create_courier(self, data):
        return self.api_client.post('/api/v1/courier', data=data)

    @allure.step('Авторизация курьера')
    def login_courier(self, data):
        response = self.api_client.post('/api/v1/courier/login', data=data)
        if response.status_code == 200:
            self.courier_id = response.json().get("id")
        return response

    @allure.step('Генерация валидных данных курьера')
    def valid_courier_data(self):
        timestamp = int(time.time())
        login = f"test_courier_{timestamp}"
        password = "password123"
        first_name = "Kristina"
        return {"login": login, "password": password, "firstName": first_name}

    @allure.step('Получение ID курьера')
    def get_id_courier(self):
        return self.courier_id
