from .. import db

class Flashcard(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    collection_id = db.Column(db.Integer)
    card_front = db.Column(db.String(1000))
    card_description = db.Column(db.String(1000))
