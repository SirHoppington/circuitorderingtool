
# Test authenticated and unauthenticated user to /view_quotations

def test_view_quotations_authenticated(test_authenticated_user):
    """
    GIVEN an HTTP GET to /view_quotations
    WHEN a response is received
    THEN check the response code and initial html response contains
    """
    response = test_authenticated_user.get('/view_quotations')
    assert response.status_code == 200
    print(response.data)
    assert b"Customer Requests" in response.data

def test_view_quotations_unauthenticated(test_unauthenticated_user):
    """
    GIVEN an anonymous  HTTP GET to /view_orders
    WHEN a response is received
    THEN check the response code is redirect 302 and initial html response shows redirect
    """
    response = test_unauthenticated_user.get('/view_quotations')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data

# Test authenticated and unauthenticated user to /new_quote

def test_new_quote_authenticated_get(test_authenticated_user):
    """
    GIVEN an HTTP GET to /new_quote
    WHEN a response is received
    THEN check the response code and initial html response contains
    """
    response = test_authenticated_user.get('/new_quote')
    assert response.status_code == 200
    print(response.data)
    assert b"Request New Quote" in response.data

def test_new_quotation_unauthenticated_get(test_unauthenticated_user):
    """
    GIVEN an anonymous  HTTP GET to /new_quote
    WHEN a response is received
    THEN check the response code is redirect 302 and initial html response shows redirect
    """
    response = test_unauthenticated_user.get('/new_quote')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data

def test_new_quote_authenticated_post(test_authenticated_user):
    """
    GIVEN an HTTP GET to /new_quote
    WHEN a response is received
    THEN check the response code and initial html response contains
    """
    response = test_authenticated_user.post('/new_quote', data=dict(customer_name='Joe', customer_lastName="Bloggs",
                                         customer_email="joebloggs@gmail.com", customer_telephone="07949594950" ,
                                         net="12345", postcode="BT22 1ST"))
    assert response.status_code == 200
    print(response.data)
    assert b"Pricing results NET" in response.data

def test_new_quotation_unauthenticated_post(test_unauthenticated_user):
    """
    GIVEN an anonymous  HTTP GET to /new_quote
    WHEN a response is received
    THEN check the response code is redirect 302 and initial html response shows redirect
    """
    response = test_unauthenticated_user.post('/new_quote')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data

