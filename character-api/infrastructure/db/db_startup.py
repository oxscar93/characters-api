from infrastructure.db.test_data_factory import TestDataFactory
from infrastructure.repositories.database import DatabaseRepository
from infrastructure.repositories.character import CharacterRepository

test_data_factory = TestDataFactory()
character_repository = CharacterRepository()
database_repository = DatabaseRepository()

def create_db(app):
    #starts the database creation based on existing models along with the test data to use the API.
    with app.app_context():     
        create_model()
        set_db_test_data()

def create_model():
    #create or update database based on current models
    print('Creating/updating DB tables..')
    database_repository.create_model()
    print('Creating/updating DB tables done.')

def set_db_test_data():
    #sets test data.
    if (not character_repository.exists_any()):
        print('Inserting test data..')
        character_repository.add_all(test_data_factory.get_characters())
        print('Inserting test data done.')
    else:
        print('Test data already exists in database.')