from app import db

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20))
    order_to_quotes = db.relationship('Quote', secondary=quote_table, backref=db.backref('quote_to_order_associated', lazy="dynamic"))
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'status' : self.status
        }

    def __init__(self, status):
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)