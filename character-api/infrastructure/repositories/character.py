from infrastructure.db import db 
from infrastructure.model.character import CharacterModel

class CharacterRepository():
    def getAll(self):
        #get all characters
        return CharacterModel.query.all()
    
    def get(self, id):
        #get character by id
        return CharacterModel.query.get(id)
    
    def add(self, character):
        #add a character
        db.session.add(character)
        db.session.commit()

    def delete(self, character):
        #delete a character
        db.session.delete(character)
        db.session.commit()