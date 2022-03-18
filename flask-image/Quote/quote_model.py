from app import db

class Quotation(db.Model):
    __tablename__ = 'quotation'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
        }

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)