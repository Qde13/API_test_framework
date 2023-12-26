import allure
import pytest

from utils.request import Request as request


@allure.suite("User Api Call")
class TestUser:
    username = 'Qde13'

    @allure.title("Check is user get 200")
    @pytest.mark.api
    def test_get_user(self):
        response = request.get_user_response(self, username=self.username)
        assert response.status_code == 200

    @allure.title("Check is user data present")
    @pytest.mark.api
    def test_user_data(self):
        response = request.get_user_response(self, username=self.username)
        user_data = response.json()
        assert user_data['login'] == self.username
        assert 'id' in user_data
        assert 'name' in user_data
        assert 'email' in user_data or 'public_email' in user_data
