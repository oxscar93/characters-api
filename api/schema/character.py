from flask_marshmallow import Schema

from marshmallow import Schema, fields, validate

class CharacterBaseSchema(Schema):
    id = fields.Int(required=True, validate=validate.Range(min=1)) 
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    height =  fields.Int(required=True, validate=validate.Range(min=0)) 
    mass =  fields.Int(required=True, validate=validate.Range(min=0)) 
    eye_color = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    birth_year = fields.Int(required=True, validate=validate.Range(min=1))

class CharacterAllSchema(CharacterBaseSchema):
    pass

class CharacterSchema(CharacterBaseSchema):
    hair_color = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    skin_color = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    

character_get_schema = CharacterSchema()
characters_all_schema = CharacterAllSchema(many=True)