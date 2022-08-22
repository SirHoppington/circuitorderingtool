def test_view_orders(test_authenticated_user):
    """
    GIVEN an HTTP GET to /
    WHEN a response is received
    THEN check the response code and initial html response
    """
    response = test_authenticated_user.get('/view_orders')
    assert response.status_code == 200
    #assert b"Search existing quote" in response.data


def test_view_order(test_authenticated_user):
    """
    GIVEN an HTTP GET to /view_order
    WHEN a response is received
    THEN check the response code and initial html response
    """
    response = test_authenticated_user.get('/view_orders')
    assert response.status_code == 200
    assert b"View Orders" in response.data



def test_view_orders_route(test_unauthenticated_user):
    """
    GIVEN an HTTP GET to /new_quote
    WHEN a response is received
    THEN check the response code and initial html response
    """
    response = test_unauthenticated_user.get('/view_orders')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data