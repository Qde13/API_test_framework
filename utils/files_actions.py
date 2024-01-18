import base64

import allure
import requests


class FilesActions:
    @allure.step("Read first file from repository")
    def read_first_file_from_repository(self, files):
        if files:
            download_url = files[0]['download_url']
            response = requests.get(download_url)
            if response.status_code == 200:
                decoded_content = response.content.decode('utf-8')
                return decoded_content

    @allure.step("Read local file")
    def read_local_file(self, path):
        with open(path, 'r') as file:
            content = file.read()
        return content
