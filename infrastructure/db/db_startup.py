from infrastructure.db.test_data_factory import TestDataFactory
from . import db

test_data_factory = TestDataFactory()

def create_db(app):
    with app.app_context():     
        create_model()
        set_db_test_data()

def create_model():
    print('Creating DB tables..')
    db.create_all()
    print('Creating DB tables done.')

def set_db_test_data():
    try:        
        print('Inserting test data..')
        db.session.add_all(test_data_factory.get_characters())
        db.session.commit()
        print('Inserting test data done.')
    except:
        print("Data already created.")