def validate_schema(data):
    assert "name" in data, "Missing 'name' field"
    assert "age" in data, "Missing 'age' field"
    assert "count" in data, "Missing 'count' field"


def validate_response_time(response, max_time=1):
    assert response.response_time < max_time, f"Slow response: {response.response_time}s"