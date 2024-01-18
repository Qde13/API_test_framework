class Base:
    OWNER = 'Qde13'
    BASE_URL = 'https://api.github.com'
    ACCESS_TOKEN = 'token'
    headers = {
        'Authorization': f'token {ACCESS_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
