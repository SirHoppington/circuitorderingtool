

def test_index_route(test_client):
    """
    GIVEN an HTTP GET to /
    WHEN a response is received
    THEN check the response code and initial html response
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Search existing quote" in response.data