from domain.exceptions import EntityAlreadyExists, NotFoundException
from infrastructure.model.character import CharacterModel
from infrastructure.repositories.character import CharacterRepository


class CharacterService():
    character_repository = CharacterRepository()

    def getAll(self):
        #get all characters
        return self.character_repository.getAll()
    
    def get(self, id):
        #get character by id
        character = self.character_repository.get(id)

        if (character is None):
            raise NotFoundException()
        
        return character  
    
    def add(self, character_request):
        #add a character if not exists
        character_id = character_request['id']
        existing_character = self.character_repository.get(character_id)

        if (existing_character is not None):
            raise EntityAlreadyExists()
        
        self.character_repository.add(CharacterModel(**character_request))
        return self.get(character_id)
    
    def delete(self, id):
        #delete character if it exists
        character = self.get(id)
        return self.character_repository.delete(character)