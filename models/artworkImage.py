from db import db


class ArtworkImageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artworkId = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
