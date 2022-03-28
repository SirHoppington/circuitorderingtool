from app import db
from datetime import datetime
#from Quotes.quote_model import quote_table
from Quote.association_table import quote_table

class ProviderQuote(db.Model):
    __tablename__ = "provider_pricing"
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(50), nullable=False)
    supplier_ref = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    quotes = db.relationship('Quotation', secondary=quote_table, backref=db.backref('quote_associated', lazy="dynamic"))
    orders = db.relationship('Order', secondary=quote_table, backref=db.backref('order_associated', lazy="dynamic"))

    def __init__(self, provider, supplier_ref):
        self.provider = provider,
        self.supplier_ref = supplier_ref

    def __repr__(self):
        return '<id {}>'.format(self.id)


    @property
    def serialize(self):
        return {
            'id' : self.id,
            'provider' : self.provider,
            'supplier_ref' : self.supplier_ref,
            'created_at' : self.created_at,
        }
