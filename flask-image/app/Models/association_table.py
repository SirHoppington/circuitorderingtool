from app import db
from datetime import datetime
from flask_login import UserMixin


class Customer(db.Model):
    __tablename__ = 'customer_table'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40))
    name = db.Column(db.String(40))
    @property
    def serialize(self):
        return {
            'email' : self.email,
            'name' : self.name
        }

    def __init__(self, name, email):
        self.name = name,
        self.email = email

    def __repr__(self):
        return repr(self.name)

class Quotation(db.Model):
    __tablename__ = 'quotation_table'
    name = db.Column(db.String(20))
    net = db.Column(db.Integer, primary_key=True)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name' : self.name,
            'net' : self.net
        }

    def __init__(self, name, net):
        self.name = name,
        self.net = net

    def __repr__(self):
        return repr(self.net)

class Order(db.Model):
    __tablename__ = 'order_table'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20))
    #order_to_quotes = db.relationship('Quotation', secondary=quote_table, backref=db.backref('quote_to_order_associated', lazy="dynamic"))

    def __init__(self, status):
        self.status = status

    def __repr__(self):
        return '{}'.format(self.id)

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'status' : self.status
        }
class ProviderQuote(db.Model):
    __tablename__ = "provider_pricing"
    quoteReference = db.Column(db.Text)
    provider = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.TIMESTAMP(timezone=False),
                           default=datetime.utcnow,
                           server_default=db.text("CURRENT_TIMESTAMP"),
                           nullable=False)

    #quotes = db.relationship('Quotation', secondary=quote_table, backref=db.backref('quote_associated', lazy="dynamic"))
    #orders = db.relationship('Orders', secondary=quote_table, backref=db.backref('order_associated', lazy="dynamic"))

    def __init__(self, quoteReference, provider):
        self.quoteReference = quoteReference,
        self.provider = provider

    def __repr__(self):
        return repr(self.quoteReference)


    @property
    def serialize(self):
        return {
            'id' : self.id,
            'created_at' : self.created_at,
            'quoteReference' : self.quoteReference,
            'provider' : self.provider
        }

class ProviderProduct(db.Model):
    __tablename__ = "provider_product"
    id = db.Column(db.Integer, primary_key=True)
    accessType = db.Column(db.Text)
    bandwidth = db.Column(db.Text)
    bearer = db.Column(db.Text)
    carrier = db.Column(db.Text)
    installCharges = db.Column(db.Text)
    monthlyFees = db.Column(db.Text)
    product = db.Column(db.Text)
    productReference = db.Column(db.Text)
    accessProductId = db.Column(db.Text)
    HardwareId = db.Column(db.Text)
    term = db.Column(db.Text)
    customer_quote = db.Column(db.Text)


    def __init__(self, accessType, bandwidth, bearer, carrier, installCharges, monthlyFees, product, productReference, accessProductId, term, customer_quote):
        self.accessType = accessType,
        self.bandwidth = bandwidth,
        self.bearer = bearer,
        self.carrier = carrier,
        self.installCharges = installCharges,
        self.monthlyFees = monthlyFees,
        self.product = product,
        self.productReference = productReference,
        self.accessProductId = accessProductId,
        self.term = term,
        self.customer_quote = customer_quote

    def __repr__(self):
        return repr(self.productReference)


    @property
    def serialize(self):
        return {
            'id' : self.id,
            'supplier_ref' : self.supplier_ref,
            'created_at' : self.created_at,
            'accessType' : self.accessType,
            'bandwidth' : self.bandwidth,
            'bearer' : self.bearer,
            'carrier' : self.carrier,
            'installCharges' : self.installCharges,
            'monthlyFees' : self.monthlyFees,
            'product' : self.product,
            'productReference' : self.productReference,
            'accessProductId' : self.accessProductId,
            'term' : self.term,
            'customer_quote': self.customer_quote
        }

class NetRef(db.Model):
    __tablename__ = 'network_ref_associations'
    provider_id = db.Column(db.Integer, db.ForeignKey('provider_pricing.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('provider_product.id'), primary_key=True)
    quotation_net = db.Column(db.Integer, db.ForeignKey('quotation_table.net'), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order_table.id'), primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer_table.id'), primary_key=True)

    provider = db.relationship ('ProviderQuote', backref='networkrefs')
    product = db.relationship('ProviderProduct', backref='networkrefs')
    order = db.relationship('Order', backref='networkrefs')
    quotation = db.relationship('Quotation', backref='networkrefs')
    customer = db.relationship('Customer', backref='networkrefs')

    def __init__(self, provider, product, quotation, order, customer):
        self.provider_id = provider.id,
        self.product_id = product.id,
        self.quotation_net = quotation.net,
        self.order_id = order.id,
        self.customer_id = customer.id

    def __repr__(self):
        return '{}'.format(self.provider_id)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
