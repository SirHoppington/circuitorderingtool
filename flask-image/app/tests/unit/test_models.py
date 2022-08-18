from app.Models.association_table import Quotation, Customer, Order, ProviderQuote, ProviderProduct, User
from app import db

def test_new_quote(test_db, test_quote):
    """
    GIVEN a Quotation model
    WHEN a new Quotation is created
    THEN add to DB and check the name and net has been asserted correctly
    """
    # Add to DB.
    with test_db.app_context():
       db.session.add(test_quote)
       db.session.commit()
       # Query DB
       query = db.session.query(Quotation).filter(Quotation.net == test_quote.net).first()

       # Assert the result of the query
       assert query.net == 12345

def test_new_customer(test_db, test_customer):
    """
    GIVEN a Customer model
    WHEN a new Customer is created
    THEN add to DB and check the email, name, lastName and telephone has been asserted correctly
    """
    with test_db.app_context():
        db.session.add(test_customer)
        db.session.commit()

        query = db.session.query(Customer).filter(Customer.email == test_customer.email).first()

        assert query.email == 'johnsmith@gmail.com'
        assert query.name == 'John'
        assert query.lastName == 'Smith'
        assert query.telephone == '01234567891'

def test_new_order(test_db, test_order):
    """
    GIVEN a Order model
    WHEN a new Order is created
    THEN add to DB and check the order status and ref has been asserted correctly
    """
    with test_db.app_context():
        db.session.add(test_order)
        db.session.commit()
        query = db.session.query(Order).filter(Order.ref == test_order.ref).first()

        assert query.status == 'Not Ordered'
        assert query.ref == '12345'

def test_new_provider_quote(test_db, test_provider_quote):
    """
    GIVEN a ProviderQuote model
    WHEN a new ProviderQuote is created
    THEN add to DB and check the provider and quote Reference has been asserted correctly
    """
    with test_db.app_context():
        db.session.add(test_provider_quote)
        db.session.commit()
        query = db.session.query(ProviderQuote).filter(ProviderQuote.provider == test_provider_quote.provider).first()

        assert query.provider == 'Virtual 1'
        assert query.quoteReference == '1234567'

def test_new_provider_product(test_db, test_provider_product):
    """
    GIVEN a ProviderProduct model
    WHEN a new Product is created
    THEN check the attributes have been asserted correctly

    """
    with test_db.app_context():
        db.session.add(test_provider_product)
        db.session.commit()
        query = db.session.query(ProviderProduct).filter(ProviderProduct.accessType == test_provider_product.accessType).first()

    assert query.accessType == 'fibre'
    assert query.bandwidth == '100'
    assert query.bearer == '1000'
    assert query.carrier == 'BT'
    assert query.installCharges == '250'
    assert query.monthlyFees == '100.50'
    assert query.product == 'fibre everywhere'
    assert query.productReference == '1234567'
    assert query.hardwareId == '777777'
    assert query.term == '36'
    assert query.customer_quote == 'None'

def test_new_user(test_db, test_user):
    """
    GIVEN a User model
    WHEN a new user is created
    THEN check the email, password and role has been asserted correctly
    """
    with test_db.app_context():
        db.session.add(test_user)
        db.session.commit()

        query = db.session.query(User).filter(User.email == test_user.email).first()
        assert query.email == 'testadmin@unittest.com'
        assert query.password == 'testpassword'
        assert query.role == 'admin'