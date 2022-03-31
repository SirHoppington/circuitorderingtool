from app import db
from datetime import datetime

class NetRef(db.Model):
    __tablename__ = 'network_ref_associations'
    provider_id = db.Column(db.Integer, db.ForeignKey('provider_pricing.id'), primary_key=True)
    quotation_id = db.Column(db.Integer, db.ForeignKey('quotation.id'), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order_table.id'), primary_key=True)

    provider = db.relationship ('ProviderQuote', backref='networkrefs')
    order = db.relationship('Order', backref='networkrefs')
    quotation = db.relationship('Quotation', backref='networkrefs')

    def __init__(self, provider, quote, order):
        self.provider_id = provider.id,
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
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(50), nullable=False)
    supplier_ref = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #quotes = db.relationship('Quotation', secondary=quote_table, backref=db.backref('quote_associated', lazy="dynamic"))
    #orders = db.relationship('Order', secondary=quote_table, backref=db.backref('order_associated', lazy="dynamic"))

    def __init__(self, provider, supplier_ref):
        self.provider = provider,
        self.supplier_ref = supplier_ref

    def __repr__(self):
        return repr(self.id)


    @property
    def serialize(self):
        return {
            'id' : self.id,
            'provider' : self.provider,
            'supplier_ref' : self.supplier_ref,
            'created_at' : self.created_at,
        }