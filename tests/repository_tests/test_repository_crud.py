import random
import allure
import pytest
from generator.generator import generated_repository
from utils.api_requests import APIRequests as r


@allure.suite("Repository CRUD API tests")
class TestRepository:
    repository = next(generated_repository())
    repository_name = repository.repository_name
    repository_description = repository.repository_description

    @allure.title("Check repository creation")
    @pytest.mark.api
    def test_create_repository(self):
        response = r.create_repository(self, name=self.repository_name,
                                       description=self.repository_description)
        assert response.status_code == 201, "The Repository has not been created"

    @allure.title("Check created repository returns 200")
    @pytest.mark.api
    def test_get_repository(self):
        response = r.get_repository(self, repo=self.repository_name)
        assert response.status_code == 200, "The Repository has not been found"

    @allure.title("Check created repository data is true")
    @pytest.mark.api
    def test_get_repository_data(self):
        response = r.get_repository(self, repo=self.repository_name)
        assert response.status_code == 200, "The Repository has not been found"
        data = response.json()
        assert data['name'] == self.repository_name, "The Repository JSON data has not been found"
        assert data['owner']['login'] == 'Qde13', "The Repository JSON data has not been found"

    @allure.title("Check if you can change the repository description")
    @pytest.mark.api
    def test_update_repository_data(self):
        data = {'description': f'test {random.randint(100, 19999)}', }
        response = r.update_repository(self, repo=self.repository_name,
                                       data=data)
        assert response.status_code == 200, "The Repository has not been found"
        result_data = response.json()
        assert data['description'] == result_data['description'], "The Repository has not been updated"

    @allure.title('Check repository deletion')
    @pytest.mark.api
    def test_delete_repository(self):
        response = r.delete_repository(self, repo=self.repository_name)
        assert response.status_code == 204, "The Repository has not been deleted"
