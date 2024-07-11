from domain.exceptions import EntityAlreadyExists, NotFoundException
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
    
    def add(self, character_request):
        existing_character = self.character_repository.get(character_request['id'])

        if (existing_character is not None):
            raise EntityAlreadyExists()
        
        self.character_repository.add(CharacterModel(**character_request))
        return self.get(character_request['id'])
    
    def delete(self, id):
        character = self.get(id)
        return self.character_repository.delete(character)