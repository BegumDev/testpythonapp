from financetracker import db

class Customer(db.Model):
    # schema for the Customer model
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self, full_name, age):
        self.id = id
        self.full_name = full_name
        self.age = age
