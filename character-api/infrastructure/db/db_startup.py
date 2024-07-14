from infrastructure.db.test_data_factory import TestDataFactory
from infrastructure.model.character import CharacterModel
from . import db

test_data_factory = TestDataFactory()

def create_db(app):
    #starts the database creation based on existing models along with the test data to use the API.
    with app.app_context():     
        create_model()
        set_db_test_data()

def create_model():
    #create or update database based on current models
    print('Creating/updating DB tables..')
    db.create_all()
    print('Creating/updating DB tables done.')

def test_data_already_created():
    # Check if the test data already exists in the database
    return db.session.query(CharacterModel).count() > 0

def set_db_test_data():
    #sets test data.
    if (not test_data_already_created()):
        print('Inserting test data..')
        db.session.add_all(test_data_factory.get_characters())
        db.session.commit()
        print('Inserting test data done.')
    else:
        print('Test data already exists in database.')