import allure
import pytest

from utils.request import Request as r


@allure.suite("Repository API tests")
class TestRepository:
    owner = "Qde13"
    repository_name = "MyRepositoryName"
    repository_description = "My repository description"

    @allure.title("Check repository creation")
    @pytest.mark.api
    def test_post_create_repository(self):
        response = r.post_create_repository(self, name=self.repository_name,
                                            description=self.repository_description)
        assert response.status_code == 201, "The Repository has not been created"

    @allure.title("Check created repository returns 200")
    @pytest.mark.api
    def test_get_repository(self):
        response = r.get_repository_response(self, owner=self.owner, repro_name=self.repository_name)
        assert response.status_code == 200, "The Repository has not been found"

    @allure.title("Check created repository data is true")
    @pytest.mark.api
    def test_get_repository_data(self):
        response = r.get_repository_response(self, owner=self.owner, repro_name=self.repository_name)
        assert response.status_code == 200, "The Repository has not been found"
        data = response.json()
        assert data['name'] == self.repository_name, "The Repository JSON data has not been found"
        assert data['owner']['login'] == self.owner, "The Repository JSON data has not been found"

    @allure.title('Check that the created repository can be deleted')
    @pytest.mark.api
    def test_delete_repository(self):
        response = r.delete_repository(self, owner=self.owner, repo_name=self.repository_name)
        assert response.status_code == 204, "The Repository has not been deleted"
