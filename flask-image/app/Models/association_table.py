from app import db
from datetime import datetime

class NetRef(db.Model):
    __tablename__ = 'network_ref_associations'
    provider_id = db.Column(db.Integer, db.ForeignKey('provider_pricing.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('provider_product.id'), primary_key=True)
    quotation_id = db.Column(db.Integer, db.ForeignKey('quotation.id'), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order_table.id'), primary_key=True)

    provider = db.relationship ('ProviderQuote', backref='networkrefs')
    product = db.relationship('ProviderProduct', backref='networkrefs')
    order = db.relationship('Order', backref='networkrefs')
    quotation = db.relationship('Quotation', backref='networkrefs')

    def __init__(self, provider, product, quote, order):
        self.provider_id = provider.id,
        self.product_id = product.id,
        self.quotation_id = quote.id,
        self.order_id = order.id

    def __repr__(self):
        return '{}'.format(self.provider_id)

class Quotation(db.Model):
    __tablename__ = 'quotation'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    net = db.Column(db.String(20))
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'net' : self.net
        }

    def __init__(self, name, net):
        self.name = name,
        self.net = net

    def __repr__(self):
        return repr(self.id)

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
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    #quotes = db.relationship('Quotation', secondary=quote_table, backref=db.backref('quote_associated', lazy="dynamic"))
    #orders = db.relationship('Order', secondary=quote_table, backref=db.backref('order_associated', lazy="dynamic"))

    def __init__(self, quoteReference, provider):
        self.quoteReference = quoteReference,
        self.provider = provider

    def __repr__(self):
        return repr(self.productReference)


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
    term = db.Column(db.Text)


    def __init__(self, accessType, bandwidth, bearer, carrier, installCharges, monthlyFees, product, productReference, term):
        self.accessType = accessType,
        self.bandwidth = bandwidth,
        self.bearer = bearer,
        self.carrier = carrier,
        self.installCharges = installCharges,
        self.monthlyFees = monthlyFees,
        self.product = product,
        self.productReference = productReference,
        self.term = term

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
            'term' : self.term
        }
