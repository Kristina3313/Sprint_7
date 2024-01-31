import allure
import pytest
from utils.api_client import APIClient
from pages.courier_page import CourierPage
from pages.order_page import OrderPage


@allure.story('Получение списка заказов')
class TestOrderList:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def courier_page(self, api_client):
        return CourierPage(api_client)

    @pytest.fixture
    def order_api(self, api_client):
        return OrderPage(api_client)

    @allure.title('Получение списка заказов с несуществующим courierId')
    def test_get_list_order_with_nonexistent_courier_id(self, order_api):
        nonexistent_courier_id = 999999
        response = order_api.get_orders(courierId=nonexistent_courier_id)
        assert response.status_code == 404
        assert response.json()["message"] == f"Курьер с идентификатором {nonexistent_courier_id} не найден"

    @allure.title('Получение списка заказов с существующим courierId')
    def test_get_list_order_with_correct_courier_id(self, courier_page, order_api):
        courier_page.login_courier({"login": "naumova", "password": "kristina"})
        id_courier = courier_page.get_id_courier()
        response2 = order_api.get_orders(id_courier)
        orders = response2.json().get('orders', [])
        assert response2.status_code == 200
        assert any('track' in order for order in orders), "Ни один заказ не содержит 'track'"
