from app import db


class Brand (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, nullable=True)
    surname = db.Column(db.String(20), index=True, nullable=True)
    fragnances = db.relationship("Fragnance", backref="brand", lazy="dynamic")

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Fragnance (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, nullable=True)
    year = db.Column(db.Integer, index=True, nullable=True)
    brand_id = db.Column(db.Integer, db.ForeignKey("brand.id"))

    stock = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f"{self.name}"
