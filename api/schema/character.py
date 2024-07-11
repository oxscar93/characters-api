from flask_marshmallow import Schema

class CharacterSchema(Schema):
    class Meta:
        fields = ("id", "name", "height", "mass", "hair_color", "skin_color", "eye_color", "birth_year")

character_schema = CharacterSchema()
characters_schema = CharacterSchema(many=True)