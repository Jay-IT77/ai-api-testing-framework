import pytest
from utils.assertions import validate_schema, validate_response_time

names = ["john", "maria", "alex", "", "!!!"]

@pytest.mark.parametrize("name", names)
def test_api_response(get_response, name):
    res = get_response(name)

    # Status Code
    assert res.status_code == 200

    data = res.json()

    # Schema Validation
    validate_schema(data)

    # Response Time Check
    validate_response_time(res)


def test_bug_simulation(get_response):
    res = get_response("john")
    data = res.json()

    # Intentional bug check (for demo)
    assert data["age"] > 0, "Age should be greater than 0"

def test_fail_wrong_status(get_response):
    res = get_response("john")
    
    # ❌ Intentionally wrong expectation
    assert res.status_code == 404, "Expected 404 but got 200"


def test_fail_wrong_schema(get_response):
    res = get_response("john")
    data = res.json()

    # ❌ Field does not exist
    assert "salary" in data, "Missing 'salary' field"