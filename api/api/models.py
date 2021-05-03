from api import db

from sqlalchemy.inspection import inspect


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    image = db.Column(db.String(128), nullable=False)
    rarity = db.Column(db.String(32), nullable=False)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String, nullable=False)
    shiny = db.Column(db.Boolean, nullable=False, default=False)
    color = db.Column(db.String(7), nullable=False, default="#808080")

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    def __repr__(self):
        return f"<Card @id:{self.id}, @name:{self.name}>"