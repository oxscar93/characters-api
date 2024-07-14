from infrastructure.db import db 
from infrastructure.model.character import CharacterModel

class DatabaseRepository():
    def create_model(self):
        #create or update database based on current models
        db.create_all()