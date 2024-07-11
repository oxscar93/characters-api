from http import HTTPStatus
from flask import Blueprint, request
from flasgger import swag_from
from api.request import get_request
from api.response import create_response, create_simple_message_response
from api.schema.character import AllCharacterSchema, CharacterSchema
from flasgger.marshmallow_apispec import schema2jsonschema

from services.character import CharacterService

character_api = Blueprint('character', __name__, url_prefix='/character')
character_service = CharacterService()
character_schema = CharacterSchema()
all_characters_schema = AllCharacterSchema(many=True)

#getAll
@character_api.route('/getAll')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'get all available characters',
            'schema': schema2jsonschema(AllCharacterSchema)
        }
    }
})
def get_all():
    characters = character_service.getAll()
    return create_response(characters, all_characters_schema, HTTPStatus.OK)

#get
@character_api.route('/get/<int:id>')
@swag_from({
    'parameters': [{
        'name': 'id',
        'in': 'path',
        'description': 'Character id used to retrieve the entity',
        'type': 'integer'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'get character by id',
            'schema': schema2jsonschema(CharacterSchema)
        }
    }
})
def get(id):
    character = character_service.get(id)
    return create_response(character, character_schema, HTTPStatus.OK)

#add
@character_api.route('/add', methods=['POST'])
@swag_from({
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'schema': schema2jsonschema(CharacterSchema)
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'add a character based on the incoming request body'
        }
    }
})
def add():
    character_request = get_request(request.json, character_schema)
    saved_character = character_service.add(character_request) 
    return create_response(saved_character, character_schema, HTTPStatus.OK)

#delete
@character_api.route('/delete/<int:id>', methods=['DELETE'])
@swag_from({
    'parameters': [{
        'name': 'id',
        'in': 'path',
        'description': 'Character ID',
        'type': 'integer'
    }],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'delete a character by id'
        }
    }
})
def delete(id):
    character_service.delete(id) 
    return create_simple_message_response("Character deleted successfully", HTTPStatus.OK)