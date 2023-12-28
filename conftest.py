import pytest
import requests
from utils.api_requests import APIRequests as r
from generator.generator import generated_repository
from utils.base import Base


repository = next(generated_repository())
repository_description = repository.repository_description
repo_name = 'TestName'


@pytest.fixture
def fixture_repository():
    endpoint = '/user/repos'
    data = {
        'name': f'{repo_name}',
        'description': f'{repository_description}',
        'private': False,
        'is_template': True
    }
    response = requests.post(Base.BASE_URL + endpoint, headers=Base.headers, json=data)
    assert response.status_code == 201
    yield
    endpoint = f'/repos/{Base.OWNER}/{repo_name}'
    response = requests.delete(Base.BASE_URL + endpoint, headers=Base.headers)
    assert response.status_code == 204

