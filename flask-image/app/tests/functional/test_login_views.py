
# Test authenticated and unauthenticated user to /login

def test_view_login_authenticated(test_authenticated_user):
    """
    GIVEN an HTTP GET to /login signed in as a test user account.
    WHEN a response is received
    THEN check the response code and initial html response contains
    """
    response = test_authenticated_user.get('/login')
    assert response.status_code == 200
    print(response.data)
    assert b"Login" in response.data

def test_view_login_unauthenticated(test_unauthenticated_user):
    """
    GIVEN an anonymous  HTTP GET to /login with an annoymous account
    WHEN a response is received
    THEN check the response code is redirect 302 and initial html response shows redirect
    """
    response = test_unauthenticated_user.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data

# Test authorised and unauthorised user to /signup

def test_view_signup_authorised(test_authenticated_user):
    """
    GIVEN an HTTP GET to /login signed in as a test user account.
    WHEN a response is received
    THEN check the response code and initial html response contains
    """
    response = test_authenticated_user.get('/signup')
    assert response.status_code == 200
    print(response.data)
    assert b"Signup" in response.data

# Test authenticated and unauthenticated user to /view_quotations

def test_view_signup_unauthorised(test_authenticated_standard_user):
    """
    GIVEN an HTTP GET to /login signed in as a test user account.
    WHEN a response is received
    THEN check the response code and initial html response contains
    """
    response = test_authenticated_standard_user.get('/signup')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data

