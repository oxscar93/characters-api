from flask import app, jsonify
from marshmallow import ValidationError

from domain.exceptions import NotFoundException


def register_error_handlers(app):
    def handle_not_found_exception(error):
        response = {
            'error': 'NotFound',
            'message': error.error_message
        }
        return jsonify(response), error.status_code
    
    def handle_validation_fields_error(error):
        response = {
            'error': 'Entity fields are not correct.',
            'message': error.messages
        }
        return jsonify(response), 400
    
    app.errorhandler(ValidationError)(handle_validation_fields_error)
    app.errorhandler(NotFoundException)(handle_not_found_exception)
