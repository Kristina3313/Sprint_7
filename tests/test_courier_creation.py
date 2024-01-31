import allure
import pytest
from utils.api_client import APIClient
from pages.courier_page import CourierPage


@allure.story('Создание курьера')
class TestCourierCreation:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def courier_page(self, api_client):
        return CourierPage(api_client)

    @allure.title('Создание курьера с передачей обязательных полей')
    def test_create_courier(self, courier_page):
        courier_data = courier_page.valid_courier_data()
        response = courier_page.create_courier(courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Создание дубликата курьера')
    def test_create_duplicate_courier(self, courier_page):
        courier_data = courier_page.valid_courier_data()
        courier_page.create_courier(courier_data)
        response = courier_page.create_courier(courier_data)
        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Создание курьера с недостаточными данными')
    def test_create_courier_missing_one_field(self, courier_page):
        courier_data = courier_page.valid_courier_data()
        del courier_data['password']
        response = courier_page.create_courier(courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
