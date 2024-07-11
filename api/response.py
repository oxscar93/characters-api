from flask import jsonify

def create_response(item=None, schema=None, status_code=200): 
   result = schema.dump(item)
   return jsonify(schema.load(result)), status_code
    

def create_simple_message_response(message=None,status_code=200):
    return jsonify(message), status_code
