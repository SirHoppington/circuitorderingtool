from app import db

quote_table = db.Table('quote_table',
                    db.Column('provider_id', db.Integer, db.ForeignKey('provider_pricing.id'), primary_key=True),
                    db.Column('quotation_id', db.Integer, db.ForeignKey('quotation.id'), primary_key=True)
                    )