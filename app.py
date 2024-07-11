from flask import Flask
from flasgger import Swagger
from flask_marshmallow import Marshmallow
from api.db.db_startup import create_db
from api.route.character import character_api
from api.db import db

def create_app():
    app = Flask(__name__)
    ma = Marshmallow(app)
    app.config['SWAGGER'] = {
        'title': 'Character API',
    }

    Swagger(app)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(character_api)
    create_db(app)

    return app

