from faker import Faker

from infrastructure.model.character import CharacterModel
fake = Faker()

class TestDataFactory():
    def create_character(self, id):
        character = CharacterModel()
        character.id = id
        character.name= fake.name()
        character.height= fake.random_int(min=100, max=300)
        character.mass= fake.random_int(min=50, max=150)
        character.hair_color= fake.color_name()
        character.skin_color= fake.color_name()
        character.eye_color= fake.color_name()
        character.birth_year= fake.random_int(min=1900, max=2023)
        
        return character

    def get_characters(self, count=50):
        result = []
        for i in range(1, count + 1):
            result.append(self.create_character(i))
         
        return result
    