from http import HTTPStatus
from flask import Blueprint, jsonify
from flasgger import swag_from
from api.model.character import CharacterModel
from api.schema.character import CharacterSchema, characters_schema
from flasgger.marshmallow_apispec import schema2jsonschema

character_api = Blueprint('character', __name__, url_prefix='/character')

@character_api.route('/getAll')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'getAll',
            'schema': schema2jsonschema(CharacterSchema)
        }
    }
})
def get_all():
    all_users = CharacterModel.query.all()
    result = characters_schema.dump(all_users)
    return jsonify(result), HTTPStatus.OK
