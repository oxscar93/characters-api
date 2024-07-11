def get_request(body, schema): 
   #validate the body against the schema and return the result
   return schema.load(body)