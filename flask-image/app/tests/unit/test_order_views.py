
def place_order(test_client):
    """
    GIVEN an HTTP GET to /view_pricing
    WHEN a response is received
    THEN check the response code and initial html response
    """
    response = test_client.get('/place_order')
    assert response.status_code == 200
    assert b"Search existing quote" in response.data

def test_view_quote_route(test_client):
    """
    GIVEN an HTTP GET to /new_quote
    WHEN a response is received
    THEN check the response code and initial html response
    """
    response = test_client.get('/view_quote')
    assert response.status_code == 200
    assert b"View all quotations" in response.data

def test_new_quote_route(test_client):
    """
    GIVEN an HTTP GET to /new_quote
    WHEN a response is received
    THEN check the response code and initial html response
    """
    response = test_client.get('/new_quote')
    assert response.status_code == 200
    assert b"Request New Quote" in response.data

def test_view_orders_route(test_client):
    """
    GIVEN an HTTP GET to /new_quote
    WHEN a response is received
    THEN check the response code and initial html response
    """
    response = test_client.get('/view_orders')
    assert response.status_code == 200
    assert b"View all orders" in response.data