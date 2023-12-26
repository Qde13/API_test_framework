class BaseUrl:
    BASE_URL = 'https://api.github.com'
    ACCESS_TOKEN = 'your token'
    headers = {
        'Authorization': f'token {ACCESS_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
