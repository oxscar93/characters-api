from api.db import db

class CharacterModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)  
    hair_color = db.Column(db.String(100), nullable=False)  
    skin_color = db.Column(db.String(100), nullable=False) 
    eye_color = db.Column(db.String(100), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)

    def __init__(self):
        pass
