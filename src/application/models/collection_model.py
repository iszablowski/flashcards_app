from .. import db

class FlashcardsCollection(db.Model):
    collection_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer)
    collection_name = db.Column(db.String(100))