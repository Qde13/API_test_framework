import base64
import random
import time

import allure
import requests
from utils.base import Base
from utils.waits import WaitFor


class APIRequests(Base):
    @allure.step("Get User")
    def get_user(self, username):
        endpoint = f'/users/{username}'
        response = requests.get(Base.BASE_URL + endpoint, headers=Base.headers)
        return response

    @allure.step("Get repository")
    def get_repository(self, repo):
        endpoint = f'/repos/{Base.OWNER}/{repo}'
        response = requests.get(Base.BASE_URL + endpoint, headers=Base.headers)
        return response

    @allure.step("Create reository")
    def create_repository(self, name, description):
        endpoint = '/user/repos'
        data = {
            'name': f'{name}',
            'description': f'{description}',
            'private': False,
            'is_template': True
        }
        response = requests.post(Base.BASE_URL + endpoint, headers=Base.headers, json=data)
        return response

    @allure.step("Delete repository")
    def delete_repository(self, repo):
        endpoint = f'/repos/{Base.OWNER}/{repo}'
        response = requests.delete(Base.BASE_URL + endpoint, headers=Base.headers)
        return response

    @allure.step("Update repository")
    def update_repository(self, repo, data):
        endpoint = f'/repos/{Base.OWNER}/{repo}'
        response = requests.patch(Base.BASE_URL + endpoint, headers=Base.headers, json=data)
        return response

    @allure.step("Add file to repository")
    def add_file_to_repository(self, repo, path):
        endpoint = f'/repos/{Base.OWNER}/{repo}/contents/{path}'
        message = f'add file - {path}'

        with open(path, 'r') as file:
            content = file.read()

        encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')

        data = {
            'message': message,
            'content': encoded_content,
            'branch': 'master',
        }
        response = requests.put(Base.BASE_URL + endpoint, headers=Base.headers, json=data)
        return response

    @allure.step("Get file from repository")
    def get_file_from_repository(self, repo):
        endpoint = f'/repos/{Base.OWNER}/{repo}/contents'
        url = Base.BASE_URL + endpoint
        response = WaitFor.wait_for_get_api(self, url)
        response.raise_for_status()
        return response

    @allure.step("Update file with new data")
    def update_file_from_repository(self, repo, file, content):
        endpoint = f"/repos/{Base.OWNER}/{repo}/contents/{file['path']}"
        url = Base.BASE_URL + endpoint
        encoded_content = base64.b64encode(content.encode()).decode()
        data = {
            "message": "Test commit",
            "content": encoded_content,
            "sha": file["sha"],
        }
        response = WaitFor.wait_for_put_api(self, url=url, data=data)
        return response
