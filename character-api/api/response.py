from flask import jsonify

def create_response(item=None, schema=None, status_code=200): 
   #validate entity to retrieve against the schema and create response
   result = schema.dump(item)
   return jsonify(schema.load(result)), status_code
    

def create_simple_message_response(message=None,status_code=200):
    return message, status_code
