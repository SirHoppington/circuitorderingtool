"""from app import db
#from Quote.association_table import quote_table

class Order(db.Model):
    __tablename__ = 'order_table'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20))
    #order_to_quotes = db.relationship('Quotation', secondary=quote_table, backref=db.backref('quote_to_order_associated', lazy="dynamic"))

    def __init__(self, status):
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'status' : self.status
        }"""