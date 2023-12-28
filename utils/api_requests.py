import base64

import requests
from utils.base import Base


class APIRequests(Base):
    def get_user(self, username):
        endpoint = f'/users/{username}'
        response = requests.get(Base.BASE_URL + endpoint, headers=Base.headers)
        return response

    def get_repository(self, repo):
        endpoint = f'/repos/{Base.OWNER}/{repo}'
        response = requests.get(Base.BASE_URL + endpoint, headers=Base.headers)
        return response

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

    def delete_repository(self, repo):
        endpoint = f'/repos/{Base.OWNER}/{repo}'
        response = requests.delete(Base.BASE_URL + endpoint, headers=Base.headers)
        return response

    def update_repository(self, repo, data):
        endpoint = f'/repos/{Base.OWNER}/{repo}'
        response = requests.patch(Base.BASE_URL + endpoint, headers=Base.headers, json=data)
        return response

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

