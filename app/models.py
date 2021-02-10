from app import db


class Room(db.Model):
    id = db.Column(db.String(4), primary_key=True)
    last_activation = db.Column(db.Integer)
    placement = db.Column(db.Integer)
