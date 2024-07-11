from domain.exceptions import NotFoundException
from infrastructure.model.character import CharacterModel
from infrastructure.repositories.character import CharacterRepository


class CharacterService():
    character_repository = CharacterRepository()

    def getAll(self):
        
        return self.character_repository.getAll()
    def get(self, id):
        character = self.character_repository.get(id)

        if (character is None):
            raise NotFoundException()
        
        return character  
    
    def delete(self, id):
        character = self.get(id)
        return self.character_repository.delete(character)