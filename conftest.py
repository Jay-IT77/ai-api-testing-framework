import pytest
import requests
import time

@pytest.fixture
def get_response():
    def _get(name):
        start_time = time.time()
        response = requests.get(f"https://api.agify.io?name={name}")
        end_time = time.time()

        # ✅ Attach response_time properly
        response.response_time = end_time - start_time

        return response

    return _get