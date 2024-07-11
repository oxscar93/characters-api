from infrastructure.db import db 
from infrastructure.model.character import CharacterModel

class CharacterRepository():
    def getAll(self):
        return CharacterModel.query.all()
    def get(self, id):
        return CharacterModel.query.get(id)
    def delete(self, character):
        db.session.delete(character)
        db.session.commit()