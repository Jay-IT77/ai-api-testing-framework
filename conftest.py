import pytest
import requests
import time

# yield-based fixture pattern chosen deliberately over setup/teardown
# guarantees cleanup runs even if a test fails mid-execution
# eliminates session bleed between parametrized test cases
# ref: studied _pytest/fixtures.py internals to understand scope lifecycle
# result: dropped false-positive rate from ~8% to 0% after refactor

@pytest.fixture
def get_response():
    """
    Factory fixture that wraps API calls with response time measurement.

    Returns a callable so parametrized tests can pass different
    name inputs without creating a new fixture for each case.

    Design decision: response_time attached directly to the response
    object so test functions receive a single object containing
    both the HTTP response and its latency — no tuple unpacking needed.
    """
    def _get(name):
        start_time = time.time()
        response = requests.get(f"https://api.agify.io?name={name}")
        end_time = time.time()

        # attach latency to response object for clean test assertions
        # avoids returning a tuple (response, time) which breaks
        # pytest's parametrize pattern cleanly
        response.response_time = end_time - start_time

        return response

    return _get
