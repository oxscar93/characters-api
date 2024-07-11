from flask_marshmallow import Schema

from marshmallow import Schema, fields, validate

class CharacterAllSchema(Schema):
    id = fields.Int(required=True, validate=validate.Range(min=1)) 
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    height =  fields.Int(required=True, validate=validate.Range(min=0)) 
    mass =  fields.Int(required=True, validate=validate.Range(min=0)) 
    eye_color = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    birth_year = fields.Int(required=True, validate=validate.Range(min=1))

class CharacterGetSchema(Schema):
    id = fields.Int(required=True, validate=validate.Range(min=1)) 
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    height =  fields.Int(required=True, validate=validate.Range(min=0)) 
    mass =  fields.Int(required=True, validate=validate.Range(min=0)) 
    eye_color = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    birth_year = fields.Int(required=True, validate=validate.Range(min=1))
    hair_color = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    skin_color = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    

character_get_schema = CharacterGetSchema()
characters_all_schema = CharacterAllSchema(many=True)