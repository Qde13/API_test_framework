import requests
from utils.base_url import BaseUrl


class Request(BaseUrl):
    def get_user_response(self, username):
        endpoint = f'/users/{username}'
        response = requests.get(BaseUrl.BASE_URL + endpoint, headers=BaseUrl.headers)
        return response

    def get_repository_response(self, owner, repro_name):
        endpoint = f'/repos/{owner}/{repro_name}'
        response = requests.get(BaseUrl.BASE_URL + endpoint, headers=BaseUrl.headers)
        return response

    def post_create_repository(self, name, description):
        endpoint = '/user/repos'
        data = {
            'name': f'{name}',
            'description': f'{description}',
            'private': False,
            'is_template': True
        }
        response = requests.post(BaseUrl.BASE_URL + endpoint, headers=BaseUrl.headers, json=data)
        return response

    def delete_repository(self, owner, repo_name):
        endpoint = f'/repos/{owner}/{repo_name}'
        response = requests.delete(BaseUrl.BASE_URL + endpoint, headers=BaseUrl.headers)
        return response
