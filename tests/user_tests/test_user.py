import allure
import pytest

from utils.api_requests import APIRequests as request


@allure.suite("User API tests")
class TestUser:
    username = 'Qde13'

    @allure.title("Check that user get call is 200")
    @pytest.mark.api
    def test_get_user(self):
        response = request.get_user_response(self, username=self.username)
        assert response.status_code == 200, 'User is not found, or status code is different'

    @allure.title("Check that user data is present")
    @pytest.mark.api
    def test_user_data(self):
        response = request.get_user_response(self, username=self.username)
        user_data = response.json()
        assert user_data['login'] == self.username, 'User is not found, or data is different'
        assert 'id' in user_data, 'User is not found, or data is different'
        assert 'name' in user_data, 'User is not found, or data is different'
        assert 'email' in user_data or 'public_email' in user_data, 'User is not found, or data is different'
