import os
import time
import requests
import allure
import pytest
from utils.api_requests import APIRequests as r
from generator.generator import generated_file, generated_repository
from utils.files_actions import FilesActions


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
        assert add_file_response.status_code == 201, "The file hasn't been added"

    @allure.title("Check reading file from repository")
    @pytest.mark.api
    def test_read_file_from_repository(self, fixture_repository):
        add_file_response = r.add_file_to_repository(self, repo=self.repository_name, path=self.path)
        assert add_file_response.status_code == 201, "The file hasn't been added"
        read_file = r.get_file_from_repository(self, self.repository_name)
        assert read_file.status_code == 200, "The file hasn't been received"
        file = read_file.json()
        uploaded_content = FilesActions.read_local_file(self, path=self.path)
        downloaded_content = FilesActions.read_first_file_from_repository(self, files=file)
        assert uploaded_content == downloaded_content, "The file content is different"

    @allure.title("Check updating file from repository")
    def test_update_file_in_repository(self, fixture_repository):
        add_file_response = r.add_file_to_repository(self, repo=self.repository_name, path=self.path)
        assert add_file_response.status_code == 201, "The file hasn't been added"
        read_file = r.get_file_from_repository(self, self.repository_name)
        assert read_file.status_code == 200, "The file hasn't been received"
        response_json = read_file.json()
        file = response_json[0]
        update_response = r.update_file_from_repository(self, repo=self.repository_name, file=file,
                                                        content=self.repository_description)
        assert update_response.status_code == 200, "The file content is different"
        os.remove(path=self.path)
