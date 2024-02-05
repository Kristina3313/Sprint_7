import allure
import pytest


@allure.story('Создание заказов')
class TestOrderCreation:
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.title('Создание заказа с указанием цвета: {colors}')
    def test_successful_order_creation(self, api_client, order_page, colors):
        order_data = {
            "firstName": "Kristina",
            "lastName": "Naumova",
            "address": "Ufa",
            "metroStation": "4",
            "phone": "+7 800 000 00 01",
            "rentTime": 3,
            "deliveryDate": "2024-02-25",
            "comment": "Hello from Kristina :)",
            "color": colors
        }
        response = order_page.create_order(order_data)
        assert response.status_code == 201
        assert "track" in response.json()
