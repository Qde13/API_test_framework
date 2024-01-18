import time
import requests
from utils.base import Base


class WaitFor:
    def wait_for_get_api(self, url, timeout=10):
        start_time = time.time()

        while time.time() < start_time + timeout:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    return response
            except requests.RequestException:
                pass
            time.sleep(0.5)
        raise TimeoutError(f"Timed out waiting for API response at {url}")

    def wait_for_put_api(self, url, data, timeout=10):
        start_time = time.time()

        while time.time() < start_time + timeout:
            try:
                response = requests.put(url, headers=Base.headers, json=data)
                if response.status_code == 200:
                    return response
            except requests.RequestException:
                pass
            time.sleep(0.5)
        raise TimeoutError(f"Timed out waiting for API response at {url}")
