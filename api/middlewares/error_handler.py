from http import HTTPStatus
from flask import app, jsonify
from marshmallow import ValidationError

from domain.exceptions import EntityAlreadyExists, NotFoundException


def register_error_handlers(app):
    def handle_custom_exception(error):
        response = {
            'error': 'An exception has ocurred',
            'message': error.error_message
        }
        return jsonify(response), error.status_code
    
    def handle_internal_error(error):
        response = {
            'error': 'An internal error has ocurred',
            'message': str(error)
        }
        return jsonify(response), HTTPStatus.INTERNAL_SERVER_ERROR
    
    def handle_validation_fields_error(error):
        response = {
            'error': 'Entity fields are not correct.',
            'message': error.messages
        }
        return jsonify(response), HTTPStatus.BAD_REQUEST
    
    app.errorhandler(ValidationError)(handle_validation_fields_error)
    app.errorhandler(NotFoundException)(handle_custom_exception)
    app.errorhandler(EntityAlreadyExists)(handle_custom_exception)
    app.errorhandler(Exception)(handle_internal_error)