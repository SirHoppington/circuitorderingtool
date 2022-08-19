def test_view_orders(test_authentication):
    """
    GIVEN an HTTP GET to /
    WHEN a response is received
    THEN check the response code and initial html response
    """
    response = test_authentication.get('/view_orders')
    assert response.status_code == 200
    #assert b"Search existing quote" in response.data


def view_order(test_db, test_client):
    """
    GIVEN an HTTP GET to /view_pricing
    WHEN a response is received
    THEN check the response code and initial html response
    """
    with self.test_client:

        login = self.test_client.post('login', {username : "admin", password : "AnimalAcc3ss"})

        response = test_client.get('/view_orders')
        assert response.status_code == 200
        assert b"View Orders" in response.data

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