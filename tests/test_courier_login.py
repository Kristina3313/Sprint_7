import allure


@allure.story('Авторизация курьера')
class TestCourierLogin:
    @allure.title('Успешная авторизация')
    def test_successful_login(self, courier_page):
        login_data = {
            "login": "naumova",
            "password": "kristina"
        }
        response = courier_page.login_courier(data=login_data)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title('Авторизация без ввода логина')
    def test_login_without_login(self, courier_page):
        login_data = {
            "login": "",
            "password": "123456"
        }
        response = courier_page.login_courier(data=login_data)
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Авторизация под несуществующим пользователем')
    def test_login_nonexistent_user(self, courier_page):
        login_data = {
            "login": "hello",
            "password": "byebye"
        }
        response = courier_page.login_courier(data=login_data)
        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"

    @allure.title('Авторизация без логина и пароля')
    def test_login_without_login_and_password(self, courier_page):
        login_data = {
            "login": "",
            "password": ""
        }
        response = courier_page.login_courier(data=login_data)
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для входа"
