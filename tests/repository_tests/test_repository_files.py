import allure
import pytest
from utils.api_requests import APIRequests as r
from generator.generator import generated_file, generated_repository


@allure.suite("Repository Files API tests")
class TestRepositoryFiles:
    repository = next(generated_repository())
    repository_name = 'TestName'
    repository_description = repository.repository_description
    path = generated_file()

    @allure.title("Check adding file to repository")
    @pytest.mark.api
    def test_adding_file_to_repository(self, fixture_repository):
        add_file_response = r.add_file_to_repository(self, repo=self.repository_name, path=self.path)
        assert add_file_response.status_code == 201









