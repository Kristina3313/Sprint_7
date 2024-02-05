import allure


@allure.story('Получение списка заказов')
class TestOrderList:
    @allure.title('Получение списка заказов с несуществующим courierId')
    def test_get_list_order_with_nonexistent_courier_id(self, order_page):
        nonexistent_courier_id = 999999
        response = order_page.get_orders(courierId=nonexistent_courier_id)
        assert response.status_code == 404
        assert response.json()["message"] == f"Курьер с идентификатором {nonexistent_courier_id} не найден"

    @allure.title('Получение списка заказов с существующим courierId')
    def test_get_list_order_with_correct_courier_id(self, courier_page, order_page):
        courier_page.login_courier({"login": "naumova", "password": "kristina"})
        id_courier = courier_page.get_id_courier()
        response2 = order_page.get_orders(id_courier)
        orders = response2.json().get('orders', [])
        assert response2.status_code == 200
        assert any('track' in order for order in orders), "Ни один заказ не содержит 'track'"
