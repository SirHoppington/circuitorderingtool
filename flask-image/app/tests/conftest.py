from app.Models.association_table import Quotation, Order, NetRef, ProviderQuote, ProviderProduct, Customer, User
import pytest
from app import create_app, db
from werkzeug.security import generate_password_hash
import requests
import requests_mock

@pytest.fixture(scope='module')
def test_quote():
    quote = Quotation('BT349Gh', '12345')
    return quote

@pytest.fixture(scope='module')
def test_provider_quote():
    provider_quote = ProviderQuote("1234567", 'Virtual 1')
    return provider_quote

@pytest.fixture(scope='module')
def test_order():
    order = Order("Not Ordered", ref="12345")
    return order

@pytest.fixture(scope='module')
def test_customer():
    customer = Customer("John", "johnsmith@gmail.com","Smith", "01234567891")
    return customer


@pytest.fixture(scope='module')
def test_provider_product():
    provider_product = ProviderProduct('fibre', '100', '1000', 'BT', '250', '100.50', 'fibre everywhere', '1234567', '777777', '36', 'None')
    return provider_product

@pytest.fixture(scope='module')
def test_user():
    test_admin = User(email="testadmin@unittest.com", password="testpassword", role="admin")
    return test_admin



@pytest.fixture(scope='module')
def test_association():
    test_provider_pricing = ProviderQuote("Virtual1", "12345")
    test_order = Order("Not Ordered", ref="12345")
    test_customer = Customer("John", "johnsmith@gmail.com","Smith", "01234567891")
    test_provider_product = ProviderProduct('fibre', '100', '1000', 'BT', '250', '100.50', 'fibre everywhere', '1234567','777777',
                                       '36', 'None')
    test_quote = Quotation("BT234AG", "12345")
    assoc = NetRef(test_pricing, test_quote, test_order, test_customer,test_provider_pricing, test_provider_product)
    return assoc
# fixture to create a test application using "testing" config
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    with flask_app.test_client() as test_client:
        #create application context
        with flask_app.app_context():
            yield test_client

# Fixture to create new database tables in the test database, yield results for unit test and once run to drop tables.
@pytest.fixture(scope='module')
def test_db():
    flask_app = create_app('testing')
    with flask_app.app_context():
        db.create_all()
        yield flask_app
        db.session.remove()
        db.drop_all()

# Fixture to create a test user account, log the user in and yield test client and destroy DB after test.
@pytest.fixture(scope='module')
def test_authenticated_user():
    flask_app = create_app('testing')
    with flask_app.test_client() as test_client:
        with flask_app.app_context():
            db.create_all()
            test_admin = User(email="testadmin@unittest.com",
                              password=generate_password_hash("testpassword", method='sha256'), role="admin")
            db.session.add(test_admin)
            db.session.commit()
            test_client.post('/login', data=dict(email='testadmin@unittest.com', password="testpassword"))
            yield test_client
            db.session.remove()
            db.drop_all()

# Fixture to test unauthenticated user access.
@pytest.fixture(scope='module')
def test_unauthenticated_user():
    flask_app = create_app('testing')
    with flask_app.test_client() as test_client:
        with flask_app.app_context():
            db.create_all()
            yield test_client
            db.session.remove()
            db.drop_all()

@pytest.fixture(scope='module')
def test_provider():
    filters = {'fibre', '100', '1000', 'BT', '250', '100.50', 'fibre everywhere', '1234567', '36', 'None'}
    return filters

match_data = {"customer_name":'Joe', "customer_lastName":"Bloggs",
                "customer_email":"joebloggs@gmail.com", "customer_telephone":"07949594950",
                "net":"12345", "postcode":"BT22 1ST"}

@pytest.fixture(scope='function')
def mock_post_v1_quote():
    with requests_mock.Mocker() as requests_mocker:
        def match_data(request):
            """
            This is just optional. Remove if not needed. This will check if the request contains the expected body.
            """
            return request.json() == {"customer_name":'Joe', "customer_lastName":"Bloggs",
                "customer_email":"joebloggs@gmail.com", "customer_telephone":"07949594950",
                "net":"12345", "postcode":"BT22 1ST"}

        requests_mocker.post(
            "https://apitest.virtual1.com/layer2-api/quoting",
            status_code=200,
            #additional_matcher=match_data,
            json={ "quoteReference":"123456789","accessProducts":[{"accessType":"Fibre","availableWithoutHardware":"false","bandwidth":"10","bearer":"100","carrier":"Level 3 Communications","hardwareOptions":[{"hardwareOption":"FCM9005 Dual Power","hardwareReference":"278316372"},{"hardwareOption":"FCM9005","hardwareReference":"278316373"}],"indicative":"false","installCharges":"0.0000","leadTime":"55","monthlyFees":"441.7800","product":"Ethernet Everywhere\xe2\x84\xa2","productReference":"278316398","secondaryOptions":[],"term":"36"}]},)
        yield
